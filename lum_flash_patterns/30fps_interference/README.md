# Luminance flash patterns with two areas
All source CSV files in this folder are patterns at 30 fps for testing the luminance flash thresholds:
> - luminance threshold of 0.1 relative luminance (RL)
> - flash count threshold of >3 flashes per second (i.e., 7 or more alternating transitions)

Filenames with `"alt"` are hand-adjusted alternatives where at least one flash is out of sync with the non-alt version.

Files without `"alt"` are identical to those in the `../rel_lum/` directory.

These are a limited selection of patterns and do not cover all possible combinations that might be tested.

Filenames that start with 
 - 'f' are failing - fail luminance threshold (0.1 RL) and fail count threshold (>3 flash/s)
 - 'c' are passing - fail luminance threshold (0.1 RL) and pass count threshold (>3 flash/s)
 - 'y' are passing - pass luminance threshold with only one flash in the sequence below threshold (0.1 RL) and fail count threshold (>3 flash/s)



For any failing pattern incorporated into a video, 
all of the other thresholds also need to fail for a video sequence to be 
considered potentially hazardous. 
Area patterns will need to be carefully chosen so that they do not unintentionally sum in area to exceed the area threshold within a 10-degree field of view.

Note that many of the flashes marked 'f' in this folder would pass the NAB-J standards.
