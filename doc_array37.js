// Write a Python program to pair up the consecutive elements
//  of a given list.
// Original lists:
// [1, 2, 3, 4, 5, 6]
// Pair up the consecutive elements of the said list:
// [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
// Original lists:
// [1, 2, 3, 4, 5]
// Pair up the consecutive elements of the said list:
// [[1, 2], [2, 3], [3, 4], [4, 5]]

var a=[1, 2, 3, 4, 5];
var b=a.length;
var i=0;
var j=1;
var s=[];
var k=[];
while (i<b-1){
    s=[+a[i],a[j]]
    j=j+1
    i=i+1
    k.push(s)
}
console.log(k);

    