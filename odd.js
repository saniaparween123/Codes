// 34. Write a program to print only odd numbers from the given
//  list using  a while loop . L = [23, 45, 32, 25, 46, 33, 71, 90]

var array = [23, 45, 32, 25, 46, 33, 71, 90];
var l=array.length;
var i = 0;
while (i<l){
    if (array[i]%2!=0){
        console.log(array[i]);
    }
    i=i+1;
}




