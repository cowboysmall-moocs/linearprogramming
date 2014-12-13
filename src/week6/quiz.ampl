var x1 integer >= 0, <= 7;
var x2 integer >= 0, <= 13;

# maximize obj: x1 + x2;
maximize obj: x2;

c1:   x1 - 3*x2 <= 10;
c2: 2*x1 + 3*x2 <= 15;

solve;

# display x1, x2;
printf '\n\nx1: %f, x2: %f\n', x1, x2;
printf '\nOptimal Value: %f\n\n\n', (x1 + x2);

end;
