import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
const task="range-span";
const helper=(await import(pathToFileURL(process.argv[2])))["rangeSpan"];
const cases=JSON.parse(readFileSync(new URL('./fixtures/cases.json',import.meta.url)));
function check(args,expected) {
 const before=structuredClone(args);
 const a=helper(...args),b=helper(...args);
 assert.equal(typeof a,typeof expected);assert.equal(typeof b,typeof expected);
 assert.ok(Object.is(a,expected),String(a));assert.ok(Object.is(b,expected),String(b));
 assert.deepEqual(args,before,'input mutation');
}
const rejects=(args,ErrorType)=>assert.throws(()=>helper(...args),e=>e!==null && typeof e==='object' && e.constructor===ErrorType,String(args.length));
function inheritedHole(value,probe) {
 // A hole must be rejected even when Array.prototype supplies a value of the right type at that index.
 Object.defineProperty(Array.prototype,1,{value,configurable:true,writable:true});
 try {probe();} finally {delete Array.prototype[1];}
 assert.equal(Object.hasOwn(Array.prototype,1),false);
}
for(const row of cases) {if(Object.hasOwn(row,'error')) rejects(row.args,{TypeError,RangeError}[row.error]);else check(row.args,row.expected);}
check([[-0]],0);
check([[1e15,-1e15,0]],2e15);
rejects([[]],RangeError);
rejects([[1.5]],RangeError);
rejects([[NaN]],RangeError);
rejects([[Infinity]],RangeError);
rejects([[1e15+1]],RangeError);
rejects([['1']],TypeError);
rejects([[1n]],TypeError);
rejects([[new Number(1)]],TypeError);
rejects([[1.5,'x']],TypeError);
rejects([Array(1)],TypeError);
rejects([new Proxy([1],{})],TypeError);
class A extends Array {} class S extends String {} class N extends Number {}
const proxy=x=>new Proxy(x,{}),revoked=()=>{const p=Proxy.revocable([],{});p.revoke();return p.proxy;};
const badArrays=()=>[undefined,null,true,1,'ab',{},{length:0},new Set(),new A(),A.from(['a']),Object.setPrototypeOf([],null),Object.setPrototypeOf(['a'],Object.prototype),Array(1),['a',,'b'],proxy([]),proxy(['a']),revoked()];
const badStrings=[undefined,null,true,1,1n,Symbol('x'),[],['a'],{},new String('a'),new S('a'),proxy(new String('a'))];
const badNumbers=[undefined,null,true,'1',1n,Symbol('x'),[],[1],{},new Number(1),new N(1),proxy(new Number(1))];
const shadowed=['slice','concat','map','forEach','filter','reduce','push','at','entries','keys','values','join','indexOf','fill','flatMap','sort','constructor'];
function shadow(values) {
 const copy=[...values];for(const name of shadowed) copy[name]=null;copy[Symbol.iterator]=null;copy.extra='ignored';return copy;
}
function unchangedShadow(copy,values) {
 for(const name of shadowed) assert.equal(copy[name],null);assert.equal(copy[Symbol.iterator],null);assert.equal(copy.extra,'ignored');
 assert.equal(copy.length,values.length);for(let i=0;i<values.length;i++) assert.ok(Object.is(copy[i],values[i]));
}
if(task==='range-span') {
 for(const v of badArrays()) rejects([v],TypeError);
 for(const v of badNumbers) {rejects([[v]],TypeError);rejects([[1,v]],TypeError);rejects([[1.5,v,NaN]],TypeError);}
 inheritedHole(7,()=>{rejects([[1,,3]],TypeError);});
 for(const v of [0.5,-0.5,NaN,Infinity,-Infinity,1e15+2,-1e15-2,2**53,Number.MAX_VALUE,Number.EPSILON]) {rejects([[v]],RangeError);rejects([[1,v]],RangeError);}
 rejects([[]],RangeError);
 const values=shadow([3,9,1]);assert.equal(helper(values),8);unchangedShadow(values,[3,9,1]);
 assert.equal(helper(Object.freeze([2,7,4])),5);
 const big=Array.from({length:1000},(_,i)=>(i*7919)%1000-500);assert.equal(helper(big),999);
 check([[-7]],0);check([[2**40,-(2**40)]],2**41);check([[-0,0]],0);check([[0,-0]],0);check([[1e15,1e15]],0);check([[-1e15]],0);
} else {
 for(const v of badArrays()) rejects([v],TypeError);
 for(const v of badStrings) {rejects([[v]],TypeError);rejects([['a',v]],TypeError);rejects([['abc',v,'a']],TypeError);}
 inheritedHole('p',()=>{rejects([['a',,'b']],TypeError);});
 rejects([[]],RangeError);
 const values=shadow(['abx','aby','abz']);assert.equal(helper(values),'ab');unchangedShadow(values,['abx','aby','abz']);
 assert.equal(helper(Object.freeze(['pre1','pre2'])),'pre');
 const big=Array.from({length:1000},(_,i)=>'common/'+i);assert.equal(helper(big),'common/');
 check([['\ud83d\ude80','\ud83d\ude80']],'\ud83d\ude80');check([['a\ud83d\ude80','a\ud83d']],'a');check([['a\ud83d','a\ud83d\ude80']],'a');
 check([['  a',' a']],' ');check([['x','xy','xyz','x']],'x');check([['abc','abd','xbc']],'');check([['\ud800\ud800a','\ud800\ud800b']],'\ud800\ud800');
}
console.log(`PASS ${task}: ${cases.length} fixtures plus specials, exact types, proxies, subclasses, holes, frozen, shadowed-method and independence probes`);
