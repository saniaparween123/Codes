// 
// Convert Character Matrix to single String;
// The original list is: [ ['g', 'f', 'g'], ['i', 's'],
//  ['b', 'e', 's', 't'] ]
// The String after join: gfgisbest

const array =[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ];
var s=" ";
for (i of array){
    var j=0;
    for (j of i){
        s=s+j;
    }
    
}
console.log(s);













