# Red flash patterns
Children directories contain CSV patterns that define the color of each frame.
Each pattern is a CSV file with values defined for each color channel.
Currently, the project only has colors defined using sRGBA with 8 bits per channel.

These patterns are primarily used to test red flashes,
where one state is (or is close to) "saturated red" and
alternating states differ in chromaticity from the saturated red color(s).


| Directory | Description of contents | Flash type | Frame rate (fps) | Color | Dynamic Range | iso |itu_r1702 | ofcom | trace24 | wcag2 | nab_j |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30fps | Patterns for testing single-area red flashing at 30 fps for standards with a 3-flashes/s flash count threshold | Red | 30 | sRGB | SDR | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
