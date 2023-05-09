if true
    filename='D:\Core\BTP\BTP Arpita\SST-2008.nc'
%Read the header
ncdisp(filename)
%surf_temp
%Open the file in read only mode
ncid=netcdf.open(filename,'NOWRITE')
%inspect num of dimensions, variables, attributes, unim
[ndim, nvar, natt, unlim]=netcdf.inq(ncid)
for i=0:nvar-1
[varname, xtype, dimid, natt]=netcdf.inqVar(ncid,i);
if strcmp(varname,'surf_temp')==1
    varnumber=i;
end
end
for i=1:length(dimid)
    [dimname, dimlength]=netcdf.inqDim(ncid,dimid(1,i))
end
for i=0:nvar-1
[varname, xtype, dimid, natt]=netcdf.inqVar(ncid,i);
if strcmp(varname,'latitude')==1
    dimnumber=i
end
end
lat=ncread(filename,'lat')
lon=ncread(filename,'lon')
sst = ncread(filename, 'sst');
tim = ncread(filename, 'time');
for i = 1:1
    Z = reshape(sst(:,:,1,i), size(lat,1), size(long,1));
    Z(isnan(Z)) = 0;
pcolor(lat,lon,permute(Z, [2 1 3]))
load coast
hold on
plot(long,lat,'k','LineWidth',1.5)
plot(long+360,lat,'k','LineWidth',1.5)
  end