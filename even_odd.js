// Even and Odd Numbers.

let a=require('readline-sync');
let user = a.question('enter');
let i = 0;
while (i<=user){
    if (i%2==0){
        console.log(i,"even number");
    }
    else{
        console.log(i,"odd number");
    }
    i=i+1;
}

