import serial
from time import sleep
import sys
import os


COM = "/dev/ttyACM0" #(Linux)
BAUD = 115200

ser = serial.Serial(COM, BAUD, timeout = .1)


print('Waiting for device');
sleep(3)
print(ser.name)

#check args
if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
else:
	monitor= False

while True:
    val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
    valA = val.split("/")
    if(val == "run"):
        print(val)
        os.system("python3 /home/pi/Documents/project/Continuous/camtest.py")
    if(monitor == True):
        print(val, end="\r", flush=True)
