class Book:
    # Initialize book
    def __init__(self, title, author, pubYear):
        self.title = title
        self.author = author
        self.pubYear = pubYear

    # Return book
    def __str__(self):
        return f"{self.title} by {self.author} (Published in {self.pubYear})"
    
def addBook(booksList):
    title = input("Enter the book title: ")
    bookExist = False
    # Checks if book already exists
    # While not end of list and book does not exist
    for book in booksList and not bookExist:
        # Convert title to lower, to easy searching of book title
        if (book.title.lower() == title.lower()):
            print(f"Book {title} already exists")
            bookExist = True

    if not bookExist:
        author = input("Enter the author's name: ")
        pubYear = input("Enter the publication year: ")
        # If pubYear is less than 0 (invalid), require to input again
        while (int(pubYear) < 0):
            pubYear = input("Enter the publication year: ")

        newBook = Book(title, author, pubYear)
        booksList.append(newBook)
        print(f"Book \"{title}\" added!\n")

def removeBook(booksList):
    # If books list is empty
    if (len(booksList) == 0):
        print("No Books yet\n")
    else:
        title = input("Enter the title of the book to remove: ")
        bookFound = False
        # While not end of list and book is not found
        for index, book in enumerate(booksList) and not bookFound:
            # Convert title to lower, to easy searching of book title
            if book.title.lower() == title.lower():
                # Delete found book from list
                del booksList[index]
                print(f"Book {title} removed!")
                bookFound = True
        if not bookFound:
            print("Book not found!\n")

def listAllBooks(booksList):
    # If books list is empty
    if (len(booksList) == 0):
        print("No Books yet\n")
    else:
        print("\n\t\tALL BOOKS")
        for index, book in enumerate(booksList):
            print(f"{index + 1}. {book.title}")
            # Print new line to seperate from menu
        print("\n")
    #Time.sleep removed. Used to wait 2 seconds before displaying next statement

def searchBook(booksList):
    # If books list is empty
    if (len(booksList) == 0):
        print("No Books yet\n")
    else:
        bookFound = False
        title = input("Enter the title of the book to search: ")
        # While not end of list and book is not found
        for book in booksList and not bookFound:
            # Convert title to lower, to easy searching of book title
            if book.title.lower() == title.lower():
                print(book)
                bookFound = True
        if not bookFound:
            print("Book not found!\n")

def updateBook(booksList):
    # If books list is empty
    if (len(booksList) == 0):
        print("No Books yet\n")
    else:
        title = input("Enter the title of the book to update: ")
        bookFound = False
        # While not end of list and book is not found
        for book in booksList and not bookFound:
            # Convert title to lower, to easy searching of book title
            if book.title.lower() == title.lower():
                newTitle = input("Enter the new title: ")
                newAuthor = input("Enter the new author's name: ")
                newPubYear = input("Enter the new publication year: ")
                # If newPubYear is less than 0 (invalid), require to input again
                if (int(newPubYear) < 0):
                    newPubYear = input("Enter the publication year: ")
                book.title = newTitle if newTitle else book.title
                book.author = newAuthor if newAuthor else book.author
                book.pubYear = newPubYear if newPubYear else book.pubYear
                print(f"Book {title} updated!\n")
                bookFound = True
        #   Book has not been found
        if not bookFound:
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
    booksList = []

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
            # Call listAllBooks with parameter the booksList
            listAllBooks(booksList)
        elif choice == 2:
            # Call addBook with parameter the booksList
            addBook(booksList)
        elif choice == 3:
            # Call updateBook with parameter the booksList
            updateBook(booksList)
        elif choice == 4:
            # Call removeBook with parameter the booksList
            removeBook(booksList)
        elif choice == 5:
            # Call searchBook with parameter the booksList
            searchBook(booksList)

        # Choice is not exit, reset choice
        if choice != 6:
            choice = 0

# Call main method
if __name__ == "__main__":
    main()