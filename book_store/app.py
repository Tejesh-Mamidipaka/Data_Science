from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 's' to search a book
- 'u' to update a book
- 'an' to analyse the books
- 'q' to quit

Your choice: """


def menu():
   
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'd':
            prompt_delete_book()
        elif user_input == 's':            
            prompt_search_book()
        elif user_input == 'u':
            prompt_update_book()
        
        elif user_input == 'an':
            prompt_analyze()
        else:
            print("Enter valid choice!")
        user_input = input(USER_CHOICE)
    
def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    cost = int(input("Enter the new book cost in rupees: "))
    if  database.check_book(name,author)== -1:
        print(f"The entered book already exists")
    
    else:
        database.insert_book(name,author,cost)

def list_books():
    for book in database.get_all_books():
        print(f"{book[0]} by {book[1]} which costs {book[2]}")

def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')
    author = input("Enter the name of the author you wish to delete: ")
    database.delete_book(name,author)

def prompt_search_book():
    name = input("Enter the name of the book you want to search: ")
    author = input("Enter the name of the author you want to search: ")
    
    print(database.search_book(name,author))

def prompt_update_book():
    name=input("Enter the name of the book which you want to update: ")
    author=input("Enter the name of the author which you want to update: ")

    database.update_book(name,author)


def prompt_analyze():
    database.analyze()



menu()