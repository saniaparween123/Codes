/*
45)
 Accept the number of days from the user and calculate the charge 
for library according to following :
First five days : Rs 2/day.
Six to ten days  : Rs 3/day.
Ten to 15 days  : Rs 4/day
After 15 days    : Rs 5/day*/


var a=require('readline-sync');
var days=a.question('enter number of days')

if (days<=5){
    console.log(days*2);
}
else if (days>= 6 && days<=10){
    console.log((days-5)*3+10);
}
else if (days>10 && days<=15){
    console.log((days-10)*4+25);
}
else if (days>15){
    console.log((days-15)*5+45);
}

