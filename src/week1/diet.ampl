var x1 >= 0;
var x2 >= 0;
var x3 >= 0;
var x4 >= 0;
var x5 >= 0;

minimize obj: 0.5*x1 + 0.9*x2 + 0.1*x3 + 0.6*x4 + 0.4*x5;

c1: 100 <= 53*x1 + 40*x2 + 12*x3 + 53*x4 + 6*x5 <= 1000;
c2: 10 <= 4.4*x1 + 8*x2 + 3*x3 + 12*x4 + 1.9*x5 <= 100;
c3: 0 <= 0.4*x1 + 3.6*x2 + 2*x3 + 0.9*x4 + 0.3*x5 <= 100;

c4: 0.5*x1 <= 0.6*(0.5*x1 + 0.9*x2 + 0.1*x3 + 0.6*x4 + 0.4*x5);
c5: 0.9*x2 <= 0.6*(0.5*x1 + 0.9*x2 + 0.1*x3 + 0.6*x4 + 0.4*x5);
c6: 0.1*x3 <= 0.6*(0.5*x1 + 0.9*x2 + 0.1*x3 + 0.6*x4 + 0.4*x5);
c7: 0.6*x4 <= 0.6*(0.5*x1 + 0.9*x2 + 0.1*x3 + 0.6*x4 + 0.4*x5);
c8: 0.4*x5 <= 0.6*(0.5*x1 + 0.9*x2 + 0.1*x3 + 0.6*x4 + 0.4*x5);

solve;
display x1, x2, x3, x4, x5;
display obj;
end;
