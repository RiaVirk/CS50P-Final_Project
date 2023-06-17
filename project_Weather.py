from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

Search_image = PhotoImage(file="./bar2.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center", width=20,font=("poppins", 20,"bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50,y=46)
textfield.focus()

Search_icon=PhotoImage(file="./search_icon3.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040")
myimage_icon.place(x=350, y=50)

#Logo
Logo_image=PhotoImage(file="./logo.png")
logo=Label(image=Logo_image)
logo.place(x=150, y=100)

#Bottom Box
Frame_image=PhotoImage(file="./box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side="bottom")

#Label

label1=Label(root,text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2=Label(root,text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=225, y=400)

label3=Label(root,text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4=Label(root,text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)










root.mainloop()

# Search Box
