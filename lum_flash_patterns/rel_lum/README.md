# Luminance flash patterns for 0.1 relative luminance and >3 flashes/s thresholds
All source images in this folder are patterns for testing the luminance flash thresholds:
> - luminance threshold of 0.1 relative luminance (RL)
> - flash count threshold of >3 flashes per second (i.e., 7 or more alternating transitions)

Filenames that start with 
 - 'f' are failing - fail luminance threshold (0.1 RL) and fail count threshold (>3 flash/s)
 - 'c' are passing - fail luminance threshold (0.1 RL) and pass count threshold (>3 flash/s)
 - 'l' are passing - pass luminance threshold (0.1 RL) and fail count threshold (>3 flash/s)

For any failing pattern incorporated into a video, 
all of the other thresholds also need to fail for a video sequence to be 
considered potentially hazardous.

Note that many of the flashes marked 'f' in this folder would pass the NAB-J strandards.

## Patterns
Representations of temporal-color patterns.

### 30 fps tests

| Scheme | Description | *f* - Failure | *l* - Lum. Pass | *c* - Flash Count Pass |
| --- | --- | --- | --- | --- |
| *x*00*n*_ srgba. csv | 6 or 7 quick transitions right away | ![Failure with 7 quick transitions](./documentation/f00n_srgba.svg) | ![Low luminance pass with 7 quick transitions](./documentation/l00n_srgba.svg "Image Title") | ![Count pass with 6 quick transitions](./documentation/c00n_srgba.svg "Image Title") |
| *x*r00*n*_ srgba. csv | 6 or 7 quick transitions right away (reversed polarity) | ![Failure with 7 quick transitions (reversed polarity)](./documentation/fr00n_srgba.svg) | ![Low luminance pass with 7 quick transitions (reversed polarity)](./documentation/lr00n_srgba.svg "Image Title") | ![Count pass with 6 quick transitions (reversed polarity)](./documentation/cr00n_srgba.svg "Image Title") |
