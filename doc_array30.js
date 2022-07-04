// Given a list of numbers, write a Python program to 
// count positive and negative numbers in a List.
// Example:
// list1 = [2, -7, 5, -64, -14]
// Output: pos = 2, neg = 3

// Iist2 = [-12, 14, 95, 3]
// Output: pos = 3, neg = 1

var a = [-12, 14, 95, 3];
var neg=0;
var pos=0;
var i=0;
for(i of a){
    if(!'-'.includes('-',i)){
        pos+=1
    }
    else{
        neg+=1
    }
}
console.log("pos =",pos,", neg =",neg)
