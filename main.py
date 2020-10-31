import time
import datetime
import playsound
import random

def checktime():
    while True:
        d = datetime.datetime.now()
        month = d.month
        day = d.day
        hour = d.hour
        time.sleep(300)
        if month == 10 and day == 31 and hour in range(7):
            playsounds()
def playsounds():
    n = random.randint(1,8)
    playsound( str(n) + '.mp3')

checktime()
