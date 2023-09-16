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
    new_book = Book(title, author, pubYear)
    Books_List.append(new_book)
    print(f"Book {title} added!")

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
                book.title = new_title if new_title else book.title
                book.author = new_author if new_author else book.author
                book.pubYear = new_pubYear if new_pubYear else book.pubYear
                print(f"Book {title} updated!")
                return
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
    # Passing the books list as parameter to functions
    Books_List = []

    choice = int(0)

    # While not the exit choice, continue to prompt user to input choice
    while choice != 6:
        # If choice is out of range
        while choice > 6 or choice < 1:
            menu()
            # Convert choice to int for comparison
            choice = int(input("Enter choice: "))

        # If choice is in menu range, display corresponding menu item
        if choice == 1:
            listAllBooks(Books_List)
        elif choice == 2:
            addBook(Books_List)
        elif choice == 3:
            updateBook(Books_List)
        elif choice == 4:
            removeBook(Books_List)
        elif choice == 5:
            searchBook(Books_List)

        # Choice is not exit, reset choice
        if choice != 6:
            choice = 0

# Call main method
if __name__ == "__main__":
    main()