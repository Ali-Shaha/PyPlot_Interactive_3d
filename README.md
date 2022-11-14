# PyPlot interactive 3D

is a script for portable loading and visualizing (at the moment) the MultiBlock (.vtm) and STL files.

## Overview

In this script I tried to find a workaround for interactive visualization of generated results by e.g. [OpenFOAM][OF], namely vtm and stl files, in a portable format (e.g. .html file). The notebook file uses [vtk][vtk], [k3d][k3d] and [pyvista][pyvista] modules for handling and visualization of the files. This script is originally written in **2020**, and the choice of packages are based on performance of available ones at the time.

<!-- ## Theory

The system of ordinary differential equations (ODEs) for a constant volume batch reactor can be written as:

$$ \frac{\partial T}{\partial t} = \frac{-1}{\rho c_v} \sum_{k = 1}^{N_{sp}} u_k W_k \dot{\omega_k},$$

$$\frac{\partial Y_k}{\partial t} = \frac{W_k}{\rho} \dot{\omega_k} \;\;k = 1,...,N_{sp}-1$$

where $c_v$ is the mass-averaged constant volume specific heat, $u_k$, $W_k$, and $\dot{\omega_k}$ are internal energy, molecular weight and production rate of the $k$ th species, respectively. In current implementation of the code the density ( $\rho$ ) is assumed to be constant and hence the pressure is updated from the ideal gas equation of state [[1][canteraZeroD],[2][pyJacPaper]].

## Dependencies

cvpyJac requires installation of :
- [Cantera]
- [pyJac]

## Installation

Using the downloaded source code, cvpyJac can be installed as a Python module:
```
> python setup.py install
```

## Usage

cvpyJac can be run as a python module:
```
> python -m cvpyjac [options]
```

The generated source code is placed within the `out` (by default) directory,
which is created if it doesn't exist initially.
See the documentation or use `python cvpyjac -h` for the full list of options. -->

## Author
- [Ali Shahanaghi](https://github.com/Ali-Shaha)

[OF]: https://openfoam.org/
[vtk]: https://gitlab.kitware.com/vtk/vtk
[k3d]: https://github.com/K3D-tools/K3D-jupyter
[pyvista]: https://docs.pyvista.org/
