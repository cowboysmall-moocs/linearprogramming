var x1 binary;
var x2 binary;
var x3 binary;
var z1 binary;
var z2 binary;
var z3 binary;
var z4 binary;
var z5 binary;

maximize obj: z1 + z2 + z3 + z4 + z5;

c1:  x1 + x2 + (1 - x3)       >=  z1;
c2:  x1 + x2 + x3             >=  z2;
c3:  x1 + (1 - x2) + (1 - x3) >=  z3;
c4:  x1 + (1 - x2) + x3       >=  z4;
c5:  (1 - x1)                 >=  z5;

solve;
display x1, x2, x3;
display z1, z2, z3, z4, z5;
display obj;
end;
