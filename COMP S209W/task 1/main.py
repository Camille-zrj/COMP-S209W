from book import Book
from user import User
from library import Library

def print_menu():
    print()
    print("Library Management System")
    print()
    print("1. Add New Book")
    print("2. Register New User")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Show All Books")
    print("7. Check User Borrowed Books")
    print("0. Exit System")
    print()

def main():
    library = Library("Library Management System")
    while True:
        print_menu()
        choice = input("Please enter operation number: ")

        if choice == "1":
            isbn = input("Enter book ISBN: ")
            title = input("Enter book title: ")
            author = input("Enter author: ")
            book = Book(title, author, isbn)
            if library.add_book(book):
                print("Book added successfully!")
            else:
                print("ISBN already exists!")

        elif choice == "2":
            uid = input("Enter user ID: ")
            name = input("Enter user name: ")
            user = User(uid, name)
            if library.add_user(user):
                print("User registered successfully!")
            else:
                print("User ID already exists!")

        elif choice == "3":
            isbn = input("Enter ISBN to search: ")
            book = library.search_book(isbn)
            print(book.show_info() if book else "Book not found!")

        elif choice == "4":
            uid = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            success, msg = library.borrow_book(uid, isbn)
            print(msg)

        elif choice == "5":
            uid = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            success, msg = library.return_book(uid, isbn)
            print(msg)

        elif choice == "6":
            books = library.show_all_books()
            if not books:
                print("No books in library!")
            else:
                for b in books:
                    print(b.show_info())

        elif choice == "7":
            uid = input("Enter user ID: ")
            user = library.find_user(uid)
            print(user.show_borrowed_books() if user else "User not found!")

        elif choice == "0":
            print("Thank you for using Library Management System. Goodbye!")
            break

        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main()
