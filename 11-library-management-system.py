# Library Management System

# Task Description

# Create a simple library management system using Python. The system should allow users to perform basic operations such as adding, removing, and searching for books.

# Requirements

# 1. Use Python 3.x
# 2. Use a dictionary to store book data (title, author, publication year, status)
# 3. Implement the following features:

# Features

# 1. Add Book
#     - Prompt user for book title, author, and publication year
#     - Add book to library dictionary with status "available"

# 2. Remove Book
#     - Prompt user for book title
#     - Remove book from library dictionary if found

# 3. Search Book
#     - Prompt user for book title or author
#     - Display book details if found

# 4. Borrow Book
#     - Prompt user for book title
#     - Update book status to "borrowed" if available

# 5. Return Book
#     - Prompt user for book title
#     - Update book status to "available" if borrowed

# 6. Display All Books
#     - Display list of all books in library

library = {
    "Book1": {
        "author": "Author One",
        "publication_year": 2001,
        "status": "available"
    },
    "Book2": {
        "author": "Author Two",
        "publication_year": 2002,
        "status": "available"
    },
    "Book3": {
        "author": "Author Three",
        "publication_year": 2003,
        "status": "available"
    }
}

def add_book():
    book = input("Enter the name of book: ")
    if book not in library:
        author = input("Enter the name of author: ")
        publication_year = input("Enter the publication year: ")
        library[book] = {
            "author": author,
            "publication year": publication_year,
            "status": "available"
        }
    elif book in library:
        print(f"The book {book} is already in the library.")

def remove_book():
    book = input("Enter the name of book you want to remove: ")
    if book in library:
        library.__delitem__(book)
    if book not in library:
        print("The book doesn't exist in the library.")

def search_book():
    book = input("Enter the name of book you want to search for: ")
    if book in library:
        if library[book]["status"] == "available":
            print(f"{book} is available in the library.")    
        if library[book]["status"] == "borrowed":
            print(f"{book} is borrowed by someone.")
    else:
        print(f"Sorry, the book named {book} is unavailable")    

def borrow_book():
    book = input("Enter the name of book you want to borrow: ")
    if book in library:
        if library[book]["status"] == "available":
            print("You can borrow the book.")  
            library[book]["status"] = "borrowed" 
        if library[book]["status"] == "borrowed":
            print("The book is already borrowed.")
    elif book not in library:
        print(f"The book {book} is not in the library.")

def return_book():
    book = input("Enter the name of book you want to return: ")
    if book in library:
        if library[book]["status"] == "borrowed":
            print("You can return the book.")  
            library[book]["status"] = "available"
        if library[book]["status"] == "available":
            print("The book is available.")
    if book not in library:
        print("The book was never placed in the library.")

def show_library():
    print("\nThese are the books available in the library.")
    for book in library:
        if library[book]["status"] == "available":
            print("  -",book)

    print("\nThese are the books borrowed from the library.")
    for book in library:  
        if library[book]["status"] != "available":
            print("  -",book)

def show_details_of_book():
    book = input("Enter the name of book: ")
    if book in library:   
        details = f"""
        Details of '{book}': 
            Author: {library[book]["author"]}  
            Publication Year: {library[book]["publication_year"]}
        """
        print(details)
    
def main():
    print(
        "\n1. To add a book.\n"
        "2. To remove a book.\n"
        "3. To search a book.\n"
        "4. To borrow a book.\n"
        "5. To return a book.\n"
        "6. To display the library.\n"
    )
    choice = input("Enter your choice for action: ")
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        choice = input("Invalid input. Enter your choice for action: ")
    if int(choice) == 1:
        add_book()
    if int(choice) == 2:
        remove_book()
    if int(choice) == 3:
        search_book()
    if int(choice) == 4:
        borrow_book()
    if int(choice) == 5:
        return_book()
    if int(choice) == 6:
        show_library()
i = 0
while i >= 0:
        main()







