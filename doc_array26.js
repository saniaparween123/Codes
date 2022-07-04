// Our task is to print the element which occurs 3
//  consecutive times in a Python list.
// Example:
// Input: [4, 5, 5, 5, 3, 8]
// Output: 5
// Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
// Output: 1, 22


var a=[1, 1, 1, 64, 23, 64, 22, 22, 22];
var i=0;
var s=[];
for(i of a){
    var j=0;
    var count=0;
    for(j of a){
        if(i==j){
            count+=1;
        }
    }
    if(count>=3){
        if(!s.includes(i)){
            s.push(i);
        }
    }
}
console.log(s);


