class Book:
    # Initialize book
    def __init__(self, title, author, pubYear):
        self.title = title
        self.author = author
        self.pubYear = pubYear

    # Return book
    def __str__(self):
        return f"{self.title} by {self.author} (Published in {self.pubYear})"
    
def addBook(Books_List):
    title = input("Enter the book title: ")
    # Checks if book already exists
    for book in Books_List:
        # Convert title to lower, to easy searching of book title
        if (book.title.lower() == title.lower()):
            print(f"Book {title} already exists")
            return

    author = input("Enter the author's name: ")
    pubYear = input("Enter the publication year: ")
    # If pubYear is less than 0 (invalid), require to input again
    if (int(pubYear) < 0):
        pubYear = input("Enter the publication year: ")

    new_book = Book(title, author, pubYear)
    Books_List.append(new_book)
    print(f"Book {title} added!\n")

def removeBook(Books_List):
    # If books list is empty
    if (len(Books_List) == 0):
        print("No Books yet\n")
    else:
        title = input("Enter the title of the book to remove: ")
        book_found = False
        for index, book in enumerate(Books_List):
            # Convert title to lower, to easy searching of book title
            if book.title.lower() == title.lower():
                # Delete found book from list
                del Books_List[index]
                print(f"Book {title} removed!")
                book_found = True
                return
        if not book_found:
            print("Book not found!\n")

def listAllBooks(Books_List):
    # If books list is empty
    if (len(Books_List) == 0):
        print("No Books yet\n")
    else:
        print("\n\t\tALL BOOKS")
        for book in Books_List:
            print(book.title)
    #Time.sleep removed. Used to wait 2 seconds before displaying next statement

def searchBook(Books_List):
    # If books list is empty
    if (len(Books_List) == 0):
        print("No Books yet\n")
    else:
        title = input("Enter the title of the book to search: ")
        for book in Books_List:
            # Convert title to lower, to easy searching of book title
            if book.title.lower() == title.lower():
                print(book)
                return
    print("Book not found!\n")

def updateBook(Books_List):
    # If books list is empty
    if (len(Books_List) == 0):
        print("No Books yet\n")
    else:
        title = input("Enter the title of the book to update: ")
        for book in Books_List:
            # Convert title to lower, to easy searching of book title
            if book.title.lower() == title.lower():
                new_title = input("Enter the new title: ")
                new_author = input("Enter the new author's name: ")
                new_pubYear = input("Enter the new publication year: ")
                # If new_pubYear is less than 0 (invalid), require to input again
                if (int(new_pubYear) < 0):
                    new_pubYear = input("Enter the publication year: ")
                book.title = new_title if new_title else book.title
                book.author = new_author if new_author else book.author
                book.pubYear = new_pubYear if new_pubYear else book.pubYear
                print(f"Book {title} updated!\n")
                return
        #   Book has not been found
        print("Book not found!\n")

# Placeholder for the main execution loop, if needed
# while True:
#     # TODO: Add a menu for the user to interact with
def menu():
    print("1. List all books")
    print("2. Add new Book")
    print("3. Update book")
    print("4. Delete book")
    print("5. Search book")
    print("5. Exit")

def main():
    # A list to store books
    # Local variable to make accessible only to main function
    Books_List = []

    choice = int(0)

    # While not the exit choice, continue to prompt user to input choice
    while choice != 6:
        # If choice is out of range
        while choice > 6 or choice < 1:
            #Call menu function
            menu()
            # Convert choice to int for comparison
            choice = int(input("Enter choice: "))

        # If choice is in menu range, display corresponding menu item
        if choice == 1:
            # Call listAllBooks with parameter the Books_List
            listAllBooks(Books_List)
        elif choice == 2:
            # Call addBook with parameter the Books_List
            addBook(Books_List)
        elif choice == 3:
            # Call updateBook with parameter the Books_List
            updateBook(Books_List)
        elif choice == 4:
            # Call removeBook with parameter the Books_List
            removeBook(Books_List)
        elif choice == 5:
            # Call searchBook with parameter the Books_List
            searchBook(Books_List)

        # Choice is not exit, reset choice
        if choice != 6:
            choice = 0

# Call main method
if __name__ == "__main__":
    main()