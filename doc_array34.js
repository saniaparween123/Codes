// Write a Python program to remove all the values except 
// integer values from a given array of mixed values.
// Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']

// After removing all the values except integer values 
// from the said array of mixed values: [12, 0]


var a=[34.67, 12, -9489, 'Python', 0, 'C#'];
var i=0;
var s=[];
for(i of a){
    if (Number.isInteger(i) && i>=0){
        s.push(i);
    }

}
console.log(s);
