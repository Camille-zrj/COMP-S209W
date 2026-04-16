class Library:
    def __init__(self, name):
        self.name = name
        self._book_list = []
        self._user_list = []


    def add_book(self, book):
        for b in self._book_list:
            if b.get_isbn() == book.get_isbn():
                return False  
        self._book_list.append(book)
        return True

    def search_book(self, isbn):
        for b in self._book_list:
            if b.get_isbn() == isbn:
                return b
        return None

    def show_all_books(self):
        return self._book_list
    

    def add_user(self, user):
        for u in self._user_list:
            if u.get_user_id() == user.get_user_id():
                return False
        self._user_list.append(user)
        return True
    

    def find_user(self, user_id):
        for u in self._user_list:
            if u.get_user_id() == user_id:
                return u
        return None
        

    def borrow_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.search_book(isbn)
        if not user or not book:
            return False, "User or book not found"
        if not book.is_available():
            return False, "Book already borrowed"
        book.set_available(False)
        user.borrow_book(book)
        return True, "Borrow successful"
    

    def return_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.search_book(isbn)
        if not user or not book:
            return False, "User or book not found"
        if user.return_book(book):
            book.set_available(True)
            return True, "Return successful"
        return False, "Book not borrowed by this user"
