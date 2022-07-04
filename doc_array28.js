// The task is to perform the operation of removing 
// all the occurrences of a given item/element present in a list.
// Input :

// 1 1 2 3 4 5 1 2
// 1

// Output :
// 2 3 4 5 2

// Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] 
// and the item to be removed is 1.
// After removing the item, the output list is [2, 3, 4, 5, 2]
// Input :
// 5 6 7 8 9 10
// 7

// Output :
// 5 6 8 9 10


var array=[1, 1, 2, 3, 4, 5, 1, 2] ;
var a=[];
var i=0;
for(i of array){
    var count=0;
    var j=0;
    for(j of array){
        if (i==j){
            count+=1;
        }
    }
    if(count==1){
        a.push(i)
    }

}
console.log(a)



// Input :
// 5 6 7 8 9 10
// 7

// Output :
// 5 6 8 9 10

var a =[5, 6, 7, 8, 9, 10];
var i=0;
var k=[];
for(i of a){
    if (i!=7){
        k.push(i);
    }
}
console.log(k);



