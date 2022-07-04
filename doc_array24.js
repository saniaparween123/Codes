// Remove duplicates from a list.
// List = [1,2,3,1,2,2]
// Output: [1,2,3]

let a = [1,2,3,1,2,2];
var i = 0;
var b = [];
for (i of a){
    if (!b.includes(i)){
        b.push(i);
    }
}
console.log(b);