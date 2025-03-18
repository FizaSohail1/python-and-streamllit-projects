import json

LIBRARY_FILE = 'library.json'

def load_library():
    try:
        with open(LIBRARY_FILE , 'r') as file:
            return json.load(file)
    except (FileNotFoundError , json.JSONDecodeError):
        return []

def save_library(library):
    with open(LIBRARY_FILE , 'w') as file:
        json.dump(library , file , indent = 3)        

def add_book(library):
    title = input("Enter book title: ") 
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read_status = input("Have you read it? (yes/no): ").strip().lower()   

    book = {
        "title" : title,
        "author" :author,
        "year" :year ,
        "genre" : genre,
        "read_status" : read_status
    }

    library.append(book)
    save_library(library)
    print(f'Book "{title}" Added successfully! ✅')

def remove_book(library):
    title = input("Enter the name of the book you want to remove: ").lower()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print('Book "{title}" removed successfully! ')    
            return
    print('Book not found!')    

def search_book(library):
    title = input("Enter book title or author to search: ").lower()
    results = [book for book in library if title in book["title"].lower() or title in book["author"].lower()]

    if results:
        for book in results:
            print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {"Read" if book["read_status"] else "Unread"}')
    else:
        print("No Book Found!")   

def book_list(library):
    if not library:
        print("Your Library is empty!")
    else:
        for book in library:
         print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {"Read" if book["read_status"] == True else "Unread"}')


def statics(library):
    total_books = len(library)
    read_books = len([book for book in library if book["read_status"] == True])
    unread_books = total_books - read_books
    print("\nLibrary Statistics:")
    print(f'Total books: {total_books}')
    print(f'Read books: {read_books}')
    print(f'Unread books: {unread_books}')


def main():
    library = load_library()
    while True:
        print("\nLibrary Manager 📚")
        print("1. Add a Book 📖")
        print("2. Remove a Book 🗑")
        print("3. Search for a Book 🔎")
        print("4. List All Books 📃")
        print("5. Library Statistics 📈")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            book_list(library)
        elif choice == "5":
             statics(library)
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

main()            
    


