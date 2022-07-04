/* 
n)
0  
0 1  
0 2 4  
0 3 6 9  
0 4 8 12 16
*/

var i = 0;
var s=0;
while (i<=4){
    var j=0;
    var t='';
    while (j<=i){
        t=t+' '+s*j;
        j=j+1

    }
    s=s+1;
    i=i+1;
    console.log(t);
}  