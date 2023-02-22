class Book(object):
    isbn
    title
    author

class Person(object):
    name 
    address
    start_memebership
    rented_books

    def rent_book(book) # Funktionen
        pass # erst mal weiter

    def return_book(book):
        pass

    def lose(book):
        pass

class Library(object):
    inventory
    members

class Main(object):
    library = Library()  # konkrete Bibliothek mit Namen library erstellen
    # library.members = [Person("Heike", dsdas), Person("nächste")]...
    
    hitchhikers_guide = Book(1234342, "Hitchhiker's guide throug the galaxy", "Douglas Adams")
    pride_and_prejudice = Book(31231, "Pride and Prejudice", "Jane Austen")
    herr_der_ringe = Book(321232333, "Der Herr Der Ringe", "J.R.R. Tolkien")

    lusy = Person("Lusy", "Berlin","21.01.2001")
    heike = Person("Heike", "Villingen","21.02.2023")
    sandra = Person("Sandra", "Karlsruhe", "22.02.2022")

    lusy.rent_book(herr_der_ringe)
    lusy.return_book(herr_der_ringe)


