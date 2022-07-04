var a=require('readline-sync');
var b = a.question("enter");
var m=b;
var l=b.length
var i=0;
var k='';
while (i<l){
    var s=b%10;
    var j=b/10;
    b=Math.floor(j);
    k=k+s;
    i++
}
if (k==m){
    console.log(m,'it is a palindrome number');
}
else{
    console.log(m,'its not palindrome number')
}

