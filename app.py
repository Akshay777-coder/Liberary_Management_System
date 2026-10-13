import liberary
import sys

liberary.create_table_books()
liberary.create_table_members()

def books():
    flag = True
    while(flag):
        print("\n *** Welcome to the Book Section *** \n")
        print("1. Insert books\n2. Display Books\n3. Update Books\n4. Delete Books\n5. Back to Main Menu\n6. Exit\n")
        choice = int(input("Enter your Choice: "))
        match choice:
            case 1:
                print("\n --- Insert Books --- \n")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                temp = input("Enter if issued(yes or no): ")
                if temp=='yes':
                    is_issued = 1
                else:
                    is_issued = 0
                price = float(input("Enter Price: "))
                liberary.insert_into_books(title, author, is_issued, price)
            case 2:
                liberary.display_books()
            case 3:
                print("\n --- Update Books --- \n")
                book_id = int(input("Enter book id: "))
                title = input("Enter New title: ")
                author = input("Enter New author: ")
                temp = input("Enter if issued(yes or no): ")
                if temp=='yes':
                    is_issued = 1
                else:
                    is_issued = 0
                price = float(input("Enter New Price: "))
                liberary.update_books(book_id, title, author, is_issued, price)
            case 4:
                print("\n --- Delete Books --- \n")
                book_id = int(input("Enter book id: "))
                print(f"Are you sure you want to delete the book with ID {book_id}? (yes/no): ", end="")
                confirmation = input().strip().lower()
                if confirmation == "yes":
                    liberary.delete_book(book_id)
                else:
                    print("Deletion cancelled.")
            case 5:
                print("\nReturning to Main Menu...")
                flag = False
            case 6:
                print("Exiting the program.")
                sys.exit(0)
            case _:
                print("Wrong Choice!")

def members():
    flag = True
    while(flag):
        print("\n *** Welcome to the Member Section *** \n")
        print("1. Insert Member\n2. Display Member\n3. Update Member\n4. Delete Member\n5. Back to Main Menu\n6. Exit\n")
        choice = int(input("Enter your Choice: "))
        match choice:
            case 1:
                print("\n --- Insert Members --- \n")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                number = input("Enter Number: ")
                liberary.insert_into_members(name, email, number)
            case 2:
                liberary.display_members()
            case 3:
                print("\n --- Update Members --- \n")
                member_id = int(input("Enter member id: "))
                name = input("Enter New name: ")
                email = input("Enter New email: ")
                number = input("Enter new number: ")
                liberary.update_members(member_id, name, email, number)
            case 4:
                print("\n --- Delete members --- \n")
                member_id = int(input("Enter member id: "))
                print(f"Are you sure you want to delete a member with ID {member_id}? (yes/no): ", end="")
                confirmation = input().strip().lower()
                if confirmation == "yes":
                    liberary.delete_members(member_id)
                else:
                    print("Deletion cancelled.")
            case 5:
                print("\nReturning to Main Menu...")
                flag = False
            case 6:
                print("Exiting the program.")
                sys.exit(0)
            case _:
                print("Wrong Choice!")

def main():
    flag = True
    while(flag):
        print("\n *** Welcome to the Library Management System *** \n")
        print("1. Books\n2. Members\n3. Exit\n")
        choice = int(input("Enter your Choice: "))
        match choice:
            case 1:
                books()
            case 2:
                members()
            case 3:
                print("\nExiting the program...")
                flag = False
            case _:
                print("Wrong Choice!")

main()