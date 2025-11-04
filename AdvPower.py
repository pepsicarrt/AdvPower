import os
import tkinter
from tkinter import ttk
from tkinter import messagebox

# Commands
def placeholder():
    tkinter.messagebox.showinfo(title="Works", message="it work")


# Window Management
adv = tkinter.Tk()
options = ttk.Frame(adv, padding=20)
tkinter.Label(options, text="AdvPower", font="arial 15 bold").pack()
ttk.Label(options, text="/// made by macchiato ///", font="arial 8 italic").pack()
ttk.Button(options, text="Sign Out", command=os.system("shutdown /l")).pack()
ttk.Button(options, text="Shutdown", command=os.system("shutdown")).pack()
ttk.Button(options, text="Hibernate", command=os.system("shutdown /h")).pack()
ttk.Button(options, text="Restart", command=os.system("shutdown /r")).pack()
ttk.Button(options, text="Restart to Advanced Startup", command=os.system("shutdown /r /o")).pack()
ttk.Button(options, text="Restart to BIOS", command=os.system("shutdown /r /fw")).pack()
adv.resizable(False, False)
adv.title("AdvPower")
adv.maxsize(450, 450)
options.pack()
adv.mainloop()
