var a=require('readline-sync');
num=a.question('enter');
var i = 1;
var c=0;
while (i<=num){
    if (num%i==0){
        c=c+1;
    }
    i=i+1;
}
if (c==2){
    console.log(num,"prime number");
}
else{
    console.log(num,"not a prime number");
}