import sys
import datetime
import time
import requests

hourMatch = int(sys.argv[1])
minuteMatch = int(sys.argv[2])
#secondMatch = int(sys.argv[3])
state = int(sys.argv[3])

while True:
    hr = int(datetime.datetime.now().strftime("%H"))
    mn = int(datetime.datetime.now().strftime("%M"))
#    sc = int(datetime.datetime.now().strftime("%S"))
    if hr == hourMatch:
        if mn == minuteMatch:
            if state == 0:
                requests.get("http://127.0.0.1/heateroff")
                break
            elif state == 1:
                requests.get("http://127.0.0.1/heateron")
                break
