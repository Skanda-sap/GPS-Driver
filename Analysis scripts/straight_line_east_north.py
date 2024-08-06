import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#readind a csv file
data = pd.read_csv('straight_line_data 2:03pm-GPS_Puck_Message.csv')
easting=data['.utm_easting']
northing=data['.utm_northing']
altitude=data['.altitude']
fig=plt.figure()
myaxes=fig.add_axes([0,0,1,1])
myaxes.plot(easting,northing,'r', lw='3')

#Labeling the plot
myaxes.set_title('straight line data')
myaxes.set_xlabel('UTM_Easting (Meter)')
myaxes.set_ylabel('UTM_Northing (Meter)')
#Slope(m) and Y intercept(c) calculation
m, c = np.polyfit(easting, northing,1)
plt.plot(easting, m*easting + c)
new_northing=[]
#updating Y (northing) values
for i in data['.utm_easting']:
    new= m*i+c
    new_northing.append(new)
#finding values of error terms
error_par = new_northing - northing
#square of the error terms
error_square= pow(error_par,2)
#sum of error_sqaure's
error_sum=sum(error_square)
#dividing the error value by number of total observations 
error=error_sum/119
print("Mean Squared Error in square meter is",error)
Root_mean_error_square= pow(error,0.5)
print("Root Mean Square Error in meter is",Root_mean_error_square)

