import argparse,json,os,re,subprocess,sys,tempfile
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--solution',type=Path,required=True)
source=p.parse_args().solution;here=Path(__file__).resolve().parent
variants=[('reference',here/'implementation.py')]+[(x.stem,x) for x in sorted((here/'fixtures/mutants').glob('*.py'))]
assert len(variants)==11
kills=0
for name,implementation in variants:
    with tempfile.TemporaryDirectory() as folder:
        root=Path(folder);(root/'implementation.py').write_bytes(implementation.read_bytes());(root/'tests_submission.py').write_bytes(source.read_bytes())
        proc=subprocess.run([sys.executable,'-I','-B',str(here/'runner.py'),str(root)],capture_output=True,text=True,timeout=5)
        matches=re.findall(r'^TEST_RESULT (.+)$',proc.stdout,re.M)
        assert proc.returncode==0 and len(matches)==1,('invalid test run',name,proc.stdout,proc.stderr)
        result=json.loads(matches[0]);assert not any(result[x] for x in ['skipped','expected','unexpected','system_exits']),('invalid suite',name,result)
        failed=result['failures']+result['errors']>0
        if name=='reference':
            # Eight discovered methods are counted before running, so a class fixture that errors on a mutant still kills it.
            assert result['discovered']>=8 and result['run']>=8 and not result['import_failures'],('invalid suite',name,result)
            assert not failed,('tests must pass reference',proc.stderr)
        else: kills+=failed and not result['import_failures']
assert kills>=8,('too few mutants killed',kills)
print(f'PASS leap-tests: reference passed; {kills}/10 implementation mutants killed')
