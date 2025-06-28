import matplotlib.pyplot as plt
import numpy as np
xaxis = np.array([1, 2, 3, 4, 5])
yaxis = np.array([2, 3, 5, 7, 11])
plt.plot(xaxis,yaxis)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()