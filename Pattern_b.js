/* 
b)
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1 
*/


var i = 5;
var s='' ;
while (i>=1){
    var j = 1;
    while (j<=i){
        s=s+j;
        j=j+1;
    }
    console.log(s);
    i=i-1;
    s='';
}
