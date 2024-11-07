# Modules
import mysql.connector
from mysql.connector import Error

# Connecting to database
try:
    mycon = mysql.connector.connect(host="localhost",user="root",passwd="root")
    if mycon.is_connected():
        print("Connection with MySQL is Successfull")
        cur=mycon.cursor()
except Error as e: 
    print("Error while connecting to MySQL, Error: ", e)  

# ---- MySQL Initial Commands ----
try:
    cur.execute("CREATE DATABASE IF NOT EXISTS flight_booking_system")
    cur.execute("USE flight_booking_system")
    cur.execute("""CREATE TABLE IF NOT EXISTS FLIGHTS(
        F_NAME VARCHAR(30),
        F_ID INTEGER PRIMARY KEY,
        DEP_LOCN VARCHAR(30),
        DEST_LOCN VARCHAR(30),
        TVL_DATE DATE, DEP_TIME TIME,
        ARVL_TIME TIME,
        ECO_CAP INTEGER,
        BNSS_CAP INTEGER,
        FCLASS_CAP INTEGER,
        ECO_PRICE INTEGER,
        BNSS_PRICE INTEGER,
        FCLASS_PRICE INTEGER)""")
    
    # Entering Values
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS001',101,'Delhi','Mumbai','2024-12-20','05:30','08:00',70,30,null,8000,20000,null)")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS002',102,'Delhi','Bengaluru','2023-12-30','09:00','12:00',70,30,null,10000,22000,null)")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS003',103,'Hyderabad','Delhi','2024-12-10','12:30','02:00',70,30,null,12000,25000,null)")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS004',104,'Chennai','Kolkata','2024-12-15','15:00','19:00',70,30,null,15000,22000,null)")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS005',105,'Ahmedabad','Delhi','2024-12-01','20:30','23:00',70,30,null,12000,25000,null)")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS001',106,'Delhi','Mumbai','2024-12-10','05:30','08:00',70,30,null,8000,20000,null)")
    mycon.commit()
except Error as e:
    print("Error: ",e)

# ---- Menu ----
opt=314159265359
while opt!=0:
    # Baic sturcture:
    print("""1: Book a Flight
    2: Update Booking
    3: View Booking
    4: Cancel Booking
    5: View Available Flights
    0: Exit""")
    opt = int(input("Chooose an option: "))
    
# ---- Functions ----
# Book a flight
def bookflight():
    # ---- Location & Time ----
    print("Available Departure Locations: ")
    cur.execute("SELECT DISTINCT DEP_LOCN FROM FLIGHTS")
    for location in cur.fetchall():
        print(location[0])
    dep = input("Enter the Departure Location: ")
    dep=dep.title()
    
    print("Available Destination Locations:")
    cur.execute("SELECT DISTINCT DEST_LOCN FROM FLIGHTS WHERE DEP_LOCN = %s", (dep,))
    for location in cur.fetchall():
        print(location[0])
    dest = input("Enter Destination Location: ")
    dest=dest.title()
    
    print("Available Dates For Flight: ")
    cur.execute("SELECT DEP_LOCN, DEST_LOCN, TVL_DATE FROM FLIGHTS WHERE DEP_LOCN='{}' AND DEST_LOCN='{}'".format(dep, dest))
    print("Date of Flights: ")
    for dates in cur.fetchall():
        print(dates[2])
    dot = input("Enter Date of Travel(YYYY-MM-DD): ")
    seatclass = input("Select Seat Class || First Class | Business | Economy || : ")
    
    cur.execute("SELECT * FROM FLIGHTS WHERE DEP_LOCN='{}' AND DEST_LOCN='{}' AND TVL_DATE='{}'".format(dep, dest, dot))
    flight = cur.fetchone()
    if not flight:
        print("No flights available for the selected route and date.")
        return

    # ---- Personal Details ----
    name = input("Enter name: ")
    contact = input("Enter Contact Number: ")
    email = input("Enter Email: ")
    age = int(input("Enter age: "))
    pssprt = input("Enter Passport Number: ")