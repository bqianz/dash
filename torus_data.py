import scipy.io
import numpy as np
from scipy.spatial import Delaunay

matfile = 'torus_data.mat'

c, a = 2, 1

u = np.linspace(0, 2*np.pi, 20)
v = np.linspace(0, 2*np.pi, 20)
u,v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()

def tor2cart(u,v):
    x = (c + a*np.cos(v)) * np.cos(u)
    y = (c + a*np.cos(v)) * np.sin(u)
    z = a * np.sin(v)
    return x, y, z

x,y,z = tor2cart(u,v)

# trisurf (surface composed of triangles)
points2D = np.vstack([u,v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

scipy.io.savemat(matfile, mdict={'xyz': (x,y,z), 'simplices':simplices})