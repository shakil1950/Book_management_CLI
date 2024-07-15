def lent_book(book_management):
    while True:
        for index,book in enumerate(book_management):
                    print(f"Serial Number:{index+1}")
                    print(f"Title:{book['Title']}\nISBN:{book['ISBN']}\nAuthor's:{book['Authors']}\nprice:{book['Price']}\nPub_Year:{book['Year']}\nQuantity:{book['Quantity']}\nState:{book['State']}\n-----------------------------\n")
        lent_isbn=int(input('Enter ISBN Number For Lent a Book:'))
        flag=False

        for book in book_management:
            if lent_isbn==book['ISBN']:
                flag=True
                lent_quantity=int(input('Enter Quantity of lent:'))
                if book['Quantity']>=lent_quantity:
                    lender_name=input("Enter Lender Name:").capitalize()
                    book['Quantity']=book['Quantity']-lent_quantity
                    book['State']={'Not Available' if book['Quantity']<=0 else 'Available'}
                    with open('Lent_book.csv','a') as fp:
                        line=f"State:Lent\nTitle:{book['Title']}\nISBN:{book['ISBN']}\nAuthor's:{book['Authors']}\nprice:{book['Price']}\nPub_Year:{book['Year']}\nQuantity:{lent_quantity}\n-----------------------------\n"
                        fp.write("Lent BY:"+lender_name+'\n')
                        fp.write(line)
                    print('Successfull')
                else:
                    print('Not enough books available to lend.')
        if flag==False:
            print('Book Not Found')
        lent_again=input('Do you want to lent again(N/Y)').upper()
        if lent_again=='N':
            break
        else:
            continue