# library_system.tstl

# Include the necessary modules
include "code.py"

# Declare variables for the library, books, and patrons
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", copies=3)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", copies=2)
patron1 = Patron("Alice", 1)
patron2 = Patron("Bob", 2)

# Add books and patrons to the library
library.add_book(book1)
library.add_book(book2)
library.add_patron(patron1)
library.add_patron(patron2)

# Test check_out and check_in functions
library.check_out("The Great Gatsby", 1)
library.check_out("To Kill a Mockingbird", 2)
library.check_in("The Great Gatsby")
library.check_in("To Kill a Mockingbird")

# Test display_available_books function
library.display_available_books()

# Test search_books function
library.search_books("Great")

# Test checkout_book and checkin_book functions with due dates
library.checkout_book("The Great Gatsby", 1, datetime.now() + timedelta(days=14))
library.checkout_book("The Great Gatsby", 2, datetime.now() + timedelta(days=7))
library.checkout_book("To Kill a Mockingbird", 1, datetime.now() + timedelta(days=14))
library.checkin_book("The Great Gatsby", 1)
library.checkin_book("To Kill a Mockingbird", 2)

# Test reserve_book function
library.reserve_book("The Great Gatsby", 1)
library.reserve_book("The Great Gatsby", 2)
library.reserve_book("Nonexistent Book", 1)

# Test overdue_books function
library.overdue_books()

# Test get_popular_books function
library.get_popular_books()
