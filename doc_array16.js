// Write a Python program to find the difference between 
// elements (n+1th - nth) of a given list of numeric values.
// Original list:
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// Difference between elements (n+1th - nth) of the said list :
// [1, 1, 1, 1, 1, 1, 1, 1, 1]
// Original list:
// [2, 4, 6, 8]
// Difference between elements (n+1th - nth) of the said list :
// [2, 2, 2]


let a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var i = 0;
var s=0;
var k=[];
for (i of a){
    s=i-s;
    k=[k+s]
    s=i
}
k = Array.from(String(k),Number);
console.log(k)