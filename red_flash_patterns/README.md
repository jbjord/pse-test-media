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

Selected colors used in sRGB

| Swatch | R | G | B | Hex | Saturated red (r/(r+g+b))| Luminance Y |
| --- | --- | --- | --- | --- | --- | --- |
| ![#CD4E4E](documentation/swatch_CD4E4E.png) | 205 | 78 | 78 | #CD4E4E | **0.8003** | 0.1898 |
| ![#3C8484](documentation/swatch_3C8484.png) | 60 | 132 | 132 | #3C8484 | 0.0892 | 0.1913 |
| ![#1F8686](documentation/swatch_1F8686.png) | 31 | 134 | 134 | #1F8686 | 0.0279 | 0.1906 |
| ![#DC3768](documentation/swatch_DC3768.png) | 220 | 55 | 104 | #DC3768 | **0.8021** | 0.1895 |
| ![#816BC1](documentation/swatch_816BC1.png) | 129 | 107 | 193 | #816BC1 | 0.2440 | 0.1903 |
| ![#776DC5](documentation/swatch_776DC5.png) | 119 | 109 | 197 | #776DC5 | 0.2059 | 0.1889 |
| ![#E90D7A](documentation/swatch_E90D7A.png) | 233 | 13 | 122 | #E90D7A | **0.8040** | 0.1902 |
| ![#C124F1](documentation/swatch_C124F1.png) | 193 | 36 | 241 | #C124F1 | 0.3728 | 0.1895 |
| ![#BE25F8](documentation/swatch_BE25F8.png) | 190 | 37 | 248 | #BE25F8 | 0.3498 | 0.1905 |
| ![#C44A4A](documentation/swatch_C44A4A.png) | 196 | 74 | 74 | #C44A4A | **0.8012** | 0.1713 |
| ![#397D7D](documentation/swatch_397D7D.png) | 57 | 125 | 125 | #397D7D | 0.0907 | 0.1702 |
| ![#1D7F7F](documentation/swatch_1D7F7F.png) | 29 | 127 | 127 | #1D7F7F | 0.0281 | 0.1697 |
| ![#D23463](documentation/swatch_D23463.png) | 210 | 52 | 99 | #D23463 | **0.8020** | 0.1706 |
| ![#7A65B8](documentation/swatch_7A65B8.png) | 122 | 101 | 184 | #7A65B8 | 0.2420 | 0.1691 |
| ![#7168BC](documentation/swatch_7168BC.png) | 113 | 104 | 188 | #7168BC | 0.2048 | 0.1704 |
| ![#DE0B74](documentation/swatch_DE0B74.png) | 222 | 11 | 116 | #DE0B74 | **0.8041** | 0.1703 |
| ![#B822E6](documentation/swatch_B822E6.png) | 184 | 34 | 230 | #B822E6 | 0.3725 | 0.1705 |
| ![#B423EC](documentation/swatch_B423EC.png) | 180 | 35 | 236 | #B423EC | 0.3479 | 0.1696 |
| ![#AD4040](documentation/swatch_AD4040.png) | 173 | 64 | 64 | #AD4040 | **0.8030** | 0.1292 |
| ![#316E6E](documentation/swatch_316E6E.png) | 49 | 110 | 110 | #316E6E | 0.0897 | 0.1293 |
| ![#187070](documentation/swatch_187070.png) | 24 | 112 | 112 | #187070 | 0.0274 | 0.1295 |
| ![#BA2D57](documentation/swatch_BA2D57.png) | 186 | 45 | 87 | #BA2D57 | **0.8016** | 0.1300 |
| ![#6C59A3](documentation/swatch_6C59A3.png) | 108 | 89 | 163 | #6C59A3 | 0.2434 | 0.1298 |
| ![#645BA7](documentation/swatch_645BA7.png) | 100 | 91 | 167 | #645BA7 | 0.2060 | 0.1298 |
| ![#C50966](documentation/swatch_C50966.png) | 197 | 9 | 102 | #C50966 | **0.8046** | 0.1303 |
| ![#A31DCC](documentation/swatch_A31DCC.png) | 163 | 29 | 204 | #A31DCC | 0.3728 | 0.1302 |
| ![#A01ED2](documentation/swatch_A01ED2.png) | 160 | 30 | 210 | #A01ED2 | 0.3484 | 0.1306 |
| ![#8B3232](documentation/swatch_8B3232.png) | 139 | 50 | 50 | #8B3232 | **0.8019** | 0.0800 |
| ![#265858](documentation/swatch_265858.png) | 38 | 88 | 88 | #265858 | 0.0903 | 0.0810 |
| ![#115959](documentation/swatch_115959.png) | 17 | 89 | 89 | #115959 | 0.0273 | 0.0799 |
| ![#952244](documentation/swatch_952244.png) | 149 | 34 | 68 | #952244 | **0.8029** | 0.0795 |
| ![#564683](documentation/swatch_564683.png) | 86 | 70 | 131 | #564683 | 0.2441 | 0.0800 |
| ![#4F4885](documentation/swatch_4F4885.png) | 79 | 72 | 133 | #4F4885 | 0.2071 | 0.0799 |
| ![#9E0551](documentation/swatch_9E0551.png) | 158 | 5 | 81 | #9E0551 | **0.8032** | 0.0797 |
| ![#8215A4](documentation/swatch_8215A4.png) | 130 | 21 | 164 | #8215A4 | 0.3708 | 0.0796 |
| ![#8016A9](documentation/swatch_8016A9.png) | 128 | 22 | 169 | #8016A9 | 0.3478 | 0.0803 |
| ![#652222](documentation/swatch_652222.png) | 101 | 34 | 34 | #652222 | **0.8027** | 0.0403 |
| ![#193E3E](documentation/swatch_193E3E.png) | 25 | 62 | 62 | #193E3E | 0.0917 | 0.0400 |
| ![#093F3F](documentation/swatch_093F3F.png) | 9 | 63 | 63 | #093F3F | 0.0267 | 0.0397 |
| ![#6D1630](documentation/swatch_6D1630.png) | 109 | 22 | 48 | #6D1630 | **0.8027** | 0.0404 |
| ![#3D315E](documentation/swatch_3D315E.png) | 61 | 49 | 94 | #3D315E | 0.2465 | 0.0400 |
| ![#383260](documentation/swatch_383260.png) | 56 | 50 | 96 | #383260 | 0.2099 | 0.0397 |
| ![#730339](documentation/swatch_730339.png) | 115 | 3 | 57 | #730339 | **0.8039** | 0.0401 |
| ![#5E0C77](documentation/swatch_5E0C77.png) | 94 | 12 | 119 | #5E0C77 | 0.3730 | 0.0397 |
| ![#5C0D7B](documentation/swatch_5C0D7B.png) | 92 | 13 | 123 | #5C0D7B | 0.3462 | 0.0399 |







