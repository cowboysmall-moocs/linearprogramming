var x1  integer >= 0;
var x2  integer >= 0;
var x3  integer >= 0;
var x4  integer >= 0;
var x5  integer >= 0;
var x6  integer >= 0;
var x7  integer >= 0;
var x8  integer >= 0;
var x9  integer >= 0;
var x10 integer >= 0;

maximize obj: (0.0) + (-2.0) * x1 + (-1.0) * x2 + (3.0) * x3 + (0.0) * x4 + (-2.0) * x5;

c1: x6  =  (0.0) +  (8.0) * x1 +  (0.0) * x2 + (-1.0) * x3 + (-6.0) * x4 +  (3.0) * x5;
c2: x7  = (-4.0) +  (4.0) * x1 + (-6.0) * x2 +  (7.0) * x3 +  (5.0) * x4 +  (4.0) * x5;
c3: x8  = (-3.0) + (-1.0) * x1 +  (6.0) * x2 +  (6.0) * x3 + (-5.0) * x4 + (-1.0) * x5;
c4: x9  = (-2.0) + (-6.0) * x1 +  (4.0) * x2 +  (1.0) * x3 + (-4.0) * x4 +  (7.0) * x5;
c5: x10 = (20.0) +  (0.0) * x1 +  (0.0) * x2 + (-1.0) * x3 +  (0.0) * x4 +  (0.0) * x5;

solve;

display (0.0) + (-2.0) * x1 + (-1.0) * x2 + (3.0) * x3 + (0.0) * x4 + (-2.0) * x5;

end;
