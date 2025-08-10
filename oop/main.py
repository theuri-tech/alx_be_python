from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)  #Creating an instance of Book
    print(my_book) #Demonstrating the __str__ method.  #Expected to use __str__
    print(repr(my_book)) #Demonstrating the __repr__ method and expected to use __repr__
    del my_book #Deleting a book instance trigger __del__

if __name__ == "__main__":
    main()
    