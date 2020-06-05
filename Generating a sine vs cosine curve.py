import matplotlib.pyplot as plt
import numpy as np
#For simple sine vs cosine curve.
x=np.arange(0,np.pi*4,0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,x,z)
plt.show()
# To make this more difficult, make the graph go from -360° to 360°, with there being a 180° difference between each point on the x-axis.
x=np.arange(-np.pi*4,np.pi*4,0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,x,z)
plt.show()