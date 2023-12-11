# code.py
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = copies
        self.available_copies = copies
        self.checked_out = {}
        self.due_dates = {}
        self.reserved_by = None
        self.popularity = 0  # Track popularity based on checkouts

    def checkout(self, patron_id, due_date):
        if self.available_copies > 0 and self.reserved_by is None:
            self.available_copies -= 1
            self.checked_out[patron_id] = datetime.now()
            self.due_dates[patron_id] = due_date
            self.popularity += 1
            return f"{self.title} checked out successfully by Patron {patron_id}."
        elif self.reserved_by == patron_id:
            self.reserved_by = None
            return self.checkout(patron_id, due_date)  # Proceed with checkout after reservation
        elif self.reserved_by is not None:
            return f"Sorry, {self.title} is reserved by another patron."
        else:
            return f"Sorry, no available copies of {self.title}."

    def checkin(self, patron_id):
        if patron_id in self.checked_out:
            self.available_copies += 1
            check_out_date = self.checked_out.pop(patron_id)
            due_date = self.due_dates.pop(patron_id)
            return f"{self.title} checked in successfully by Patron {patron_id}. Checked out on {check_out_date}, due on {due_date}."
        else:
            return f"Error: {self.title} was not checked out by Patron {patron_id}."

    def reserve(self, patron_id):
        if self.available_copies > 0 and self.reserved_by is None:
            self.reserved_by = patron_id
            return f"{self.title} reserved successfully by Patron {patron_id}."
        elif self.reserved_by == patron_id:
            return f"{self.title} is already reserved by Patron {patron_id}."
        else:
            return f"Sorry, {self.title} is not available for reservation."

class Patron:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def get_info(self):
        return f"{self.name} (ID: {self.member_id})"

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def add_patron(self, patron):
        self.patrons.append(patron)

    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]

    def display_available_books(self):
        return [book for book in self.books if book.available_copies > 0]

    def checkout_book(self, title, patron_id, due_date):
        for book in self.books:
            if book.title == title:
                return book.checkout(patron_id, due_date)
        return f"Error: {title} does not exist in the library."

    def checkin_book(self, title, patron_id):
        for book in self.books:
            if book.title == title:
                return book.checkin(patron_id)
        return f"Error: {title} does not exist in the library."

    def reserve_book(self, title, patron_id):
        for book in self.books:
            if book.title == title:
                return book.reserve(patron_id)
        return f"Error: {title} does not exist in the library."

    def overdue_books(self):
        today = datetime.now()
        overdue_books = []

        for book in self.books:
            for patron_id, due_date in book.due_dates.items():
                if today > due_date:
                    overdue_books.append(f"{book.title} is overdue for {self.get_patron_info(patron_id)}. Due date was {due_date}.")

        return overdue_books

    def get_patron_info(self, patron_id):
        for patron in self.patrons:
            if patron.member_id == patron_id:
                return patron.get_info()

    def get_popular_books(self, num_books=5):
        popular_books = sorted(self.books, key=lambda x: x.popularity, reverse=True)[:num_books]
        return [f"{book.title} by {book.author}. Popularity: {book.popularity}" for book in popular_books]
