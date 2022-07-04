// For example, if we give 9119  the function should 
// return  811181, as the  square of 9 is 81 and square
//  of 1  is 1.

var a = 9119;
a = Array.from(String(a),Number);
console.log(a);

var i=0;
var s=" "
for(i of a){
    s=s+i**2;
}
console.log(s);


