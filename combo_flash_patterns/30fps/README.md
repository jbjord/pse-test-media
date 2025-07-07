# Combination (luminance & red) flash patterns 
All source CSV files in this folder are patterns at 30 fps for testing the luminance flash thresholds and red flash thresholds:
> - luminance threshold of 0.1 relative luminance (RL)
> - red flash threshold of
>     - one state a saturated red (where gamma corrected R/(R+G+B) >= 0.8)
>     - each state differs by 0.2 on the u'v' coordinate system of the 1976 UCS chromaticity diagram
> - flash count threshold of >3 flashes per second (i.e., 7 or more alternating transitions)

**Convention:** Filenames that end with 
 - 'fb' - fail both the luminance and thresholds and each sequence fails the count threshold (>3 flash/s)
 - 'fl' - fail the luminance threshold (0.1 RL) and fail count threshold (>3 flash/s), but pass the red thresholds with delta u'v' just less than 0.2 for at least one flash
 - 'fr' - fail the red thresholds and the fail count threshold (>3 flash/s), but pass the luminance thresholds with delta Y just less than 0.1 for at least one flash
 - 'p' - pass



For any failing pattern incorporated into a video, 
all of the other thresholds also need to fail for a video sequence to be 
considered potentially hazardous. 

Note that many of the flashes marked 'f' in this folder would pass the NAB-J standards.
