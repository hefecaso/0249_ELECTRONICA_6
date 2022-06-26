import ISS_Info
import turtle
import time
import threading

import math
import time
from datetime import datetime
import ephem

screen = turtle.Screen()
screen.title("ISS Rastreador")
screen.setup(1146,573)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.color()
iss.penup()


def tracker():
    while True:
        try:
            location = ISS_Info.iss_current_loc()
            lat = location['iss_position']['latitude']
            lon = location['iss_position']['longitude']
            screen.title("ISS TRACKER: (Latitude: {},  Longitude: {})".format(lat,lon))
            iss.goto(float(lon),float(lat))
            iss.dot()
            degrees_per_radian = 180.0 / math.pi
            home = ephem.Observer()
            home.lon = '-90.51327'   # +E
            home.lat = '14.64072'      # +N
            home.elevation = 1729 # meters
            # Always get the latest ISS TLE data from:
            # http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
            iss_1 = ephem.readtle('ISS',
                '1 25544U 98067A   22162.52439360  .00005833  00000+0  11028-3 0  9998',
                '2 25544  51.6455   4.6361 0004468 222.6641 220.6469 15.49954017344301'
            )
            home.date = datetime.utcnow()
            iss_1.compute(home)
            Angulo_Elevacion = '%4.1f' % (iss_1.alt * degrees_per_radian)
            Azimut =  '%5.1f' % (iss_1.az * degrees_per_radian)
            print('Angulo de Elevacion:', Angulo_Elevacion ,', Azimut:', Azimut)
            time.sleep(5)
        except Exception as e:
            print(str(e))

t = threading.Thread(target=tracker())
t.start()
