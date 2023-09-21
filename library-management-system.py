import datetime

class Book:
    # Initialize book
    def __init__(self, title, author, pubYear, borrowed, borrowedBy):
        self.title = title
        self.author = author
        self.pubYear = pubYear
        self.borrowed = borrowed
        self.borrowedBy = borrowedBy

    # Return book
    def __str__(self):
        return f"{self.title} by {self.author} (Published in {self.pubYear})"

# Return index of book
# If not found return -1
def checkBookIndex(bookTitle, booksList):
    bookIndex = -1
    # Checks if book already exists
    # While not end of list and book does not exist
    # for index, book in enumerate(booksList) and bookIndex != -1:
    for index, book in enumerate(booksList):
        # Convert title to lower, to easy searching of book title
        if (book.title.lower() == bookTitle.lower()):
            bookIndex = index

    return bookIndex

def borrowBook(booksList):
    title = input("Enter the book title: ")
    bookIndex = checkBookIndex(title, booksList)

    if (booksList[bookIndex].borrowed == True):
        print("Book is already borrowed by someone else")
    else:
        if bookIndex != -1:
            name = input("Enter your name: ")
            # Set book as borrowed
            booksList[bookIndex].borrowed = True
            # Set name of person who borrowed book
            booksList[bookIndex].borrowedBy = name
            # Display message
            print(f"{name} has borrowed {booksList[bookIndex]}\n")
        else: 
            print("Book does not exist\n")

# Function to return borrowed book
def returnBook(booksList):
    title = input("Enter the book title: ")
    bookIndex = checkBookIndex(title, booksList)

    if bookIndex != -1:
        # If book is borrowed
        if booksList[bookIndex].borrowed == True:
            name = input("Enter your name: ")
            # If name matches person who borrowed, allow return
            if (booksList[bookIndex].borrowedBy.lower() == name.lower()):
                booksList[bookIndex].borrowed = False
                booksList[bookIndex].borrowedBy = ""
                print(f"{name} has returned {booksList[bookIndex]}\n")
            else:
                print("Borrower's name is not the same\n")
        else:
            print("Book has not been borrowed\n")
    else: 
        print("Book does not exist\n")

def addBook(booksList):
    title = input("Enter the book title: ")
    bookIndex = checkBookIndex(title, booksList)

    # Book does not exist
    if bookIndex == -1:
        author = input("Enter the author's name: ")
        # Adding try except to handle the user input on int and prevent the program from craching
        try:
            pubYear = int(input("Enter the publication year: "))
            # If pubYear is less than 0 (invalid), require to input again
            while (int(pubYear) < 0):
                pubYear = int(input("Enter the publication year: "))

            # Create a new book with title, author, pubYear, not borrowed, max datetime, and no borrower Name
            newBook = Book(title, author, pubYear, False, "")
            booksList.append(newBook)
            print(f"Book \"{title}\" added!\n")
        except:
            print("Year input was not in a correct format.\n")
    else:
        print(f"Book {title} already exists\n")

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
        title = input("Enter the title of the book to search: ")
        bookIndex = checkBookIndex(title, booksList)

        if bookIndex != -1:
            print(booksList[bookIndex])
        else:
            print("Book does not exist")

def updateBook(booksList):
    # If books list is empty
    if (len(booksList) == 0):
        print("No Books yet\n")
    else:
        title = input("Enter the title of the book to update: ")
        bookIndex = checkBookIndex(title, booksList)

        if bookIndex != -1:
            newTitle = input("Enter the new title: ")
            newAuthor = input("Enter the new author's name: ")
            newPubYear = input("Enter the new publication year: ")
            # If newPubYear is less than 0 (invalid), require to input again
            if (int(newPubYear) < 0):
                newPubYear = input("Enter the publication year: ")
            booksList[bookIndex].title = newTitle if newTitle else booksList[bookIndex].title
            booksList[bookIndex].author = newAuthor if newAuthor else booksList[bookIndex].author
            booksList[bookIndex].pubYear = newPubYear if newPubYear else booksList[bookIndex].pubYear
            print(f"Book {title} updated!\n")
                
        #   Book has not been found
        else:
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
    print("6. Borrow book")
    print("7. Return book")
    print("8. Exit")

def main():
    # A list to store books
    # Local variable to make accessible only to main function
    booksList = []

    choice = int(0)

    # While not the exit choice, continue to prompt user to input choice
    while choice != 8:
        # If choice is out of range
        while choice > 8 or choice < 1:
            #Call menu function
            menu()
            # Convert choice to int for comparison
            choice = int(input("Enter choice: "))

        # If choice is in menu range, display corresponding menu item
        match choice:
            case 1:
                # Call listAllBooks with parameter the booksList
                listAllBooks(booksList)
            case 2:
                # Call addBook with parameter the booksList
                addBook(booksList)
            case 3:
                # Call updateBook with parameter the booksList
                updateBook(booksList)
            case 4:
                # Call removeBook with parameter the booksList
                removeBook(booksList)
            case 5:
                # Call searchBook with parameter the booksList
                searchBook(booksList)
            case 6:
                # Call borrowBook with parameter the booksList
                borrowBook(booksList)
            case 7:
                # Call returnBook with parameter the booksList
                returnBook(booksList)

        # Choice is not exit, reset choice
        if choice != 8:
            choice = 0

# Call main method
if __name__ == "__main__":
    main()