#!/usr/bin/python
import os
import sys
import time
import RPi.GPIO as GPIO
import cherrypy
import requests
import atexit
import multiprocessing as mp
import serial

#max_floor
max_floor = 20
floor_per_board = 10
number_board = (((max_floor+2)-(max_floor+2)%floor_per_board)/floor_per_board)+1

Buttom_number_open = (max_floor+1)%floor_per_board)
board_open = (((max_floor+1)-Buttom_number_open/floor_per_board)+1

Buttom_number_close = (max_floor+2)%floor_per_board)
board_close = (((max_floor+2)-Buttom_number_close/floor_per_board)+1

Buttom_number_release = (max_floor+3)%floor_per_board)
board_release = (((max_floor+3)-Buttom_number_release/floor_per_board)+1

os.system('fuser -n tcp -k 8080')

s = requests.Session()

"""
GPIO.setmode(GPIO.BCM)
PB0    = 18     #Floor 1
PB1    = 23     #Floor 2
PB2    = 24     #Floor 3
PB3    = 25     #Floor 4
PB4    = 8      #Floor 5
PB5    = 7      #Floor 6
PB6    = 12     #Floor 7
PB7    = 16     #Floor 8
PB8    = 20     #Open
PB9    = 21     #Close

LED0 = 4        #Floor 1 LED
LED1 = 17       #Floor 2 LED
LED2 = 27       #Floor 3 LED
LED3 = 22       #Floor 4 LED
LED4 = 10       #Floor 5 LED
LED5 = 5        #Floor 6 LED
LED6 = 6        #Floor 7 LED
LED7 = 13       #Floor 8 LED
LED8 = 19       #Open LED
LED9 = 26       #Close LED

GPIO.setwarnings(False)
GPIO.setup(PB0,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(PB1,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(PB2,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(PB3,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(PB4,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(PB5,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(PB6,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(PB7,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(PB8,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(PB9,GPIO.OUT,initial = GPIO.LOW)

GPIO.setup(LED0,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED8,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED9,GPIO.IN, pull_up_down=GPIO.PUD_UP)

"""

def pushbutton(PB_Num,board):
    
    amr_server_flag = False
    publish_counter = 0
    
    try:
	
		usb_write(PB_Num,board)
	"""
        GPIO.output(PB_Num,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(PB_Num,GPIO.LOW)
        time.sleep(0.2)
        
        while GPIO.input(LED_num) == GPIO.LOW:
            time.sleep(0.1)

        # delay a time between two push button actions
        time.sleep(0.5)
            
        GPIO.output(PB_Num,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(PB_Num,GPIO.LOW)
        time.sleep(0.2)
        
        while GPIO.input(LED_num) == GPIO.LOW:
            time.sleep(0.1)

        # open the elevator's doors
        print('Doors open')
        sys.stdout.flush()
        GPIO.output(PB8,GPIO.HIGH)
        GPIO.output(PB9,GPIO.LOW)
        
        # wait for elevator's doors open fully
        time.sleep(4.0)
		
	"""
            
        while (amr_server_flag == False and publish_counter <= 3):
            try:
                publish_counter += 1
                r = s.get('http://192.168.65.202:7070/reached', timeout=10) #AMR Server Address
                amr_server_flag = True
                pb_return_str = "And Reached Floor!"
            except requests.Timeout:
                print('AMR Server Error!!')
                pb_return_str = " And Reached Floor, But AMR Server Error!!"
            except requests.ConnectionError:
                print('Lost connection!Publish reached message again!')
                pb_return_str = "And Reached Floor, but fail to connect to AMR server!"
                time.sleep(10)
            except:
                print('Other exceptions')
                pb_return_str = "And Reached Floor, but something is wrong."
                time.sleep(10)
                
                
        return str(PB_Num) + pb_return_str
    except:
        return str(PB_Num) + " And Reached Floor, but something is wrong!!"

def exit_handler():
    GPIO.cleanup()
    print 'Elevator_server is ending!!'
	
def usb_write(command,board):
    if(board == 1):
        device = serial.Serial('/dev/ttyACM1',9600)
    elif (board == 2):
        device = serial.Serial('/dev/ttyACM2',9600)
    elif (board == 3):
        device = serial.Serial('/dev/ttyACM3',9600)
		
	time.sleep(10)
	device.write(command)
	device.close()

class Elevator_server(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def call(self, floor=0):
	"""
        if(floor == '1'):
            result = pushbutton(PB0,LED0)
        elif (floor == '2'):
            result = pushbutton(PB1,LED1)
        elif (floor == '3'):
            result = pushbutton(PB2,LED2)
        elif (floor == '4'):
            result = pushbutton(PB3,LED3)
        elif (floor == '5'):
            result = pushbutton(PB4,LED4)
        elif (floor == '6'):
            result = pushbutton(PB5,LED5)
        elif (floor == '7'):
            result = pushbutton(PB6,LED6)
        elif (floor == '8'):
            result = pushbutton(PB7,LED7)
        elif expression:
            pass	
	"""
		floor_demand = int(floor)
		
		Buttom_number = (floor_demand)%floor_per_board)
		board = (((floor_demand)-Buttom_number/floor_per_board)+1
		
		pushbutton(Buttom_number,board)
        
        print "Request push " + floor + " floor!!"

        return "PUUUUUUSH PB ", board, Buttom_number
    
    @cherrypy.expose
    def open(self):
	"""
        GPIO.output(PB8,GPIO.HIGH)
        GPIO.output(PB9,GPIO.LOW)
	"""
	
		usb_write(Buttom_number_open,board_open)
        return "Open Sesame!"

    @cherrypy.expose
    def close(self):
	"""
        GPIO.output(PB9,GPIO.HIGH)
        GPIO.output(PB8,GPIO.LOW)
        time.sleep(2)
        GPIO.output(PB9,GPIO.LOW)
	"""
	
		usb_write(Buttom_number_close,board_close)
	
        return "When God closes a door, he opens a window!"

    @cherrypy.expose
    def release_button(self):
	"""
        GPIO.output(PB8, GPIO.LOW)
        GPIO.output(PB9, GPIO.LOW)
	"""
		usb_write(Buttom_number_release,board_release)
        return "Release Buttons"



if __name__ == '__main__':  
    atexit.register(exit_handler)
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.thread_pool = 30
    cherrypy.quickstart(Elevator_server())
    
