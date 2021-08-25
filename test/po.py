import pyvista as pv
from pyvista import examples

dataset = pv.read('block1.vtm')
clipped = dataset.clip('y', invert=False)
head = examples.download_head()

print(head)

p = pv.Plotter()
#p.add_mesh(dataset, style='wireframe', color='blue', label='Input')
#p.add_mesh(clipped, label='Clipped')
p.add_volume(head, cmap="cool", opacity="sigmoid_6")

#p.add_legend()

p.show() 
