books = []

def check_book(name,author):
    ser = [book for book in books if book['name'] == name and book['author']== author]

    if ser:
        return -1
    else:
        return 0

def insert_book(name, author,cost):
    books.append({'name': name, 'author': author, 'cost': cost, 'read': False})
    print(books)
    
def get_all_books():
    return books


def mark_book_as_read(name,author):
    for book in books:
        if book['name'] == name and book['author'] == author:
            book['read'] = True
        
def delete_book(name,author):
    global books
    books = [book for book in books if book['name'] != name and book['author'] != author]


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)

def search_book(name, author):

    ser = [book for book in books if book['name'] == name and book['author']== author]
    
    if ser:
        return f"Book found: {ser[0]}"
    else:
        return 'book is not found'



def update_book(name,author):
    
    for book in books:
        if book['name'] == name and book['author']==author:
            choice=""""
Enter:
'n' to update name of the book
'au' to update author of the book
'c' to update cost of the book

Your choice: """
            update_choice=input(choice)

            if update_choice=='n':
                new_name=input("Enter the updated book name:")
                book['name']=new_name
                print(f"Book name {book['name']} updated succesfully")
            
            elif update_choice == 'au':
                new_author=input("Enter the updated author name:")
                book['author']=new_author
                print(f"Author name {book['author']} updated succesfully")

            elif update_choice == 'c':
                new_cost=int(input("Enter the updated cost:"))
                book['cost']=new_cost
                print(f"Book cost updated succesfully to {book['cost']} rupees")
            else:
                print("Enter valid choice!")

        else:
            print(f"enterd book {name} doesnot exist")
            

def analyze():
    max_cost=max(books,key=lambda books:books['cost'])
    print("\nThe costly book is", max_cost)
    min_cost=min(books,key=lambda books:books['cost'])
    print("\nThe cheapest book is", min_cost)
    sort_books= sorted(books,key=lambda books:books['name'])
    print("\nBook names according to Aplabetical order",sort_books)
    sort_cost= sorted(books,key=lambda books:books['cost'])
    print("\nBook names according to ascending order of cost",sort_cost)


    
