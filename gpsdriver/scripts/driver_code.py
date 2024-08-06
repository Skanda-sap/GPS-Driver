#!/usr/bin/env python3
import serial
import rospy
import datetime
import utm
from gps_driver.msg import gps

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 4800
linez = []

def utm_s(latitude,longitude):
	return utm.from_latlon(latitude, longitude)
	

global latitude_deg

msg = gps()

def talker():
    pub = rospy.Publisher('GPS_Puck_Message', gps, queue_size=10)
    rospy.init_node('GPS', anonymous=True)
    r = rospy.Rate(10)
       
    while not rospy.is_shutdown():
            
        serialin = str(ser.readline())
        linez = serialin.split("b'")
        coms = linez[1].split(",")
        if coms[0] == "$GPGGA":
            print(coms)
            latitude_gps = float(coms[2])
            latitude_mins = latitude_gps%100
            latitude_degree = int(latitude_gps/100)
            latitude = latitude_degree + (latitude_mins/60)

            longitude_gps = float(coms[4])
            longitude_mins = longitude_gps%100
            longitude_degree = int(longitude_gps/100)
            longitude_ = longitude_degree + (longitude_mins/60)
            longitude = -1*(longitude_)
        
            u=utm_s(latitude,longitude)
            altitude = float(coms[9])
            
            msg.header = coms[0]
            msg.latitude = float(latitude)
            msg.longitude = float(longitude)
            msg.altitude = float(altitude)
            msg.utm_easting = float(u[0])
            msg.utm_northing = float(u[1])
            msg.zone = int(u[2])
            msg.letter = u[3]
            rospy.loginfo(msg)
            pub.publish(msg)
            r.sleep()
if __name__ == '__main__':
    talker()

