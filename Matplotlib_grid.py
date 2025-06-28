import matplotlib.pyplot as plt
import numpy as np
plotx = np.array([0, 5,5,7,12,3, 2, 1])
ploty = np.array([2, 8, 3, 6, 4, 5, 9, 10])
plt.title('Grid Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(plotx,ploty)
plt.grid(True)  # Enable grid
plt.show()  # Display the plot with grid