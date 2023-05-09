# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:46:14 2018

@author: Arpita
"""

import numpy as np
import matplotlib
from netCDF4 import Dataset
from matplotlib.mlab import griddata
from matplotlib import pyplot as plt
import seaborn as sns

my_file = 'D:/BTP/BTP Arpita/SST-2008.nc'

fh = Dataset(my_file, mode='r')

lons = fh.variables['lon'][:]
lats = fh.variables['lat'][:]
sst = fh.variables['sst'][:]
time = fh.variables['time'][:]
sst_units = fh.variables['sst'].units


sst[sst==None]=-1
sst = np.asarray(sst)

high_1=32.52
low_1=18.2
slope=(0-(-1000))/(high_1-low_1)
const_c=-slope*high_1
time_curr = 0
sst_curr = sst[time_curr][0]

sst_curr[sst_curr==-999]=23.222222222222222

s=[]
for i in range(0,7):
    s.append(min(sst_curr[i]))


#sst_curr=slope*sst_cu+const_c



import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



# Get some parameters for the Stereographic Projection
lon_0 = lons.mean()
lat_0 = lats.mean()
m = Basemap(width=5000000,height=3500000,
            resolution='l',projection='stere',\
            lat_ts=40,lat_0=lat_0,lon_0=lon_0)
            
# Because our lon and lat variables are 1D,
# use meshgrid to create 2D arrays
# Not necessary if coordinates are already in 2D arrays.
lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)


# Plot Data
cs = m.pcolor(xi,yi,np.squeeze(sst_curr))

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(sst_units)

# Add Title
plt.title('DJF Maximum Temperature')

plt.show()
plt.savefig('mera_sst.png')