import sys,time,json
from pathlib import Path
import argparse
parser=argparse.ArgumentParser(description='Reproduce the completion and clamshell fixtures.')
parser.add_argument('--source',type=Path,required=True,help='MeshMill 0.4 source checkout')
parser.add_argument('--output',type=Path,required=True,help='New result directory')
args=parser.parse_args()
if __name__=='__main__' and args.output.exists():parser.error('Choose a new output directory to preserve recorded evidence.')
sys.path.insert(0,str(args.source.resolve()))
import numpy as np
from vtkmodules.util.numpy_support import vtk_to_numpy
from vtkmodules.vtkIOXML import vtkXMLPolyDataWriter
from vtkmodules.vtkFiltersCore import vtkDelaunay3D,vtkTriangleFilter,vtkImplicitPolyDataDistance
from vtkmodules.vtkFiltersGeometry import vtkDataSetSurfaceFilter
from meshmill import arrays_polydata
from solidify import solidify_mesh,offset_solid
from clamshell_mold import clamshell_mold
from imprint_cleanup import clean_generated_mesh

W=args.output;W.mkdir(parents=True,exist_ok=True)
def save(mesh,name):
 writer=vtkXMLPolyDataWriter();writer.SetFileName(str(W/(name+'.vtp')));writer.SetInputData(mesh);writer.Write()
def arrays(mesh):return vtk_to_numpy(mesh.GetPoints().GetData()),vtk_to_numpy(mesh.GetPolys().GetConnectivityArray()).reshape(-1,3)
def volume(mesh):
 p,f=arrays(mesh);tri=p[f].astype(float);return abs(float(np.einsum('ij,ij->i',tri[:,0],np.cross(tri[:,1],tri[:,2])).sum()/6))
def keys(mesh):
 p,f=arrays(mesh);return {tuple(sorted(map(tuple,p[face].astype(np.float32)))) for face in f}
def boundary(mesh):
 p,f=arrays(mesh);_,inv=np.unique(p.astype(np.float32),axis=0,return_inverse=True);f=inv[f];e=np.sort(np.concatenate((f[:,[0,1]],f[:,[1,2]],f[:,[2,0]])),axis=1);_,n=np.unique(e,axis=0,return_counts=True);return int((n==1).sum())
def hull(mesh):
 d=vtkDelaunay3D();d.SetInputData(mesh);s=vtkDataSetSurfaceFilter();s.SetInputConnection(d.GetOutputPort());t=vtkTriangleFilter();t.SetInputConnection(s.GetOutputPort());t.Update();return t.GetOutput()
def bracket():
 xy=np.array([(0,0),(30,0),(30,10),(10,10),(10,30),(0,30)],float);p=np.vstack((np.c_[xy,np.zeros(6)],np.c_[xy,np.full(6,8)]));cap=np.array([(0,1,3),(1,2,3),(0,3,5),(3,4,5)]);faces=list(cap[:,::-1])+list(cap+6)
 for i in range(6):j=(i+1)%6;faces.extend([(i,j,j+6),(i,j+6,i+6)])
 f=np.array(faces);keep=np.ones(len(f),bool);keep[4:6]=False;return p,f,keep
def tube():
 n=64;a=np.arange(n)*2*np.pi/n;p=np.vstack([np.c_[r*np.cos(a),r*np.sin(a),np.full(n,z)] for z,r in [(0,12),(20,12),(0,7),(20,7)]]).astype(np.float32);f=[];keep=[]
 for i in range(n):
  j=(i+1)%n;items=[(i,j,n+j),(i,n+j,n+i),(2*n+i,3*n+j,2*n+j),(2*n+i,3*n+i,3*n+j),(n+i,n+j,3*n+j),(n+i,3*n+j,3*n+i),(i,2*n+j,j),(i,2*n+i,2*n+j)]
  f.extend(items);keep.extend([True,True,True,True,not(12<=i<20),not(12<=i<20),True,True])
 return p,np.array(f),np.array(keep)
def sample_error(reference,result):
 p,f=arrays(reference);q,g=arrays(result);a=vtkImplicitPolyDataDistance();a.SetInput(reference);b=vtkImplicitPolyDataDistance();b.SetInput(result)
 samples1=p[f].mean(1);samples2=q[g].mean(1);dist=np.array([abs(b.EvaluateFunction(x)) for x in samples1]+[abs(a.EvaluateFunction(x)) for x in samples2]);return dict(centroid_distance_rms_mm=float(np.sqrt(np.mean(dist**2))),centroid_distance_max_mm=float(dist.max()))
def plain(v):
 if isinstance(v,np.ndarray):return v.tolist()
 if isinstance(v,np.generic):return v.item()
 raise TypeError(type(v).__name__)
if __name__=='__main__':
 rows=[]
 for name,make in [('concave-bracket',bracket),('hollow-tube',tube)]:
  p,f,keep=make();truth=arrays_polydata(p,f);source=arrays_polydata(p,f[keep]);save(truth,name+'-truth');save(source,name+'-input');start=time.perf_counter()
  try:
   result,report=solidify_mesh(source,'Surface repair',1.,.35,128*1024**2);seconds=time.perf_counter()-start;save(result,name+'-completed');convex=hull(source);save(convex,name+'-convex');_,topology=clean_generated_mesh(result,closed=True)
   row=dict(fixture=name,status='accepted',input_faces=len(f[keep]),reference_faces=len(f),output_faces=result.GetNumberOfCells(),source_faces_retained=len(keys(source)&keys(result)),source_unique_faces=len(keys(source)),reference_volume_mm3=volume(truth),result_volume_mm3=volume(result),convex_volume_mm3=volume(convex),input_open_edges=boundary(source),result_open_edges=boundary(result),seconds=seconds,topology=topology,report=report,**sample_error(truth,result))
   rows.append(row);print(name,seconds,row['source_faces_retained'],row['result_volume_mm3'],flush=True)
  except Exception as e:rows.append(dict(fixture=name,status='failed',error_type=type(e).__name__,error=str(e)));print(name,'failed',type(e).__name__,flush=True)
 # The bracket has a known concavity; use it for cast sections and split outputs.
 source=arrays_polydata(*bracket()[:2]);skin,_=offset_solid(source,.5);save(skin,'cast-clearance');casts=[]
 for shape in ('Blob','Box'):
  start=time.perf_counter()
  try:
   halves,report=clamshell_mold(skin,wall_mm=2,bridge_mm=0,pitch_mm=.35,split_normal=(0,0,1),shape=shape,memory_budget_bytes=256*1024**2)
   elapsed=time.perf_counter()-start
   for i,half in enumerate(halves):save(half,'cast-'+shape.lower()+'-'+str(i))
   whole,_=clamshell_mold(skin,wall_mm=2,bridge_mm=0,pitch_mm=.35,split_normal=None,shape=shape,memory_budget_bytes=256*1024**2)
   unsplit_volume=volume(whole[0]);split_volume=sum(volume(x) for x in halves)
   casts.append(dict(unsplit_volume_mm3=unsplit_volume,split_volume_change_percent=100*(split_volume/unsplit_volume-1),shape=shape,status='accepted',seconds=elapsed,faces=[x.GetNumberOfCells() for x in halves],volume_mm3=sum(volume(x) for x in halves),open_edges=[boundary(x) for x in halves],report=report));print('cast',shape,elapsed,flush=True)
  except Exception as e:casts.append(dict(shape=shape,status='failed',error_type=type(e).__name__,error=str(e)))
 (W/'results.json').write_text(json.dumps(dict(completion=rows,cast=casts),default=plain,indent=2))
