# fill-missing-values-SST
A sea surface temperature (SST) data from the NOAA AVHRR data is reconstructed for various percentage of missing values spread to check the algorithm’s utility. The objective of the project is to:
* filling in the missing values of SST using matrix factorization algorithm.
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

## Result
The algorithm is computationally less expensive but has its own limitation. The model worked well for smaller patches up to 12 % of the missing values. Considering a single patch, the model gave good result up to 5% of the missing values.


<img width="337" alt="image" src="https://user-images.githubusercontent.com/12899164/233885048-c414854c-3cc8-4076-b55e-97be7c779f73.png">
Chlorophyll Image retrieved from Oceansat-2 Satellite Data


