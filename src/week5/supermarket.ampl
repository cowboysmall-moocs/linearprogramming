var z1 binary;
var z2 binary;
var z3 binary;
var z4 binary;
var z5 binary;
var z6 binary;
var z7 binary;

# minimize obj: z1 + z2 + z3 + z4 + z5 + z6 + z7;
minimize obj: 12*z1 + 8*z2 + 12*z3 + 10*z4 + 9*z5 + 10*z6 + 7*z7;

c1:  z4 + z5 + z7             >=  1;
c2:  z2 + z4 + z6             >=  1;
c3:  z1 + z5 + z7             >=  1;
c4:  z3 + z4 + z6 + z7        >=  1;
c5:  z1 + z2 + z3 + z4        >=  1;
c6:  z1 + z2 + z3 + z6        >=  1;
c7:  z1 + z2 + z3 + z5        >=  1;

solve;
display z1, z2, z3, z4, z5, z6, z7;
display obj;
end;
