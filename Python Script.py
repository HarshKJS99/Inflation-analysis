
# Import necessary Python Libraries
import csv
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Generating the Random Data for Inflation Rate over years 1900 - 2022 using NumPy
header = ['year', 'inflation']
data = []
for yr in range(1900, 2023):
    infl = round(np.random.uniform(0.0, 10.0), 2)
    data.append([yr, infl])

# Writing the Generated Data to the file
with open('inflationData.csv', 'w', encoding='UTF8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(header)
    writer.writerows(data)

# Read the Data from the file
df = pd.read_csv('inflationData.csv')


# Determine the Range for Years on the x Axis
length = list(df.shape)[0]
xstart = int(df.iloc[0][0])
xend = xstart + length

initial = 0

v = df[initial:120]
l = list(v.inflation)

# Determine the Range for the Inflation Rate on the y Axis
ystart = math.floor(min(l))
yend = math.ceil(max(l))

# Plotting the Axes
fig = plt.figure()
ax = plt.axes(xlim = (xstart, xend), ylim = (ystart, yend))
line, = ax.plot([], [], lw = 2)

# Initialising the Graph
def init():
    line.set_data([],[])
    return line,

# Function For Cotinuously Plotting the Graph and Get the Maximum and Minimum for the 30 Years Time frame
a = 0;
def animate(i):
    global a
    b = a * 30
    a = a + 1;
    if(b + xstart) > xend :
        b = xend
        a = 0

    
    v = df[initial:b]
    x = v.year
    y = v.inflation
    line.set_data(x, y)            # Plotting the Values Continuously
    l = list(v.inflation)
    upperlimit = b + 1900
    if(upperlimit) > 1900 + length:
        upperlimit = 1900 + length

    # Getting Maximum and Minimum values for 30 Years Time Timeframe
    if(len(l) > 2):
         print("For years ",1900 + (b - 30), " to ", upperlimit )
         print("Max Inflation Rate = ", max(l))
         print("Min Inflation Rate = ", min(l))
         print("")
    return line,

# Execute the Animation
ani = FuncAnimation(fig, animate, init_func = init, frames = list(df.shape)[0], interval = 1000, repeat = True, blit = True)

# Labeling The Axis and Title
plt.xlabel("Year")
plt.ylabel("Inflation Rate")              
plt.title("Inflation Rate over years")

plt.show()






