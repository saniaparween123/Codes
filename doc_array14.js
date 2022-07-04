// Write a Python program to find the list with maximum and minimum length.
// Original list:
// [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
// List with maximum length of lists:
// (3, [13, 15, 17])
// List with minimum length of lists:
// (1, [0])


var l = [[0], [1, 3], [5, 7],[9, 11], [13, 15, 17]];
var s=l[0];
var k=l[0];
var i=0;
var j =0;
for (i in l){
    if (s.length < l[i].length){
        s=l[i];
    }
}
for (j in l){
    if (k.length > l[j].length){
        k=l[j]
    }
}
console.log(s.length,s);
console.log(k.length,k);  






// var l = [[0], [1, 3], [5, 7], [13, 15, 17],[9, 11]];
// var s=l[0];
// var i=0;
// for(i in l){
//     if(s<=l[i]){
//         s=l[i];
//     }
//     console.log(s);
// }
