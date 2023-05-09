function [ssta] = factorization(temp)

ssta = [];

ssta = temp;
X = ssta;
rng('default'); % For reproducibilityproducibility
opt = statset('MaxIter',300,'Display','final');
[W0,H0] = nnmf(X,3,'replicates',10,'options',opt,'algorithm','mult');

opt = statset('MaxIter',1000,'Display','final');
[W,H] = nnmf(X,3,'w0',W0,'h0',H0,'options',opt,'algorithm','als');

R = W*H;
