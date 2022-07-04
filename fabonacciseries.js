// 15. Write a program to print the Fibonacci series till n
//  terms (Accept n from user)


var a=require('readline-sync');
var b=a.question('enter');
var i=0;
var c=0;
var d=1;
var e=0;
var r='0 1';

while (i<=b){
    e=d+c
    c=d
    d=e
    r=r+' '+d
    i=i+1
}
console.log(r)


