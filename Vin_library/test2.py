# import modules
from tkinter import *
from vininfo import Vin
from tkinter import messagebox


def check_vin():
	try:
		vin = Vin(str(e.get()))
		country.set(vin.country)
		manufacturer.set(vin.manufacturer)
		region.set(vin.region)
		model.set(vin.wmi)
		Plant.set(vin.vds)
		Serial.set(vin.vis)
		year.set(vin.years)
		res.set("SUCCESS")
	except:
		messagebox.showerror("showerror", "VIN not found")


# object of tkinter
# and background set for light grey
master = Tk()
master.configure(bg='light grey')

# Variable Classes in tkinter
country = StringVar()
manufacturer = StringVar()
region = StringVar()
model = StringVar()
Plant = StringVar()
Serial = StringVar()
year = StringVar()
res = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="VIN NUMBER :", bg="light grey").grid(row=0, sticky=W)
Label(master, text="Status :", bg="light grey").grid(row=3, sticky=W)
Label(master, text="Country :", bg="light grey").grid(row=4, sticky=W)
Label(master, text="Manufactures :", bg="light grey").grid(row=5, sticky=W)
Label(master, text="Region :", bg="light grey").grid(row=6, sticky=W)
Label(master, text="Model :", bg="light grey").grid(row=7, sticky=W)
Label(master, text="Plant :", bg="light grey").grid(row=8, sticky=W)
Label(master, text="Serial no:", bg="light grey").grid(row=9, sticky=W)
Label(master, text="Year :", bg="light grey").grid(row=10, sticky=W)


# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=res, bg="light grey").grid(
	row=3, column=1, sticky=W)
Label(master, text="", textvariable=country,
	bg="light grey").grid(row=4, column=1, sticky=W)
Label(master, text="", textvariable=manufacturer,
	bg="light grey").grid(row=5, column=1, sticky=W)
Label(master, text="", textvariable=region,
	bg="light grey").grid(row=6, column=1, sticky=W)
Label(master, text="", textvariable=model,
	bg="light grey").grid(row=7, column=1, sticky=W)
Label(master, text="", textvariable=Plant,
	bg="light grey").grid(row=8, column=1, sticky=W)
Label(master, text="", textvariable=Serial,
	bg="light grey").grid(row=9, column=1, sticky=W)
Label(master, text="", textvariable=year, bg="light grey").grid(
	row=10, column=1, sticky=W)


e = Entry(master)
e.grid(row=0, column=1)

# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Show", command=check_vin)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
