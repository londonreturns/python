# library management system

def addBook(bookList):
    bookName = input("Enter book name: ")
    authorName = input("Enter author name: ")
    year = input("Enter year: ")
    bookList.append({"title": bookName, "author": authorName, "year": year})
    print("Book added \n")
    return bookList
def removeBook(bookList):
    bookDeleted = False
    bookName = input("Enter book name: ")
    for i in range(0, len(bookList)):
        if bookName in books[i]["title"]:
            del bookList[i]
            bookDeleted = True
    if bookDeleted:
        print("Book Deleted \n")
    else:
        print("Book not found \n")
    return bookList
def searchBookByBookName(bookList):
    isBookFound = False
    bookName = input("Enter book name: ")
    for i in range(0, len(bookList)):
        if bookName in books[i]["title"]:
            isBookFound = True
            break
    if isBookFound:
        print("Book found\n", books[i])
    else:
        print("Book not found")
def searchBookByAuthor(bookList):
    isBookFound = False
    allBooksFound = []
    bookName = input("Enter author name: ")
    for i in range(0, len(bookList)):
        if bookName in books[i]["author"]:
            isBookFound = True
            allBooksFound.append(bookList[i])
    if isBookFound:
        for singleBook in allBooksFound:
            print("Book found", singleBook)
    else:
        print("Book not found")
def listAllBooks(bookList):
    for book in bookList:
        print(book["title"], "by",  book["author"])
    print("\n")

books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
]

while True:
    choice = input(""" What do  you want to do?
    1. Add a book
    2. Remove a book
    3. Search a book by name
    4. Search a book by author
    5. List all books
    Press q to quit\n""")
    if choice == "q":
        break
    elif choice == "1":
        books = addBook(books)
    elif choice == "2":
        books = removeBook(books)
    elif choice == "3":
        searchBookByBookName(books)
    elif choice == "4":
        searchBookByAuthor(books)
    elif choice == "5":
        listAllBooks(books)
    else:
        print("Please enter 1, 2, 3, 4, 5 or q")