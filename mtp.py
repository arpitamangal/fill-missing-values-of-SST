# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:08:24 2018

@author: Arpita
"""

from netCDF4 import Dataset
dataset_pacific=Dataset('D:/BTP/sst_xyt_5day_20190310_2byte.cdf')
dataset_indian=Dataset('D:/BTP/sst_xyt_dy.cdf')

my_file = 'D:/BTP/BTP Arpita/SST-2008.nc'

data_avhrr = Dataset(my_file, mode='r')
