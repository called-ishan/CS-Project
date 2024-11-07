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
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS003',103,'Hyderabad','Delhi','2024-12-20','05:30','08:00',70,30,null,8000,20000,null)")
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
    print("Select Departure Location from below: ")
    # Here importing the available location for departure using distinct to show only unique locations
    dep = input("Enter the Departure Location: ")
    dep=dep.lower()
    print("Select Destination Location from below: ")
    # Here importing the available location for departure using distinct to show only unique locations
    dest = input("Enter Destination Location: ")
    dest=dest.lower()
    
    
    dot = input("Enter Date of Travel(YYYY-MM-DD): ")
    seatclass = input("Select Seat Class || First Class | Business | Economy || : ")
    # Feeding all data to database    

    # ---- Personal Details ----
    name = input("Enter name: ")
    contact = input("Enter Contact Number: ")
    email = input("Enter Email: ")
    age = int(input("Enter age: "))