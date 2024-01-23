import psutil
import tkinter as tk
from tkinter import ttk, messagebox
from playsound import playsound
import threading

from PyQt5.QtWidgets import QMessageBox, QApplication
import sys

isTimeForReward = False


def main():
    global isTimeForReward
    print("isTimeForReward", isTimeForReward)
    # try:
    threading.Timer(5.0, main).start()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)

    if (int(percent) >= 78) and plugged:
        playsound('unplug.mp3')
        if not isTimeForReward:
            messagebox.showinfo("Info", "Please unplug your laptop charger")

        isTimeForReward = True
        # show_fullscreen_message("Please unplug your laptop charger")
        # messagebox.showinfo("Info", "Please unplug your laptop charger")

    if (int(percent) <= 32) and not plugged:
        playsound('plugin.mp3')

        if not isTimeForReward:
            messagebox.showinfo("Info", "Please plugin your laptop charger")

        isTimeForReward = True

        # show_fullscreen_message("Please plugin your laptop charger")

    if ((int(percent) <= 32) and plugged) or ((int(percent) >= 78) and not plugged) and isTimeForReward:
        playsound('welldone.mp3')

        isTimeForReward = False
        # close_fullscreen()
    # except Exception as e:
    #     print("Error", str(e))
    #     messagebox.showerror("Error", str(e))
    #     pass


if __name__ == "__main__":
    main()
