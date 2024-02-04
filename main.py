import psutil
from tkinter import ttk, messagebox
from playsound import playsound
import threading
import tkinter

root = tkinter.Tk()
isTimeForReward = False


def getIsTimeForReward():
    return isTimeForReward


def setIsTimeForReward(val):
    global isTimeForReward
    isTimeForReward = val


def main():
    threading.Timer(5.0, main).start()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)

    if plugged == False:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"

    if (int(percent) >= 78) and plugged == "Plugged In":
        playsound('unplug.mp3')
        if not getIsTimeForReward():
            setIsTimeForReward(True)

            root.wm_attributes("-topmost", 1)
            root.withdraw()

            tkinter.messagebox.showinfo("Info", "Please unplug your laptop charger")
            root.destroy()

    if (int(percent) <= 35) and plugged != "Plugged In":
        playsound('plugin.mp3')

        if not getIsTimeForReward():
            setIsTimeForReward(True)

            root.wm_attributes("-topmost", 1)
            root.withdraw()

            tkinter.messagebox.showinfo("Info", "Please plugin your laptop charger")
            root.destroy()

    if ((int(percent) <= 32) and plugged) or ((int(percent) >= 78) and not plugged) and getIsTimeForReward():
        setIsTimeForReward(False)
        playsound('welldone.mp3')


if __name__ == "__main__":
    main()
