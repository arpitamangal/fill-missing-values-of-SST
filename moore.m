load moore
X = moore(:,1:6);
rng('default'); % For reproducibility
opt = statset('MaxIter',50,'Display','final');
[W0,H0] = nnmf(X,3,'replicates',10,'options',opt,'algorithm','mult');
opt = statset('Maxiter',1000,'Display','final');
[W,H] = nnmf(X,3,'w0',W0,'h0',H0,'options',opt,'algorithm','als');
R = W*H;