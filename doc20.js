/*Write a python program to input electricity unit charges and calculate 
total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill */

var a=require('readline-sync');
var b=a.question('enter');
var total = b*20/100

if (b<=50){
    console.log((b*0.50)+total);
}
else if (b<=150){
    console.log((b*0.75)+total);
}
else  if (b>150 && b<=250){
    console.log((b*1.20)+total);
}
else if (b>250){
    console.log((b*1.50)+total);
}



