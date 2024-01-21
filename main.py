import psutil
import tkinter as tk
from tkinter import ttk, messagebox
from playsound import playsound
import threading

root = tk.Tk()


def close_fullscreen():
    if root.winfo_width() == root.winfo_screenwidth() and root.winfo_height() == root.winfo_screenheight():
        root.destroy()


def show_fullscreen_message(message):
    root.attributes('-fullscreen', True)  # Make the window full screen

    label = tk.Label(root, text=message, font=('Helvetica', 24))
    label.pack(expand=True)

    close_button = ttk.Button(root, text="X", command=close_fullscreen)
    close_button.place(relx=1.0, rely=0, anchor='ne')  # Position the button in the top-right corner

    root.mainloop()


def main():
    try:
        threading.Timer(20.0, main).start()
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)

        if (int(percent) >= 78) and plugged:
            playsound('unplug.mp3')
            show_fullscreen_message("Please unplug your laptop charger")
        elif (int(percent) <= 32) and not plugged:
            playsound('plugin.mp3')
            show_fullscreen_message("Please plugin your laptop charger")
        elif ((int(percent) <= 32) and plugged) or ((int(percent) >= 78) and not plugged):
            close_fullscreen()
            playsound('welldone.mp3')
    except Exception as e:
        messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    main()
