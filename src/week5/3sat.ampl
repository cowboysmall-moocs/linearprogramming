var x1 binary;
var x2 binary;
var x3 binary;

minimize obj: 0;

c1:  x1 + x2 + (1 - x3)       >=  1;
c2:  x1 + x2 + x3             >=  1;
c3:  x1 + (1 - x2) + (1 - x3) >=  1;
c4:  x1 + (1 - x2) + x3       >=  1;
c5:  (1 - x1)                 >=  1;

solve;
display x1, x2, x3;
end;
