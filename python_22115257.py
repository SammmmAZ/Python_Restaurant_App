# MODULES USED

import random as random #--- imported as of 6/7/2023
#to be located at ==<?>==
import datetime as datetime #--- imported as of 10/7/2023
#to be located at ==<?>==
import os as os #--- imported as of 10/7/2023
#to be located at ==<?>==

# FILES INVLOVLED

GUEST_TXT="reservation_22115257.txt"
MENU_TXT="menuitem_22115257.txt"

# Customer Info
#list=[{name},{e-mail},{phone-number},{pax}] => Format {name}|{e-mail}|{phone-number}|{pax}
# data type for each element [{type(name)=str},{type(e-mail)=str},type{phone-number}=int,type{pax}=int]
cust_info=[]

# Reservation Info
# Format {date}|{session}|{slot}
# data type for {date}-> str, {session}-> str with len(str)=1, slot=int with 0<slot<9
book_info=[]

#--- to hold current reservation from user info
#--- once complete, append the list within to list reservation as format below
#--- current_resservation =[[book_info[0],bokk_info[1],book_info[2],cust_info[0],cust_info[1],cust_info[2],cust_info[3]]]
#--- insert with list_reservation.append(current_reservation) -- at sub_menu1
current_reservation=[]
menu_items=[]

#format for better display

format_string=("""
=================================================
/\_/\_/\_/\_/\_RESERVATION_/\_/\_/\_/\_/\_/\_/\_/
=================================================
date={date}
session={session}
slot={slot}
name={name}
email={email}
phone number={number}
pax={pax}
=================================================
/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/
=================================================
""")


date_format="%Y-%M-%d"

# to welcome the user when program starts
#==<<COMPLETED AS OF 17/7/2023>>==


def main_menu():    #to be located in main section of main()
    current_reservation=Read_file(1)
    menu_items=Read_file(2)
    while True:
     os.system("cls")
     print(
        """
\t\t\t<Welcome To Charming Thyme Terracota>\t\t\t\t\t\t\t
\t\t\t<Management service by: SUNWAY STUDENTS>\t\t\t\t
\t\t\t<to manage reservations & Menu suggestions>\t\t\t
TO PROCEED PLEASE ENTER NUMBERS INTO THE CHOICE BASED ON THE
FOLLOWING OPTIONS BELOW:\t\t\t\t\t\t\t\t\t
\t[1]ADD RESERVATION \t\t\t\t[2]CANCEL RESERVATION\t\t
\t[3]EDIT RESERVATION\t\t\t\t[4]DISPLAY RESERVATION\t
\t[5]GENERATE RECOMMENDATIONS\t\t\t[6] EXIT\t\t
        """
    )
     try:
        choice = int(input("ENTER CHOICE FROM MENU ABOVE:")) # DIrects user to the next sub menu
        
     except choice>= 6 or choice ==0 as ValueError1:
        print("Please Enter an valid option")
        
     except type(choice)==str or type(choice)== float as ValueError2:
        print("Please Enter a number from 1 to 6")

     if choice==1:
        sub_menu(1) # Prints greeting as user enters sub-menu 1
        get_cust_info(cust_info) #---get customer Info
        book_info=getBookingInfo(current_reservation) #--- gets booking info
        current_reservation.append(book_info+cust_info) # appends newly get reservation into
        input("Enter to continue\n")
        continue
     if choice==2:
        sub_menu(2)
        delete_reservation(skim_reservation(current_reservation),current_reservation) # gets customer reservation, then opens it, choose reservation to delete, then exits
        input("Enter to continue\n")
        continue
     if choice==3:
        sub_menu(3) # greets user
        edit_reservation(skim_reservation(current_reservation),current_reservation) #opens customer reservation, then edit it by list in list info
        input("Enter to continue\n")            
        continue
     if choice==4:
        sub_menu(4)
        display_reservations(current_reservation) # displays 
        print()
        input("Enter to continue\n")
        continue
     if choice==5:
        sub_menu(5)
        random_meal() #Generates the random meal
        input("Enter to continue\n")
     if choice==6:
        sub_menu(6)
        input("Goodbye. Press enter to continue\n")
        write_file(current_reservation)
        break


     


#Welcomes user to each respective sub-menu
# briefs on how input format to utilise write and append to reservation file
#===<DONE>===

def sub_menu(main_menu):    #to be located in front of each section  of after main()
    os.system('cls')
    if main_menu==1: # Sub-Menu Greetings for option 1
     print("""
\t\t\t\t<<WELCOME TO THE SUBMENU A>>\t\t\t\n
\t\t\t\t\t\t<<=ADD RESERVATION=>>\t\t\t\n
\t\t\t\t<<FILL IN CUSTOMER INFO>>\t\t\t\n
""")
     
    if main_menu==2:
        print("""
\t\t\t\t\t\t<<WELCOME TO SUB-MENU B>>\t\t\t\n
\t\t\t\t\t\t<<CANCEL RESERVATION>>\t\t\t\n
\t\t\t\t<<REMOVE CUSTOMER RESERVATION>>\t\t\t\n
""")
        
    if main_menu==3:
        print("""
\t\t\t\t<<WELCOME TO SUB MENU C>>\t\t\t\n
\t\t\t\t<< UPDATE RESERVATION >>\t\t\t\n
\t\t\t\t<<=_-_-_-_-_-_-_-_-_-_-_>>\t\t\n
""")
        
    if main_menu==4:
        print("""
\t\t\t\t<<WELCOME TO SUB-MENU D>>\t\t\t\n
\t\t\t\t<<DISPLAY RESERVATIONS>>\t\t\t\n
\t\t\t\t<<-_-_-_-_-_-_-_-_-_-_->>\t\t\t\n
""")
    
    if main_menu==5:
        print("""
\t\t\t\t<<<<<WELCOME TO SUB-MENU E>>>>>\t\t\t\t
\t\t\t\t<<GENERATE RANDOM SUGGESTIONS>>\t\t\t\t
\t\t\t\t<<-_-+-_-+-_-+-_-+-_-+-_-+-_->>\t\t\t\t
""")
        
    if main_menu==6:
        print("<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>")
        print("Thank You For Using Our services")
        print("\t\tGoodbye-and-Have-a-Nice-Day\t\t")
        print("<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>")


def Read_file(choice):
    # Function takes choice [1] or [2] provided at the start of each sub-section
    # Reads guestlist.txt or menuitems.txt based on the choice provided

    Guest_info=[]
    Guest_info.clear
    
    Menu_info=[] 
    Menu_info.clear


    match choice:
        case 1:
         # Opens guestlist, read the file, format each line into an element in a list
         with open(GUEST_TXT,"r") as guestFile:
            guest_list = guestFile.read()
            for lines in guest_list.split('\n'): # Reads each reservation as a line
                Guest_info.append(lines.split('|')) # splits each info in reservation separated in a 
         return Guest_info
        case 2:
         #Opens Menulist, reads the file, format each line into an element in a list
         with open(MENU_TXT,"r") as MenuFile:
             Menu_item = MenuFile.read()
         for line in Menu_item.split('\n'):
             Menu_info.append(line)
         return Menu_info 

def add_list(Book_list, User_list, lists):
    current_list = Book_list + User_list # combines collected user info into a list before attaching it to current reservations
    lists.append(current_list)
   
def write_file(lists):
    lines ="" #hold all reservation as a string text
    for guest_info in lists: # goes through list in lists
        for info in guest_info: # goes through info in list
            lines += str(info) +"|" #appends info by info separated by "|"
        lines = lines[:-1] #adds the line to the furthest of lines
        lines += "\n" # adds a \n so that each reservation is separated by a \n
    with open(GUEST_TXT, "w") as writetofile:
        writetofile.writelines(lines)

#SUBMENU 1#      

def get_cust_info(list):     #to be located in section 1 of main()
     list.clear()
     while True:
      try:
       name=input("ENTER NAME:")
       phone = input("ENTER PHONE NUMBER:")
       email = input("ENTER E-MAIL: ")
       pax= input("ENTER PAX:")

      except type(name) != str as NameValueERROR:
         print("Please Enter alphabets only")
         print("EXclude Numerals")
         continue
      except len(name)>= 10 or len(name)<0:
          print("Please Enter a name within 0-20 letters only")
          continue
      except int(phone)!=int as PhoneValueERROR:
          print("Please enter a valid phone number")
          print("Exclude special characters such as '-' to prevent errors")
          continue
      except type(pax)!= int as PaxTypeError:
          print("Please enter a single digit number from 1 to 4")
          continue
      except int(pax)>=4 or int(pax)<=0 as PaxValueERROR:
          print("Please enter a value for Pax that is within 1 to 4")
          continue
      else:
          list.append(name)
          list.append(phone)
          list.append(email)
          list.append(pax)
          return list

# date_session_slot list format - list of lists containing - string= identifier, and list of strings
# =[
# ["SESSION",["slot_1","slot_2","slot_3","slot_4","slot_5","slot_6","slot_7","slot_8"]],
# ["SESSION",["slot_1","slot_2","slot_3","slot_4","slot_5","slot_6","slot_7","slot_8"]],
# ["SESSION",["slot_1","slot_2","slot_3","slot_4","slot_5","slot_6","slot_7","slot_8"]],
# ["SESSION",["slot_1","slot_2","slot_3","slot_4","slot_5","slot_6","slot_7","slot_8"]]
# ]
# = slots=["slot_1","slot_2","slot_3","slot_4","slot_5","slot_6","slot_7","slot_8"]

def getBookingInfo(lists):
    date_format = "%Y-%m-%d" # to hold date format
    date_session_slot = [
        ["12.00 pm - 02.00 pm", ["slot_1", "slot_2", "slot_3", "slot_4", "slot_5", "slot_6", "slot_7", "slot_8"]],
        ["02.00 pm - 04.00 pm", ["slot_1", "slot_2", "slot_3", "slot_4", "slot_5", "slot_6", "slot_7", "slot_8"]],
        ["06.00 pm - 08.00 pm", ["slot_1", "slot_2", "slot_3", "slot_4", "slot_5", "slot_6", "slot_7", "slot_8"]],
        ["08.00 pm - 10.00 pm", ["slot_1", "slot_2", "slot_3", "slot_4", "slot_5", "slot_6", "slot_7", "slot_8"]]
    ]  #for all available sessions and slots
    while True:
     try:
        BookedDate = input("Enter Date[yyyy-mm-dd]:")   # gets user input in date form
        booking_date= datetime.datetime.strptime(BookedDate, date_format) # formats the date
        DayDifference = booking_date - datetime.datetime.today() # calculates date difference

        if DayDifference.days < 5: # checks if date entered is 5 days ahead
            raise ValueError("Booking is available for 5 days in advance")
            continue

     except ValueError:
        print("please enter a date that is 5 days in advance")
        return None

     BookingDate = BookedDate #assigns booked date to place holder

     for list in lists:   # goes through reservation
        if list[0] == BookedDate: # checks if date in each reservation is similar to the date booked
            for j in date_session_slot: # if date booked is similar, then for date_session_slot's sessions
                if j[0] == list[1]: # if session in reservation is same to session in date_session_slot
                    if list[2] in date_session_slot[j][1]: # and slot in reservation is same to slot in date_session_slot
                        date_session_slot[j][1].remove(list[2]) # remove the slot's from date_session_slot
                        break

     print("These are the remaining slots:") # prints header to slots
     for i in date_session_slot:
        print(f"{i[0]}: {i[1]}") #formats and prints available sessions and slots

     if all(date_session_slot[1] == [] for i in date_session_slot): # Tells the user if a session is booked
        print("All sessions are fully booked.")
        print("Please select another date")
        return None
        continue

     try:
        print("""
[1] Session 12.00 pm - 02.00 pm
[2] Session 02.00 pm - 04.00 pm
[3] Session 06.00 pm - 08.00 pm
[4] Session 08.00 pm - 10.00 pm
Choose a session, Enter [Number]
""")    #promts user to choose a session by entering a number
        while True:
         choose_session = int(input("Enter Session [1-4]:"))

         if not 1 <= choose_session <= 4:  #checks for error in user input
             raise ValueError("Enter a valid session number (1-4)")

         chosen_session_info = date_session_slot[choose_session - 1] #chooses session for user
         if chosen_session_info[1] == []:  #
              print("The chosen session is fully booked. Please choose another session.")
              return None
              continue

         print("Choose one of the following slots:")
         print(chosen_session_info[1]) # prints the slot in the session chosen

         choose_slot = input("Enter slot as listed above:") # promts user for an 
         if choose_slot not in chosen_session_info[1]:
             raise ValueError("Enter a valid slot from the list")

         BookingSession = chosen_session_info[0]
         BookingSlot = choose_slot

         reservation_info = [BookedDate,BookingSession,BookingSlot]
         return reservation_info
         break
     except ValueError:
        print("Enter a valid input")
        continue



# goes through reservations lists one by one
# returns a list selected: passed on to delete function and edit function


def skim_reservation(lists):
    list_to_edit=[] # placeholder for a list to be selected
    for list in lists: # goes through reservation
        count=len(lists)
        counter=1
        os.system('cls')
        if count+1== counter:
            break

        else:
         
         print(format_string.format(date=list[0],session=list[1],slot=list[2],name=list[3],email=list[4],number=list[5],pax=list[6]))
         print("Do you want to edit this reservation?") # asks user if he wants to edit the current reservation
         choose=input("Enter [Y/N]:") # receives user input
         count+=1
         if choose.upper()=="Y":
            list_to_edit=list # attach list to list
            return list # returns the list
            break # end the loop

         else:
            continue # continues until desired reservation is found


#SUBMENU 2# - delete reservation
def delete_reservation(list,lists): # takes in a list to be deleted
    choice=input("Are you sure to delete this reservation?") # asks for user confirmation
    if choice.upper()=="Y":
       lists.remove(list) # removes the list from the reservations lists
       print("{list} is deleted from reservations") #tells the user that the reservation has been deleted

#SUBMENU 3# - replace info

def edit_reservation(list,lists):
   original_list=list
   edit_list=list
   print("""
[1] Edit User Info (Name|email|number|pax)
[2] Edit Booking Info (Date|Session|Slot)
""")
   while True:
    try:
       ask=int(input("what would you like to edit[1|2]?"))
    
    except ask!=1 or ask!=2:
       print("Enter Either 1 or 2 only")
       input("Press Enter to continue\n")
       continue
    
    if ask==1:
       while True:
         try:
          NewName=input("Enter New Name:")
          NewEmail=input("Enter New Email:")
          NewNumber=input("Enter New Number:")
          NewPax=int(input("Enter New Pax:"))
          break

         except type(NewName)!=str or type(NewEmail)!=str or NewNumber!=str or NewPax!=int:
           print("Enter valid inputs only")
           continue

       os.system('cls')
       print(format_string.format(name=NewName,email=NewEmail,number=NewNumber,pax=NewPax,date=list[0],session=list[1],slot=list[2]))
       change=input("Save Changes? [Y/N]:")

       if change.upper()=="Y":
           edit_list[3]=NewName
           edit_list[4]=NewEmail
           edit_list[5]=NewNumber
           edit_list[6]=NewPax
           lists.remove(original_list)
           lists.append(edit_list)
           print("list is edited succesfully")
           break

       else:
           print("No changes are made")
           break
       break

    if ask ==2:
        date_format = "%Y-%m-%d" # to hold date format
        date_session_slot = [
        ["12.00 pm - 02.00 pm", ["slot_1", "slot_2", "slot_3", "slot_4", "slot_5", "slot_6", "slot_7", "slot_8"]],
        ["02.00 pm - 04.00 pm", ["slot_1", "slot_2", "slot_3", "slot_4", "slot_5", "slot_6", "slot_7", "slot_8"]],
        ["06.00 pm - 08.00 pm", ["slot_1", "slot_2", "slot_3", "slot_4", "slot_5", "slot_6", "slot_7", "slot_8"]],
        ["08.00 pm - 10.00 pm", ["slot_1", "slot_2", "slot_3", "slot_4", "slot_5", "slot_6", "slot_7", "slot_8"]]]

        while True: 
         try: #gets new date #new session #new slot
            print("Date Format yyyy-mm-dd")
            NewDate=input("Enter a New Date Based on Format:")
             
         except datetime.datetime.strptime(NewDate,date_format)!= True as FormatError:
            print("Enter a date that is written within the format provided")
            continue
         
         for list in lists:
            if list[0]==NewDate:
               for j in date_session_slot:
                  if j[0]==list[1]:
                     if list[2] in date_session_slot[j][1]:
                        date_session_slot[j][1].remove(list[2])

         print(f"These are the remaining slots available for"+NewDate)
         for i in date_session_slot:
          print(f"{i[0]}: {i[1]}")

         if all(date_session_slot[1] == [] for i in date_session_slot): # Tells the user if a session is booked
          print("All sessions are fully booked.")
          print("Please select another date")
          return None
          continue
         
         print("""
[1] Session 12.00 pm - 02.00 pm
[2] Session 02.00 pm - 04.00 pm
[3] Session 06.00 pm - 08.00 pm
[4] Session 08.00 pm - 10.00 pm
Choose a session, Enter [Number]
""") 
         try:
            choose_session = int(input("Enter Session [1-4]:"))

            if not 1 <= choose_session <= 4:  #checks for error in user input
              raise ValueError("Enter a valid session number (1-4)")
         
            chosen_session_info = date_session_slot[choose_session - 1] #chooses session for user
            if chosen_session_info[1] == []:  #
              print("The chosen session is fully booked. Please choose another session.")
              return None
              continue
         
            print("Choose one of the following slots:")
            print(chosen_session_info[1]) # prints the slot in the session chosen

            choose_slot = input("Enter slot as listed above:") # promts user for an 
            if choose_slot not in chosen_session_info[1]:
              raise ValueError("Enter a valid slot from the list")

            NewSession = chosen_session_info[0]
            NewSlot = choose_slot

            os.system('cls')
            print(format_string.format(name=list[3],email=list[4],number=list[5],pax=list[6],date=NewDate,session=NewSession,slot=NewSlot))
            change=input("Save Changes? [Y/N]:")

            if change.upper()=="Y":
              edit_list[0]=NewDate
              edit_list[1]=NewSession
              edit_list[2]=NewSlot
              lists.remove(original_list)
              lists.append(edit_list)
              print("list is edited succesfully")
              break

            else:
              print("No changes are made")
              break

         except ValueError:
            print("Enter valid inputs only")
            continue
        break
        
      





#SUBEMENU 4# - display reservations

#fuction that formats the reservations data within the  guestlist.txt
#whole operation done by one function
# COMPLETED ##

def display_reservations(lists):
    os.system('cls') # clears the screen
    reservation_header() # print out the header
    reservation_body(lists) # print out the reservations in current_reservations

def reservation_header():
    # displays info label into screen
    HEADER="""
+----+----------+-------------------+-------+---------------+------------------+-----------+---+    
|{H1:.<4}|{H2:.<10}|{H3:.<19}|{H4:.<7}|{H5:.<15}|{H6:.<18}|{H7:.<11}|{H8:.<3}|
+----+----------+-------------------+-------+---------------+------------------+-----------+---+
""".format(H1="NO",H2="DATE",H3="SESSION",H4="SLOT",H5="NAME",H6="E-MAIL",H7="NUMBER",H8="pax") #formats these lables into the headings
    print(HEADER,end="") #prints out the header

def reservation_body(lists):
   count=1 # provide numbering to the reservations
   for list in lists:
       string="|{no:.<4}|{date:.<10}|{session:.<19}|{slot:.<6}|{name:.<15}|{email:.<15}|{number:.<10}|{pax:.<3}|" #as place holders for the reservation info 
       print(string.format(no=count,date=list[0],session=list[1],slot=list[2],name=list[3],email=list[4],number=list[5],pax=list[6])) # formats the reservation info into the string above
       count+=1 # adds as the reservation is finished and a new one enters
       if len(list)<=6:
        while len(list) <=6:
         list.append("")
        break

# done -- --

#--- submenu_5
def random_meal():
    while True:
        with open(MENU_TXT, "r") as meal: # opens the menu list and writes it into a list
            meal_items = meal.readlines()
            number = random.randint(0, len(meal_items) - 1) # select random element in the list
            print(f"hmmm....we suggest you try our {meal_items[number]}") # prints the randomly selected menu into format,
        
        choice = input("Uninterested in the dish suggested, Want to try again? [Y/N]: ").upper() # Lets user go as much until a desired menu item is given
        if choice != "Y":
            break# as to exit the loop




main_menu() # calls the main_menu adhering all the functions 