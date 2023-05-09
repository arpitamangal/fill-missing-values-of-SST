# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:25:44 2018

@author: Arpita
"""

>>> from spacepy import pycdf
>>> cdf = pycdf.CDF('MyCDF.cdf')
>>> print(cdf)
    Epoch: CDF_EPOCH [60]
    data: CDF_FLOAT [60]
>>> cdf['data'][4]
    0.8609974384307861
>>> data = cdf['data'][...] # don't forget the [...]
>>> cdf_dat = cdf.copy()
>>> cdf_dat.keys()
    ['Epoch', 'data']
>>> cdf.close()