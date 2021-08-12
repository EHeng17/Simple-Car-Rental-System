### All functions used in Main Menu
def main_menu():

    # Display when user enters the main menu
    print("\n************************************************************")
    print("************Welcome to Super Car Rental Services************")

    # Options for users to select
    # \n will start print the displays in a new line
    print ("1. Admin Login \n2. Customer Login \n3. Login as guest \n4. Exit \n5. Forgot Username and Password")
    print("************************************************************")
    # Users will type the number they want to access. (E.g. When users type 1, they will go to the admin login)
    try:
        user_input = int(input("Enter a number: "))

    # except ValueError is used to handle issues when user types anything other than numbers
    except ValueError:
        print ("\nPLEASE ENTER A NUMBER FROM 1 TO 5 \nTRY AGAIN")
        main_menu() # Redirect users back to the main menu to retry
    
    if user_input == 1:
        # Directs users to the admin_login function
        admin_login() 
        
    elif user_input == 2:
        # Directs users to the customer_login function
        customer_login() 

    elif user_input == 3:
        # Directs users to the guest_menu function
        guest_menu() 

    elif user_input == 4:
        print("Goodbye") 
        exit() # Ends the execution

    elif user_input == 5:
        forget_password() # Directs users to the forget_password function

    else:
        # Precaution just in case user types anything else other than 1 to 5
        print("PLEASE ENTER A NUMBER FROM 1 TO 5 \nTRY AGAIN")
        main_menu()
## Forget Password
def forget_password():
    print("\n------------ Forgot Username or Password ------------")
    contact_number = input("Enter your contact number: ")
    contact_number = contact_number.replace(" ", "") # Removes spaces

    with open("login.txt", "r") as all_user_info:
        if contact_number in all_user_info.read(): # Read the whole file as one string, then check for contact number
            recover_info = [] # Empty list to store stings
            with open ("login.txt", "r") as user_info: # Open cars.txt in read mode
                for users in user_info: # For the lines in cars.txt
                    user = users.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
                    if contact_number in user: # If the  car plate is detected
                        recover_info.append(user)
            
            print("\n----------------------------------------------")
            print("-------------  User Information --------------")
            # Display list output in an organized manner
            print ("{:<15} {:<15} {:<15}".format("USERNAME", "PASSWORD", "CONTACT NUMBER"))
            for users in recover_info:
                print("{:<15} {:<15} {:<15}".format(users[0], users[1], users[2]))
            print("----------------------------------------------")
            print("\nPlease remember your user information \nYou can now log in and proceed to the modify user details section to change your details.")
        
        else:
            print("No such phone number in our database \nYou have not registered for an account, or you may have typed in wrongly")

        all_user_info.close() # Close text file after reading

    exit = input("\nInput any letter or numbers to return to the main menu: ")
    if exit == "y": # Lets user to go back to main menu, no matter what kind of input
        main_menu()
    else:
        main_menu()
## Admin Login Interface
def admin_login():

    print ("\n---------- Admin Login Interface ------------")
    count = 0 # Limit on how many times admin can retry password (Maybe got intruders)
    while count < 3:
        admin_username = input("Enter your name: ") # Ask admin for name
        admin_username = admin_username.replace(" ", "") # Removes spaces

        admin_password = input("Enter the password: ") # Ask admin for password
        admin_password = admin_password.replace(" ","")

        admin_information = open("admin_info.txt", "r") # Open admin_info.txt in read mode

        admin_data = [] # Empty list to store strings
        for lines in admin_information: # For every line in the text file
            admin_data.append(lines.split()) # Split the strings when a space is detected, and add it into the empty list

        total_user = len(admin_data) # Determine length of the list
        increment = 0
        login_success = 0

        while increment < total_user: 
            usernames = admin_data[increment][0] # Check the first row of the first column, followed by second row of the first column, and so on, while the increment is increasing
            passwords = admin_data[increment][1] # Check the first row of the second column, followed by second row of the second column, and so on, while the increment is increasing

            if admin_username == usernames and admin_password == passwords: # If the input matches to the first and second column of the same row.
                login_success = 1
            increment += 1

        if login_success == 1:
            print ("\nWelcome back", admin_username, "!!!")
            admin_interface() # Directs user to the admin_interface function

        else:
            print ("\nWrong Username or Password. Please try again") # Let admin know its the wrong password
            count += 1 # Add 1 to the count

    if count == 3: # If its looped 3 times
        print ("You are now denied of access") # Displayed
        exit() # Stop the code
## Customer Login Interface
def customer_login():
    print("\n-----------------------------------------------------------")
    print("------------Please enter your details to log in------------")
    # Customers will enter their username
    username = input("Enter your username: ")
    username = username.replace(" ", "")

    # Customers will enter their password
    password = input("Enter your password: ")
    password = password.replace(" ", "")
    print("-----------------------------------------------------------")


    # Opens login.txt as read mode and read the lines inside the text file
    customer_information = open("login.txt", "r") 

    # Lists for the username and passwords
    user_data = [] 
    for lines in customer_information: 
        # Split username and passwords if they detect a space. After splitting, add the username and passwords into the list
        user_data.append(lines.split()) 

    # Determines the amount of username and data in the text file.
    total_user = len(user_data)
    increment = 0
    login_success = 0
    
    while increment < total_user: # Keeps increasing the increment. Loop will stop once it is less than 1 of the total_user

        # Checks the first row and column for the username. As it increases, it checks the second row, then the third row.
        usernames = user_data[increment][0]  

        # Checks the first row and second column for the password. As it increases, it checks the second row, then the third row.
        passwords = user_data[increment][1]  

        if username == usernames and password == passwords: 
            login_success = 1
        
        increment += 1
    
    if login_success == 1:
        print("\nWelcome back", username, "!!!")
        customer_interface(username)
    else:
        print ("\nInvalid username or password")
        print ("1. Forget Username or Password")
        print ("2. Try to login again")
        customer_input = input("Enter a number: ")
        if customer_input == "1":
            forget_password()
        elif customer_input == "2":
            customer_login()
        else:
            customer_login()
## Guest Menu
def guest_menu():
    # This is how the interface will look like for the guests.
    print("\n---------------------------------- \n------------Guest Menu------------")
    print("1. View cars available for rent")
    print("2. Create an account")
    print("3. Back to main menu")
    print("NOTE: An account is needed to access features such as detail of cars and booking a car")
    print("----------------------------------")

    guest_input = input("Enter a number: ")

    if guest_input == "1":
        available_cars()
        #  return to the menu
        exit = input("\nInput any letter or numbers to return to the guest menu: ")
        if exit == "y":
            guest_menu()
        else:
            guest_menu()

    elif guest_input == "2":
        # Guests below 18 will not be able to rent for a car.
        import datetime
        year = datetime.date.today().year # Get the year from today's date

        print("\n------------ Creating an account ------------")

        try:
            year_of_birth = (input("Please enter the year that you were born in: "))
        except:
            print("\nENTER A YEAR")
            guest_menu()

        if len(year_of_birth) == 4 and year_of_birth.isdigit(): # If users enter a proper year, and the input are all in numbers
            age = year - int(year_of_birth) # To determine age
            if age > 17: # If the age is above 17 (18 is the legal age)       

                username = input("Please enter a username: ") # Guests will enter the username they want. 
                username = username.replace(" ", "") # Remove any spaces between username

                if len(username) == 0: # If the input is blank (length of input == 0, means that the input is blank)
                    print("Please Do Not Leave it Empty!!!")
                    guest_menu()
                else: # If it is not left empty
                    same_username = 0
                    try:
                        with open ("login.txt","r") as account_informations: # Open text file
                            for accounts in account_informations: # For every line in the text file,
                                account = accounts.strip().split() # Remove newlines in the text file, and split the string when a space is detected
                                if username in account[0]: # If the desired username is found in the first column of the list
                                    same_username = 1
                            account_informations.close()

                    except FileNotFoundError: # If login.txt is not found
                        print("\nSOMETHING IS WRONG WITH THE PROGRAM, PLEASE WAIT WHILE WE INVESTIGATE THIS ISSUE")
                        main_menu()
                    

                    # check for username
                    if same_username == 1:
                        print("\nUsername is taken, please try a new username")
                        print("You will be redirected to the guest menu to retry")
                        guest_menu() # Redirect user back to guest menu
                    

                    else:
                        # Guests will enter the password they want
                        print("------------------------------------------------")
                        password = input ("Please enter a password: ") # Ask for password
                        password = password.replace(" ", "") # Remove spaces in input
                        
                        if len(password) == 0: # If the input is blank
                            print("Please do not leave it empty!!!")
                            guest_menu()
                        else:
                            contact_no = input("Please enter your contact number: ") # Ask for contact number
                            contact_no = contact_no.replace(" ","") # Remove spaces in input

                            if len(contact_no) == 0: # If the input is blank
                                print("Please do not leave it empty!!!")
                                guest_menu()
                            elif len(contact_no) < 9: # If phone number is leser than 9 characters
                                print("Please enter a proper contact number !!!")
                                guest_menu()

                            elif len(contact_no) >= 9 and contact_no.isdigit(): # If phone number is more or same as 9 characters, and the input is in numbers,
                                same_contact_number = 0
                                with open ("login.txt","r") as account_informations:
                                    for accounts in account_informations:
                                        account = accounts.strip().split()
                                        if contact_no in account[2]: # If the contact number entered is found in the third column of the list
                                            same_contact_number = 1
                                    account_informations.close() # Close text file after reading

                                if same_contact_number == 1: # If contact number is found
                                    print("\nContact number is found in the database \nPlease make sure you have inputted the correct contact number")
                                    guest_menu()
                                else:
                                    # Display all inputted information to show it to user
                                    print("\nUsername:", username)
                                    print("Password:", password)
                                    print("Contact Number:", contact_no)
                                    print("\nPlease double-check your information before continuing")
                                    confirmation = input("Are you sure with your details(Y/N): ").lower()

                                    if confirmation == "y":
                                        #Open the text file in append mode (Which is to add new inputs)
                                        customer_information = open("login.txt", "a")

                                        # Add new strings which is inputed by guests
                                        customer_information.write(username + " " + password + " " + contact_no + "\n") 

                                        #Close the text file after it is used
                                        customer_information.close() 

                                        #Display to tell guests that they are registered into the system
                                        print("----------------------------------------------")
                                        print("\nUser was successfully registered") 
                                        login_interface = input("Would you like to proceed to the login interface?(Y/N): ").lower()

                                        if login_interface == "y":
                                            customer_login() #This command will direct the guests to the login interface
                                        else:
                                            print("\nYou will be redirected to the main menu")
                                            main_menu()

                                    elif confirmation == "n":
                                        print ("\nYou will be redirected to the guest menu to retry")
                                        guest_menu()

                                    else:
                                        print("\nYou will be redirected back to the guest menu")
                                        guest_menu()
                            else:
                                print("\nOnly Input Numbers!")
                                guest_menu()
            else:
                print("You are below the legal age to rent a car. You will be redirected to the main menu. \n")
                main_menu()
        else: # If users enter anything weird (Symbols or letters)
            print("Enter a proper year !")
            guest_menu()

    elif guest_input == "3":
        #Redirect guests back to the main menu
        main_menu() 

    else:
        # Handle error if user does not use number from 1 to 3
        print("PLEASE SELECT A NUMBER FROM 1 TO 3.")
        print("You will now be redirected back to the guest interface")
        guest_menu()



## FUNCTIONS USED IN ADMIN MENU
# Admin Interface
def admin_interface():
    print ("\n------------ Admin Interface ------------")
    print ("1. Add Cars to be rented out")
    print ("2. Modify Car Details")
    print ("3. Display Cars that will be rented out today")
    print ("4. Display Records")
    print ("5. Search specific record")
    print ("6. Return a rented car")
    print ("7. Remove a car booking")
    print ("8. Add new admin")
    print ("9. Remove admin")
    print ("10. Return to main menu")
    print ("-----------------------------------------")
    try:
        admin_input = int(input("Enter a number: "))
    except ValueError:
        print ("Enter a number from 1 to 10 !!!")
        admin_interface()
    
    if admin_input == 1: # If admins want to add cars to be rented out
        add_car()

    elif admin_input == 2: # If admins want to modify car details
        modify_car_function()

    elif admin_input == 3: # If admins want to display cars that will be rented out today
        display_cars_today()

    elif admin_input == 4: # If admins want to display records
        display_records()

    elif admin_input == 5: # If admins want to search a specific record
        search_specific_record()

    elif admin_input == 6: # If admins want to return a rented car
        return_a_car()

    elif admin_input == 7: # If customers did not pay before due date. Their booking must be removed
        remove_car_booking()

    elif admin_input == 8: # If admins want to add more admins
        add_new_admin()

    elif admin_input == 9:
        remove_admin()

    elif admin_input == 10: # If admins want to return to the main menu.
        print("Logged out successfully !")
        main_menu()

    else: # If admins enter anything else other than 1 to 9
        print("Enter a number from 1 to 10!!!!")
        print("Please try again")
        admin_interface()
# For viewing cars that are available
def available_cars():
    available_for_rent = [] # Empty list to store strings
    success = 0
    with open ("cars.txt", "r") as car_information: # Open cars.txt in read mode
        for cars in car_information: # For the lines in cars.txt
            car = cars.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
            if "Available" in car: # If the string "available" is detected
                available_for_rent.append(car) # Add into the empty list
                success = 1
                
    if success == 1:
        print("\n----------------------------------------------------------")
        print("---------------- Cars Available for Rent -----------------\n")
        # Display list in an organized manner
        print ("{:<15} {:<15} {:<15} {:<15}".format("CAR MODEL", "CAR COLOR", "CAR PLATE", "CAR STATUS\n")) # Print each string within the 15 spaces, and repeat for each strings. Each string has 15 spaces
        for cars in available_for_rent: # For the list(cars) inside the list(available_for_rent)
            print("{:<15} {:<15} {:<15} {:<15}".format(cars[0], cars[1], cars[2], cars[3])) # Print each string within the 15 spaces from the list, and repeat for each strings. Each string has 15 spaces
        print("----------------------------------------------------------")
    
    else: # If the text file contains no cars that has the 'Available' string
        print("No cars are available at the moment")
# Modify car function
def modify_car_function():
    available_cars() # Call available_cars() function (Show cars that can be modified)
    success = 0
    car_plate = input("Enter the car plate: ").upper() # Make the inputted letters uppercase (All cars plates are uppercase)
    if len(car_plate) == 0: # If empty input
        print("Please Do Not Leave It Blank !!!")
    else:
        with open("cars.txt", "r") as car_information: # Open text file
            for cars in car_information: 
                car = cars.strip().split() # Remove all the newlines in the text file, and split strings when a space is detected.
                if car_plate in car[2]: # If the inputted string by the user is found in the second column of the lists,
                    success = 1
            
        if success == 1:
            with open("cars.txt", "r") as car_information:
                for cars in car_information:
                    car = cars.strip().split()
                    if car_plate in car[2]:
                        print("1. Car Model: ", car[0]) # Display the first column of that specific list (That the car plate was found in)
                        print("2. Car Color: ", car[1]) # Display the second column of that specific list (That the car plate was found in)
                        print("3. Car Plate: ", car[2]) # Display the third column of that specific list (That the car plate was found in)
                        print("4. Return to Admin Menu")
                        try:
                            fno = int(input("\nEnter the field number to modify: "))
                        except ValueError:
                            print("Please enter a number from 1 to 4 !!! ")
                            break
                        
                        if fno == 1:
                            print("The existing Car Model is : ", car[fno - 1]) # The inputted number must be subtracted by 1 (First column of every list is the number '0', not '1')
                            car[fno - 1] = input("Enter new Car Model: ") # Ask for new car model
                            car[fno - 1] = car[fno - 1].replace (" ", "") # Remove spaces

                            if len(car[fno - 1]) == 0: # If the inputted string by the user is blank
                                print("\nPlease do not leave it blank !!!")

                            elif car[fno - 1].isdigit(): # If the inputted string by the user is in numbers (Car Models are not in numbers)
                                print("\nPlease do not input numbers !!!")
                            
                            else:
                                modify_car_text_file(car_plate, car) # modify_car_text_file(car_plate, new_car_info) function executed
                                # Display new changes
                                print("\nYour new Car Model is: ")
                                print("1. Car Model: ", car[0])
                                print("2. Car Color: ", car[1])
                                print("3. Car Plate: ", car[2])
                                break

                        elif fno == 2:
                            print("The existing Car Color is : ", car[fno - 1])
                            car[fno - 1] = input("Enter new Car Color: ")
                            car[fno - 1] = car[fno - 1].replace (" ", "")

                            if len(car[fno - 1]) == 0:
                                print("\nPlease do not leave it blank !!!")

                            elif car[fno - 1].isdigit():
                                print("\nPlease do not input numbers!")
                                
                            else:
                                modify_car_text_file(car_plate, car)
                                print("\nYour new Car Color is: ")
                                print("1. Car Model: ", car[0])
                                print("2. Car Color: ", car[1])
                                print("3. Car Plate: ", car[2])
                                break
                        
                        elif fno == 3:
                            print("The existing Car Plate is : ", car[fno - 1])
                            car[fno - 1] = input("Enter new Car Plate: ").upper()
                            car[fno - 1] = car[fno - 1].replace (" ", "")

                            if len(car[fno - 1]) == 0:
                                print("\nPlease do not leave it blank !!!")
                                
                            else:
                                with open("cars.txt","r") as all_car_info:
                                    if car[fno - 1] in all_car_info.read(): # If car plate is detected in the text file after reading it (There is no such thing as the same car plate)
                                        print("\nCar plate has been registered into the database \nPlease recheck your car plate before re-entering")
                                        all_car_info.close()
                                    else:
                                        modify_car_text_file(car_plate, car)
                                        print("\nYour new Car Plate is: ")
                                        print("1. Car Model: ", car[0])
                                        print("2. Car Color: ", car[1])
                                        print("3. Car Plate: ", car[2])
                                        break
                        elif fno == 4:
                            admin_interface()
                        else:
                            print("\nEnter a number from 1 to 4 !!!")
        else:
            print("\nNo such car in database.")

    adminmenu = input("\nInput any letter or numbers to return to the admin menu: ")
    if adminmenu == "y":
        admin_interface()
    else:
        admin_interface()
# Modify car function (Text File)
def modify_car_text_file(car_plate, car):
    cars_information = open("cars.txt", "r") # Open cars.txt in read mode
    lines = cars_information.readlines() # Read each line one by one
    cars_information.close() # Close after reading each lines
                                        
    new_information = open("cars.txt", "w") # Open cars.txt in write mode
    for line in lines: 
        if car_plate not in line: # If the car plate(Unique ID for each car) is not in the lines
            new_information.write(line) # Write it in the text file (The one with the specific contact number will not be written)
    new_information.close() # Close after writing

    with open("cars.txt", "a") as cars_information: # Open login.txt in append mode
        for strings in car:
            cars_information.write(strings + " ") # Add car information, and then add a space, and then continue (We are not replacing, we are adding in as if its new information)
        cars_information.write("\n") # Add a new line after finish adding the information    
        cars_information.close()
# Add New Admin
def add_new_admin():
    print("\n--------------------------------------------")
    print("------------ Adding a New Admin ------------")

    # Ask admin for input
    admin_name = input("\nEnter your real name: ")
    admin_name = admin_name.replace(" ", "")

    if len(admin_name) == 0: # If the input is blank
        print("\nPlease Do Not Leave it Empty")
        retry = input("\nWould You Like To Retry?(Y/N): ").lower()
        if retry == "y":
            add_new_admin()
        else:
            admin_interface()
    else:
        same_name = 0
        # Checking for the same username in the admin information text file
        with open ("admin_info.txt","r") as account_informations:
            for accounts in account_informations:
                account = accounts.strip().split()
                if admin_name in account[0]:
                    same_name = 1
            account_informations.close()
        
        if same_name == 1: # If the same name is detected
            print("\nLooks like another admin has taken this name. \nPlease try a new name")
            
        else:
            admin_password = input("\nEnter your password: ")
            admin_password = admin_password.replace(" ", "")

            if len(admin_password) == 0:
                print("\nPlease Do Not Leave it Empty")
                retry = input("\nWould You Like To Retry?(Y/N): ").lower()
                if retry == "y":
                    add_new_admin()
                else:
                    admin_interface()

            else:
                # Add the inputted strings into the text file
                new_admin = open("admin_info.txt", "a") # Open text file in append mode (Append is for adding new strings)
                new_admin.write (admin_name + " " + admin_password + " " + "\n") # Add the admin username first, followed by a space, and the password, followed by a space, and then add a newline (So next admin information will start in the next line)
                new_admin.close()
                print("\nNew Admin has been added !!!")
                
        exit = input("\nInput any letter or numbers to return to the admin menu: ")
        if exit == "y":
            admin_interface()
        else:
            admin_interface()
# Add cars
def add_car():
    print ("\n------------ Add Cars to be rented out ------------")
    car_model = input("Enter car model: ") # Ask for car model. 
    car_model = car_model.replace(" ", "")
    if len(car_model) == 0:
        print("\nPlease do not leave it blank !!!")
        add_car()
    else:
        car_color = input("Enter car color: ") # Ask for car color. 
        car_color = car_color.replace(" ", "")
        if len(car_color) == 0:
            print("\nPlease do not leave it blank !!!")
            add_car()
        else:
            car_plate = input("Enter car plate number: ").upper() # Ask for car plate. 
            car_plate = car_plate.replace(" ", "")
            if len(car_plate) == 0:
                print("\nPlease do not leave it blank !!!")
                add_car()
            else:
                # Checking for the same car plate in the text file
                with open("cars.txt","r") as all_car_info:
                    if car_plate in all_car_info.read():
                        print("\nThis car plate has already been registered into the database \nPlease recheck your car plate before re-entering")
                        exit = input("\nInput any letter or numbers to return to the admin menu: ")
                        if exit == "y":
                            admin_interface()
                        else:
                            admin_interface()

                    else:
                        print("Enter car availability: \n1.Available \n2.Unavailable") # Ask for car availability, who knows that the car might be brought to be serviced.
                        car_availability = input("Enter a number for the availability: ")

                        if car_availability == "1":
                            car_availability = "Available"

                        elif car_availability == "2":
                            car_availability = "Unavailable"

                        else:
                            print("\nENTER 1 OR 2 !!! \nYOU WILL NOW RE-ENTER THE CAR INFORMATION \n")
                            add_car()
                            
                        print("\n")
                        print("Car Model:", car_model)
                        print("Car Color:", car_color)
                        print("Car Plate:", car_plate)
                        print("Car Availability:", car_availability)
                        print("\n")

                        print("1. Confirm Entry")
                        print("2. Redo Entry")
                        print("3. Delete Entry")
                        choice = input("Enter a number: ")

                        if choice == "1":
                            car_information = open ("cars.txt", "a") # Open cars.txt in append mode. Append mode is to add the strings that have been inputted just now
                            car_information.write (car_model + " " + car_color + " " + car_plate + " " + car_availability + "\n") # Add all inputted strings into cars.txt
                            car_information.close() # Close cars.txt. Closing files is important as it reduces resources can does not slower your code.
                            print ("\nCar information is saved. You will be redirected to the admin menu") # Display that the car information is saved
                            admin_interface() # Redirect user back to the admin interface.
                                
                        elif choice == "2": # If admins want to redo their entry
                            add_car()

                        elif choice == "3": # If admins want to delete their entry
                            print("Entry Deleted. You will be redirected to the admin menu!")
                            admin_interface()
                        
                        else:
                            print("Enter a number from 1 to 3 !")
                            admin_interface()
# Displaying Cars that Will Be Rented Out Today
def display_cars_today():
    from datetime import date
    today = date.today()
    success = 0
    rented_today = []
    with open ("renthistory.txt","r") as rent_info:
        for cars in rent_info:
            car = cars.strip().split()
            if str(today) in car[3]:
                rented_today.append(car)
                success = 1
        rent_info.close()

    if success == 1:
        print("\n---------------------------------------------------------------------------")
        print("------------------- Cars That Will be Rented Out Today --------------------\n")
        print ("{:<15} {:<15} {:<15} {:<15} {:<15}".format("USERNAME", "CAR MODEL", "CAR PLATE", "RENTING FROM", "TO\n"))
        for lines in rented_today:
                print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(lines[0], lines[1], lines[2], lines[3], lines[4]))
        print ("--------------------------------------------------------------------------")
    else:
        print("\nNo cars will be rented out today.")
    
    adminmenu = input("\nInput any letter or numbers to return to the admin menu:")
    if adminmenu == "y":
        admin_interface()
    else:
        admin_interface()
# Display Customer Bookings
def display_customer_bookings():
    customer_bookings = [] # Empty list to store strings
    with open ("renthistory.txt","r") as rent_history:  # Open renthistory.txt in read mode
        for bookings in rent_history: # For lines in renthistory.txt
            booking = bookings.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
            customer_bookings.append(booking) # Add into the empty list
    print ("\n--------------------------------------------------------------------------")
    print ("---------------------------- Customer Bookings ---------------------------\n")
    # Organizing list when displayed
    print ("{:<15} {:<15} {:<15} {:<15} {:<15}".format("USERNAME", "CAR MODEL", "CAR PLATE", "RENTING FROM", "TO\n"))
    for lines in customer_bookings[::-1]:
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(lines[0], lines[1], lines[2], lines[3], lines[4]))
    print ("--------------------------------------------------------------------------")
# For searching specific record
def search_specific_record(): 
    print("\n------------ Searching Specific Record ------------")
    print("1. Customer Bookings")
    print("2. Customer Payment")

    try:
        record = int(input("\nWhich record do you want to search: ")) 
    except ValueError:
        print("ENTER A NUMBER FROM 1 TO 2 !!!")
        admin_interface()
        
    if record == 1:
        success = 0
        username = input("Please enter the username: ")
        username = username.replace(" ","")

        rental_history = [] # Empty list to store variables
        with open ("renthistory.txt", "r") as rent_history: # Open renthistory.txt in read mode
            for rents in rent_history: # For the strings inside renthistory.txt
                rent = rents.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
                if username in rent: # For strings inside "rent" list
                    rental_history.append(rent) # Add the strings from the rent list into the empty list
                    success = 1

            if success == 1: # If username is found in renthistory.txt
                print("\n--------------------------------------------------------------------------")
                print("------------------------ Personal Rental History -------------------------")
                # Displaying the strings in the list in an organized manner
                print ("{:<15} {:<15} {:<15} {:<15} {:<15}".format("USERNAME", "CAR MODEL", "CAR PLATE", "RENTING FROM", "TO"))
                for lines in rental_history:
                    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(lines[0], lines[1], lines[2], lines[3], lines[4]))
                print("--------------------------------------------------------------------------")

            else: # If username is not found in renthistory.txt
                print("\nUser has not rented any cars")
                
    elif record == 2:
        success = 0
        username = input("Please enter username: ")
        username = username.replace(" ","")

        payment_history = [] # Empty list to store variables
        with open ("payment.txt", "r") as payment: # Open payment.txt in read mode
            for customers in payment: # For the strings inside payment.txt
                customer = customers.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
                if username in customer: # For strings inside "customer" list
                    payment_history.append (customer) # Add the strings from the customer list into the empty list
                    success = 1
            payment.close()

            if success == 1: # If username is found
                print ("\n--------------------------------------------------------------")
                print ("---------------------- Customer Payment ----------------------")
                # Displaying the strings in the list in an organized manner
                print ("{:<15} {:<15} {:<15} {:<15}".format("PAYMENT DUE", "USERNAME", "AMOUNT", "PAYMENT STATUS"))            
                for users in payment_history:
                    print ("{:<15} {:<15} {:<15} {:<15}".format(users[0], users[1], users[2], users[3]))
                print ("--------------------------------------------------------------")

            else: # If username is not found
                print("\nUser does not have any payment information")

    else:
        print("\nEnter a number from 1 to 2 !!!")

    # For admins to return to the admin menu
    adminmenu = input("Input any letter or numbers to return to the admin menu: ")
    if adminmenu == "y":
        admin_interface()
    else:
        admin_interface()
# Function that removes car booking
def remove_car_booking(): 
    success = 0
    customer_bookings = [] # Empty list to store strings
    with open ("renthistory.txt","r") as rent_history:  # Open renthistory.txt in read mode
        for bookings in rent_history: # For lines in renthistory.txt
            booking = bookings.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
            customer_bookings.append(booking) # Add into the empty list
        rent_history.close()
    print ("\n--------------------------------------------------------------------------")
    print ("---------------------------- Customer Bookings ---------------------------\n")
    # Organizing list when displayed
    print ("{:<15} {:<15} {:<15} {:<15} {:<15}".format("USERNAME", "CAR MODEL", "CAR PLATE", "RENTING FROM", "TO\n"))
    for lines in customer_bookings[::-1]:
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(lines[0], lines[1], lines[2], lines[3], lines[4]))
    print ("--------------------------------------------------------------------------")

    remove_car_username = input("Enter the username of the booking you want to remove: ") # Ask admin for username
    remove_car_username = remove_car_username.replace(" ", "") # Remove spaces

    car_plate = input("Enter the car plate of the booking you want to remove: ").upper() # Ask for car plate (All letters will be capitalized)
    car_plate = car_plate.replace(" ", "") # Remove spaces

    for lists in customer_bookings: 
        if remove_car_username in lists and car_plate in lists: # If the car plate is found in any of the lists in customer_bookings
            success = 1

    if success == 1: 
        rent_history = open("renthistory.txt", "r") # Open renthistory.txt in read mode
        lines = rent_history.readlines() # Read each line one by one
        rent_history.close() # Close after reading each lines

        new_rent_history = open("renthistory.txt", "w") # Open renthistory.txt in write mode
        for line in lines: 
            if remove_car_username in line and car_plate in line: # If the username and car plate that was inputted is found in one of the lines in renthistory.txt
                pass # Ignore it
            else:
                new_rent_history.write(line) # Write the strings back into renthistory.txt
        new_rent_history.close() # Close text file after overwriting
        print("\nBooking has been removed successfully")

        remove_payment = open("payment.txt", "r")
        lines = remove_payment.readlines()
        remove_payment.close()

        new_payment = open("payment.txt", "w")
        for line in lines:
            if remove_car_username in line and "Unpaid" in line:  # If the username and the string "Unpaid" that was inputted is found in one of the lines in payment.txt
                pass
            else:
                new_payment.write(line)
        new_payment.close()

        ## Return car function
        making_car_available(car_plate)

        print ("\nCar has also been returned. You do not have to go to return the rented car manually. ")

    else:
        print("\nNo such username or car plate is being booked")

    adminmenu = input("Input any letter or numbers to return to the admin menu:")
    if adminmenu == "y":
        admin_interface()
    else:
        admin_interface()
# Display records menu
def display_records(): 
    print ("\n------------ Which Record Do You Want To Display ? ------------")
    print ("1. Cars Rented Out")
    print ("2. Cars available for Rent")
    print ("3. Customer Bookings")
    print ("4. Customer Payment by Month")
    print ("5. Return to Admin Menu")

    try:
        display_admin_input = int(input("Enter a number: "))
    except ValueError:
        print ("Enter a number from 1 to 5 !!!")
        display_records()

    if display_admin_input == 1: # If admins want to view the cars that are rented out
        view_unavailable_cars()
        
    elif display_admin_input == 2: # If admins want to view the cars that are available to rent
        available_cars()
        
    elif display_admin_input == 3: # If admins want to view customer bookings
        display_customer_bookings()
 
    elif display_admin_input == 4: # If admins wants to view customer payment status
        admin_input_date()

    elif display_admin_input == 5:# If admins wants to return to the admin menu
        admin_interface()
        
    else:
        print("Enter a number from 1 to 5 !!!")
    
    #  return to the menu
    adminmenu = input("Input any letter or numbers to return to the display records menu:")
    if adminmenu == "y":
        display_records()
    else:
        display_records()
# Function used for displaying customer payments by month and year (Month and Year Validation)
def admin_input_date():
    from datetime import datetime # Import module
    
    input_year = input("Enter a year: ") # Ask admin to enter the year

    print("\n1. January", input_year)
    print("2. February", input_year)
    print("3. March", input_year)
    print("4. April", input_year)
    print("5. May", input_year)
    print("6. June", input_year)
    print("7. July", input_year)
    print("8. August", input_year)
    print("9. September", input_year)
    print("10. October", input_year)
    print("11. November", input_year)
    print("12. December", input_year)

    user_input = input("\nEnter a number: ") # Input a number (Months)
    
    if user_input == "1":
        input_month = "01" 

    elif user_input == "2":
        input_month = "02"

    elif user_input == "3":
        input_month = "03"

    elif user_input == "4":
        input_month = "04"

    elif user_input == "5":
        input_month = "05"

    elif user_input == "6":
        input_month = "06"

    elif user_input == "7":
        input_month = "07"

    elif user_input == "8":
        input_month = "08"

    elif user_input == "9":
        input_month = "09"

    elif user_input == "10":
        input_month = "10"

    elif user_input == "11":
        input_month = "11"

    elif user_input == "12":
        input_month = "12"

    else: # If admin enter a number other than numbers ranging from 1 to 12
        print("Please enter a number from 1 to 12 !!!")
        retry = input("Enter any letter or number to continue: ")
        if retry == "y": 
            display_records()
        else:
            display_records()

    try:
        # Data Validation
        # Convert variable into a datetime format using strptime()
        input_month = datetime.strptime(input_month,'%m') # Only month 
        input_year = datetime.strptime(input_year, '%Y') # Only year
        
        input_month = input_month.strftime('%m')
        input_year = input_year.strftime('%Y')
    except:
        # If its not in a year format. For example (1234 is not a year)
        print("\nEnter the year in a proper manner !!! (E.g. 2021)")
        adminmenu = input("Input any letter or numbers to return to the display records menu:").lower()
        if adminmenu == "y":
            display_records()
        else:
            display_records()

    display_payment_month(input_month, input_year) #display_payment_month is called
# Function used for displaying customer payments by month and year (After Validating Month and Year)
def display_payment_month(input_month, input_year):
    import datetime
    success = 0
    data = [] # Empty list to store strings
    with open ("payment.txt", "r") as payment: # Open payment.txt in read mode
        for customers in payment: # For lines in payment.txt
            customer = customers.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
            
            date = datetime.datetime.strptime(customer[0], "%Y-%m-%d") # Change the strings in the first column of every row into a datetime format (year,month,day)
            month = date.strftime('%m') # only month is extracted from the date variable
            year = date.strftime('%Y') # only year is extracted from the date variable

            if month == input_month and year == input_year: # If year and month variable matches the year and month of the admin input
                data.append(customer) # Add strings into the empty list
                success = 1 # Store the integer 1 into the success variable, previously was 0
        
    if success == 1: # If success contains the integer 1
        print ("\n--------------------------------------------------------------")
        print ("---------------------- Customer Payment ----------------------")
        print ("{:<15} {:<15} {:<15} {:<15}".format("PAYMENT DUE", "USERNAME", "AMOUNT", "PAYMENT STATUS")) # Print each string within the 15 spaces, and repeat for each strings(E.g. "PAYMENT DUE" is also included in the 15 spaces)        
        for users in data: # For the list(users) inside the list(data)
            print ("{:<15} {:<15} {:<15} {:<15}".format(users[0], users[1], users[2], users[3])) # Print each string within the 15 spaces from the list, and repeat for each strings. Each string has 15 spaces
        print ("--------------------------------------------------------------")

    else: # If no information is found in the text file (success variable contain 0), which means month and year does not match with admin input
        print("\nNo payment information available during that period") 
# View unavailable cars
def view_unavailable_cars():
    unavailable_for_rent = []
    success = 0
    with open ("cars.txt", "r") as car_information: # Open cars.txt in read mode
        for cars in car_information: # For the lines(cars) in car_information(cars.txt)
            car = cars.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
            if "Unavailable" in car: # If the string "Unavailable" is detected
                unavailable_for_rent.append(car) # Add into the empty list
                success = 1
                
    if success == 1:
        print("\n----------------------------------------------------------")
        print("-------------------- Cars Rented Out ---------------------\n")
        # Organizing list when displayed
        print ("{:<15} {:<15} {:<15} {:<15}".format("CAR MODEL", "CAR COLOR", "CAR PLATE", "CAR STATUS\n")) # Print each string within the 15 spaces from the list, and repeat for each strings. Each string has 15 spaces
        for cars in unavailable_for_rent: # For the list(cars) inside the list(unavailable_for_rent)
            print("{:<15} {:<15} {:<15} {:<15}".format(cars[0], cars[1], cars[2], cars[3])) # Print each string within the 15 spaces from the list, and repeat for each strings. Each string has 15 spaces
        print("----------------------------------------------------------")
        
    else:
        print('No cars are rented out at the moment.')
# Returning rented car
def return_a_car():
    success = 0
    unavailable_for_rent = [] # Empty list to store strings
    with open ("cars.txt", "r") as car_information: # Open cars.txt in read mode
        for cars in car_information: # For the lines in cars.txt
            car = cars.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
            if "Unavailable" in car: # If the string "unavailable" is detected
                unavailable_for_rent.append(car) # Add into the empty list
    print("\n----------------------------------------------------------")
    print("-------------------- Cars Rented Out ---------------------\n")
    # Organizing list when displayed
    print ("{:<15} {:<15} {:<15} {:<15}".format("CAR MODEL", "CAR COLOR", "CAR PLATE", "CAR STATUS\n"))
    for cars in unavailable_for_rent:
        print("{:<15} {:<15} {:<15} {:<15}".format(cars[0], cars[1], cars[2], cars[3]))
    print("----------------------------------------------------------")


    car_plate = input("Enter the car model's car plate: ") # Ask which car plate
    car_plate = car_plate.replace(" ", "")

    for cars in unavailable_for_rent: # For the strings inside the rented_out list,
        if car_plate in cars:
            success = 1

    if success == 1: # If both inputs are in the list
        making_car_available(car_plate)
        
        # Return to admin interface
        admin_menu = input("\nCar has been returned. Would you like to return any more cars?(Y/N): ").lower()
        if admin_menu == "y":
            return_a_car()
        else:
            admin_interface()
                
    else: # If both inputs are not in the list
        print("\nNo such car that is rented out in database !!! \nPLEASE ENTER THE CAR MODEL AND CAR PLATE EXACTLY.")
        retry = input("\nWould you like to retry?(Y/N): ").lower()
        if retry == "y":
            return_a_car()
        else:
            admin_interface()
# Remove admin
def remove_admin():
    success = 0
    all_admins = [] # Empty list for storing strings
    with open('admin_info.txt','r') as admin_information: 
        for admins in admin_information:
            admin = admins.strip().split()
            all_admins.append(admin)
    print("\n------------------------------------")
    print("------------ All Admins ------------")
    #Organizing list when displayed
    print("{:<20} {:<20}".format("USERNAME", "PASSWORD\n"))
    for admins in all_admins:
        print("{:<20} {:<20}".format(admins[0], admins[1]))
    print("-----------------------------------")

    remove_username = input("Enter the username of the admin that you want to remove: ") #Ask admin for username which they would like to remove
    remove_username = remove_username.replace(" ", "")

    for admin in all_admins:
        if remove_username in admin: # if the inputted username is found in the list,
            success = 1
    
    if success == 1:
        # Read lines in admin_info.txt
        admin_info = open('admin_info.txt', 'r')
        lines = admin_info.readlines()
        admin_info.close()

        # Rewrite lines in admin_info.txt
        new_admin_info = open('admin_info.txt', 'w')
        for line in lines:
            if remove_username in line: # Skip the line which contain the username from the admin input
                pass 
            else:
                new_admin_info.write(line)
        new_admin_info.close()
        print("\nAdmin has been removed successfully !")
        
    else: # If username is not found
        print("\nNo such username found in the admin database\nMake sure that you enter the username accurately.")
    
    # Returning to admin menu
    adminmenu = input("\nInput any letter or numbers to return to the admin menu: ")
    if adminmenu == "y":
        admin_interface()
    else:
        admin_interface()    
# Making car available (Used for returning a rented car)
def making_car_available(car_plate):
    with open("cars.txt", "r") as car_information: # Open cars.txt in read mode
        car_details = [] # Make an empty list (To put the strings from the text file)
        for cars in car_information: # For the lines in the text file,
            car = cars.strip().split()
                
            if car_plate in car:
                for strings in car:
                    car_new = strings.replace("Unavailable", "Available") # Replace the string "Unavailable" with "Available"
                    car_details.append(car_new) # Add the new strings into the empty list
                    
                cars_information = open("cars.txt", "r") # Open cars.txt in read mode
                lines = cars_information.readlines() # Read lines in the text file
                cars_information.close()

                new_information = open("cars.txt", "w") # Open cars.txt in write mode
                for line in lines: # For the strings inside in each lines that was read just now,
                    if car_plate not in line: # If the car plate is not detected,
                        new_information.write(line) # write the strings 
                new_information.close()

                with open("cars.txt", "a") as cars_information: # Open cars.txt in append mode
                    for car in car_details: # for strings inside the car_details list (The empty list that was created just recently)
                        cars_information.write(car + " ") # Add the first string inside, then add a space, and repeat until there is none
                    cars_information.write("\n") # Add new line after all the strings are added into cars.txt
                    cars_information.close() # Close cars.txt

        car_information.close()




## FUNCTIONS USED IN CUSTOMER MENU
# Modify user function (Text File)
def modify_user_text_file(contact_number, user):
    user_information = open("login.txt", "r") # Open cars.txt in read mode
    lines = user_information.readlines() # Read each line one by one
    user_information.close() # Close after reading each lines
                                        
    new_information = open("login.txt", "w") # Open cars.txt in write mode
    for line in lines: 
        if contact_number not in line: # If the car plate(Unique ID for each car) is not in the lines
            new_information.write(line) # Write it in the text file (The one with the specific contact number will not be written)
    new_information.close() # Close after writing

    with open("login.txt", "a") as user_information: # Open login.txt in append mode
        for strings in user:
            user_information.write(strings + " ") # Add car information, and then add a space, and then continue (We are not replacing, we are adding in as if its new information)
        user_information.write("\n") # Add a new line after finish adding the information    
        user_information.close()
# Modify user function
def modify_user_function(username):
    success = 0
    contact_number = input("\nEnter your contact number: ") # Ask user for contact number
    if len(contact_number) == 0: # If the input is blank
        print("Please Do Not Leave It Blank !!!")
    else:
        with open("login.txt", "r") as user_information: # Open login.txt 
            for users in user_information:
                user = users.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
                if username in user[0] and contact_number in user[2]: # If the username is found in the first column and the contact number is found in the third column of that specific list during looping,
                    success = 1 # Store the integer 1 in the success variable
            

        if success == 1:
            with open("login.txt", "r") as user_information:
                for users in user_information:
                    user = users.strip().split()
                    if contact_number in user[2]:
                        print("1. Username       : ", user[0]) # Display the first column of that specific list (That the car plate was found in)
                        print("2. Password       : ", user[1]) # Display the second column of that specific list (That the car plate was found in)
                        print("3. Contact Number : ", user[2]) # Display the third column of that specific list (That the car plate was found in)
                        print("4. Return to Customer Menu")
                        try:
                            fno = int(input("Enter the field number to modify: ")) # Ask user which field they would like to modify
                        except:
                            print("Please enter a number from 1 to 4 !!! ")
                            break # Break for loop
                        
                        if fno == 1:
                            print("Your current Username is : ", user[fno - 1]) # The inputted number must be subtracted by 1 (First column of every list is the number '0', not '1')
                            user[fno - 1] = input("Enter new Username: ") # Ask for new username
                            user[fno - 1] = user[fno - 1].replace (" ", "") # Remove spaces

                            if len(user[fno - 1]) == 0: # If the inputted string by the user is blank
                                print("\nPlease do not leave it blank !!!")
                                break # Break for loop
                            
                            else:
                                # Checking for the same username in login.txt
                                same_username = 0
                                with open ("login.txt","r") as account_informations:
                                    for accounts in account_informations:
                                        account = accounts.strip().split()
                                        if user[fno - 1] in account[0]:
                                            same_username = 1
                                    account_informations.close()

                                if same_username == 1: # If the same username is detected
                                    print("\nUsername is taken \nPlease try a new username")
                                    break # Break for loop

                                else:
                                     # Add the list that was changed, into the empty list
                                    modify_user_text_file(contact_number, user) # modify_user_text_file(contact_number, user_details) function executed
                                    # Display new changes
                                    print("\nYour new Username is: ")
                                    print("1. Username       : ", user[0])
                                    print("2. Password       : ", user[1])
                                    print("3. Contact Number : ", user[2])
                                    

                                    # Changing the username in the renthistory.txt file, if the previous username is detected.
                                    rental_history = []
                                    with open("renthistory.txt", "r") as customer_bookings:
                                        for customers in customer_bookings:
                                            customer = customers.strip().split()
                                            if username in customer[0]: # If the old username is detected in the first column of a list
                                                customer[0] = user[fno - 1] # Replace old username with new username
                                            rental_history.append(customer) # Add the changed list into the empty list (rental_history)
                
                                    increment = 0
                                    with open("renthistory.txt", "w") as customer_bookings:
                                        # Add the new lists into renthistory.txt
                                        while increment < len(rental_history): 
                                            customer_bookings.write(" ".join(rental_history[increment]) + "\n")
                                            increment += 1
                                    
                                    # Changing the username in the payment.txt file, if the previous username is detected.
                                    payment_history = []
                                    with open("payment.txt", "r") as customer_payment:
                                        for customers in customer_payment:
                                            customer = customers.strip().split()
                                            if username in customer[1]: # If the old username is detected in the second column of a list
                                                customer[1] = user[fno - 1] # Replace old username with new username
                                            payment_history.append(customer) # Add the changed list into the empty list (payment_history)
                                    
                                    increment_payment = 0
                                    with open("payment.txt", "w") as customer_payment:
                                        # Add the new lists into renthistory.txt
                                        while increment_payment < len(payment_history):
                                            customer_payment.write(" ".join(payment_history[increment_payment])+"\n")
                                            increment_payment += 1
                                    
                                    username = user[fno - 1] # Store the new username that was inputted in the username variable(So that in the other functions, it can detect the new username)
                                    break # Break for loop

                        elif fno == 2:
                            print("Your current Password is : ", user[fno - 1])
                            user[fno - 1] = input("Enter new Password: ")
                            user[fno - 1] = user[fno - 1].replace (" ", "")

                            if len(user[fno - 1]) == 0:
                                print("\nPlease do not leave it blank !!!")
                                break # Break for loop
                            else:
                                modify_user_text_file(contact_number, user)
                                print("\nYour new Password is: ")
                                print("1. Username       : ", user[0])
                                print("2. Password       : ", user[1])
                                print("3. Contact Number : ", user[2])
                                break # Break for loop
                        
                        elif fno == 3:
                            print("Your current Contact Number is : ", user[fno - 1])
                            user[fno - 1] = input("Enter new Contact Number: ").upper()
                            user[fno - 1] = user[fno - 1].replace (" ", "")

                            if len(user[fno - 1]) == 0:
                                print("\nPlease do not leave it blank !!!")
                                break # Break for loop
                            elif len(user[fno - 1]) < 9:
                                print("\nPlease enter a proper contact number !!!")
                                break # Break for loop
                            elif len(user[fno - 1]) >= 9 and user[fno - 1].isdigit():
                                same_contact_number = 0
                                # Cheking for the same contact number in login.txt
                                with open ("login.txt","r") as account_informations:
                                    for accounts in account_informations:
                                        account = accounts.strip().split()
                                        if user[fno - 1] in account[2]:
                                            same_contact_number = 1
                                    account_informations.close()
                                if same_contact_number == 1:
                                    print("\nContact number is taken and found in the database\nPlease make sure you have inputted the correct contact number")
                                    
                                else:
                                    modify_user_text_file(contact_number, user)
                                    print("\nYour new Contact Number is: ")
                                    print("1. Username       : ", user[0])
                                    print("2. Password       : ", user[1])
                                    print("3. Contact Number : ", user[2])
                                    break # Break for loop
                            else:
                                print("Enter a proper contact number !!!")
                                break # Break for loop
                            
                        elif fno == 4:
                            customer_interface(username)
                        else:
                            print("\nEnter a number from 1 to 4 !!!")
        else:
            print("\nInvalid contact number !")

    menu = input("\nInput any letter or numbers to return to the customer menu: ")
    if menu == "y":
        customer_interface(username)
    else:
        customer_interface(username)
# For customers to book a car
def book_a_car(username):
    available_cars()
    print("\nAll the cars costs RM40 per day")
    rent_car_model = input("\nWhich car model do you want to rent?: ") #Input which car model
    rent_car_model = rent_car_model.replace(" ","")

    rent_car_plate = input("Enter the car model's car plate: ").upper() # Input car plate
    rent_car_plate = rent_car_plate.replace(" ","")

    cars_information = open ("cars.txt", "r").readlines() # Open cars.txt in read mode and read each line.
    car_data = [] # Create an empty list

    for lines in cars_information:
        car_data.append(lines.split()) # Split strings when a space is detected. Add the strings into the empty list

    increment = 0 # Increment will be used for looping
    success = 0 

    while increment < len(car_data):
        car_models = car_data[increment][0] # If the increment is less than the length of the list, check the first column of the first row, which will gradually increase to first column of the second row 
        car_plates = car_data[increment][2] # If the increment is less than the length of the list, check the third column of the first row, which will gradually increase to third column of the second row

        if rent_car_model == car_models and rent_car_plate == car_plates: 
            success = 1 #If car model and car plates finally match one another, success will become 1, so that the code than continue
        increment += 1 # Add increment by 1, so that it won't loop forever in 0.
        
    if success == 1: 
        from datetime import datetime # Import datetime module
        try:
            print("\nYou can only rent the car for more than 24 hours. \nYou can not rent the car in an hourly manner\n")
            start = input("From which day (dd/mm/yyyy): ") # Ask user when do they want to start booking the car (Not everyone wants to book it during that day)
            end = input("To which day (dd/mm/yyyy): ") # Until the final day
            start = datetime.strptime(start, '%d/%m/%Y').date() # Change the format to (day/month/year) and change the format to days as well
            end = datetime.strptime(end, '%d/%m/%Y').date()
        except:
            print("\nPlease enter date in a dd/mm/yyyy format")
            print ("FOR EXAMPLE: 03/03/2021")
            print ("DO NOT FORGET ABOUT /")
            retry = input("\nWould you like to retry?(Y/N): ").lower()
            if retry == "y":
                book_a_car(username)
            else:
                customer_interface(username)

        day_diff = end - start # Difference between the end date and the start date is the number of days that the car will be used by the customers
        price = day_diff.days * 40 # Multiply it with the cost of renting a car per day

        if price <= 0:
            print("\nYou have entered the starting day earlier than the ending date ! \nTRY AGAIN")

        else:
            payment_info = open("payment.txt", "a") # Open payment.txt in append mode
            payment_info.write(str(start) + " " + username + " " + "RM" + str(price) + " " + "Unpaid" + "\n") # Add the starting date of the booking (Must be in string as it is a text file) 
            payment_info.close() # Close the text file

            rent_car = open("renthistory.txt","a") # Open renthistory.txt in append mode
            rent_car.write(username + " " + rent_car_model + " " + rent_car_plate + " " + str(start) + " " + str(end) + "\n") # Add username
            rent_car.close() # Close the text file

            print("\nCar is successfully booked, please proceed to the payment page") # Tell user that their desired car is successfully booked and to go to the payment page
            print("Your payment is RM",price, "and must be paid before,", str(start)) # Show user their due date of the payment (Some may not have money now)

            car_details = [] # Make an empty list (To put the strings from the text file)
            with open("cars.txt", "r") as car_information: # Open cars.txt in read mode
                for cars in car_information: # For the lines in the text file,
                    car = cars.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method

                    if rent_car_plate in car: # If car model and car plate is detected in the text file
                        for strings in car: # For i inside the car list,
                            car_new = strings.replace("Available", "Unavailable") # Replace the word "available" with "unavailable"
                            car_details.append(car_new) # Add it into the empty list that was created

                        cars_information = open("cars.txt", "r") # Open cars.txt in read mode
                        lines = cars_information.readlines() # Read lines in the text file
                        cars_information.close() # Close text file after reading lines

                        new_information = open("cars.txt", "w") # Open cars.txt in write mode
                        for line in lines: # For the strings inside in each lines that was read just now,
                            if rent_car_plate not in line: # If the car plate is not detected,
                                new_information.write(line) # write the strings 
                        new_information.close() # Close after writing all the lines without that car plate.

                        with open("cars.txt", "a") as cars_information: # Open cars.txt in append mode
                            for car in car_details: # for strings inside the car_details (The empty list that was created just recently)
                                cars_information.write(car + " ") # Add the first string inside, then add a space, and repeat until there is none
                            cars_information.write("\n") # Add new line after all the strings are added into cars.txt
                            cars_information.close() # Close cars.txt after adding new strings

                cars_information.close() # Close cars.txt

        exit = input("\nInput any letter or numbers to return to the customer menu: ")
        if exit == "y":
            customer_interface(username)
        else:
            customer_interface(username)

    else: # If car model does not match any of the car plate
        print("\nNo such car in our database \nPLEASE MAKE SURE THAT YOU TYPE IN THE CAR MODEL AND CAR PLATE EXACTLY \nPLEASE TRY AGAIN") # Let user know that there is no such car in the database 
        retry = input("\nWould you like to retry?(Y/N): ").lower()
        if retry == "y":
            book_a_car(username)
        else:
            customer_interface(username)
# For customers to view their personal rental history
def personal_rental_history(username):
    success = 0
    rental_history = [] # Empty list to store strings
    with open ("renthistory.txt", "r") as rent_history: 
        for rents in rent_history:
            rent = rents.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
            if username in rent:
                rental_history.append(rent)
                success = 1

    if success == 1:
        print("\n--------------------------------------------------------------------------")
        print("------------------------ Personal Rental History -------------------------")
        print ("{:<15} {:<15} {:<15} {:<15} {:<15}".format("USERNAME", "CAR MODEL", "CAR PLATE", "RENTING FROM", "TO"))
        for lines in rental_history:
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(lines[0], lines[1], lines[2], lines[3], lines[4]))
        print("--------------------------------------------------------------------------")
                        
    else:
        print("\nYou have not rented any cars.")

    # For users to return to customer menu after viewing
    exit = input("\nInput any letter or number to go to the customer menu: ")
    if exit == "y":
        customer_interface(username)
    else:
        customer_interface(username)
# For customers to do payment
def customer_payment(username):
    success = 0
    payment_history = [] # Empty list to store variables
    with open ("payment.txt", "r") as payment: # Open payment.txt in read mode
        for customers in payment: # For the strings inside payment.txt
            customer = customers.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method
            if username in customer and "Unpaid" in customer: # For strings inside "customer" list
                payment_history.append (customer) # Add the strings from the customer list into the empty list
                success = 1
        payment.close()

    if success == 1: # If username is found
        import datetime # Datetime module
        print ("\n--------------------------------------------------------------")
        print ("---------------------- Customer Payment ----------------------")
        # Displaying strings in list in an organized manner
        print ("{:<15} {:<15} {:<15} {:<15}".format("PAYMENT DUE", "USERNAME", "AMOUNT", "PAYMENT STATUS",))            
        for users in payment_history:
            print ("{:<15} {:<15} {:<15} {:<15}".format(users[0], users[1], users[2], users[3]))
        print ("--------------------------------------------------------------")

        pay_now = input("Would you like to pay now?(Y/N): ").lower()
        if pay_now == "y":
            print("\nPLEASE ENTER THE AMOUNT FOR ONE TRANSACTION\nIF YOU HAVE 2 PAYMENTS, PLEASE DO IT ONE BY ONE")
            print("\n------------ Instructions to confirm Payment -----------")

            card_number = input("\nEnter your credit/debit card number: ") # Ask for card number
            if len(card_number) == 0: # If the length of the string that was inputted by the user is 0 (It means that its a blank input)
                print("\nPlease do not leave it blank !")
                customer_payment(username)

            elif card_number.isdigit():
                try:
                    exp_date = input("Enter the expiry date of your credit/debit card in mm/yyyy format: ") # Ask user for the expiry date of their card
                    datetime.datetime.strptime(exp_date, '%m/%Y') # Change the format to (month/year) 
                    
                except: # If expiry date not inputted in a mm/yyyy format
                    print("Please enter date in a mm/yyyy format")
                    print ("FOR EXAMPLE: 03/2026")
                    print ("DO NOT FORGET ABOUT /")
                    customer_payment(username)
            
                cvv = input("Enter your credit/debit card's cvv: ") # Ask for cvv
                if len(cvv) == 0: # If the user enters a blank input
                    print("\nPlease do not leave it blank !")
                    customer_payment(username)

                elif cvv.isdigit(): # If the cvv is all in numbers
                    price = input("Enter amount to pay (ENTER THE EXACT AMOUNT): ") # Ask for amount
                    if len(price) == 0: # If the input is a blank input
                        print("\nPlease do not leave it blank !")
                        customer_payment(username)
                    elif price.isdigit(): # If the amount is all in numbers
                        price = ("RM"+price) # Add the strings "RM" in front of the amount

                        print("\n--------------------------------------------------------")
                        print ("Before proceeding with payment, please double confirm your card information again:")
                        print("--------------------------------------------------------")
                        # Display all inputted information
                        print("Card number:", card_number)
                        print("Valid Through:", exp_date)
                        print("CVV number:", cvv)
                        print("Amount to pay:", price) 
                        

                        confirm = input("\nDo you confirm that it is the correct information?(Y/N): ").lower()
                        if confirm == "y":
                            # Checking for the correct card number, expiry date, and cvv combination in the text file
                            # All the concepts below was explained in the codes above
                            card_information = open("card_information.txt", "r")
                            card_data = []
                            for lines in card_information:
                                card_data.append(lines.split())
                            
                            card_confirmed = 0
                            increment = 0

                            while increment < len(card_data): # Keeps increasing the increment. Loop will stop once the increment is more than the length of card_data
                                card_numbers = card_data [increment][0] # Checks the first row and column of the card_data list. As it increases, it checks the second row, then the third row.
                                expiry_dates = card_data [increment][1] # Checks the first row and second column of the card_data list. As it increases, it checks the second row, then the third row.
                                cvv_numbers = card_data [increment][2] # Checks the first row and  third column of the card_data list. As it increases, it checks the second row, then the third row.

                                if card_number == card_numbers and expiry_dates == exp_date and cvv_numbers == cvv: 
                                    card_confirmed = 1
                                increment += 1

                            if card_confirmed == 1:
                                user_payment_information = open("payment.txt", "r")

                                user_data = [] # Empty list for the strings inside login.txt
                                for lines in user_payment_information: # For the strings in each line
                                    user_data.append(lines.split()) # Split the strings when a space is detected

                                increment = 0 # Increment will increase when used in while loop
                                success = 0

                                while increment < len(user_data): 
                                    usernames = user_data [increment][1] # If the increment is less than the length of the list, check the first column of the first row, which will gradually increase to first column of the second row 
                                    prices = user_data [increment][2] # If the increment is less than the length of the list, check the third column of the first row, which will gradually increase to third column of the second row

                                    if username == usernames and price == prices: #If username and contact number finally match one another, success will become 1, so that the code than continue
                                        success = 1 # Success variable will become 1
                                    increment +=1 # Gradually add increment by 1. So it wont loop forever in zero
                                
                                if success == 1:
                                    payment_details = []
                                    with open("payment.txt","r") as payment_done:
                                        for payments in payment_done:
                                            payment = payments.strip().split() # Strings will be splitted when a space is detected. After splitting, newlines are removed through the strip method

                                            if username in payments and price in payments: # If username and price is detected 
                                                for strings in payment: # For the strings inside the payment list
                                                    payment_new = strings.replace("Unpaid", "Paid") # Replace the string "unpaid" with "paid"
                                                    payment_details.append(payment_new) # Add the strings into the empty list

                                                payment_information = open("payment.txt","r") # Open payment.txt in read mode
                                                lines = payment_information.readlines() # Read each line one by one
                                                payment_information.close() # Close after reading each lines

                                                new_information = open("payment.txt", "w") # Open payment.txt in write mode
                                                for line in lines:
                                                    if username in line and price in line and "Unpaid" in line: # If the username and amount is found in one of the lines
                                                        pass # Ignore it
                                                    else: # If not,
                                                        new_information.write(line) # Write the strings back into the text file
                                                new_information.close() # Close after writing

                                                with open("payment.txt", "a") as payment_information: # Open payment.txt in append mode
                                                    for payment in payment_details:
                                                        payment_information.write(payment + " ") # Add payment information, and then add a space, and then continue (We are not replacing, we are adding in as if its new information)
                                                    payment_information.write("\n") # Add a new line after finish adding the information  
                                                    payment_information.close()
                                                    
                                        payment_done.close()

                                    print("Payment Successful !!!")
                                    print("Please come at receive the car you have selected during the day of rent from our car centre in Kuala Lumpur!! ")
                                    customer_interface(username)
                                else:
                                    print("Amount Entered is Wrong.")
                                    customer_payment(username)

                            else: # If the combination of card number, expiry date, and cvv combination in the text file is wrong
                                print("\nInvalid card information.\nPlease Try Again")
                                customer_payment(username)

                        elif confirm == "n": # If user would like to re-enter the card information or amount
                            print("\nPlease re-enter your card details")
                            print("You will be redirected back to the payment menu to retry")
                            customer_payment(username)

                        else: # If users type anything other than y or n
                            print("Type in either y or n !!!")
                            customer_payment(username)

                    else:
                        print("Input only numbers !")
                        customer_payment(username)

                else:
                    print("Input only numbers !")
                    customer_payment(username)
            else:
                print("Input only numbers !")
                customer_payment(username)
                
        elif pay_now == "n": # If users would like to pay later
            print("You will be redirected to the customer menu.")
            customer_interface(username)
        else:
            customer_interface(username)
    
    else:
        print("You have no payments due.")
        customer_interface(username)
## Customer Interface
def customer_interface(username):

    print ("\n--------------------------------------------")
    print ("------------ Customer Interface ------------")
    print ("1. Modify Personal Details")
    print ("2. View Personal Rental History")
    print ("3. View Detail of Cars to be Rented Out")
    print ("4. Select and Book a car for a specific duration")
    print ("5. Do payment to confirm Booking")
    print ("6. Return to main menu")
    print ("--------------------------------------------")
    
    try:
        customer_input = int(input("Enter a number: "))
    except ValueError:
        print ("ENTER A NUMBER FROM 1 TO 6")
        customer_interface(username)

    if customer_input == 1: # If users want to modify their personal details.
        modify_user_function(username)
                  
    elif customer_input == 2: # If users want to view their personal rental history.
        personal_rental_history(username)
        
    elif customer_input == 3: # If customers want to look at available cars.
        available_cars()
        #  return to the menu
        exit = input("\nInput any letter or numbers to return to the customer menu: ")
        if exit == "y":
            customer_interface(username)
        else:
            customer_interface(username)

    elif customer_input == 4: # If customers wants to book a car
        book_a_car(username)

    elif customer_input == 5: # If customers want to do payment
        customer_payment(username)

    elif customer_input == 6: # If customers want to return to the main menu
        print("Logged out successfully")
        main_menu()
    
    else:
        print("Enter a number from 1 to 6 !!!")
        customer_interface(username)


main_menu()