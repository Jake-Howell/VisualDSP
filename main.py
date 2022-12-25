##          Import Libraries 
###############################################
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

##   Create some data to use in the graphs
###############################################

## return 500 sample array between 0 and 2 Pi
x1 = np.linspace(0, 2*np.pi, 500)   
## for each x coord, y = sin(x^2)
y1 = np.sin(x1 ** 2)



##    Create a figure to plot the data on
##############################################
fig, (ax1, ax2) = plt.subplots(2,2)

##      Plot data on each axis
##############################################
ax1[0].plot(x1, y1)
ax1[1].plot(x1, y1)
ax2[0].plot(x1,-y1)
ax2[1].plot(x1, -y1)


##  Set title for each plot
#############################################
ax1[0].set_title('ax1')
ax2[0].set_title('ax2')

##              Display all plots
#############################################
plt.show()

#############################################

