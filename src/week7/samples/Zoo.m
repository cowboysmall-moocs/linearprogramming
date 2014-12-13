%%%%%%%%%%%%%%%%%%%%
%
% Shalom D. Ruben
%
%%%%%%%%%%%%%%%%%%%%

clear all
clc
close all

%%%%%% Make the X's and O's and Labels %%%%%%%%%
rand('state',47)
x1 = 8*rand(100,1);
x2 = 7*rand(100,1)-4;
Hold1 = x2+.8*x1-4;
Flag1 = find(Hold1>=0); %Labels for X's or Elephants
Hold2 = x2+.8*x1-2;
Flag2 = find(Hold2<0); %Labels for O's or Giraffes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%% Plot X's and 0's
plot(x1(Flag1),x2(Flag1),'rx','markersize',15,'linewidth',2)
hold on 
plot(x1(Flag2),x2(Flag2),'bo','markersize',15,'linewidth',2)
axis equal
legend('Elephant','Giraffe')
set(gca,'FontSize',15)
Hold = axis;
axis(Hold)

%%% Plot Seperating Hyperplane
x = 0:.001:8;
y = -.8*x +3;
plot(x,y,'--k','linewidth',2)

%%%%%% Plot Outlier (if you want to add it)
 plot(2,2,'bo','markersize',15,'linewidth',2)

Animals = [x1 x2];

%%%%%%%% Pull out the Giraffes and Elephants from the DATA
        Elephants = Animals(Flag1,:);
        Giraffes = Animals(Flag2,:);
        %%%% Use this line to add the outlier or comment out
        Giraffes = [Giraffes;2 2]; 

        R = length(Elephants(:,1));
        Q = length(Giraffes(:,1));
        g = .1;
        n = length(Animals(1,:));
       
        %%%%%%%% Solve for the support vector
        cvx_begin
            cvx_precision low
            variables a(n) b(1) u(R) v(Q)
            minimize (ones(1,R)*u + ones(1,Q)*v)
            %minimize (norm(a) + g*(ones(1,R)*u + ones(1,Q)*v))
            Elephants*a - b >= 1 - u;
            Giraffes*a - b <= -(1 - v);
            u >= 0;
            v >= 0; 
        cvx_end
        
        plot(x,(-a(1).*x+b)./a(2),'--r','linewidth',2)
        
   
        

        



