import copy, importlib.util, json, sys
from pathlib import Path
TASK=Path(__file__).parent.name
spec=importlib.util.spec_from_file_location('candidate',sys.argv[1]);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
f=getattr(m,TASK.replace('-','_'))
rows=json.loads(Path(__file__).with_name('fixtures').joinpath('cases.json').read_text())
class I(int):pass
class S(str):pass
class L(list):pass
class D(dict):pass
def exact(a,b):
    assert type(a) is type(b),(a,b)
    if type(b) is dict:
        assert (list(a)==list(b) if TASK=='merge-counters' else a.keys()==b.keys()),(a,b)
        for k in b: exact(a[k],b[k])
    elif type(b) is list:
        assert len(a)==len(b),(a,b)
        for x,y in zip(a,b):exact(x,y)
    else:assert a==b,(a,b)
def check(args,row):
    before=copy.deepcopy(args)
    if 'error' in row:
        try:f(*args)
        except Exception as e:assert type(e) is {'TypeError':TypeError,'ValueError':ValueError}[row['error']],repr(e)
        else:raise AssertionError(('missing exception',args,row))
    else:
        a=f(*args);b=f(*args);exact(a,row['expected']);exact(b,row['expected'])
        if type(a) in (list,dict):
            assert a is not b and all(a is not x for x in args)
            if TASK=='coalesce-ranges':
                assert all(x is not y for x in a for y in args[0])
                if a:a[0].append(999)
            elif TASK=='paginate-items':
                assert a['items'] is not args[0] and a['items'] is not b['items']
                a['items'].append('changed')
            elif type(a) is list:a.append(999)
            else:a['changed']=999
            exact(f(*args),row['expected'])
    assert args==before,('input mutation',args,before)
for row in rows:check(row['args'],row)
bad=[[x] for x in [L(),L([1,2]),(),None,'ab',{}]]+[[[x]] for x in [True,I(1),1.0,'1',None]]+[[[1,x]] for x in [False,I(2)]]+[[[0]*1001+[True]],[[10**9+1,True]],[[3,3,True]]]; bounds=[[[]],[[1]],[[3,3,3]],[[10**9+1,1]],[[-10**9-1,1]],[list(range(1001))],[[1,-10**9-1]]]
for args in bad:check(args,{'error':'TypeError'})
for args in bounds:check(args,{'error':'ValueError'})
print('PASS '+TASK+': '+str(len(rows))+' examples plus exact types, bounds and isolation probes')
