import sys
def innitial_phonebook():
    rows, cols= int(input("Please enter initial number of contacts: ")), 5
    phone_book = []
    for i in range(rows):
        print("\nEnter contact %ddetails in the following order (ONLY):" % (i+1))
        print("NOTE: * indicates mandatory field")
        print(("................................................................."))
        temp=[]
        for j in range(cols):
            if j==0:
                temp.append(input("Enter Name*: "))
                if temp[j]=='' or temp[j]== ' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            if j == 1:
                temp.append(int(input("Enter Number*: ")))
            if j == 2:
                temp.append(input("Enter e-mail address: "))
                if temp[j] =='' or temp[j]== ' ':
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter date of birth (DD/MM/YYYY): ")))
                if temp[j] =='' or temp[j]== ' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter category (Family/Friends/Work/Others): ")))
                if temp[j] =='' or temp[j]== ' ':
                    temp[j] = None
        phone_book.append(temp)
    print(phone_book)
    return phone_book
def menu():
    print(("*"* 20))
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print(("*"* 20))
    print("\tYou can perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("Please enter your choice: "))
    return choice
def add_contact(pb):
    dip=[]
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter Name*: ")))
        if i == 1:
            dip.append(int(input("Enter Number*: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth (DD/MM/YYYY): ")))
        if i == 4:
            dip.append(str(input("Enter category (Family/Friends/Work/Others): ")))
    pb.append(dip)
    return pb
def remove_existing(pb):
    query= str(input("Please enter the name of the contact to be removed: "))
    temp = 0
    for i in range(len(pb)):
        if pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("This query has now been removed")
            return pb
    if temp == 0:
        print("Sorry, you have entered an invalid query.\nPlease recheck and try again.")
    return pb
            