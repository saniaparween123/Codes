// Remove empty List from List                
// The original list is: [5, 6, [], 3, [], [], 9]
// List after empty list removal: [5, 6, 3, 9]

var a=[5, 6, [], 3, [], [], 9];
var i=0;
var k=[];
for(i of a){
    if(i.length != 0){
        k.push(i);
    }
}
console.log(k);