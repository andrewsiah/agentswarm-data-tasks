import argparse, subprocess, sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--solution',required=True)
a=p.parse_args()
try:
    result=subprocess.run([sys.executable,'-B',str(Path(__file__).with_name('worker.py')),str(Path(a.solution).resolve())],timeout=5,capture_output=True,text=True)
    print(result.stdout,end='');print(result.stderr,end='',file=sys.stderr)
    sys.exit(0 if result.returncode==0 else 1)
except subprocess.TimeoutExpired:
    sys.exit('checker timeout')
