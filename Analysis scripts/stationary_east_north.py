import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statistics import stdev
#readind a csv file
data = pd.read_csv('stationary data -3pm-GPS_Puck_Message.csv')
easting=data['.utm_easting']
northing=data['.utm_northing']
altitude=data['.altitude']
fig=plt.figure()
myaxes=fig.add_axes([0,0,1,1])
myaxes.plot(easting,northing,'o', lw='3')


print('Standard Deviation of UTM_Easting:',stdev(easting))
print('Standard Deviation of UTM_Northing',stdev(northing))


#Labeling the plot
myaxes.set_title('Stationary Data (Easting-Northing)')
myaxes.set_xlabel('UTM_Easting(Meter)')
myaxes.set_ylabel('UTM_Northing(Meter)')

