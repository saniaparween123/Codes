/*A company decided to give a bonus of 5% to an employee if 
his/her year of service is more than 5 years. Ask users for their 
salary and year of service and print the net bonus amount.*/


var a=require('readline-sync');
var salary=a.question("enter your salary");
var service_year=a.question("enter your service year");


if(service_year>=5){
    console.log(salary*5/100,"is your bonus amount");
}
else{
    console.log("no bonus");
}