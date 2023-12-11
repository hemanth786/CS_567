import unittest
from code import Book, Patron, Library
from datetime import datetime, timedelta

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()

        self.book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", copies=3)
        self.book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", copies=2)

        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

        self.patron1 = Patron("Alice", 1)
        self.patron2 = Patron("Bob", 2)

        self.library.add_patron(self.patron1)
        self.library.add_patron(self.patron2)

    def test_checkout_book(self):
        due_date1 = datetime.now() + timedelta(days=14)
        due_date2 = datetime.now() + timedelta(days=7)

        self.assertEqual(self.library.checkout_book("The Great Gatsby", 1, due_date1),
                         "The Great Gatsby checked out successfully by Patron 1.")
        self.assertEqual(self.library.checkout_book("The Great Gatsby", 2, due_date2),
                         "The Great Gatsby checked out successfully by Patron 2.")
        self.assertEqual(self.library.checkout_book("To Kill a Mockingbird", 1, due_date1),
                         "To Kill a Mockingbird checked out successfully by Patron 1.")
        self.assertEqual(self.library.checkout_book("Nonexistent Book", 1, due_date1),
                         "Error: Nonexistent Book does not exist in the library.")

    def test_checkin_book(self):
        due_date1 = datetime.now() + timedelta(days=14)
        self.library.checkout_book("The Great Gatsby", 1, due_date1)
        self.library.checkout_book("To Kill a Mockingbird", 2, due_date1)

        self.assertEqual(self.library.checkin_book("The Great Gatsby", 1),
                         "The Great Gatsby checked in successfully by Patron 1.")
        self.assertEqual(self.library.checkin_book("To Kill a Mockingbird", 2),
                         "To Kill a Mockingbird checked in successfully by Patron 2.")

    def test_display_available_books(self):
        available_books = self.library.display_available_books()
        self.assertEqual(len(available_books), 2)
        self.assertEqual(available_books[0].title, "The Great Gatsby")

    def test_search_books(self):
        search_results = self.library.search_books("Great")
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0].title, "The Great Gatsby")

    def test_overdue_books(self):
        due_date1 = datetime.now() - timedelta(days=7)
        due_date2 = datetime.now() - timedelta(days=14)

        self.library.checkout_book("The Great Gatsby", 1, due_date1)
        self.library.checkout_book("To Kill a Mockingbird", 2, due_date2)

        overdue_books = self.library.overdue_books()
        self.assertEqual(len(overdue_books), 2)
        self.assertIn("The Great Gatsby is overdue for Patron 1.", overdue_books)
        self.assertIn("To Kill a Mockingbird is overdue for Patron 2.", overdue_books)

if __name__ == "__main__":
    unittest.main()
