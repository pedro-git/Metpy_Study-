import matplotlib.pyplot as plt
import numpy as np 
from metpy import plots


x = np.arange(100)
y = np.random.random(100)

fig = plt.figure(figsize=(10,7.5))
ax = fig.add_subplot(1,1,1)
ax.scatter(x,y,color="red")

plots.add_metpy_logo(fig, x=30)
plots.add_unidata_logo(fig, x=420, size="large" )
plots.add_timestamp(ax,y=1.01)

plt.show()