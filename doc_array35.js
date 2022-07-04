
// Write a Python program to check if first digit/character 
// of each element in a given list is same or not.
// Original list:
// [1234, 1922, 1984, 19372, 100]
// true
// Original list:
// ['aabc', 'abc', 'ab', 'a']
// Check if first character in each element of the said 
// given list is same or not!
// True


var array=[1234, 1922, 1984, 19372, 100];
var a=Array.from(String(array[0]), Number);
var i=0;
var s=0;
for (i of array){
    var b=Array.from(String(i),Number);
    if (b[0]==a[0]){
        s+=1;
    }
    
}
if (s==array.length){
    console.log('True');
}
else{
    console.log('False')
}



var a=['aabc', 'abc', 'ab', 'a'];
var b=a[0][0];
var i=0;
var s=0;
for (i of a){
    var k= i[0];
    if (b==k){
        s+=1;
    }
}
if(s==a.length){
    console.log('True');
}
else{
    console.log('false');
}




