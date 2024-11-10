# Modules
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Connecting to database
try:
    mycon = mysql.connector.connect(host="localhost", user="root", passwd="root")
    if mycon.is_connected():
        print("Connection with MySQL is Successful")
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
        F_TYPE VARCHAR(30),
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
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS001',101,'Domestic','Delhi','Mumbai','2024-12-20','05:30','08:00',70,30,null,8000,20000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS002',102,'Domestic','Delhi','Bengaluru','2023-12-30','09:00','12:00',70,30,null,10000,22000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS003',103,'Domestic','Hyderabad','Delhi','2024-12-10','12:30','02:00',70,30,null,12000,25000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS004',104,'Domestic','Chennai','Kolkata','2024-12-15','15:00','19:00',70,30,null,15000,22000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS005',105,'Domestic','Ahmedabad','Delhi','2024-12-01','20:30','23:00',70,30,null,12000,25000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACS001',106,'Domestic','Delhi','Mumbai','2024-12-10','05:30','08:00',70,30,null,8000,20000,null,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACL001',107,'Domestic','Delhi','Mumbai','2024-12-11','05:30','08:00',70,30,10,8000,20000,50000,'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES('ACL002',108,'International','Delhi','Mexico','2024-12-14','09:30','13:00',70,30,10,25000,90000,150000,'Scheduled')")

    mycon.commit()
except Error as e:
    print("Error: ", e)

# ---- Functions ----

def choose_flight_type():
    while True:
        f_type = input("Enter flight type (1 for Domestic, 2 for International): ")
        if f_type == "1":
            return "Domestic"
        elif f_type == "2":
            return "International"
        else:
            print("Invalid selection. Please enter 1 or 2.")

# Book a flight
def book_flight():
    # Choose flight type before displaying locations
    f_type = choose_flight_type()
    
    # Departure location selection with validation
    print("Available Departure Locations: ")
    cur.execute("SELECT DISTINCT DEP_LOCN FROM FLIGHTS WHERE F_TYPE = %s", (f_type,))
    dep_locations = [location[0] for location in cur.fetchall()]
    for i in range(len(dep_locations)):
        print(f"{i + 1}. {dep_locations[i]}")
    while True:
        try:
            dep_choice = int(input("Enter the number for the Departure Location: ")) - 1
            if dep_choice < 0 or dep_choice >= len(dep_locations):
                print("Invalid selection. Please enter a number within the options provided.")
                continue
            dep = dep_locations[dep_choice]
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Destination location selection with validation
    print("Available Destination Locations:")
    cur.execute("SELECT DISTINCT DEST_LOCN FROM FLIGHTS WHERE DEP_LOCN = %s AND F_TYPE = %s", (dep, f_type))
    dest_locations = [location[0] for location in cur.fetchall()]
    for i in range(len(dest_locations)):
        print(f"{i + 1}. {dest_locations[i]}")
    while True:
        try:
            dest_choice = int(input("Enter the number for the Destination Location: ")) - 1
            if dest_choice < 0 or dest_choice >= len(dest_locations):
                print("Invalid selection. Please enter a number within the options provided.")
                continue
            dest = dest_locations[dest_choice]
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Date selection with validation
    print("Available Dates For Flight: ")
    cur.execute("SELECT TVL_DATE, DEP_TIME FROM FLIGHTS WHERE DEP_LOCN = %s AND DEST_LOCN = %s AND F_TYPE = %s", (dep, dest, f_type))
    travel_dates = cur.fetchall()
    for i in range(len(travel_dates)):
        print(f"{i + 1}. Date: {travel_dates[i][0]}, Departure Time: {travel_dates[i][1]}")
    while True:
        try:
            date_choice = int(input("Enter the number for the Date of Travel: ")) - 1
            if date_choice < 0 or date_choice >= len(travel_dates):
                print("Invalid selection. Please enter a number within the options provided.")
                continue
            dot = travel_dates[date_choice][0]
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Seat class selection with validation
    while True:
        print("Select Seat Class:")
        print("1. First Class")
        print("2. Business")
        print("3. Economy")
        seat_class_option = input("Enter the number corresponding to your choice: ")
        
        seat_class_map = {"1": "First Class", "2": "Business", "3": "Economy"}
        if seat_class_option not in seat_class_map:
            print("Invalid selection. Please choose a valid option.")
            continue
        seat_class = seat_class_map[seat_class_option]  # Get the selected seat class

        # Retrieve the selected flight data
        cur.execute("SELECT * FROM FLIGHTS WHERE DEP_LOCN = %s AND DEST_LOCN = %s AND TVL_DATE = %s", (dep, dest, dot))
        selected_flight = cur.fetchone()
        if not selected_flight:
            print("No flights available for the selected route and date.")
            return
        flight_id = selected_flight[1]

        # ---- Seat Availability Check ----
        seat_index = {"First Class": 10, "Business": 9, "Economy": 8}
        class_price_index = {"First Class": 13, "Business": 12, "Economy": 11}

        available_seats = selected_flight[seat_index[seat_class]]
        seat_price = selected_flight[class_price_index[seat_class]]

        if available_seats is None or available_seats <= 0:
            print(f"No seats available in {seat_class} class.")
            continue

        # Get number of seats to book with validation
        while True:
            try:
                seats_to_book = int(input(f"Enter the number of {seat_class} seats to book: "))
                if seats_to_book > available_seats:
                    print(f"Only {available_seats} seats are available in {seat_class} class.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Calculate new seat count
        new_seat_count = available_seats - seats_to_book
        break  # Exit loop when valid selection and seats are available

    # ---- Personal Details ----
    print("\nEnter Customer Details:")
    c_name = input("Enter name: ")
    c_age = int(input("Enter age: "))
    email = input("Enter Email: ")
    ph_no = input("Enter Phone Number: ")

    # Check if customer already exists
    cur.execute("SELECT * FROM CUSTOMERS WHERE PH_NO = %s AND C_NAME = %s", (ph_no, c_name))
    customer = cur.fetchone()

    if not customer:
        # Insert customer details (C_ID will auto-increment)
        cur.execute("INSERT INTO CUSTOMERS (C_NAME, C_AGE, EMAIL, PH_NO) VALUES (%s, %s, %s, %s)", (c_name, c_age, email, ph_no))
        mycon.commit()
        print("Customer details saved.")
        
        # Get the newly generated customer ID (C_ID) using lastrowid
        customer_id = cur.lastrowid
    else:
        customer_id = customer[1]  # Use the existing customer ID

    # ---- Booking ----
    # Booking ID and Date
    booking_id = f"BK{datetime.now().strftime('%Y%m%d%H%M%S')}"
    booking_date = datetime.now().date()
    
    # Calculate total price
    total_price = seat_price * seats_to_book
    
    # Insert booking into BOOKINGS table
    cur.execute("INSERT INTO BOOKINGS (B_ID, C_ID, F_ID, SEAT_CLASS, SEATS_BOOKED, B_DATE, TOTAL_PRICE, STATUS) VALUES (%s, %s, %s, %s, %s, %s, %s, 'Confirmed')", 
                (booking_id, customer_id, flight_id, seat_class, seats_to_book, booking_date, total_price))
    
    # Update available seats in FLIGHTS table
    seat_column = {"First Class": "FCLASS_CAP", "Business": "BNSS_CAP", "Economy": "ECO_CAP"}[seat_class]
    cur.execute(f"UPDATE FLIGHTS SET {seat_column} = %s WHERE F_ID = %s", (new_seat_count, flight_id))

    # Commit changes
    mycon.commit()

    print("\nBooking Confirmed!")
    print(f"Booking ID: {booking_id}")
    print(f"Total Price: {total_price}")


## NOTE FOR ME: Change names of plane to model number so that default seats capacity can be restored.
def update_seat_count_in_flights(flight_id, seat_class, seat_diff):
    # Adjusts the seat count for a specific flight and seat class in FLIGHTS
    seat_column = {"First Class": "FCLASS_CAP", "Business": "BNSS_CAP", "Economy": "ECO_CAP"}.get(seat_class)
    if seat_column:
        cur.execute(f"UPDATE FLIGHTS SET {seat_column} = {seat_column} + %s WHERE F_ID = %s", (seat_diff, flight_id))
        mycon.commit()

def update_booking():
    # Define a mapping for seat class to the corresponding column in the FLIGHTS table
    seat_column_map = {
        "First Class": "FCLASS_CAP",
        "Business": "BNSS_CAP",
        "Economy": "ECO_CAP"
    }

    booking_id = input("Enter Booking ID to update: ")
    cur.execute("SELECT * FROM BOOKINGS WHERE B_ID = %s", (booking_id,))
    booking = cur.fetchone()

    if not booking:
        print("Booking not found.")
        return

    flight_id = booking[2]  # Get the flight ID from the booking record
    old_class = booking[3]  # Original seat class in the booking
    seats_booked = booking[4]  # Original number of seats booked

    print("1. Update Seat Class")
    print("2. Update Number of Seats")
    choice = int(input("Choose an option to update: "))

    if choice == 1:
        # Update seat class
        print("Select new seat class:")
        print("1. First Class")
        print("2. Business")
        print("3. Economy")
        new_class_choice = int(input("Enter your choice (1, 2, or 3): "))
        
        if new_class_choice == 1:
            new_class = "First Class"
        elif new_class_choice == 2:
            new_class = "Business"
        elif new_class_choice == 3:
            new_class = "Economy"
        else:
            print("Invalid choice.")
            return

        if new_class != old_class:
            # Check available seats in the new class
            cur.execute(f"SELECT {seat_column_map[new_class]} FROM FLIGHTS WHERE F_ID = %s", (flight_id,))
            available_seats = cur.fetchone()[0]

            if available_seats >= seats_booked:
                # Update the seat counts: add seats back to the old class and subtract from new class
                cur.execute(f"UPDATE FLIGHTS SET {seat_column_map[old_class]} = {seat_column_map[old_class]} + %s WHERE F_ID = %s", (seats_booked, flight_id))
                cur.execute(f"UPDATE FLIGHTS SET {seat_column_map[new_class]} = {seat_column_map[new_class]} - %s WHERE F_ID = %s", (seats_booked, flight_id))
                cur.execute("UPDATE BOOKINGS SET SEAT_CLASS = %s WHERE B_ID = %s", (new_class, booking_id))
                mycon.commit()
                print("Seat class updated successfully.")
            else:
                print("Not enough seats available in the selected class.")
        else:
            print("You are already booked in this class.")
            
    elif choice == 2:
        # Update number of seats
        new_seats = int(input("Enter new number of seats: "))
        seat_diff = new_seats - seats_booked

        # Check if enough seats are available for the update
        cur.execute(f"SELECT {seat_column_map[old_class]} FROM FLIGHTS WHERE F_ID = %s", (flight_id,))
        available_seats = cur.fetchone()[0]

        if available_seats + min(0, seat_diff) >= abs(seat_diff):
            # Update the seats in FLIGHTS table based on the difference
            cur.execute(f"UPDATE FLIGHTS SET {seat_column_map[old_class]} = {seat_column_map[old_class]} - %s WHERE F_ID = %s", (seat_diff, flight_id))
            cur.execute("UPDATE BOOKINGS SET SEATS_BOOKED = %s WHERE B_ID = %s", (new_seats, booking_id))
            mycon.commit()
            print("Number of seats updated successfully.")
        else:
            print("Not enough seats available to make this change.")
    else:
        print("Invalid choice.")



def view_booking():
    booking_id = input("Enter Booking ID to view: ")
    cur.execute("SELECT * FROM BOOKINGS WHERE B_ID = %s", (booking_id,))
    booking = cur.fetchone()

    if booking:
        print("Booking Details:")
        print(f"Booking ID: {booking[0]}")
        print(f"Customer ID: {booking[1]}")
        print(f"Flight ID: {booking[2]}")
        print(f"Seat Class: {booking[3]}")
        print(f"Seats Booked: {booking[4]}")
        print(f"Booking Date: {booking[5]}")
        print(f"Total Price: {booking[6]}")
        print(f"Status: {booking[7]}")
    else:
        print("Booking not found.")

def cancel_booking():
    booking_id = input("Enter Booking ID to cancel: ")
    cur.execute("SELECT * FROM BOOKINGS WHERE B_ID = %s", (booking_id,))
    booking = cur.fetchone()

    if not booking:
        print("Booking not found.")
        return

    # Retrieve booking details
    f_id = booking[2]           # Flight ID from booking
    seat_class = booking[3]      # Seat class (First Class, Business, Economy)
    seats_booked = booking[4]    # Number of seats booked

    # Update the status of the booking to "Cancelled"
    cur.execute("UPDATE BOOKINGS SET STATUS = 'Cancelled' WHERE B_ID = %s", (booking_id,))
    
    # Determine the correct column in FLIGHTS based on seat class
    seat_column = ""
    if seat_class == "First Class":
        seat_column = "FCLASS_CAP"
    elif seat_class == "Business":
        seat_column = "BNSS_CAP"
    elif seat_class == "Economy":
        seat_column = "ECO_CAP"

    # Restore the seats to the flight's availability
    cur.execute(f"UPDATE FLIGHTS SET {seat_column} = {seat_column} + %s WHERE F_ID = %s", (seats_booked, f_id))

    # Commit changes
    mycon.commit()
    print("Booking cancelled successfully, and seats have been returned to availability.")


def view_available_flights():
    flight_type = choose_flight_type()

    # Departure location selection with validation
    print("Available Departure Locations:")
    cur.execute("SELECT DISTINCT DEP_LOCN FROM FLIGHTS WHERE STATUS = 'Scheduled' AND F_TYPE = %s", (flight_type,))
    dep_locations = [location[0] for location in cur.fetchall()]
    for i in range(len(dep_locations)):
        print(f"{i + 1}. {dep_locations[i]}")
    
    while True:
        try:
            dep_choice = int(input("Enter the number for the Departure Location: ")) - 1
            if dep_choice < 0 or dep_choice >= len(dep_locations):
                print("Invalid selection. Please enter a number within the options provided.")
                continue
            dep = dep_locations[dep_choice]
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Destination location selection with validation
    print("Available Destination Locations:")
    cur.execute("SELECT DISTINCT DEST_LOCN FROM FLIGHTS WHERE DEP_LOCN = %s AND STATUS = 'Scheduled' AND F_TYPE = %s", (dep, flight_type))
    dest_locations = [location[0] for location in cur.fetchall()]
    for i in range(len(dest_locations)):
        print(f"{i + 1}. {dest_locations[i]}")
    
    while True:
        try:
            dest_choice = int(input("Enter the number for the Destination Location: ")) - 1
            if dest_choice < 0 or dest_choice >= len(dest_locations):
                print("Invalid selection. Please enter a number within the options provided.")
                continue
            dest = dest_locations[dest_choice]
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Display available flights based on selections
    cur.execute(
        "SELECT F_NAME, DEP_LOCN, DEST_LOCN, TVL_DATE, DEP_TIME, ARVL_TIME "
        "FROM FLIGHTS WHERE DEP_LOCN = %s AND DEST_LOCN = %s AND STATUS = 'Scheduled' AND F_TYPE = %s",
        (dep, dest, flight_type)
    )
    flights = cur.fetchall()
    if flights:
        print("Available Flights:")
        for flight in flights:
            print(f"Flight: {flight[0]}, From: {flight[1]}, To: {flight[2]}, Date: {flight[3]}, Departure: {flight[4]}, Arrival: {flight[5]}")
    else:
        print("No flights are currently available for the selected route.")






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
        book_flight()  # Call the function to book a flight
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
