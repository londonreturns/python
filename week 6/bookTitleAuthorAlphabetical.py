"""this code takes in a list of tuples representing
book titles and their corresponding authors and returns
a new list of tuples sorted by author name in alphabetical order."""

def sortingAlgorithm(bookList):
    length = len(bookList)
    for i in range(length):
        for j in range(i + 1, length):
            if bookList[j][1] < bookList[i][1]:
                bookList[i], bookList[j] = bookList[j], bookList[i]
    return bookList

books = [
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("The Lord of the Rings", "J.R.R. Tolkien"),
    ("The Da Vinci Code", "Dan Brown")
]

print(sortingAlgorithm(books))