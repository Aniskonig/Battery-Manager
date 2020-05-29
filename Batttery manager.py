import psutil
from playsound import playsound
import threading

def repeater():
  threading.Timer(20.0, repeater).start()
  battery = psutil.sensors_battery()
  plugged = battery.power_plugged
  percent = str(battery.percent)
  if plugged==False: plugged="Not Plugged In"
  else: plugged="Plugged In"
  print(percent+'% | '+plugged)
  if (int(percent) >= 78) and plugged =="Plugged In":
  	playsound('unplug.mp3')
  if (int(percent) <= 42) and plugged!="Plugged In":
    playsound('plugin.mp3')
repeater()

