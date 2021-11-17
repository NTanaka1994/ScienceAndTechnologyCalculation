#ArtistAnimation
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
import matplotlib.animation as animation

def generate(X, Y, phi):
    return np.cos((X)**2+(Y)**2-phi)*0.95**(X*X+Y*Y)
    

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make the X, Y meshgrid.
coords=np.linspace(-4,4,200)
X,Y=np.meshgrid(coords,coords)

# Set the z axis limits so they aren't recalculated each frame.
ax.set_zlim(-1, 1)

#animation function
phi = np.linspace(0, 180. / np.pi, 50)
ims = []
for i in range(50):
    at_z = phi[i]
    Z = generate(X,Y,at_z)
    im = ax.plot_wireframe(X, Y, Z, cmap="rainbow",rstride=1, cstride=1,linewidth=0.1)
    ims.append([im])   
    
ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save('test_wave.gif',writer="ffmpeg")
HTML(ani.to_html5_video())
