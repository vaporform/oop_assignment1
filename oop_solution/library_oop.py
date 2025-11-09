class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []

    def add_book(self,book_id, title, author, available_copies):
        """Add a new book to the library"""
        book = {
            'id': book_id,
            'title': title,
            'author': author,
            'available_copies': available_copies,
            'total_copies': available_copies
        }
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def add_member(self, member_id, name, email):
        """Register a new library member"""
        member = {
            'id': member_id,
            'name': name,
            'email': email,
            'borrowed_books': []
        }
        self.members.append(member)
        print(f"Member '{name}' registered successfully!")

    def find_book(self,book_id):
        """Find a book by ID"""
        for book in self.books:
            if book['id'] == book_id:
                return book
        return None

    def find_member(self,member_id):
        """Find a member by ID"""
        for member in self.members:
            if member['id'] == member_id:
                return member
        return None

    def borrow_book(self,member_id, book_id):
        """Process a book borrowing transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            print("Error: Member not found!")
            return False
        
        if not book:
            print("Error: Book not found!")
            return False
        
        if book['available_copies'] <= 0:
            print("Error: No copies available!")
            return False
        
        if len(member['borrowed_books']) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        
        # Process the borrowing
        book['available_copies'] -= 1
        member['borrowed_books'].append(book_id)
        
        transaction = {
            'member_id': member_id,
            'book_id': book_id,
            'member_name': member['name'],
            'book_title': book['title']
        }
        self.borrowed_books.append(transaction)
        
        print(f"{member['name']} borrowed '{book['title']}'")
        return True

    def return_book(self,member_id, book_id):
        """Process a book return transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member or not book:
            print("Error: Member or book not found!")
            return False
        
        if book_id not in member['borrowed_books']:
            print("Error: This member hasn't borrowed this book!")
            return False
        
        # Process the return
        book['available_copies'] += 1
        member['borrowed_books'].remove(book_id)
        
        # Remove from borrowed_books list
        for i, transaction in enumerate(self.borrowed_books):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                self.borrowed_books.pop(i)
                break
        
        print(f"{member['name']} returned '{book['title']}'")
        return True

    def display_available_books(self):
        """Display all books with available copies"""
        print("\n=== Available Books ===")
        for book in self.books:
            if book['available_copies'] > 0:
                print(f"{book['title']} by {book['author']} - {book['available_copies']} copies available")

    def display_member_books(self,member_id):
        """Display books borrowed by a specific member"""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member['name']} ===")
        if not member['borrowed_books']:
            print("No books currently borrowed")
        else:
            for book_id in member['borrowed_books']:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book['title']} by {book['author']}")
