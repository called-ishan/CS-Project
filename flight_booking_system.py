# Modules
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Connecting to database
try:
    mycon = mysql.connector.connect(host="localhost", user="root", passwd="root")
    if mycon.is_connected():
        print("Connection with MySQL is Successfull")
        cur = mycon.cursor()
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
        FCLASS_PRICE INTEGER,
        STATUS VARCHAR(30))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS BOOKINGS(
        B_ID VARCHAR(30) PRIMARY KEY,
        C_ID INTEGER,
        F_ID VARCHAR(30),
        SEAT_CLASS VARCHAR(30),
        SEATS_BOOKED INTEGER,
        B_DATE DATE,
        TOTAL_PRICE INTEGER,
        STATUS VARCHAR(30))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS CUSTOMERS(
        C_NAME VARCHAR(30),
        C_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
        C_AGE VARCHAR(30),
        EMAIL VARCHAR(30),
        PH_NO VARCHAR(15))""")
    
    # Entering Values
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS001',101,'Delhi','Mumbai','2024-12-20','05:30','08:00',70,30,null,8000,20000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS002',102,'Delhi','Bengaluru','2023-12-30','09:00','12:00',70,30,null,10000,22000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS003',103,'Hyderabad','Delhi','2024-12-10','12:30','02:00',70,30,null,12000,25000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS004',104,'Chennai','Kolkata','2024-12-15','15:00','19:00',70,30,null,15000,22000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS005',105,'Ahmedabad','Delhi','2024-12-01','20:30','23:00',70,30,null,12000,25000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS001',106,'Delhi','Mumbai','2024-12-10','05:30','08:00',70,30,null,8000,20000,null,'Scheduled')")

    mycon.commit()
except Error as e:
    print("Error: ", e)

# ---- Functions ----
# Book a flight
def bookflight():
    # ---- Location & Time ----
    print("Available Departure Locations: ")
    cur.execute("SELECT DISTINCT DEP_LOCN FROM FLIGHTS")
    for location in cur.fetchall():
        print(location[0])
    dep = input("Enter the Departure Location: ")
    dep = dep.title()

    print("Available Destination Locations:")
    cur.execute("SELECT DISTINCT DEST_LOCN FROM FLIGHTS WHERE DEP_LOCN = %s", (dep,))
    for location in cur.fetchall():
        print(location[0])
    dest = input("Enter Destination Location: ")
    dest = dest.title()

    print("Available Dates For Flight: ")
    cur.execute("SELECT DEP_LOCN, DEST_LOCN, TVL_DATE FROM FLIGHTS WHERE DEP_LOCN='{}' AND DEST_LOCN='{}'".format(dep, dest))
    print("Date of Flights: ")
    for dates in cur.fetchall():
        print(dates[2])
    dot = input("Enter Date of Travel(YYYY-MM-DD): ")
    seat_class = input("Select Seat Class || First Class | Business | Economy || : ").title()
    cur.execute("SELECT * FROM FLIGHTS WHERE DEP_LOCN='{}' AND DEST_LOCN='{}' AND TVL_DATE='{}'".format(dep, dest, dot))
    selected_flight = cur.fetchone()
    flight_id = selected_flight[1]
    if not selected_flight:
        print("No flights available for the selected route and date.")
        return
    
    # ---- Seat Availability Check ----
    seat_index = {"First class": 9, "Business": 8, "Economy": 7}
    class_price_index = {"First class": 12, "Business": 11, "Economy": 10}

    available_seats = selected_flight[seat_index[seat_class]]
    seat_price = selected_flight[class_price_index[seat_class]]

    if available_seats is None or available_seats <= 0:
        print(f"No seats available in {seat_class} class.")
        return

    # Get number of seats to book
    seats_to_book = int(input(f"Enter the number of {seat_class} seats to book: "))

    if seats_to_book > available_seats:
        print(f"Only {available_seats} seats are available in {seat_class} class.")
        return

    # Calculate new seat count
    new_seat_count = available_seats - seats_to_book    
    
    # ---- Personal Details ----
    print("\nEnter Customer Details:")
    c_name = input("Enter name: ")
    c_age = int(input("Enter age: "))
    email = input("Enter Email: ")
    ph_no = input("Enter Phone Number: ")

    # Check if customer already exists
    cur.execute(f"SELECT * FROM CUSTOMERS WHERE PH_NO = '{ph_no}' AND C_NAME = '{c_name}'")
    customer = cur.fetchone()

    if not customer:
        # Insert customer details (C_ID will auto-increment)
        cur.execute(f"INSERT INTO CUSTOMERS (C_NAME, C_AGE, EMAIL, PH_NO) VALUES ('{c_name}', {c_age}, '{email}', '{ph_no}')")  # Added PH_NO field
        mycon.commit()
        print("Customer details saved.")
        
        # Get the newly generated customer ID (C_ID) using lastrowid
        customer_id = cur.lastrowid  # This retrieves the auto-incremented C_ID
    else:
        customer_id = customer[1]  # Use the existing customer ID

    # ---- Booking ----
    # Booking ID and Date
    booking_id = f"BK{datetime.now().strftime('%Y%m%d%H%M%S')}"
    booking_date = datetime.now().date()
    
    # Calculate total price
    total_price = seat_price * seats_to_book
    
    # Insert booking into BOOKINGS table
    cur.execute(f"INSERT INTO BOOKINGS (B_ID, C_ID, F_ID, SEAT_CLASS, SEATS_BOOKED, B_DATE, TOTAL_PRICE, STATUS) VALUES ('{booking_id}', {customer_id}, '{flight_id}', '{seat_class}', {seats_to_book}, '{booking_date}', {total_price}, 'Confirmed')")
    
    # Update available seats in FLIGHTS table
    if seat_class == "First class":
        seat_column = "FCLASS_CAP"
    elif seat_class == "Business":
        seat_column = "BNSS_CAP"
    else:
        seat_column = "ECO_CAP"

    cur.execute(f"UPDATE FLIGHTS SET {seat_column} = {new_seat_count} WHERE F_ID='{flight_id}'")

    # Commit changes
    mycon.commit()

    print("\nBooking Confirmed!")
    print(f"Booking ID: {booking_id}")
    print(f"Total Price: {total_price}")

## NOTE FOR ME: Change names of plane to model number so that default seats capacity can be restored.








# ---- Menu ----
opt = 314159265359
while opt != 0:
    # Basic structure:
    print("""
    ---- Flight Booking System ----
    ===============================
    1: Book a Flight
    2: Update Booking
    3: View Booking
    4: Cancel Booking
    5: View Available Flights
    0: Exit
    ===============================
    """)
    opt = int(input("Choose an option: "))
    print("--------------------------")
    if opt == 1:
        bookflight()  # Call the function to book a flight
    elif opt == 2:
        update_booking()  # Call the function to update booking
    elif opt == 3:
        view_booking()  # Call the function to view booking
    elif opt == 4:
        cancel_booking()  # Call the function to cancel booking
    elif opt == 5:
        view_available_flights()  # Call the function to view available flights
    elif opt == 0:
        print("Exiting...")  # Exit message
    else:
        print("Invalid option, please try again.")
