# -*- coding: utf-8 -*-
import my_sql as mysql
import pandas as pd
from datetime import datetime
import time

# LED https://howtoraspberrypi.com/led-raspberry-pi-2/

#!/usr/bin/python
import sys
import Adafruit_DHT

LED = 31
meteo_sensor = 4

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)

period = 15 #minutes
while True:
    values_ok = False
    n_tries_max = 3
    n_tries = 0
    while (values_ok == False and n_tries<n_tries_max):
        humidity, temperature = Adafruit_DHT.read_retry(11, meteo_sensor)
        if humidity > 0 and temperature > -272:
            measure_time = datetime.now()
            measure_time = measure_time.strftime("%Y-%m-%d %H:%M:%S")
            print(measure_time + ": " + str(temperature) + " °C, " + str(humidity) + " %.")
            query = "INSERT INTO TEMPERATURE (MEASURE_TIME, VALUE) VALUES ('" + str(measure_time) + "', " + str(temperature) + ")"
            mysql.Insert(query)
            query = "INSERT INTO HUMIDITY (MEASURE_TIME, VALUE) VALUES ('" + str(measure_time) + "', " + str(humidity) + ")"
            mysql.Insert(query)
            # Switching on led
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(period*60)
            values_ok = True
        else:
            n_tries += 1
    if values_ok == False:
        print("Error in sensor")
        break
