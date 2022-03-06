from m5stack import *
from m5ui import *
from uiflow import *
import time




setScreenColor(0xF5EEF8)

# Salmon
# 0xFA8072	

# Screen size 135 x 240
label0 = M5TextBox(10, 225, "CBR Light Rail", lcd.FONT_Ubuntu, 0x000000, rotate=0)

# East stops
GungahlinEast = M5Circle(77, 10, 5, 0xFA8072, 0x000000)
ManningEast = M5Circle(77, 25, 5, 0xFA8072, 0x000000)
MapletonEast = M5Circle(77, 40, 5, 0xFA8072, 0x000000)
NullarborEast = M5Circle(77, 55, 5, 0xFA8072, 0x000000)
WellEast = M5Circle(77, 70, 5, 0xFA8072, 0x000000)
SandfordEast = M5Circle(77, 85, 5, 0xFA8072, 0x000000)
EpicEast = M5Circle(77, 100, 5, 0xFA8072, 0x000000)
PhillipEast = M5Circle(77, 115, 5, 0xFA8072, 0x000000)
SwindenEast = M5Circle(77, 130, 5, 0xFA8072, 0x000000)
DicksonEast = M5Circle(77, 145, 5, 0xFA8072, 0x000000)
MacarthurEast = M5Circle(77, 160, 5, 0xFA8072, 0x000000)
IpimaEast = M5Circle(77, 175, 5, 0xFA8072, 0x000000)
EloueraEast = M5Circle(77, 190, 5, 0xFA8072, 0x000000)
AlingaEast = M5Circle(77, 205, 5, 0xFA8072, 0x000000)


# West stops
GungahlinWest = M5Circle(57, 10, 5, 0xFA8072, 0x000000)
ManningWest = M5Circle(57, 25, 5, 0xFA8072, 0x000000)
MapletonWest = M5Circle(57, 40, 5, 0xFA8072, 0x000000)
NullarborWest = M5Circle(57, 55, 5, 0xFA8072, 0x000000)
WellWest = M5Circle(57, 70, 5, 0xFA8072, 0x000000)
SandfordWest = M5Circle(57, 85, 5, 0xFA8072, 0x000000)
EpicWest = M5Circle(57, 100, 5, 0xFA8072, 0x000000)
PhillipWest = M5Circle(57, 115, 5, 0xFA8072, 0x000000)
SwindenWest = M5Circle(57, 130, 5, 0xFA8072, 0x000000)
DicksonWest = M5Circle(57, 145, 5, 0xFA8072, 0x000000)
MacarthurWest = M5Circle(57, 160, 5, 0xFA8072, 0x000000)
IpimaWest = M5Circle(57, 175, 5, 0xFA8072, 0x000000)
EloueraWest = M5Circle(57, 190, 5, 0xFA8072, 0x000000)
AlingaWest = M5Circle(57, 205, 5, 0xFA8072, 0x000000)

from time import sleep
import machine
import urequests as requests
import neopixel
import time
import json


try:
  import usocket as socket
except:
  import socket


# R G B
np = neopixel.NeoPixel(machine.Pin(27), 1)



# enable garbage collection
gc.enable()



rawstopdata = requests.get(url='https://raw.githubusercontent.com/rolly46/CBRTramTrace/main/tramdata.json')
jsonstopdata = json.loads(rawstopdata.text)
    

debugstring = M5TextBox(15, 10,"starting...", lcd.FONT_Ubuntu, 0x000000, rotate=90)

def writetoscreen():
    for stop in jsonstopdata:
      if (jsonstopdata[stop]["trampresent"] == True): # set to black (on)
        updatecircle = str(jsonstopdata[stop]["id"])
        eval(updatecircle).setBgColor(0x000000)
      elif (jsonstopdata[stop]["trampresent"] == False):
        normalcircle = str(jsonstopdata[stop]["id"])
        # eval(normalcircle).setBgColor(0xFA8073) doesnt work need it to to reset the coloring if there is no train at the station now
        
        
        
        
        # currentcircle2 = str(jsonstopdata[stop]["id"]) # set to salmon (off)
        # # eval(currentcircle2).setBgColor(0xFA8072)
        
    
        
        
        


# loop to update lightrail info
while True : 
    M5Led.on()
    debugstring.setText("Fetching data...")
#     get the new data 
    res = requests.get(url='http://www.data.act.gov.au/resource/4f7h-bvpk.json')
    jsoncars = json.loads(res.text)
    M5Led.off()

    debugstring.setText("Fetched")
    
    # reset all the trampresent values TODO
    
#     update arrays
    for car in jsoncars:
        if (car['currentstatus'] == "STOPPED_AT"):
            stopid = int(car['stopid'])
            
            for stop in jsonstopdata:
              if (int(stop) == int(stopid)):
                jsonstopdata[stop]["trampresent"] = True
              else: #reset possible
                jsonstopdata[stop]["trampresent"] = False
              

            
    # printarraytoscreen
    # listToStr = ' '.join([str(elem) for elem in westledstatus])
    # debugstring.setText(listToStr)
    writetoscreen()
    
    
    

    
 
        

    
#     sleep 
    time.sleep(5)
    

    
    


def writetoled():
#         pin, numofleds
    strip = neopixel.NeoPixel(machine.Pin(26), 30)
    for index, val in enumerate(ledstatus):
        rgbvalue = (0,0,0)
        if val == 1: # east side car at light rail stop
            rgbvalue = (0,0,255)
            strip[index] = rgbvalue
        elif val == 2: # west siide car at light rail stop
            rgbvalue = (0,255,0)
            strip[index] = rgbvalue
        elif val == 3: # west siide car at light rail stop
            rgbvalue = (148,0,211)
            strip[index] = rgbvalue
    strip.write()
  
  




