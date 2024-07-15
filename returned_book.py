def returned_book(book_management):
    
    isbn=int(input('Enter Isbn Number:'))

    for index,book in enumerate(book_management):
        if isbn==book['ISBN']:
            name=input("Enter Name:")
            quantity=int(input('Enter Number of Book Returned:'))
            book['Quantity']=book['Quantity']+quantity
            book['State']={'Not Available' if book['Quantity']>=0 else 'Available'}
            with open('Returned_book.csv','a') as fp:
                line=f"Serial Number:{index+1}\nReturned by:{name}\nState:{'Not Available' if book['Quantity']==0 else 'Available'}\nTitle:{book['Title']}\nISBN:{book['ISBN']}\nAuthor's:{book['Authors']}\nprice:{book['Price']}\nPub_Year:{book['Year']}\nAvailable Quantity:{book['Quantity']}\n-----------------------------\n"
                fp.write(line)
