# code.py

class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = copies
        self.available_copies = copies
        self.checked_out = {}
        self.due_dates = {}

    def checkout(self, patron_id, due_date):
        if self.available_copies > 0:
            self.available_copies -= 1
            self.checked_out[patron_id] = datetime.now()
            self.due_dates[patron_id] = due_date
            return f"{self.title} checked out successfully by Patron {patron_id}."
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

class Patron:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

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

    def overdue_books(self):
        today = datetime.now()
        overdue_books = []

        for book in self.books:
            for patron_id, due_date in book.due_dates.items():
                if today > due_date:
                    overdue_books.append(f"{book.title} is overdue for Patron {patron_id}. Due date was {due_date}.")

        return overdue_books
