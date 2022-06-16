import ISS_Info
import turtle
import time
import threading

screen = turtle.Screen()
screen.title("ISS TRACKER")
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.penup()

def tracker():
    while True:
        try:
            location = ISS_Info.iss_current_loc()
            lat = location['iss_position']['latitude']
            lon = location['iss_position']['longitude']
            screen.title("ISS TRACKER: (Latitude: {},  Longitude: {})".format(lat,lon))
            iss.goto(float(lon),float(lat))
            time.sleep(5)
        except Exception as e:
            print(str(e))
            break

t = threading.Thread(target=tracker())
t.start()
