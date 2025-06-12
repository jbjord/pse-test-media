# Red flash patterns at 30fps for 0.2 chromaticity difference and >3 flashes/s thresholds
All source CSV files in this folder are patterns for testing the red flash thresholds:
> - saturated red state where `R / (R + G + B) >= 0.8`
> - chromaticity difference threshold of 0.2 in u'v' chromaticity space (on the 1976 UCS chromaticity diagram) 
> - flash count threshold of >3 flashes per second (i.e., 7 or more alternating transitions)

Filenames that start with 
 - 'f' are failing - each red flash returns to a saturated red state along with failing chromaticity difference threshold (0.2) and failing count threshold (>3 flash/s)  
 - 'c' are passing - each red flash returns to a saturated red state along with failing chromaticity difference threshold (0.2) and *passing <u>c</u>ount threshold* (>3 flash/s)
 - 's' are passing - where *not all red flashes return to a <u>s</u>aturated red state* along with failing chromaticity difference threshold (0.2) and failing count threshold (>3 flash/s)
 - 'd' are passing - each red flash returns to a saturated red state along with a *passing chromaticity <u>d</u>ifference threshold* (<0.2 for at least one flash) and failing count threshold (>3 flash/s)  

For any failing pattern incorporated into a video, 
all of the other thresholds also need to fail for a video sequence to be 
considered potentially hazardous.

Note that many of the flashes marked 'f' in this folder would pass the NAB-J standards.

## Patterns 
Descriptions of temporal-color patterns.

### Simple, dual-color tests
These tests alternate between a single red color and non-red color.

| Naming Scheme | General Description | *f* - Failure | *c* - Lum. Pass | *s* - Flash Count Pass | *d* - Single Lum. Pass |
| --- | --- | --- | --- | --- | --- |
| *x*00*n*_simple.csv | 6 or 7 quick transitions right away between varying red and not-red states (multicolor) | Failure with 7 quick transitions | Pass with only 6 quick transitions | Pass where one flash does not return to a saturated red state | Pass where one transition does not exceed the 0.2 chromaticity difference threshold | 
| *x*01*n*_simple.csv | Evenly spaced (nearly so) quick flashes between varying red and not-red states (multicolor) | Failure with 4 quick, evenly-spaced flashes | Pass with quick, evenly-spaced flashes, where the fourth flash is outside the one-second period with the first | Pass with quick, evenly-spaced flashes, where one red state is not a "saturated red" | Pass with quick, evenly-spaced flashes, where one transition does not exceed the 0.2 chromaticity difference threshold | 
| *x*02*n*_simple.csv | Square wave (nearly so) between varying red and not-red states (multicolor) | Failure with a rough square wave | Pass with a rough square wave, where the start of the fourth flash is outside the one-second period with the first | Pass with a rough square wave where one red state is not a saturated red | Pass with a rough square wave, where one transition does not exceed the 0.2 chromaticity difference threshold | 

### Multi-color tests
These tests do not use the same color for the red states and non-red states.

| Naming Scheme | General Description | *f* - Failure | *c* - Lum. Pass | *s* - Flash Count Pass | *d* - Single Lum. Pass |
| --- | --- | --- | --- | --- | --- |
| *x*00*n*_multi.csv | 6 or 7 quick transitions right away between varying red and not-red states (multicolor) | Failure with 7 quick transitions | Pass with only 6 quick transitions | Pass where one flash does not return to a saturated red state | Pass where one transition does not exceed the 0.2 chromaticity difference threshold | 
| *x*01*n*_multi.csv | Evenly spaced (nearly so) quick flashes between varying red and not-red states (multicolor) | Failure with 4 quick, evenly-spaced flashes | Pass with quick, evenly-spaced flashes, where the fourth flash is outside the one-second period with the first | Pass with quick, evenly-spaced flashes, where one red state is not a "saturated red" | Pass with quick, evenly-spaced flashes, where one transition does not exceed the 0.2 chromaticity difference threshold | 
| *x*02*n*_multi.csv | Square wave (nearly so) between varying red and not-red states (multicolor) | Failure with a rough square wave | Pass with a rough square wave, where the start of the fourth flash is outside the one-second period with the first | Pass with a rough square wave where one red state is not a saturated red | Pass with a rough square wave, where one transition does not exceed the 0.2 chromaticity difference threshold | 