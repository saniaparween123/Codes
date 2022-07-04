
//  Write a Python program to compute the average of nth
//   elements in a given list of lists with different lengths.
//  Original list:
 
//  [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11],
//  [12, 13, 14]]
 
//  Average of n-th elements in the said list of lists 
//  with different lengths:

//  [4.8, 5.8, 6.8, 8.0, 11.0]

var a= [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11],[12, 13, 14]];
var b=[];
var i=0;
var s=0;
var s1=0;
var s2=0;
var s3=0;
var s4=0;
var c=0;
var c2=0;
var c3=0;
var c4=0;
var c1=0;

for(i of a){
    var j=0;
    for(j in i){
        if (j==0){
            s=s+i[j];
            c=c+1;
        }
        else if(j==1){
            s1=s1+i[j]
            c1=c1+1;
        }
        else if(j==2){
            s2=s2+i[j]
            c2=c2+1;
        }
        else if(j==3){
            s3=s3+i[j]
            c3=c3+1;
        }
        else if(j==4){
            s4=s4+i[j]
            c4=c4+1;
        }
    }
    
}

console.log([s/c,s1/c1,s2/c2,s3/c3,s4/c4])


