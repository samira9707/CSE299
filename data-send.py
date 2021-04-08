from time import sleep
import RPi.GPIO as GPIO
from gpiozero import InputDevice
from gpiozero import OutputDevice


import os
import glob
import time
import pyrebase
from datetime import datetime, timezone
import pytz
config = {
  'apiKey': "AIzaSyDuEOTHTtVqf3qVHHBjEZJM2u2uStNgAL0",
    'authDomain': "protisruti0.firebaseapp.com",
    'databaseURL': "https://protisruti0-default-rtdb.firebaseio.com",
    'projectId': "protisruti0",
    'storageBucket': "protisruti0.appspot.com",
    'messagingSenderId': "965893934891",
    'appId': "1:965893934891:web:a04fdee508d76df0633f6e",
    'measurementId': "G-BP8GN37Y3R"
}



firebase = pyrebase.initialize_app(config)
db = firebase.database()



# GPIO set



 # Turn motor off


pin_to_circuit = 11
signal = InputDevice(21)
channel= 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
#these tow lines mount the device:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_path = glob.glob(base_dir + '28*')[0] #get file path of sensor
rom = device_path.split('/')[-1] #get rom name

def read_temp_raw():
    with open(device_path +'/w1_slave','r') as f:
        valid, temp = f.readlines()
    return valid, temp
 
def read_temp():
    valid, temp = read_temp_raw()

    while 'YES' not in valid:
        time.sleep(0.2)
        valid, temp = read_temp_raw()

    pos = temp.index('t=')
    if pos != -1:
        #read the temperature .
        temp_string = temp[pos+2:]
        temp_c = float(temp_string)/1000.0 
        temp_f = temp_c * (9.0 / 5.0) + 32.0
        return temp_c, temp_f
 
print(' ROM: '+ rom)
def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly

def motor_off(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
    

def motor_on(pin):
    GPIO.output(pin, GPIO.LOW)
    # Turn motor off
def motor_control(channel):
    if __name__ == '__main__':
        try:
            motor_on(channel)
            time.sleep(5)
            motor_off(channel)
            time.sleep(5)
            GPIO.cleanup()
        except KeyboardInterrupt:
            GPIO.cleanup()
    

while True:
   
    tz= pytz.timezone('Asia/Dhaka')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    
    
   # print(time_now.timetuple())
    dt = time_now.strftime("%d-%m-%Y"+"-"+"%H:%M:%S")
    c, f = read_temp()
    print('C={:,.3f} F={:,.3f}'.format(c, f))
    ldrdata = rc_time(pin_to_circuit);
    print(rc_time(pin_to_circuit))
    
    if not signal.is_active:
            print("moisture detected")
            motor_on(channel)
            time.sleep(1)
            detected =1
    else:
            print("motor off")
            motor_off(channel)
            time.sleep(2)
            detected=0
    data ={
         "temp":str(c),
         "ldr":str(ldrdata),
         "Moisture":str (detected),
         "Time": str (dt),
        }
    

    db.child("Data").child(dt).set(data)
   
    sleep(1)
