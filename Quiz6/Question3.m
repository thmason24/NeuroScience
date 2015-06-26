M=3*[-.25 0 0.25 0.25 0; 0 -.25 0 0.25 0.25; .25 0 -.25 0 .25; 0.25 0.25 0 -.25 0 ; 0 0.25 0.25 0 -.25]

u=[0.6;0.5;0.6;0.2;0.1]

W=eye(5)*0.5 + ones(5)*0.1
h=W*u
[V lambda] = eig(M)
V=V
v = zeros(5,1)

for i = 1:5

	(h'*V(:,i)/(1-lambda(i,i)))
	v = v + (h'*V(:,i)/(1-lambda(i,i)))*V(:,i)
end