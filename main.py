import os
import time

library_catalog = {}

# Create welcome function
def library_service():
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
            print("\nInvalid input, That is not a number, Enter a valid number")
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
    check_out_isba = input("Enter the ISBA for the book you want to check out: ")
    if check_out_isba in library_catalog:
        if library_catalog[check_out_isba]["available"]:
            library_catalog[check_out_isba]["available"] = False
            print(f"Book ({library_catalog[check_out_isba]["title"]}) By ({library_catalog[check_out_isba]["author"]})"
                  f" checked out successfully.")
        else:
            print(f"Sorry this book you ordered is already checked out")
    else:
        print("Sorry we don't have this book in our library catalog.")
    if input("Do you want to check out another book. (Y/N) ").lower() == "y":
        check_out()
    else:
        pass

# Create check in function
def check_in():
    pass

# Create function to display the books in the library catalog
def list_books():
    print("\n------------------------------------------------------")
    for isba in library_catalog:
        print(f"Book: {library_catalog[isba]["title"]}, By: {library_catalog[isba]["author"]},"
              f" ISBA: {isba}, Available: {library_catalog[isba]["available"]} ")
        print("------------------------------------------------------")

# Create exit function
def exit_pro():
    print("Exiting...")
    time.sleep(2)

input("Welcome to our library, to show the list of our service press enter...")
print("Getting the list, Please wait...")
time.sleep(2)
while True:
    library_service()
    clear()
    choice = input("Select a number from the list: ")
    if choice == "1":
        add()
    elif choice == "2":
        check_out()
    elif choice == "3":
        check_in()
    elif choice == "4":
        list_books()
    elif choice == "5":
        exit_pro()
        break
    else:
        print("Invalid input, Enter a number between (1 - 5)")