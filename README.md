# fill-missing-values-SST
A sea surface temperature (SST) data from the NOAA AVHRR data is reconstructed for various percentage of missing values spread to check the algorithm’s utility. The objective of the project is to:
* filling in the missing values of SST using matrix factorization algorithm and CNN.
* see how does the algorithm responds to different spread of cloud coverage. 

## Why Sea Surface Temperature?
SST provides fundamental information on the global climate system. It is an essential parameter in weather prediction and atmospheric model simulations, and study of marine ecosystems. SST measurements benefit numerous applications, such as climate monitoring, military operations, evaluation of coral bleaching, tourism, and commercial fisheries management. Thus is there an inherent economic benefit. 

## Problem
SST data is captured using satellites. However, these SST data are often influenced by the presence of clouds in the atmosphere, malfunctions in the satellite or images noises, which can cause missing data.

## Data

The data is obtained from Indian National Centre for Ocean Information Services Data Center.

* Spatio-temporal data with a resolution of  0.25° X 0.25°
* Geographic area covered is 60–90°E and 20°N–2°S

The average loss of this data set is about 86%. Temporal variability of total missing data presents an irregular distribution with minimum average missing data of about 40% to 60% and maximum average missing data of more than 90%. Typical missing data sizes are comparative large, covering most of the experimental area at a time.


## Solution
* Matrix factorization algorithm for determination of missing values
* Convolutional Neural Network (trade-off with 2 and 3 hidden layer)

## Result
The algorithm is computationally less expensive but has its own limitation. The model worked well for smaller patches up to 12 % of the missing values. Considering a single patch, the model gave good result up to 5% of the missing values.
* Matrix Factorization Algorithm

<img width="484" alt="sst_matrix" src="https://user-images.githubusercontent.com/12899164/236991861-f90bb852-0bda-41f1-a15a-269a1cbfd105.png">


* Convolutional Neural Network

<img width="485" alt="sst_cnn" src="https://user-images.githubusercontent.com/12899164/236991826-f9a1dacb-311e-43f6-9ca8-0b537cf476fd.png">


### Sea Surface Temperature Heat Map (AVHRR Data)

![sst_AVHRR](https://user-images.githubusercontent.com/12899164/236992124-53b4100c-aaca-488b-bf8d-f86ff1857daf.jpg)


