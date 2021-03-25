from time import sleep
import RPi.GPIO as GPIO
from gpiozero import InputDevice
GPIO.setmode(GPIO.BOARD)
import os
import glob
import time
import pyrebase
from datetime import datetime, timezone
import pytz
config = {
  'apiKey': "AIzaSyDwEVg5DxCaDKmDMNj3AiVMlQzdSZu95yQ",
    'authDomain': "protisruti-6e45e.firebaseapp.com",
    'databaseURL': "https://protisruti-6e45e-default-rtdb.firebaseio.com",
    'projectId': "protisruti-6e45e",
    'storageBucket': "protisruti-6e45e.appspot.com",
    'messagingSenderId': "169084830210",
    'appId': "1:169084830210:web:4788ed7f875010cc6e1d1b",
    'measurementId': "G-L25C5J81ZM"
}



firebase = pyrebase.initialize_app(config)
db = firebase.database()


pin_to_circuit = 11
signal = InputDevice(21)
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


while True:
   
    tz= pytz.timezone('Asia/Dhaka')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    
    
   # print(time_now.timetuple())
    dt = time_now.strftime("%d-%m-%Y"+"-"+"%H:%M:%S")
    c, f = read_temp()
    print('C={:,.3f} F={:,.3f}'.format(c, f))
    abir = rc_time(pin_to_circuit);
    print(rc_time(pin_to_circuit))
    
    if not signal.is_active:
            print("Moisture Detected")
            detected= 1;
    else:
            print("Not Detected")
            detected = 0;
    data = {
         "temp":c,
         "ldr":abir,
         "Moisture":detected,
         "Time": dt,
        }
    

    db.child("Data").child(dt).set(data)
   
    sleep(5)

    