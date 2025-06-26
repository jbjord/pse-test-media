# Luminance flash patterns
Children directories contain CSV patterns that define the color of each frame.
Each pattern is a CSV file with values defined for each color channel.
Currently, the project only has colors defined using sRGBA with 8 bits per channel.

These patterns are primarily used to test luminance flashes.


| Directory | Description of contents | Flash type | Frame rate (fps) | Color | Dynamic Range | iso |itu_r1702 | ofcom | trace24 | wcag2 | nab_j |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30fps_interference | Patterns and slightly de-synchronized patterns for testing two-area flashing at 30 fps for standards that have a 25%-of-a-subset-of-the-screen area threshold | Luminance | 30 | sRGB | SDR | x | x | x | ✔️ | ✔️ | x |
| rel_lum | Patterns for testing single-area flashing at 30 fps for standards with a 3-flashes/s flash count threshold | Luminance | 30 | sRGB | SDR | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | x |
