# PyPlot interactive 3D

is a jupyter notebook for portable loading and visualizing, currently, MultiBlock (.vtm) and STL files.

## Overview

In this script I tried to find a workaround for interactive visualization of generated results by e.g. [OpenFOAM][OF], namely **vtm** and **stl** files, in a portable format (e.g. .html file). The notebook file uses [vtk][vtk], [k3d][k3d] and [pyvista][pyvista] modules for handling and visualization of the files. This script is originally written in **2020**, and the choice of packages are based on performance of available ones at the time.

## Dependencies and tested versions

- [k3d] (2.6.9)
- [pyvista] (0.37.0)
- [vtk] (9.2.2)

> &#10158; **_NOTE:_** updated `interpolate` function in the latest version of k3d (2.14) makes the contours and stls distorted.

> **Note**  
This step is required for interactive objects only

## Examples

Click the link bellow to see an example of generated html file.

- [Sandia flame D][sandiaD]

## Author
- [Ali Shahanaghi](https://github.com/Ali-Shaha)

[OF]: https://openfoam.org/
[vtk]: https://gitlab.kitware.com/vtk/vtk
[k3d]: https://github.com/K3D-tools/K3D-jupyter
[pyvista]: https://docs.pyvista.org/
[sandiaD]: https://htmlpreview.github.io/?https://github.com/Ali-Shaha/PyPlot_Interactive_3d/blob/main/examples/sandiaFlameD/volume.html
