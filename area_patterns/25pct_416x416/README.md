# Spatial patterns for "25% of 416x416 px" threshold
All source images in this folder are patterns for testing the following area threshold:
> Fail where 25% or more of the pixels are involved from any 416 x 416 px subarea

Filenames that start with 'f' are failing (i.e., more pixels than the threshold). 
Those starting with 'a' pass the area threshold.

For any failing spatial pattern incorporated into a video, 
all of the other thresholds also need to fail for a video sequence to be 
considered potentially hazardous.

| File | Description | *f* - Fail area threshold | *a* - Pass area threshold |
| --- | --- | --- | --- |
| *x*001 ... | Single contiguous shape near the middle | ![Failure of a single shape](./thumbnails/f001_on_416x416_fhd_thumb.png) | ![Pass of a single shape](./thumbnails/a001_on_416x416_fhd_thumb.png) |
| *x*002 ... | Single contiguous shape near the corner | ![Failure of a single contiguous shape near the corner](./thumbnails/f002_on_416x416_fhd_thumb.png) | ![Pass of a single contiguous shape near the corner](./thumbnails/a002_on_416x416_fhd_thumb.png) |
| *x*003 ... | Hollow shape | ![Failure of a hollow shape](./thumbnails/f003_on_416x416_fhd_thumb.png) | ![Pass of a hollow shape](./thumbnails/a003_on_416x416_fhd_thumb.png) |
| *x*004 ... | Parallel bars within a 416x416 frame | ![Failure of two parallel bars](./thumbnails/f004_on_416x416_fhd_thumb.png) | ![Pass of two parallel bars](./thumbnails/a004_on_416x416_fhd_thumb.png) |
| *x*005 ... | Two contiguous shapes within a 416x416 frame | ![Failure of 2 contiguous shapes](./thumbnails/f005_on_416x416_fhd_thumb.png) | ![Pass of 2 contiguous shapes](./thumbnails/a005_on_416x416_fhd_thumb.png) |
| *x*006 ... | Diffuse pattern within a 416x416 frame | ![Failure of a diffuse pattern](./thumbnails/f006_on_416x416_fhd_thumb.png) | ![Pass of a diffuse pattern](./thumbnails/a006_on_416x416_fhd_thumb.png) |
| *x*007 ... | Diagonal pattern within a 416x416 frame | ![Failure of a diagonal pattern](./thumbnails/f007_on_416x416_fhd_thumb.png) | ![Pass of a diagonal pattern](./thumbnails/a007_on_416x416_fhd_thumb.png) |
| *x*008 ... | Corner brackets within a 416x416 frame | ![Failure of corner brackets](./thumbnails/f008_on_416x416_fhd_thumb.png) | ![Pass of corner brackets](./thumbnails/a008_on_416x416_fhd_thumb.png) |
| *x*009 ... | Roughly S-shaped figure | ![Failure of S-shape](./thumbnails/f009_on_416x416_fhd_thumb.png) | ![Pass of S-shape](./thumbnails/a009_on_416x416_fhd_thumb.png) |
| *x*010 ... | Parallel bars inside or outside of the frame | ![Failure of parallel bars](./thumbnails/f010_on_416x416_fhd_thumb.png) | ![Pass of parallel bars with one outside the frame](./thumbnails/a010_on_416x416_fhd_thumb.png) |
| *x*011 ... | Shape with an additional dot inside or outside of the frame | ![Failure of a shape with a dot](./thumbnails/f011_on_416x416_fhd_thumb.png) | ![Pass of a shape with a dot outside the frame](./thumbnails/a011_on_416x416_fhd_thumb.png) |
| *x*012 ... | Broader shape with an additional dot inside or outside of the frame | ![Failure of a broad shape and dot](./thumbnails/f012_on_416x416_fhd_thumb.png) | ![Pass of a broad shape with a dot outside the frame](./thumbnails/a012_on_416x416_fhd_thumb.png) |
