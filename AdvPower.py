import os
import tkinter
from tkinter import ttk

# Commands
def placeholder():
    print("it work")

# Window Management
adv = tkinter.Tk()
options = ttk.Frame(adv, padding=20)
tkinter.Label(options, text="AdvPower", font="arial 15 bold").pack()
ttk.Label(options, text="/// made by macchiato ///", font="arial 8 italic").pack()
ttk.Button(options, text="Lock", command=placeholder).pack()
ttk.Button(options, text="Shutdown", command=placeholder).pack()
ttk.Button(options, text="Hibernate", command=placeholder).pack()
ttk.Button(options, text="Restart", command=placeholder).pack()
ttk.Button(options, text="Restart to Advanced Startup", command=placeholder).pack()
ttk.Button(options, text="Restart to BIOS", command=placeholder).pack()
adv.resizable(False, False)
adv.title("AdvPower")
adv.maxsize(450, 450)
options.pack()
adv.mainloop()
