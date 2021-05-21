import os

def databasesql():
	import sqlite3
	global conn
	conn = sqlite3.connect("BusDatabase.db")
	global c 
	c = conn.cursor()
	c.execute(""" CREATE TABLE bus(bus_id int, service_name varchar(15), source varchar(15), destination varchar(15), fare int) """)
	c.execute(""" INSERT INTO bus VALUES(00001, "GarudaService", "Kadapa", "Bangalore", 380 )""")
	c.execute(""" INSERT INTO bus VALUES(00002, "GarudaService", "Kadapa", "Bangalore", 380 )""")
	c.execute(""" INSERT INTO bus VALUES(00003, "APSRTC Rural", "Kadapa", "Rayachoty", 60 )""")
	c.execute(""" INSERT INTO bus VALUES(00004, "APSRTC Urban", "Kadapa", "Chittor", 250 )""")
	#c.execute(""" INSERT INTO bus VALUES(00005, "Indra AC", "Kadapa", "Bangalore", 300 )""")
	c.execute(""" INSERT INTO bus VALUES(00006, "APSRTC Rural", "Badvel", "Kadapa", 60 )""")
	c.execute(""" INSERT INTO bus VALUES(00007, "APSRTC Rural", "Badvel", "Bangalore", 450 )""")
	c.execute(""" INSERT INTO bus VALUES(00008, "APSRTC Rural", "Badvel", "Mydukuru", 50 )""")
	c.execute(""" INSERT INTO bus VALUES(00009, "APSRTC Rural", "Badvel", "Guntur", 300 )""")
	c.execute(""" INSERT INTO bus VALUES(00010, "APSRTC Rural", "Madanapalli", "Bangalore", 150 )""")
	c.execute(""" INSERT INTO bus VALUES(00011, "APSRTC Rural", "Hyderabad", "Bangalore", 400 )""")

	c.execute("""SELECT * FROM bus""")


def rows():
	global rows
	rows = c.fetchall()
	for row in rows :
		row
	conn.commit()
	conn.close()
	


databasesql()
rows()

from tkinter import *

Window = Tk()
Window.geometry("1000x1000")
Window.configure(bg = "Teal")
Window.title("Bus Finding System Using Python")
MyLabel = Label(Window, text = "Bus Finding System", width = 30)
MyLabel.grid(row = 0, column = 1, padx = 40, pady = 40)

SourceLabel = Label(Window, text = "Source").grid(row = 1, column = 0)

e = Entry(Window, width = 30, borderwidth = 2)
e.grid(row = 1, column = 1,ipadx = 10, ipady = 10)


DestinationLabel = Label(Window, text = "Destination").grid(row = 2, column = 0)

z = Entry(Window, width = 30, borderwidth = 2)
z.grid(row = 2, column = 1, ipadx = 10, ipady = 10)

def search():
	global user_source 
	user_source = e.get()
	"""UserInput = Label(Window, text = user_source)
	UserInput.grid(row = 4, column = 0)
	"""	
	global user_destination 
	user_destination = z.get()

	for row in rows :

		if user_source in row and user_destination in row :

			busid1 = Label(Window, text = "Bus ID : ", width = 30, fg = "red", font = ("Garamond", 10))
			busid1.grid(row = 4, column = 0, padx = 40, pady = 40)

			busid = Label(Window, text = row[0], width = 30, fg = "green", font = ("Garamond",  10))
			busid.grid(row = 4, column = 1, padx = 40, pady = 40)


			servicename1 = Label(Window, text = "Service Name : ", width = 30, fg = "red", font = ("Garamond",  10))
			servicename1.grid(row = 5, column = 0, padx = 40, pady = 40)


			servicename = Label(Window, text = row[1], width = 30, fg = "green", font = ("Garamond",  10))
			servicename.grid(row = 5, column = 1, padx = 40, pady = 40)


			sourcename1 = Label(Window, text = "Source :", width = 30, fg = "red", font = ("Garamond",10))
			sourcename1.grid(row = 6, column = 0, padx = 40, pady = 40)

			sourcename = Label(Window, text = row[2], width = 30, fg = "green", font = ("Garamond",  10))
			sourcename.grid(row = 6, column = 1, padx = 40, pady = 40)


			destinationname1 = Label(Window, text = "Destination : ", width = 30, fg = "red", font = ("Garamond", 10))
			destinationname1.grid(row = 7, column = 0, padx = 40, pady = 40)

			destinationname = Label(Window, text = row[3], width = 30, fg = "green", font = ("Garamond", 10))
			destinationname.grid(row = 7, column = 1, padx = 40, pady = 40)


			farename1 = Label(Window, text = "Fare : ", width = 30, fg = "red", font = ("Garamond",10))
			farename1.grid(row = 8, column = 0, padx = 40, pady = 40)

		
			farename = Label(Window, text = row[4], width = 30, fg = "green", font = ("Garamond", 10))
			farename.grid(row = 8, column = 1, padx = 40, pady = 40)




SearchButton = Button(Window, text = "search", command = search, pady = 20)
SearchButton.grid(row = 3, column = 1)
Window.mainloop()


os.system("rm BusDatabase.db")


