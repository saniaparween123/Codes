// Write a Python program to join adjacent members of a 
// given list.
// Original list:
// ['1', '2', '3', '4', '5', '6', '7', '8']
// Join adjacent members of a given list:
// ['12', '34', '56', '78']
// Original list:


var a= ['1', '2', '3', '4', '5', '6', '7', '8'];
var i=1;
var j=0;
var s='';
var k=[];
while(i<=a.length){
    s=a[j]+a[i];
    k.push(s);
    i+=2;
    j+=2;
}
console.log(k);




