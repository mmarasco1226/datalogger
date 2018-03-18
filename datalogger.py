from sense_hat import SenseHat
from datetime import datetime
from csv import writer

sense = SenseHat()

def get_sense_data():
    sense_data = []

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    

    
