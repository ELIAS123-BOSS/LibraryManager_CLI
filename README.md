# LibraryManager_CLI
# Project: LibraryManager_CLI

## 1. Requirement Analysis
**Goal:** Create a command-line system to manage library inventory.
**Functional Requirements:**
- Admin can register new books.
- Users can borrow books (status changes to unavailable).
- Users can return books (status changes to available).
- System displays current catalog status.

## 2. System Design
This project uses Object-Oriented Programming. The implementation strictly follows this nomenclature:

| Entity | Implementation Name | Description |
| :--- | :--- | :--- |
| **Class** | `BookItem` | Represents a single book. |
| **Class** | `LibraryController` | Manages the list of books. |
| **Method** | `register_book` | Adds a book to the library. |
| **Method** | `checkout_book` | Marks a book as borrowed. |
| **Method** | `checkin_book` | Marks a book as returned. |

## 3. Implementation
The project is implemented in **Python** (`main.py`). It utilizes a list data structure to hold `BookItem` objects within the `LibraryController` class.

## 4. Testing
**Test Case:** Borrowing
- **Input:** `checkout_book("B001")`
- **Expected:** Status updates to True.
- **Actual:** "Success: You borrowed..."

## 5. Deployment
The source code is hosted on GitHub for version control and distribution.
