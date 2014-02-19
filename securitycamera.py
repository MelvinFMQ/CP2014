# Author: Melvin Foo, contact me at foo.mawqing.melvin@gmail.com
# Distribution: Raspbian
# Python: 2.7
# Acknowledgements: Matt Hawkins, Ladyada, Google Drive quick-start , Pygame

import RPi.GPIO as GPIO
import time, os, pygame, pygame.camera, httplib2, pprint
from pygame.locals import *
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

# Set up authentication for Google Drive
# Copy your credentials from the console
CLIENT_ID = '<insert client id>'
CLIENT_SECRET = '<insert client secret>'
# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print('Go to the following link in your browser: ' + authorize_url)
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)
# Create an httplib2.Http object and authorize it with credentials
http = httplib2.Http()
http = credentials.authorize(http)
drive_service = build('drive', 'v2', http=http)

# Set up camera
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0" , (640,480))
cam.start()

# Set up pins
DEBUG = 1
laser_pin = 26 # laser pin
buzzer_pin = 18 # buzzer pin
lamp_pin = 10 # lamp pin (your lighting to light up your environment)
light_sensor = 23 # light sensor
switch_pin = 8 # to turn the camera on or off
GPIO.setmode(GPIO.BOARD) # tell the GPIO use board references

# Set up GPIO for switch to turn on/off security camera
GPIO.setup(switch_pin, GPIO.IN)
GPIO.input(switch_pin)
# Set up GPIO for turning on light 
GPIO.setup(lamp_pin, GPIO.OUT)
# Laser control
GPIO.setup(laser_pin, GPIO.OUT)
# Set up GPIO for buzzer
GPIO.setup(buzzer_pin, GPIO.OUT)

# Function for capturing and naming the images
def capture_img(cam):     
    for i in range(3): # capture 3 images
        # format time using -, if use / will mess up when saving image
        time_instance = time.strftime("%d-%m-%y%I:%M:%S")+'.jpg'
        image = cam.get_image()
        # create a file for Pygame cam to open
        img_holder = open(time_instance, 'w+')
        img_holder.close()
        # actually saving the image
        pygame.image.save(image, time_instance)
        print("capturing image! Suspicious activity!")
        time.sleep(0.5)        

# Function for reading the light sensor
def RCtime(RCpin, cam):    
    reading = 0
    # discharge capacitor 
    GPIO.setup(RCpin, GPIO.OUT) 
    GPIO.output(RCpin, GPIO.LOW) 
    time.sleep(0.1)    
    GPIO.setup(RCpin, GPIO.IN)
    # count loops until voltage across capacitor read high on GPIO
    while not GPIO.input(RCpin):        
        reading += 1
    if reading > 500:
        return True
    else:
        return False
    
# Function for uploading the images to google drive and deleting them afterwards
def upload_img(drive_service):
    # check through the files and give me the list of files
    # change directory if you did not follow tutorial exactly
    files = os.listdir('/home/pi/Desktop/sercam')  
    for img in files:
        if img[-4:] == '.jpg': #only dealing with .jpg files     
            # Insert the image into Google Drive
            media_body = MediaFileUpload(img, mimetype='image/jpg', resumable=True)
            body = {
              'title':'{0}'.format(img),
              'description': 'Suspicious Activty!!!',
              'mimeType': 'image/jpg'
            }

            file = drive_service.files().insert(body=body, media_body=media_body).execute()
            pprint.pprint(file)
            # remove the image 
            os.remove(img)
                      
# Main program loop
while True:     
    if 1 <= int(time.strftime('%X')[:2])<= 6:    
        while 1 <= int(time.strftime('%X')[:2]) <= 6:
            # check if time is within 1 am to 6am. If it is, keep checking if cam is on.            
            if GPIO.input(switch_pin): # if cam is on, check for movement
                # turn on laser
                GPIO.output(laser_pin, GPIO.HIGH)                 
                print("Security camera now on")
                if RCtime(light_sensor, cam):
                    # turn on light
                    GPIO.output(lamp_pin, GPIO.HIGH)
                    capture_img(cam)        
                    # turn on buzzer
                    GPIO.output(buzzer_pin, GPIO.HIGH)
                else:
                    upload_img(drive_service)
                    print("Uploading image")
            else:
                # if user disabled the security cam, sleep for 5 minutes
                # turn off laser
                GPIO.output(laser_pin, GPIO.LOW)
                print("Turning off laser")
                # turn off buzzer
                GPIO.output(buzzer_pin, GPIO.LOW)
                print("Turning off buzzer")
                # turn off light
                GPIO.output(lamp_pin, GPIO.LOW)
                print("Turning off lamp")
                print("Sleeping for 5 seconds...camera off")
                time.sleep(5)
                
    else:
        # if not within time, turn off laser and sleep for 5 minutes
        # turn off laser
        GPIO.output(laser_pin, GPIO.LOW)
        # turn off buzzer
        GPIO.output(buzzer_pin, GPIO.LOW)
        # turn off light
        GPIO.output(lamp_pin, GPIO.LOW)
        print("Sleeping for 60 seconds...not time yet")        
        time.sleep(60)        
