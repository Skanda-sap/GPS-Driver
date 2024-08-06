import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statistics import stdev
#readind a csv file
data = pd.read_csv('stationary data -3pm-GPS_Puck_Message.csv')
altitude=data['.altitude']
mean_alt=np.mean(altitude)
print("Mean of altitude in meter:",mean_alt)
time=data['time']
fig=plt.figure()
myaxes=fig.add_axes([0,0,1,1])
myaxes.plot(time,altitude,'o', lw='3')
plt.axhline(y=mean_alt, color='r', linestyle='-')
errors=mean_alt-altitude
error_square= pow(errors,2)
errors_sum=sum(error_square)
error=errors_sum/altitude.size
print('Error in mean',error)
print('Standard deviation of altitude in meter',stdev(altitude))
#Labeling the plot
myaxes.set_title('Stationary Data (Altitude - Time)')
myaxes.set_xlabel('Time (Seconds)')
myaxes.set_ylabel('Altitude (Meters)')
