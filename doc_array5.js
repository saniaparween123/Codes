
// Count unique values inside a list.
// input_list = [1, 2, 2, 5, 8, 4, 4, 8]

// Count = 5 #because [1,2,5,8,4] are unique values.

var array =[1, 2, 2, 5, 8, 4, 4, 8];
var k=[];
for (i of array){
    if (!k.includes(i,k)){
        k.push(i)
    }
}
console.log(k);
console.log(k.length);


