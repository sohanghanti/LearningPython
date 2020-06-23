class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')


b = Book('MY TITLE', 'Sohan S. Ghanti', 500)
print(b)
print(str(b))


# here, __str__ method is the string representation of the class Book
# due to this, whenever print or str functions are called, they check if the string representation of a class is present
# as Book Class has __str__ method, we can print the object b of class Book(), else it will print the memory location of
# object and not the actual string values
# ----------------------------------------------------------------------------------------------------------------------

print(len(b))

# here, len function would ask object b, if it has length representation of a class Book()
# as we have __len__ method, it ( i.e. len(b)) allows us to show the length representation of Book() class
# else, it would have given the error: TypeError: object of type 'Book' has no len()
# -----------------------------------------------------------------------------------------------------------------------

del b
# print(b.pages)
# here, an object b is deleted, and hence no further operations/attributes can be used with object b of class Book()
# for this __del__ this method id implemented
# it allows 'del' function to check if an object can be deleted
# else it will show name error
