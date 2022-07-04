
// Write a function that takes one argument “n” and delete 
// that many elements from the list.

// delete_nth ([1,1,1,1],2) # return [1,1]

// delete_nth ([20,37,20,21],1) # return [20,37,21]

let a=[20,37,20,21];
var b=[];
var i=0;
for (i of a){
    if (!b.includes(i,b)){
        b.push(i);
    }
}
console.log("(",b,",",a.length-b.length,")");
console.log(b);
