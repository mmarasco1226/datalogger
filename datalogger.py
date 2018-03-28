#drone data logger using sene hat
#!/usr/bin/env python

from sense_hat import SenseHat
from datetime import datetime
from csv import writer

sense = SenseHat()
sense.show_message("ready")



def get_sense_data():
    sense_data = []

    t = sense.get_temperature()
    #convert C to F
    tf = 9/5 * t + 32
    p = sense.get_pressure()
    h = sense.get_humidity()

    tf = round(tf, 1)
    p = round(p, 1)
    h = round(h, 1)

    sense_data.append(tf)
    sense_data.append(p)
    sense_data.append(h)

    orientation = sense.get_orientation()
    y = orientation["yaw"]
    p = orientation["pitch"]
    r = orientation["roll"]

    y = round(y, 1)
    p = round(p, 1)
    r = round(r, 1)
    
    sense_data.append(y)
    sense_data.append(p)
    sense_data.append(r)

    mag = sense.get_compass_raw()
    x = mag["x"]
    y = mag["y"]
    z = mag["z"]

    x = round(x, 1)
    y = round(y, 1)
    z = round(z, 1)

    sense_data.append(x)
    sense_data.append(y)
    sense_data.append(z)

    acc = sense.get_accelerometer_raw()
    x = acc["x"]
    y = acc["y"]
    z = acc["z"]

    x = round(x, 1)
    y = round(y, 1)
    z = round(z, 1)

    sense_data.append(x)
    sense_data.append(y)
    sense_data.append(z)

    gyro = sense.get_gyroscope_raw()
    x = gyro["x"]
    y = gyro["y"]
    z = gyro["z"]

    x = round(x, 1)
    y = round(y, 1)
    z = round(z, 1)

    sense_data.append(x)
    sense_data.append(y)
    sense_data.append(z)

    sense_data.append(datetime.utcnow())

    return sense_data

#while True:
#    print(get_sense_data())

now = datetime.now()

with open('data%s.csv' %now, 'w', newline='') as f:
    data_writer = writer(f)

    

    data_writer.writerow(['temp F', 'pres', 'hum',
                          'yaw', 'pitch', 'roll',
                          'mag_x', 'mag_y', 'mag_z',
                          'acc_x', 'acc_y', 'acc_z',
                          'gyro_x', 'gyro_y', 'gyro_z',
                          'datetime'])


    while True:
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'middle':
                sense.show_message("recording data")
                
                while True:
                    try:
                        
                        data = get_sense_data()
                        data_writer.writerow(data)

                    except Exception as e:
                        return 'Error occured : ' + str(e)
                    
        



    
    
    

    
