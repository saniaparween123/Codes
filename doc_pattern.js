var a=require('readline-sync');
var b=a.question('enter no  ');
var i=1;
while(i<=b){
    var j=5;
    var c='';
    while (j>=i){
        c=c+' '+j;
        j=j-1;
    }
    console.log(c);
    i=i+1;
}