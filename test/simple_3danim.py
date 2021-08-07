
"""
import k3d
import os
import vtk

from k3d.helpers import download

filename = 'surf0.stl'

model_matrix = (
     1.0,  0.0, 0.0, 0.0,
     0.0,  0.0, 1.0, 0.0,
     0.0,  1.0, 0.0, 0.0,
     0.0,  0.0, 0.0, 1.0
)

#reader = vtk.vtkXMLPolyDataReader()
#reader.SetFileName(filename)
#reader.Update()

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
reader.Update()
geometry_wss = reader.GetOutput()

plot = k3d.plot()
geometry_wss = reader.GetOutput()
plot += k3d.vtk_poly_data(geometry_wss, opacity=0.1, wireframe=True, color=0xaaaaaa)
#cow3d = k3d.vtk_poly_data(reader.GetOutput(), color=0xff0000,
                          #model_matrix=model_matrix)
#plot += cow3d
plot.display()

"""


#python 3 only

import pyvista as pv

# read the data
#grid = pv.read('block.vtm')
surf = pv.read ('cont.vtm')

# plot the data with an automatically created Plotter
#grid.plot(show_scalar_bar=False, show_axes=False)
surf.plot(show_scalar_bar=False, show_axes=False)

