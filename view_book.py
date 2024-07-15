def view_book(book_management):
        if len(book_management)>=1:
            for index,book in enumerate(book_management):
                print(f"Serial Number:{index+1}")
                print(f"Title:{book['Title']}\nISBN:{book['ISBN']}\nAuthor's:{book['Authors']}\nprice:{book['Price']}\nPub_Year:{book['Year']}\nQuantity:{book['Quantity']}\nState:{'Available' if book['Quantity']>0 else 'Not Available'}\n-----------------------------\n")
        else:
            with open('book_add_list.csv','r') as fp:
                for book in fp.readlines():
                    if len(book.strip().split(':'))>1:
                        print(book.strip().split(':')[0]+":"+book.strip().split(':')[1])
                    else:
                        print('------------------------')
                