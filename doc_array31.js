
// Example:
// Input: start = -4, end = 5
// Output: -4, -3, -2, -1
// Input: start = -3, end = 4
// Output: -3, -2, -1

var a=require('readline-sync');
var b=a.question('enter ending point');
var s='';
for (let i=1; b-=1; b>i){
    s=s+(-b)+', '
}
console.log(s)