import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statistics import stdev
#readind a csv file
data = pd.read_csv('straight_line_data 2:03pm-GPS_Puck_Message.csv')
altitude=data['.altitude']
mean_alt=np.mean(altitude)
print("Mean of altitude in meters",mean_alt)
time=np.arange(0, altitude.size, 1, dtype=int)
fig=plt.figure()
myaxes=fig.add_axes([0,0,1,1])
myaxes.plot(time,altitude,'o', lw='3')
plt.axhline(y=mean_alt, color='r', linestyle='-')
errors=mean_alt-altitude
error_square= pow(errors,2)
errors_sum=sum(error_square)
error=errors_sum/altitude.size
print(error)
print('Standard deviation in meters',stdev(altitude))
#Labeling the plot
myaxes.set_title('Straight Line Walking Data')
myaxes.set_xlabel('Time (Seconds)')
myaxes.set_ylabel('Altitude (Meters)')
