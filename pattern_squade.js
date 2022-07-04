/* 
p)
1
4 4
9 9 9
16 16 16 16
25 25 25 25 25
*/


var i=1;
var s=1;
while (i<=5){
    var j=1;
    var k=''
    while (j<=i){
        k=k+' '+s**2;
        j=j+1;
    }
    console.log(k);
    s=s+1
    i=i+1;
}