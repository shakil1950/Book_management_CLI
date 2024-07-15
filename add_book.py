
def search_isbn(isbn,book_management):
    
    for item in book_management:
        if isbn==item['ISBN']:
            
            return True
    return False




def add_book(book_management):
    title=input('Enter Book Titel:').capitalize()
    isbn=int(input("Enter ISBN Number:"))
    author=input('Enter Authors Name(use "," for more than one Author):').split(',')
    price=format(float(input("Enter Price:")),".2f")
    year=input('Enter Publishing Year:')
    quantity=int(input('Enter Quantity:'))
    find_isbn=search_isbn(isbn,book_management)
    print(find_isbn)
    if find_isbn==False:
        adding={
            'State':'available',
            'Title':title,
            'ISBN':isbn,
            'Authors':author,
            'Price':price,
            'Year':year,
            'Quantity':quantity
        }
        book_management.append(adding)
        with open('book_add_list.csv','a') as fp:
            for book in book_management:
                line=f"State:{book['State']}\nTitle:{book['Title']}\nISBN:{book['ISBN']}\nAuthor's:{book['Authors']}\nprice:{book['Price']}\nPub_Year:{book['Year']}\nQuantity:{book['Quantity']}\n-----------------------------\n"
                fp.write(line)
                print('Book added successfully')
    else:
        print('Duplicate ISBN not allow ')
        