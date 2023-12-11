# testcode.py
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

    def test_reserve_book(self):
        self.assertEqual(self.library.reserve_book("The Great Gatsby", 1),
                         "The Great Gatsby reserved successfully by Patron 1.")
        self.assertEqual(self.library.reserve_book("The Great Gatsby", 2),
                         "Sorry, The Great Gatsby is reserved by another patron.")
        self.assertEqual(self.library.reserve_book("Nonexistent Book", 1),
                         "Error: Nonexistent Book does not exist in the library.")

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
        self.assertIn("The Great Gatsby is overdue for Alice (ID: 1). Due date was", overdue_books[0])
        self.assertIn("To Kill a Mockingbird is overdue for Bob (ID: 2). Due date was", overdue_books[1])

    def test_get_popular_books(self):
        self.library.checkout_book("The Great Gatsby", 1, datetime.now() - timedelta(days=10))
        self.library.checkout_book("The Great Gatsby", 2, datetime.now() - timedelta(days=5))
        self.library.checkout_book("To Kill a Mockingbird", 1, datetime.now() - timedelta(days=3))

        popular_books = self.library.get_popular_books(num_books=1)
        self.assertEqual(len(popular_books), 1)
        self.assertIn("The Great Gatsby", popular_books[0])

if __name__ == "__main__":
    unittest.main()
