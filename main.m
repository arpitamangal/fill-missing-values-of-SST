clear all
clc

file = 'D:\Core\BTP\BTP Arpita\SST-2008.nc';
lat = ncread(file, 'lat');
long = ncread(file, 'lon');
sst = ncread(file, 'sst');
tim = ncread(file, 'time');

for i = 1:1
    sst1 = reshape(sst(:,:,1,i), size(lat,1), size(long,1));
    sst1(isnan(sst1)) = 0;
    
    X = sst1;
    rng('default'); % For reproducibilityproducibility
    opt = statset('MaxIter',300,'Display','final');
    [W0,H0] = nnmf(X,4,'replicates',10,'options',opt,'algorithm','mult');

    opt = statset('MaxIter',1000,'Display','final');
    [W,H] = nnmf(X,4,'w0',W0,'h0',H0,'options',opt,'algorithm','als');

    R = W*H;
    E = R;
    E(85:88,117:120)= 0;
    
    Y = E;
    rng('default'); % For reproducibilityproducibility
    opt = statset('MaxIter',300,'Display','final');
    [W0,H0] = nnmf(Y,5,'replicates',10,'options',opt,'algorithm','mult');

    opt = statset('MaxIter',1000,'Display','final');
    [W,H] = nnmf(Y,5,'w0',W0,'h0',H0,'options',opt,'algorithm','als');
    
    F = W*H;
    
    
          
    
end


