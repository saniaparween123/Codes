
// Given a List, extract all elements whose frequency 
// is greater than K.
// Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
// Output: [4, 3]
// Explanation: Both elements occur 4 times.
// Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
// Output: [4, 3, 6]
// Explanation: Occur 4, 3, and 3 times respectively.


var list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6];
var k =[];
var i=0;
for (i of list){
    var count=0;
    var s ="";
    var j=0;
    for(j of list){
        if(i==j){
            count+=1;
        }
    }
    if (2<count){
        if(!k.includes(i)){
            k.push(i);
        }
    }
}
console.log(k);


