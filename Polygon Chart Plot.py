import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches
import random

# Number of sides for the polygon
num_sides = 5
# Generate random coordinates for the polygon vertices
a = np.random.rand(num_sides, 2)
# Create a Polygon object with the random coordinates
polygon = matplotlib.patches.Polygon(a, fill=False)

# Create a figure with a polar subplot
fig = plt.figure()
polar = fig.add_subplot(111, projection='polar')

# Add the Polygon to the polar plot
polar.add_patch(polygon)

# Autoscale the plot
#polar.autoscale()

plt.show()
