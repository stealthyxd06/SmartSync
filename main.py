import tkinter as tk
import subprocess


#### GUI ####
# Main Part #


import tkinter as tk




def mainscript():
    
    color_var = tk.StringVar()
    color_var.set("white")

    label = tk.Label(root, text="Welcome to SmartSync.", bg=color_var.get())
    label.pack()
    
root = tk.Tk()

root.geometry("800x600")

root.title("Smart Sync")











# Scripts #
def youtube():
    subprocess.run(["python", "C:/Users/WIJA0601/OneDrive - IT-Enheten SML/Skrivbordet/SmartSync/commands/youtube.py"])

def github():
    subprocess.run(["python", "C:/Users/WIJA0601/OneDrive - IT-Enheten SML/Skrivbordet/SmartSync/commands/github.py"])


def open_cmd():
    subprocess.run(["python", "C:/Users/WIJA0601/OneDrive - IT-Enheten SML/Skrivbordet/SmartSync/commands/cmd.py"])

# Buttons #

button = tk.Button(root, text="Open Youtube", command=youtube)
button.pack()

button2 = tk.Button(root, text="Open Github", command=github)
button2.pack()

button3 = tk.Button(root, text="Open CMD", command=open_cmd)
button3.pack()




 



root.mainloop()




