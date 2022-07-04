// 
// List product excluding duplicates.
// List = [6,1,3,5,6,3,1]
// Output: 90

var array = [6,1,3,5,6,3,1];
var k=[];
var m=1;
for (i of array){
    if (!k.includes(i,k)){
        k.push(i);
    }
}
for (i of k){
    var m = m*i;

}
console.log(m);

