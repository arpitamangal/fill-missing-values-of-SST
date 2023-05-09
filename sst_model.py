from __future__ import print_function

import keras
from keras.layers import Dense, Dropout, Flatten
from keras.models import Sequential, Input
from keras import layers
from keras.layers import Activation, Conv2D, Conv2DTranspose, MaxPooling2D, concatenate
from keras import backend as K
from keras import losses
from keras.models import model_from_json
from keras import losses
from keras.models import Model
from keras import optimizers

from PIL import Image

import numpy as np

from os import listdir
import os.path
from collections import OrderedDict
import datetime

from netCDF4 import Dataset
import random
from random import randint
from matplotlib import pyplot as plt
"""
def train(X, Y):
    batch_size = 100
    epochs = 50
    print (X.shape)
    print (Y.shape)
    m, r, c = X.shape
    print(m,r,c)
    x_train = X.reshape(m, r*c)
    print(x_train.shape)
    y_train = Y.reshape(m, r*c)
    print(y_train.shape)

    model = Sequential()
    
    model.add(Dense(int(r*c/2), activation='relu'))
    model.add(Dense(int(2*r*c), activation='relu'))
    model.add(Dense(int(3*r*c), activation='relu'))
    model.add(Dense(r*c, activation='relu'))
    
##    sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose = 1)
    
    model_json = model.to_json()
    
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
        # serialize weights to HDF5
        model.save_weights("model.h5")
        print("Saved model to disk")
 
"""
 
if __name__ == '__main__':
    my_file = 'D:/BTP/BTP Arpita/SST-2008.nc'

    fh = Dataset(my_file, mode='r')

    lons = fh.variables['lon'][:]
    lats = fh.variables['lat'][:]
    sst = fh.variables['sst'][:]
    time = fh.variables['time'][:]
    sst_units = fh.variables['sst'].units


#    sst[sst==None]=0
    sst = np.asarray(sst)
    print (sst.shape)
     #converting from 4d to 3d
    m,n=sst.shape[::2]
    sst_new=sst.transpose(0,3,1,2).reshape(m,-1,n) 
    print (sst_new.shape)
    #transpose to get the lat and long at right place
    sst_new=np.transpose(sst_new, (0, 2, 1))
    print (sst_new.shape)
    
    
    sst1_new=sst_new[1]
    sst1_new=np.rot90(sst1_new)
    sst1_new=np.rot90(sst1_new)
    
    sst2_new=sst_new[2]
    sst2_new=np.rot90(sst2_new)
    sst2_new=np.rot90(sst2_new)

    
    sst1_new[sst1_new==-999]=np.nan
    sst2_new[sst2_new==-999]=np.nan
    sst2_new[sst2_new==np.nan]=23.2222
    plt.imshow(sst1_new,cmap='hot',interpolation='nearest')
    plt.imshow(sst2_new,cmap='hot',interpolation='nearest')

    
    no1=[randint(1, 335) for p in range(0, 25)]
    no2=[randint(1, 86) for p in range(0, 25)]
    no3=[randint(1, 119) for p in range(0, 25)]
    X1=sst_new
    X1[no1,no2,no3]=np.nan
#    train(X1, sst_new)
    sst3_new=sst2_new
    #sst3_new[np.isnan(sst3_new)]=23
    
    

    
