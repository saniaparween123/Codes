// Find the First Maximum, Second maximum,
//  Third maximum number from the List.


var array=[ 20, 34, 80, 99, 75];
array.sort();
console.log(array);

var s=0;
for (i of array){
    if (s<=i){
        s=i
    }   
}
console.log(s);
array.pop(s);


var j=0;
for (r of array){
    if (j<=r){
        j=r
    }   
}
console.log(j);
array.pop(j);


var k=0;
for (q of array){
    if (k<=q){
        k=q
    }   
}
console.log(k);

