# Spatial patterns for "25% of 416x416 px" threshold
All source images in this folder are patterns for testing the following area threshold:
> Fail where 25% or more of the pixels are involved from any 416 x 416 px subarea

Filenames that start with 'f' are failing (i.e., more pixels than the threshold). 
Those starting with 'a' pass the area threshold.

For any failing spatial pattern incorporated into a video, 
all of the other thresholds also need to fail for a video sequence to be 
considered potentially hazardous.