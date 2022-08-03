import os
import tkinter
from tkinter import *
from tkinter.ttk import *

from time import strftime

x = 0
string = ""
count = True

root = Tk()
root.title("Shutdown Timer")
root.resizable(False, False)

label = Label(root, font=("Arial", 80), background="black", foreground="cyan")
label.grid(row=0, column=0, columnspan=3, padx=3, pady=3)

label1 = Label(root, font=("Arial", 20), background="black", foreground="cyan")


label2 = Label(root, font=("Arial", 20), background="black", foreground="cyan")
label2.grid(row=4, column=2, padx=3, pady=3)


def decrease():
    value = int(lbl_value["text"])
    if value <= 0:
        pass
    else:
        lbl_value["text"] = f"{value - 10}"


def increase():
    value = int(lbl_value["text"])

    lbl_value["text"] = f"{value + 10}"


btn_decrease = tkinter.Button(master=root, text="-10", command=decrease, font=("Arial", 20))
btn_decrease.grid(row=8, column=1, padx=3, pady=3)

lbl_value = Label(master=root, text="{:02}".format(0), font=("Arial", 20), background="black", foreground="cyan")
lbl_value.grid(row=4, column=0, padx=3, pady=3)

minLabel = Label(master=root, text="Minutes", font=("Arial", 20))
minLabel.grid(row=8, column=0, padx=3, pady=3)

btn_increase = tkinter.Button(master=root, text="+10", command=increase, font=("Arial", 20))
btn_increase.grid(row=8, column=2, padx=3, pady=3)


def time():
    global x, string, count
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label1.config(text=difference1(int(lbl_value["text"]) * 60))

    if count:
        show()
        x = timeToSeconds(string) + int(lbl_value["text"]) * 60

    label.after(1, time)


def shutDown():
    global count
    helper = x
    if helper > 0:
        btn_ShutdownStart.config(state=DISABLED)
        btn_increase.config(state=DISABLED)
        btn_decrease.config(state=DISABLED)
        label2.config(text=difference1(helper))
        count = False
        varTimer = "shutdown /s /t " + str(helper - timeToSeconds(string))
        print(varTimer)
        os.system(varTimer)
    else:
        pass


def stopShutdown():
    global x, count

    helper = x
    if helper > 0:
        x = 0
        helper = 0
        btn_ShutdownStart.config(state=ACTIVE)
        btn_increase.config(state=ACTIVE)
        btn_decrease.config(state=ACTIVE)
        lbl_value.config(text="{:02}".format(0))
        label2.config(text=difference1(helper))
        count = True
        os.system("shutdown /a")
    else:
        pass


def show():
    label2.config(text=difference1(x))


btn_ShutdownStart = tkinter.Button(master=root, text="Set", font=("Arial", 20), command=shutDown)
btn_ShutdownStart.grid(row=9, column=1, padx=3, pady=3)
btn_ShutdownStop = tkinter.Button(master=root, text="Reset", font=("Arial", 20), command=stopShutdown)
btn_ShutdownStop.grid(row=9, column=2, padx=3, pady=3)

startStopLabel = Label(master=root, text="Shutdown", font=("Arial", 20))
startStopLabel.grid(row=9, column=0, padx=3, pady=3)


def timeToSeconds(timeString):
    v = timeString.split(":")
    v[0] = int(v[0]) * 3600
    v[1] = int(v[1]) * 60

    return int(v[0]) + int(v[1]) + int(v[2])


def difference(big, small):
    dif = big - small

    minuteness, seconds = divmod(dif, 60)
    hours, minuteness = divmod(minuteness, 60)
    return "{:02}:{:02}:{:02}".format(hours, minuteness, seconds)


def difference1(big):
    minuteness, seconds = divmod(big, 60)
    hours, minuteness = divmod(minuteness, 60)
    return "{:02}:{:02}:{:02}".format(hours, minuteness, seconds)


time()
mainloop()
