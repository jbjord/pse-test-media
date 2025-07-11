# Sets of videos for testing

| Directory | Description of test | Flash type | Frame rate (fps) | Color | Dynamic Range | iso |itu_r1702 | ofcom | trace24 | wcag2 | nab_j |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30fps_alternating_01 | See if algorithms are correctly counting alternating luminance transitions | Luminance | 30 | sRGB | SDR | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | x |
| broadcast_30fps_01 | Test of simple luminance flashes with no other interference for broadcast | Luminance | 30 | sRGB | SDR | ✔️ | ✔️ | ✔️ | x | x | x |
| broadcast_30fps_inf01 | Test of luminance flashes 2 areas flashing partially in sync or fully out of sync for broadcast | Luminance | 30 | sRGB | SDR | ✔️ | ✔️ | ✔️ | x | x | x |
| broadcast_30fps_combo01 | Test of combined red and luminance flashes with no other interference for broadcast | Red & Luminance | 30 | sRGB | SDR | ✔️ | ✔️ | ✔️ | x | x | x |
| broadcast_30fps_red01 | Test of simple red flashes with no other interference for broadcast | Red |30 | sRGB | SDR | ✔️ | ✔️ | ✔️ | x | x | x |
| broadcast_30fps_red02 | Test of multi-color red flashes with no other interference for broadcast | Red | 30 | sRGB | SDR | ✔️ | ✔️ | ✔️ | x | x | x |
| trace24_30fps_01 | Test of simple luminance flashes with no other interference for trace24 recommendations | Luminance | 30 | sRGB | SDR | x | x | x | ✔️ | x | x |
| trace24_30fps_combo01 | Test of combined red and luminance flashes with no other interference for trace24 recommendations | Red & Luminance | 30 | sRGB | SDR | x | x | x | ✔️ | x | x |
| trace24_30fps_inf01 | Test of luminance flashes with 2 areas flashing partially in sync (interference) for trace24 recommendations | Luminance | 30 | sRGB | SDR | x | x | x | ✔️ | x | x |
| trace24_30fps_red01 | Test of simple red flashes with no other interference for trace24 recommendations | Red |30 | sRGB | SDR | x | x | x | ✔️ | x | x |
| trace24_30fps_red02 | Test of multi-color red flashes with no other interference for trace24 recommendations | Red | 30 | sRGB | SDR | x | x | x | ✔️ | x | x |


Where the following shortcodes represent the following standards:
 - itu-r1702 = [Recommendation ITU-R BT.1702](https://www.itu.int/rec/R-REC-BT.1702/en). Guidance for the reduction of photosensitive epileptic seizures caused by television.
 - ofcom = [Ofcom guidelines](https://www.ofcom.org.uk/siteassets/resources/documents/tv-radio-and-on-demand/broadcast-guidance/programme-guidance/broadcast-code-guidance/section-2-guidance-notes.pdf) Annex 1: Ofcom Guidance Note on Flashing Images and Regular Patterns in Television. In: Ofcom Guidance Notes, Section 2: Harm and offence, pp. 18–21. 
 - iso = [ISO 9241-391 \[non-free standard\]](https://www.iso.org/standard/56350.html). Ergonomics of human-system interaction—Part 391: Requirements, analysis and compliance
test methods for the reduction of photosensitive seizures. 
 - trace24 = [Proposed Photosenstive Epilepsy Guidelines](https://github.com/traceRERC/pseGuidelines) from the TRACE Rehabilitation Engineering Research Center (from [2024 Jordan \& Vanderheiden journal article](https://doi.org/10.1145/3694790))
 - wcag2 = [WCAG 2.2 Success Criterion 2.3.1](https://www.w3.org/TR/WCAG22/#three-flashes-or-below-threshold) Success Criterion 2.3.1 Three Flashes or Below Threshold. In Web Content Accessibility Guidelines (WCAG) 2.2.
 - nab_j = [NAB-J guidelines](https://www.j-ba.or.jp/category/broadcasting/jba103852). アニメーション等の映像手法に関するガイドライン \[Guidelines on video methods such as animation\] by Japan Broadcasting Corporation & Japan Commercial Broadcasters Association.
