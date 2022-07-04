// 16. Write a program to print the factorial of a number accepted by the user.


var a=require('readline-sync');
var user=a.question('enter');
var i=1;
var fac=1;
while (i<=user){
    fac=fac*i;
    i=i+1;
}
console.log(fac);


