class Book:
  def __init__(self, title, author):
      self.title = title
      self.author = author
      self.is_borrowed = False
  def borrow(self):
      self.is_borrowed = True
      print(f"Success: You have borrowed '{self.title}' by {self.author}.")
  def return_book(self):
      self.is_borrowed = False
      print(f"Success: You have returned '{self.title}'. Thank you!")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("The Hobbit", "J.R.R. Tolkien")
book1.borrow()
book2.borrow()
book3.borrow()
print("-" * 20) 
book1.return_book()
book2.return_book()
book3.return_book()
