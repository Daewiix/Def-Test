class Book:
    def __init__(self, title, author, genre, price, number):
        self.idnumber = number
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def GetData(self):
        print("============")
        print("Title: %s" % self.title)
        print("Author: %s" % self.author)
        print("Genre: %s" % self.genre)
        print("Price: %s" % self.price)

    def __str__(self):  # this should return a string, not print like it does currently!
        return GetData(self)


info = "1000,Science: A Visual Encyclopedia,Chris Woodford,Science,23.99,1001"
args = info.split(',')[1:]
book = Book(*args)
book.GetData()