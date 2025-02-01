class Libary:
    def __init__(self):
        self.noBooks = 0
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
    
    def showInfo(self):
        print(f"The Libary has {self.noBooks} books. The Books are")
        for book in self.books:
            print(book)
        
l1 = Libary()
l1.addBook("Harry Potter")
l1.addBook("Harry Potter 2")
l1.addBook("Harry Potter 3")
l1.showInfo()


        
        
         
        