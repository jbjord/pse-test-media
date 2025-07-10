# Luminance flash patterns with two areas for broadcast
All source CSV files in this folder are patterns at 30 fps for testing the luminance flash thresholds for broadcast standards:
> - luminance threshold of 0.1 relative luminance (RL)
> - flash count threshold of >3 flashes per second (i.e., 7 or more alternating transitions)

These patterns are meant to be used in conjunction with the patterns in the `../rel_lum/` directory.
All flashes exceed the 0.1 relative luminance threshold.

Filenames that start with 
 - 'cs' are passing because there are 3 flashes within one second and all flashes are **separated** from the equivalent c*NNN*_srgba.csv in the `../rel_lum/` directory. 
 - 'co' are passing because there are 3 flashes within one second and only **one** flash is out of sync from the equivalent c*NNN*_srgba.csv in the `../rel_lum/` directory.

Flashes that are out of sync are out of sync by two frames or more so that the flashing areas area separated and do not combine in ways that change the properties of the flashing.
