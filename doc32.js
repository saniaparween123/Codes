/*
32)
Write a program to calculate the electricity bill 
(accept number of unit from user) according to the following criteria :
        Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)*/



var a=require('readline-sync');
var unit=a.question('enter');
 
if (unit<=100){
        console.log("no charge");
}
else if(unit>100 && unit<=200){
        console.log((unit-100)*5);
}

else if(unit>200){
        console.log((unit-200)*10+500);
}

