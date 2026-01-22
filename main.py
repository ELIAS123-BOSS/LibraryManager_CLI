# Project: LibraryManager_CLI
# Author: [Your Name/Matric Number]

class BookItem:
    """
    Represents a single book in the library.
    Design Match: Class 'BookItem'
    """
    def __init__(self, book_id, title):
        self.book_id = book_id      # Matches Design: book_id
        self.title = title
        self.is_borrowed = False    # Matches Design: is_borrowed

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[ID: {self.book_id}] '{self.title}' - {status}"


class LibraryController:
    """
    Manages the collection of BookItems.
    Design Match: Class 'LibraryController'
    """
    def __init__(self):
        self.inventory = []

    def register_book(self, book_id, title):
        """
        Adds a new book to the inventory.
        Matches Design: register_book()
        """
        new_book = BookItem(book_id, title)
        self.inventory.append(new_book)
        print(f"Success: '{title}' added to library.")

    def checkout_book(self, book_id):
        """
        Marks a book as borrowed if available.
        Matches Design: checkout_book()
        """
        for book in self.inventory:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"Success: You borrowed '{book.title}'.")
                    return
                else:
                    print(f"Error: '{book.title}' is already borrowed.")
                    return
        print("Error: Book ID not found.")

    def checkin_book(self, book_id):
        """
        Marks a book as returned.
        Matches Design: checkin_book()
        """
        for book in self.inventory:
            if book.book_id == book_id:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Success: '{book.title}' returned.")
                    return
                else:
                    print("Error: This book is not currently borrowed.")
                    return
        print("Error: Book ID not found.")

    def display_catalog(self):
        print("\n--- Library Catalog ---")
        if not self.inventory:
            print("Library is empty.")
        for book in self.inventory:
            print(book)
        print("-----------------------\n")


# --- Main Execution Block ---
if __name__ == "__main__":
    # Initialize the controller
    my_library = LibraryController()

    # 1. Register Books (Admin Action)
    my_library.register_book("B001", "Introduction to Software Engineering")
    my_library.register_book("B002", "Python for Beginners")

    # 2. Display initial state
    my_library.display_catalog()

    # 3. Simulate Borrowing (User Action)
    my_library.checkout_book("B001")

    # 4. Attempt to borrow the same book again (Validation Test)
    my_library.checkout_book("B001")

    # 5. Display state after borrowing
    my_library.display_catalog()

    # 6. Return the book
    my_library.checkin_book("B001")
    
    # 7. Final State
    my_library.display_catalog()
