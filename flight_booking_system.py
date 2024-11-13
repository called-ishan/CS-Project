# ---- Modules ----
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date
from datetime import datetime

# ---- Connecting to database ----
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
    # Domestic Flights - Small Planes (No First Class)
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS001', 101, 'Domestic', 'Delhi', 'Mumbai', '2024-12-01', '05:30', '08:00', 70, 30, NULL, 5000, 15000, NULL, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS002', 102, 'Domestic', 'Bangalore', 'Hyderabad', '2024-12-02', '06:00', '08:15', 70, 30, NULL, 4500, 12000, NULL, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS003', 103, 'Domestic', 'Pune', 'Jaipur', '2024-12-03', '07:30', '09:45', 70, 30, NULL, 4000, 11000, NULL, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS004', 104, 'Domestic', 'Kolkata', 'Chennai', '2024-12-04', '08:00', '10:30', 70, 30, NULL, 5500, 13000, NULL, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS005', 105, 'Domestic', 'Mumbai', 'Delhi', '2024-12-05', '09:00', '11:30', 70, 30, NULL, 5200, 14000, NULL, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS006', 106, 'Domestic', 'Jaipur', 'Ahmedabad', '2024-12-06', '10:00', '12:00', 70, 30, NULL, 4000, 11500, NULL, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS007', 107, 'Domestic', 'Chennai', 'Mumbai', '2024-12-07', '11:00', '13:30', 70, 30, NULL, 4700, 12500, NULL, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS008', 108, 'Domestic', 'Delhi', 'Pune', '2024-12-08', '12:00', '14:15', 70, 30, NULL, 4800, 13000, NULL, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS009', 109, 'Domestic', 'Mumbai', 'Goa', '2024-12-09', '13:00', '15:00', 70, 30, NULL, 4500, 12000, NULL, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACS010', 110, 'Domestic', 'Hyderabad', 'Pune', '2024-12-10', '14:00', '16:00', 70, 30, NULL, 4300, 12500, NULL, 'Scheduled')")

    # Domestic Flights - Large Planes (With First Class)
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL011', 111, 'Domestic', 'Delhi', 'Bangalore', '2024-12-11', '06:00', '09:00', 130, 50, 20, 6000, 18000, 25000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL012', 112, 'Domestic', 'Mumbai', 'Chennai', '2024-12-12', '07:00', '10:00', 130, 50, 20, 6200, 18500, 26000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL013', 113, 'Domestic', 'Hyderabad', 'Kolkata', '2024-12-13', '08:00', '11:00', 130, 50, 20, 6100, 18200, 25500, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL014', 114, 'Domestic', 'Pune', 'Delhi', '2024-12-14', '09:00', '12:00', 130, 50, 20, 6400, 19000, 26500, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL015', 115, 'Domestic', 'Chennai', 'Mumbai', '2024-12-15', '10:00', '13:00', 130, 50, 20, 6300, 18500, 26000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL016', 116, 'Domestic', 'Delhi', 'Hyderabad', '2024-12-16', '11:00', '14:00', 130, 50, 20, 6500, 19200, 27000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL017', 117, 'Domestic', 'Mumbai', 'Kolkata', '2024-12-17', '12:00', '15:00', 130, 50, 20, 6600, 19500, 27500, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL018', 118, 'Domestic', 'Jaipur', 'Delhi', '2024-12-18', '13:00', '16:00', 130, 50, 20, 6200, 18000, 25000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL019', 119, 'Domestic', 'Ahmedabad', 'Bangalore', '2024-12-19', '14:00', '17:00', 130, 50, 20, 6300, 18200, 25500, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL020', 120, 'Domestic', 'Pune', 'Chennai', '2024-12-20', '15:00', '18:00', 130, 50, 20, 6400, 18800, 26500, 'Scheduled')")

    # International Flights - All Large Planes (With First Class)
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL021', 121, 'International', 'Delhi', 'New York', '2024-12-01', '19:00', '04:00', 130, 50, 20, 25000, 60000, 100000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL022', 122, 'International', 'Mumbai', 'London', '2024-12-02', '20:00', '06:00', 130, 50, 20, 24000, 58000, 98000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL023', 123, 'International', 'Chennai', 'Dubai', '2024-12-03', '21:00', '01:30', 130, 50, 20, 18000, 45000, 85000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL024', 124, 'International', 'Bangalore', 'Singapore', '2024-12-04', '22:00', '02:30', 130, 50, 20, 20000, 50000, 90000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL025', 125, 'International', 'Delhi', 'Paris', '2024-12-05', '23:00', '05:30', 130, 50, 20, 21000, 53000, 95000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL026', 126, 'International', 'Mumbai', 'Sydney', '2024-12-06', '22:00', '10:30', 130, 50, 20, 30000, 75000, 130000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL027', 127, 'International', 'Kolkata', 'Frankfurt', '2024-12-07', '18:00', '04:30', 130, 50, 20, 26000, 62000, 105000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL028', 128, 'International', 'Delhi', 'Toronto', '2024-12-08', '17:00', '03:00', 130, 50, 20, 27000, 65000, 110000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL029', 129, 'International', 'Bangalore', 'Tokyo', '2024-12-09', '15:00', '05:30', 130, 50, 20, 28000, 67000, 115000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL030', 130, 'International', 'Mumbai', 'Cape Town', '2024-12-10', '20:00', '10:30', 130, 50, 20, 32000, 80000, 140000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL031', 131, 'International', 'Delhi', 'Berlin', '2024-12-11', '21:00', '06:00', 130, 50, 20, 22000, 55000, 93000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL032', 132, 'International', 'Mumbai', 'Los Angeles', '2024-12-12', '23:00', '07:30', 130, 50, 20, 27000, 65000, 115000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL033', 133, 'International', 'Bangalore', 'Hong Kong', '2024-12-13', '16:00', '01:00', 130, 50, 20, 23000, 57000, 96000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL034', 134, 'International', 'Chennai', 'Istanbul', '2024-12-14', '20:30', '06:00', 130, 50, 20, 25000, 60000, 100000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL035', 135, 'International', 'Delhi', 'Zurich', '2024-12-15', '18:30', '03:30', 130, 50, 20, 26000, 62000, 105000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL036', 136, 'International', 'Mumbai', 'Johannesburg', '2024-12-16', '19:30', '05:30', 130, 50, 20, 24000, 59000, 100000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL037', 137, 'International', 'Hyderabad', 'Rome', '2024-12-17', '20:00', '06:00', 130, 50, 20, 25000, 60000, 102000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL038', 138, 'International', 'Delhi', 'Barcelona', '2024-12-18', '17:30', '02:00', 130, 50, 20, 22000, 58000, 97000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL039', 139, 'International', 'Mumbai', 'Seoul', '2024-12-19', '22:00', '09:00', 130, 50, 20, 27000, 65000, 115000, 'Scheduled')")
    cur.execute("INSERT IGNORE INTO FLIGHTS VALUES ('ACL040', 140, 'International', 'Bangalore', 'Bangkok', '2024-12-20', '10:30', '14:00', 130, 50, 20, 20000, 50000, 90000, 'Scheduled')")

    mycon.commit()

except Error as e:
    print("Error: ", e)

# ---- Functions ----

# ---- Book a flight ----

def choose_flight_type():
    while True:
        f_type = input("""Enter flight type:
1: Domestic
2: International 
Your Choice: """)
        if f_type == "1":
            return "Domestic"
        elif f_type == "2":
            return "International"
        else:
            print("Invalid selection. Please enter 1 or 2.")

def calculate_dynamic_price(base_price, travel_date):
    today = date.today()
    days_until_departure = (travel_date - today).days

    # Apply price increase based on days remaining
    if days_until_departure <= 3:
        final_price = base_price * 2.0  # 100% increase
        percentage_increase = 100
    elif days_until_departure <= 5:
        final_price = base_price * 1.4  # 40% increase
        percentage_increase = 40
    elif days_until_departure <= 7:
        final_price = base_price * 1.2  # 20% increase
        percentage_increase = 20
    elif days_until_departure <= 10:
        final_price = base_price * 1.1  # 10% increase
        percentage_increase = 10
    else:
        final_price = base_price  # No increase
        percentage_increase = 0

    return int(final_price), percentage_increase  # Convert to integer for consistent pricing

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
        print(f"{i + 1}: {dest_locations[i]}")
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
        print(f"{i + 1}: Date: {travel_dates[i][0]}, Departure Time: {travel_dates[i][1]}")
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
        print("1: First Class")
        print("2: Business")
        print("3: Economy")
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

        # Seat Availability Check
        seat_index = {"First Class": 10, "Business": 9, "Economy": 8}
        class_price_index = {"First Class": 13, "Business": 12, "Economy": 11}

        available_seats = selected_flight[seat_index[seat_class]]
        base_price = selected_flight[class_price_index[seat_class]]

        if available_seats is None or available_seats <= 0:
            print(f"No seats available in {seat_class}.")
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

        # Calculate dynamic price based on remaining days
        seat_price, percentage_increase = calculate_dynamic_price(base_price, dot)

        # Calculate total price and print the increase, if any
        total_price = seat_price * seats_to_book
        if percentage_increase > 0:
            print(f"Booking price increased by {percentage_increase}% due to late booking.")
        print(f"Total price: {total_price} INR")

        # Update seat count and proceed with booking as before
        new_seat_count = available_seats - seats_to_book
        break

    # Personal Details
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

    # Booking
    # Booking ID and Date
    booking_id = f"BK{datetime.now().strftime('%Y%m%d%H%M%S')}"
    booking_date = datetime.now().date()

    # Insert booking into BOOKINGS table
    cur.execute("INSERT INTO BOOKINGS (B_ID, C_ID, F_ID, SEAT_CLASS, SEATS_BOOKED, B_DATE, TOTAL_PRICE, STATUS) VALUES (%s, %s, %s, %s, %s, %s, %s, 'Confirmed')", 
                (booking_id, customer_id, flight_id, seat_class, seats_to_book, booking_date, total_price))

    # Update available seats in FLIGHTS table
    seat_column = {"First Class": "FCLASS_CAP", "Business": "BNSS_CAP", "Economy": "ECO_CAP"}[seat_class]
    cur.execute(f"UPDATE FLIGHTS SET {seat_column} = %s WHERE F_ID = %s", (new_seat_count, flight_id))

    mycon.commit()

    print("\nBooking Confirmed!")
    print(f"Booking ID: {booking_id}")
    print(f"Total price with {percentage_increase}% increase applied: {total_price} INR")


# Update Booking

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
        print("1: First Class")
        print("2: Business")
        print("3: Economy")
        new_class_choice = int(input("Enter Your Choice: "))
        
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
        print("--------------------")
        print("Booking Details:")
        print(f"Booking ID: {booking[0]}")
        print(f"Customer ID: {booking[1]}")
        print(f"Flight ID: {booking[2]}")
        print(f"Seat Class: {booking[3]}")
        print(f"Seats Booked: {booking[4]}")
        print(f"Booking Date: {booking[5]}")
        print(f"Total Price: {booking[6]}")
        print(f"Status: {booking[7]}")
        print("--------------------")
    else:
        print("--------------------")
        print("Booking not found.")
        print("--------------------")

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
        print(f"{i + 1}: {dep_locations[i]}")
    
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
        print(f"{i + 1}: {dest_locations[i]}")
    
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
            print("--------------------")
            print(f"Flight: {flight[0]}, From {flight[1]} To {flight[2]}, Date: {flight[3]}, Departure: {flight[4]}, Arrival: {flight[5]}")
            print("--------------------")
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
    2: View Booking
    3: Update Booking
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
        view_booking()  # Call the function to view booking
    elif opt == 3:
        update_booking()  # Call the function to update booking
    elif opt == 4:
        cancel_booking()  # Call the function to cancel booking
    elif opt == 5:
        view_available_flights()  # Call the function to view available flights
    elif opt == 0:
        print("Exiting...")  # Exit message
    else:
        print("Invalid option, please try again.")
