opt=314
while opt!=0:
    # Baic sturcture:
    print("""1: Book a Flight
    2: Update Booking
    3: View Booking
    4: Cancel Booking
    5: View Available Flights
    0: Exit""")
    opt = int(input("Chooose an option: "))
    
# Functions 
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
    seatclass = input("Select Seat Class || First Class | Business | Premium Economy | Economy || : ")
    # Feeding all data to database    

    # ---- Personal Details ----
    name = input("Enter name: ")
    contact = input("Enter Contact Number: ")
    email = input("Enter Email: ")
    age = int(input("Enter age: "))
    
bookflight()