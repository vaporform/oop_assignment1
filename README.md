# Project Overview

This project changes a small library management system from procedural code to object‑oriented version in Python. It uses three main classes: Book, Member, and Library. For handling books, members, borrowing, and returning. The goal is to show how OOP makes the code clearer and easier to maintain, and to compare this design with the original procedural version. Test scripts are included to run normal cases and edge cases.

<!-- Project Structure - How files are organized -->
# Project Structure

This repository contains the following files and folders:

- `README.md`
	- This file. Includes documentation and usage instructions.
- `oop_solution/`
	- `library_oop.py` Refactored object-oriented version.
	- `test_oop.py` Tests for the object-oriented implementation.
- `procedural_version/`
	- `library_procedural.py` Original procedural code.
	- `test_procedural.py` Tests for the procedural implementation.

Use the test scripts in each folder to run the demos and confirm behavior.

<!-- Design Overview - Detailed explanation of each class, detailing attributes and key methods -->
# Design Overview

The object-oriented implementation contains three primary classes: `Book`, `Member`, and `Library`.

## Book

Represents a book object in the library.

- `__init__(self, id, title, author, available_copies)`
	- Attributes: `id`, `title`, `author`, `available_copies`, `total_copies` (initially same as available).
- `available_borrow(self)`
	- Returns `True` if at least one copy is available to borrow.
- `borrow(self)`
	- Removes one copy of the book from `available_copies` if possible and returns `True` on success, `False` otherwise.
- `return_book(self)`
	- Adds one copy of the book to `available_copies` if there are less copies than `total_copies` and returns `True`; otherwise returns `False`.

## Member

Represents a library member and tracks which book IDs they've borrowed.

- `__init__(self, id, name, email)`
	- Attributes: `id`, `name`, `email`, `borrowed_books` (a list of book IDs).
- `allow_borrowing(self)`
	- Returns `True` if the member has borrowed fewer than 3 books.
- `book_in(self, id)`
	- Returns `True` if the given book ID exists in the member's `borrowed_books`.
- `amount(self)`
	- Returns the number of books currently borrowed.
- `add_borrowed(self, book_id)`
	- Adds a book ID to `borrowed_books` if not already present and under the limit; returns `True` on success.
- `remove_borrowed(self, book_id)`
	- Removes a book ID from `borrowed_books` if present; returns `True` on success.

## Library

Manages collections of `Book` and `Member` objects and coordinates borrowing/returning transactions.

- `__init__(self)`
	- Attributes: `books` (list of `Book`), `members` (list of `Member`), `borrowed_books` (list of transaction dicts).
- `add_book(self, book_id, title, author, available_copies)`
	- Creates and adds a `Book` object to `self.books`.
- `add_member(self, member_id, name, email)`
	- Creates and adds a `Member` object to `self.members`.
- `find_book(self, book_id)`
	- Search for and return the `Book` object with the given ID; return `None` if not found.
- `find_member(self, member_id)`
	- Search for and return the `Member` object with the given ID; return `None` if not found.
- `borrow_book(self, member_id, book_id)`
	- Check if member and book exist, checks availability and member limits, updates book/member state, records a transaction in `borrowed_books`, and prints status messages.
- `return_book(self, member_id, book_id)`
	- Validates inputs, updates book/member state, removes the transaction from `borrowed_books`, and prints status messages.
- `display_available_books(self)`
	- Prints available titles and counts number of available books.
- `display_member_books(self, member_id)`
	- Prints the titles currently borrowed by a specific member.

<!-- How to test and run your code -->
# Running the test

First, check if Python is installed:

```
python3 --version
```

Next, you can download the repo as .zip or clone it by running:

```
git clone https://github.com/vaporform/oop_assignment1
```

Open the folder via prefered IDE or in the terminal:

```
cd oop_assignment1
```

Then run the test scripts included in the repository. From the project root, you can run the OOP version or the Procedural version by the following:

```
python3 oop_solution/test_oop.py
```

or

```
python3 procedural_version/test_procedural.py
```