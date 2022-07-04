// Write a python program to check whether
//  a number is divisible by 5 and 11 or not.

var a=require('readline-sync');
var number=a.question();

if (number%5==0 && number%7==0){
    console.log("yes number is divisible");
}
else{
    console.log("no number is not divisible");
}


