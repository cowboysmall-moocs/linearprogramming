var x1 >=0 ;
var x2 >=0 ;
var x3 >=0 ;
var x4 >=0 ;
var x5 >=0 ;
var x6 >=0 ;
var x7 >=0 ;
var x8 >=0 ;
var x9 >=0 ;
var x10 >=0 ;
maximize obj: 0.0  + 0.0 * x1   -1.0 * x2   -1.0 * x3   + 0.0 * x4   + 0.0 * x5 ;
c1: x6 = -5.0  -1.0 * x1  -7.0 * x2  + 8.0 * x3  -1.0 * x4  + 9.0 * x5 ;
c2: x7 = 22.0  -5.0 * x1  + 0.0 * x2  -8.0 * x3  + 3.0 * x4  -8.0 * x5 ;
c3: x8 = 20.0  -9.0 * x1  -10.0 * x2  -3.0 * x3  -4.0 * x4  -3.0 * x5 ;
c4: x9 = 0.0  + 2.0 * x1  + 1.0 * x2  -3.0 * x3  + 7.0 * x4  -2.0 * x5 ;
c5: x10 = 14.0  -8.0 * x1  -7.0 * x2  -1.0 * x3  -10.0 * x4  + 5.0 * x5 ;
solve; 
display 0.0  + 0.0 * x1   -1.0 * x2   -1.0 * x3   + 0.0 * x4   + 0.0 * x5 ;
 
 end; 