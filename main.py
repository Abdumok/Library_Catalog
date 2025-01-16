import os
import time

library_catalog = {}

# Create welcome function
def welcome():
    input("Welcome to our library, to show the list of our service press enter...")
    print("Getting the list, Please wait...")
    time.sleep(2)
    print("Please select a number from the list below: ")
    print("1- Add a book")
    print("2- Check out")
    print("3- Check in")
    print("4- List of the books")
    print("5- Exit")

# Create function to clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Create add function
def add():
    while True:
        print("------------------------------------------------------------")
        isba = input("Please enter the ISBA for the book you want to add: ")
        if not isba.isdigit():
            print("\nInvalid input, That is not a number Please enter number between (1 - 5)")
        elif  (1 > int(isba)) or (int(isba) > 5):
            print("\nInvalid input, Please enter number between (1 - 5)")
        elif isba in library_catalog:
            print("\nSorry this ISBA is already used for another book, enter another ISBA")
        else:
            break
    title = input("Enter the book's title name: ")
    author = input("Enter th book's author name: ")
    library_catalog[isba] = {"title": title, "author": author, "available": True }
    if input("Do you want to add another book? (Y/N) ").lower() == "y":
        add()


# Create check out function
def check_out():
    pass

# Create check in function
def check_in():
    pass

# Create function to display the books in the library catalog
def list_books():
    pass

# Create exit function
def exit_pro():
    pass
