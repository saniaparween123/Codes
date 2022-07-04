var a=require("readline-sync");
var b=a.question("enter");
var c=a.question("enter");
if (b>c){
    console.log(b,"b is maximum");
}
else if (c>b){
    console.log(c,"c is maximum");
}
else {
    console.log("both are equal");
}





