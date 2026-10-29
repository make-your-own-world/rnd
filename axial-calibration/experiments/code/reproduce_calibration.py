"""Run synthetic axial calibration against a matching MeshMill checkout."""
import argparse
import json
import sys
import time
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True,help='MeshMill source checkout')
    parser.add_argument('--output',type=Path,required=True,help='New result directory')
    args=parser.parse_args()
    source=args.source.resolve()
    sys.path[:0]=[str(source),str(source/'tests')]
    import numpy as np
    from test_axis_datum_stress import shape_mesh
    from lathe_contact import build_contact_index
    from lathe_spindle import pose_matrix,contact_profiles,first_harmonics
    from axis_datum import fit_probe_datum,meaningful_improvement
    args.output.mkdir(parents=True,exist_ok=False)
    rows=[]
    for kind in ('round','stepped','tapered','oval','lobed','square','noisy','dented','bent'):
        mesh=shape_mesh(kind)
        original=np.array([mesh.GetPoint(i) for i in range(mesh.GetNumberOfPoints())])
        locator=build_contact_index(mesh)
        wrong=pose_matrix((.23,-.17,.065,-.045))
        probes=[(-3.,1.,0.,1.4),(0.,1.,0.,1.4),(3.,1.,0.,1.4)]
        parameters=np.zeros(4)
        initial=None
        history=[]
        start=time.perf_counter()
        for _ in range(24):
            result=fit_probe_datum(locator,wrong,parameters,probes,14.)
            if initial is None:initial=float(np.linalg.norm(result.before))
            if not result.accepted:
                if not np.allclose(result.parameters,parameters):raise RuntimeError('Rejected fit moved the pose')
                break
            if not meaningful_improvement(result.before,result.after,14.):raise RuntimeError('Insignificant update')
            angles,before=contact_profiles(locator,wrong,parameters,probes,14.,count=257,phase_offset=.31)
            _,after=contact_profiles(locator,wrong,result.parameters,probes,14.,count=257,phase_offset=.31)
            if np.linalg.norm(first_harmonics(angles,after))>=np.linalg.norm(first_harmonics(angles,before))+1e-6:
                raise RuntimeError('Independent validation regression')
            history.append(float(np.linalg.norm(result.after)))
            parameters=result.parameters.copy()
        else:raise RuntimeError('Did not settle within 24 corrections')
        repeat=fit_probe_datum(locator,wrong,parameters,probes,14.)
        if repeat.accepted:raise RuntimeError('Fit was not stable on recheck')
        if not np.array_equal(original,[mesh.GetPoint(i) for i in range(mesh.GetNumberOfPoints())]):
            raise RuntimeError('Source geometry changed')
        rows.append(dict(shape=kind,steps=len(history),initial=initial,final=float(np.linalg.norm(result.after)),
                         seconds=time.perf_counter()-start,history=history))
    (args.output/'results.json').write_text(json.dumps(rows,indent=2))
    print('Completed nine synthetic calibration fixtures')


if __name__=='__main__':
    main()
