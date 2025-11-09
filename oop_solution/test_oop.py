from library_oop import Library,Book,Member
lib = Library()

# Test Code for Object Orientated Programming style Library System
def test_library_system():
    """Comprehensive test of all library functions"""
    
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)
    
    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    lib.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    lib.add_book(2, "Clean Code", "Robert Martin", 2)
    lib.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    lib.add_book(4, "Design Patterns", "Gang of Four", 2)
    
    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    lib.add_member(101, "Alice Smith", "alice@email.com")
    lib.add_member(102, "Bob Jones", "bob@email.com")
    lib.add_member(103, "Carol White", "carol@email.com")
    
    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    lib.display_available_books()
    
    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    lib.borrow_book(101, 1)  # Alice borrows Python Crash Course
    lib.borrow_book(101, 2)  # Alice borrows Clean Code
    lib.borrow_book(102, 1)  # Bob borrows Python Crash Course
    
    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    lib.display_member_books(101)  # Alice's books
    lib.display_member_books(102)  # Bob's books
    lib.display_member_books(103)  # Carol's books (none)
    
    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    lib.display_available_books()
    
    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    lib.borrow_book(103, 3)  # Carol borrows the only copy of Pragmatic Programmer
    lib.display_available_books()
    
    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    lib.borrow_book(102, 3)  # Bob tries to borrow unavailable book
    
    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    lib.borrow_book(101, 4)  # Alice's 3rd book
    lib.display_member_books(101)
    lib.borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)
    
    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    lib.return_book(101, 1)  # Alice returns Python Crash Course
    lib.return_book(102, 1)  # Bob returns Python Crash Course
    lib.display_member_books(101)
    lib.display_available_books()
    
    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    lib.return_book(102, 2)  # Bob tries to return book he didn't borrow
    
    # Test 12: Return and Borrow Again
    print("\n--- TEST 12: Return and Re-borrow ---")
    lib.return_book(103, 3)  # Carol returns Pragmatic Programmer
    lib.borrow_book(102, 3)  # Bob borrows it
    lib.display_member_books(102)
    
    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    lib.borrow_book(999, 1)  # Non-existent member
    lib.borrow_book(101, 999)  # Non-existent book
    lib.return_book(999, 1)  # Non-existent member
    lib.display_member_books(999)  # Non-existent member
    
    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for transaction in lib.borrowed_books:
        print(f"  {transaction['member_name']} has '{transaction['book_title']}'")
    
    print("\nAll Members and Their Books:")
    for member in lib.members:
        print(f"\n{member.name} ({member.id}):")
        if member.borrowed_books:
            for book_id in member.borrowed_books:
                book = lib.find_book(book_id)
                print(f"  - {book.title}")
        else:
            print("  (No books borrowed)")
    
    lib.display_available_books()
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)

def test_book_class():
    print("=" * 60)
    print("BOOK CLASS - COMPREHENSIVE TEST")
    print("=" * 60)

    # Test 1: Initialize a book.
    print("\n--- TEST 1: Creating a book ---")
    j = Book(1,"A Brief History of Time","Stephen Hawking",3)
    print(j)

    # Test 2: Borrowing a book.
    print("\n--- TEST 2: Borrowing a book ---")
    print(j.borrow(), j.available_copies)

    # Test 3: Returning a book.
    print("\n--- TEST 3: Returning a book ---")
    print(j.return_book(), j.available_copies)
    
    # Test 4: Borrowing more books than allowed.
    print("\n--- TEST 4: Borrowing more books than total ---")
    for i in range(0,6):
        print(j.borrow(), j.available_copies)
    
    # Test 5: Returning more books than allowed.
    print("\n--- TEST 5: Returning more books than total ---")
    for i in range(0,6):
        print(j.return_book(), j.available_copies)

def test_member_class():
    print("=" * 60)
    print("MEMBER CLASS - COMPREHENSIVE TEST")
    print("=" * 60)

    # Test 1: Creating a new member.
    print("\n--- TEST 1: Creating a member ---")
    a = Member(1,"John Doe","example@mail.com")

    # Test 2: Borrowing a book.
    print("\n--- TEST 2: Borrowing a book ---")
    print(a.add_borrowed(1))

    # Test 3: Returning a book.
    print("\n--- TEST 3: Returning a book ---")
    print(a.remove_borrowed(1))
    
    # Test 4: Borrowing more books than allowed.
    print("\n--- TEST 4: Borrowing more books than total ---")
    for i in range(0,6):
        print(a.add_borrowed(i))
    
    # Test 5: Returning more books than allowed.
    print("\n--- TEST 5: Returning more books than total ---")
    for i in range(0,4):
        print(a.remove_borrowed(i))

    # Test 6: Returning a book that does not exist
    print("\n--- TEST 6: Returning nonexistent book ---")
    print(a.remove_borrowed(123))

def test_library_class():

    print("=" * 60)
    print("LIBRARY CLASS - COMPREHENSIVE TEST")
    print("=" * 60)
    lib = Library()
    
    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    lib.add_book(1,"JoJo's Bizarre Adventure: Phantom Blood","Hirohiko Araki",1)
    lib.add_book(2,"JoJo's Bizarre Adventure: Battle Tendency","Hirohiko Araki",2)
    lib.add_book(3,"JoJo's Bizarre Adventure: Stardust Crusaders","Hirohiko Araki",3)
    lib.add_book(4,"JoJo's Bizarre Adventure: Diamond is Unbreakable","Hirohiko Araki",4)
    lib.add_book(5,"JoJo's Bizarre Adventure: Golden Wind","Hirohiko Araki",5)
    lib.add_book(6,"JoJo's Bizarre Adventure: Stone Ocean","Hirohiko Araki",6)
    lib.add_book(7,"Steel Ball Run","Hirohiko Araki",7)
    lib.add_book(8,"JoJolion","Hirohiko Araki",8)
    lib.add_book(9,"The JOJOLands","Hirohiko Araki",9)
    
    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    lib.add_member(1, "Jonathan Joestar", "JonJoe@email.com")
    lib.add_member(2, "Joseph Joestar", "JosJoe@email.com")
    lib.add_member(3, "Jotaro Kujo", "Kujo@email.com")
    lib.add_member(4, "Josuke Higashikata", "JsH@email.com")
    lib.add_member(5, "Giorno Giovanna", "GioGio@email.com")
    lib.add_member(6, "Jolyne Cujoh", "Jolyne@email.com")
    lib.add_member(7, "Johnny Joestar", "JohnJoe@email.com")
    lib.add_member(8, "Josukeight Higashikata", "Js8H@email.com")
    lib.add_member(9, "Jodio Joestar", "JDio@email.com")
    
    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    lib.display_available_books()
    
    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    lib.borrow_book(1, 1)  # Jonathan borrows Phantom Blood
    lib.borrow_book(1, 2)  # Jonathan borrows Battle Tendency
    lib.borrow_book(6, 6)  # Jolyne borrows Stone Ocean
    
    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    lib.display_member_books(1)  # Jonathan's books
    lib.display_member_books(6)  # Bob's books
    lib.display_member_books(7)  # Johnny's books (none)
    
    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    lib.display_available_books()
    
    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    lib.borrow_book(7, 2)  # Johnny borrows the only copy of Battle Tendency
    lib.display_available_books()

    print("\n--- TEST 7: Borrowing Last Copy ---")
    lib.borrow_book(7, 2)  # Johnny borrows the only copy of Battle Tendency
    lib.display_available_books()
    # Test 8: Return Books
    print("\n--- TEST 8: Returning Books ---")
    lib.return_book(1, 1)  # Jonathan returns Phantom Blood
    lib.return_book(6, 6)  # Jolyne returns Stone Ocean
    lib.display_member_books(1)
    lib.display_available_books()

    # Test 9: Nonexistent Member or Book
    print("\n--- TEST 9: Nonexistent Member or Book ---")
    lib.borrow_book(999, 1)  # Non-existent member
    lib.borrow_book(1, 999)  # Non-existent book
    lib.return_book(999, 1)  # Non-existent member
    lib.display_member_books(999)  # Non-existent member

# Run the comprehensive test
if __name__ == "__main__":
    test_book_class()
    print()
    test_member_class()
    print()
    test_library_class()
    print()
    test_library_system()
    
