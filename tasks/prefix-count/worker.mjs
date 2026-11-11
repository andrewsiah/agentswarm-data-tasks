import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
const task="prefix-count";
const helper=(await import(pathToFileURL(process.argv[2])))["prefixCount"];
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
check([['x'],'x'.repeat(64)],0);
check([['\ud800z'],'\ud800'],1);
rejects([['a'],'x'.repeat(65)],RangeError);
rejects([[1],'a'],TypeError);
rejects([[1],'x'.repeat(65)],TypeError);
rejects([Array(1),'x'.repeat(65)],TypeError);
rejects([['a'],1],TypeError);
rejects([['a'],new String('a')],TypeError);
rejects([[new String('a')],'a'],TypeError);
rejects([['a'],null],TypeError);
rejects([new Proxy(['a'],{}),'a'],TypeError);
class A extends Array {} class S extends String {}
const proxy=x=>new Proxy(x,{}),revoked=()=>{const p=Proxy.revocable([],{});p.revoke();return p.proxy;};
const badArrays=()=>[undefined,null,true,1,'ab',{},{length:0},new Set(),new A(),A.from(['a']),Object.setPrototypeOf([],null),Object.setPrototypeOf(['a'],Object.prototype),Array(1),['a',,'b'],proxy([]),proxy(['a']),revoked()];
const badStrings=[undefined,null,true,1,1n,Symbol('x'),[],['a'],{},new String('a'),new S('a'),proxy(new String('a'))];
const shadowed=['slice','concat','map','forEach','filter','reduce','push','at','entries','keys','values','join','indexOf','fill','flatMap','constructor'];
function shadow(values) {
 const copy=[...values];for(const name of shadowed) copy[name]=null;copy[Symbol.iterator]=null;copy.extra='ignored';return copy;
}
function unchangedShadow(copy,values) {
 for(const name of shadowed) assert.equal(copy[name],null);assert.equal(copy[Symbol.iterator],null);assert.equal(copy.extra,'ignored');
 assert.equal(copy.length,values.length);for(let i=0;i<values.length;i++) assert.ok(Object.is(copy[i],values[i]));
}
if(task==='longest-string') {
 for(const v of badArrays()) rejects([v],TypeError);
 for(const v of badStrings) {rejects([[v]],TypeError);rejects([['a',v]],TypeError);rejects([['abc',v,'a']],TypeError);}
 inheritedHole('p',()=>{rejects([['a',,'b']],TypeError);});
 rejects([[]],RangeError);
 const values=shadow(['ab','xyz','qrs']);assert.equal(helper(values),'xyz');unchangedShadow(values,['ab','xyz','qrs']);
 assert.equal(helper(Object.freeze(['a','bb','cc'])),'bb');
 const big=Array.from({length:1000},(_,i)=>'x'.repeat(i%50));assert.equal(helper(big),'x'.repeat(49));
 check([['\ud83d\ude80\ud83d\ude80\ud83d\ude80','abcd']],'abcd');check([['abc','\ud83d\ude80\ud83d\ude80\ud83d\ude80']],'abc');
 check([['\udc00\ud800','ab']],'\udc00\ud800');check([['a','bc','de','f']],'bc');check([['  ','a']],'  ');
} else {
 for(const v of badArrays()) {rejects([v,'a'],TypeError);rejects([v,'x'.repeat(65)],TypeError);}
 for(const v of badStrings) {rejects([[v],'a'],TypeError);rejects([['a',v],''],TypeError);rejects([[v],'x'.repeat(65)],TypeError);rejects([['a'],v],TypeError);rejects([[],v],TypeError);}
 inheritedHole('p',()=>{rejects([['a',,'b'],'p'],TypeError);});
 for(const n of [65,66,1000]) {rejects([['a'],'x'.repeat(n)],RangeError);rejects([[],'x'.repeat(n)],RangeError);}
 rejects([['a'],'\ud83d\ude80'.repeat(33)],RangeError);check([['\ud83d\ude80'.repeat(32)],'\ud83d\ude80'.repeat(32)],1);
 const values=shadow(['pa','pb','q']);assert.equal(helper(values,'p'),2);unchangedShadow(values,['pa','pb','q']);
 assert.equal(helper(Object.freeze(['ab','ac','b']),'a'),2);
 const big=Array.from({length:1000},(_,i)=>'k'+i);assert.equal(helper(big,'k1'),111);assert.equal(helper(big,''),1000);
 check([['A','a'],'A'],1);check([['ab','AB','aB'],'a'],2);check([['a b','ab'],'a '],1);check([['ab\n','ab'],'ab\n'],1);
}
console.log(`PASS ${task}: ${cases.length} fixtures plus specials, exact types, proxies, subclasses, holes, frozen, shadowed-method and independence probes`);
