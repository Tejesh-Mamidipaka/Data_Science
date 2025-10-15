books=[]

def check_book(name,author):
    check=[book for book in books if book[0]==name and book[1]==author]
    if check:
        return -1
    else:
        return 0
def insert_book(name,author,cost):
    books.append((name,author,cost))
    print(books)

def get_all_books():
    return books

def delete_book(name,author):
    global books
    books=[book for book in books if book[0]!=name and book[1]!=author]

def search_book(name,author):
    search=[book for book in books if book[0]==name and book[1]==author]
    if search:
        return f"Book found: {search[0]}"
    else:
        return 'book is not found'
def update_book(name,author):
    global books
    for book in books:
        if book[0]==name and book[1]==author:
            i = books.index(book)
            choice=""""
Enter:
'n' to update name of the book
'au' to update author of the book
'c' to update cost of the book

Your choice: """
            update_choice=input(choice)
            #if update_choice=='n':
                #new_name=input("Enter the updated book name:")
                #books[i]=(new_name, book[1], book[2])
                #print(f"Book name {books[i][0]} updated succesfully")
                #print(books)

            if update_choice == 'n':
                new_name = input("Enter the updated book name: ")
                book_list = list(book)
                book_list[0] = new_name
                books[i] = tuple(book_list)
                print(f"Book name {books[i][0]} updated successfully")
                print(books)

            
            elif update_choice == 'au':
                new_author = input("Enter the updated author name: ")
                book_list = list(book)
                book_list[1] = new_author
                books[i] = tuple(book_list)
                print(f"Author name {books[i][1]} updated successfully") 
                print(books)

            elif update_choice == 'c':
                new_cost = input("Enter the updated price: ")
                book_list = list(book)
                book_list[2] = new_cost
                books[i] = tuple(book_list)
                print(f"The book cost updated to {books[i][2]} rupees") 
                print(books)
            else:
                print("Enter valid choice!")
        else:
            print(f"enterd book {name} doesnot exist")

def analyze():
    max_cost=max(books,key = lambda books:books[2])
    print("\nThe costly book is", max_cost)
    min_cost=min(books,key=lambda books:books[2])
    print("\nThe cheapest book is", min_cost)
    sort_books= sorted(books,key=lambda books:books[0])
    print("\nBook names according to Aplabetical order",sort_books)
    sort_cost= sorted(books,key=lambda books:books[2])
    print("\nBook names according to ascending order of cost",sort_cost)