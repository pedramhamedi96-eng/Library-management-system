class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, id, title):
        self.books[id] = title
        return True

    def add_member(self, id, name):
        self.members[id] = name
        return True

    def borrow(self, id):
        if id in self.books:
            return self.books.pop(id)
        return False

    def search(self, title):
        return [b for b in self.books.values() if title in b]

    def return_book(self, id, title):
        self.books[id] = title
        return True
