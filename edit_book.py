
def serach_index(edit_index,book_management):
    for index,book in enumerate(book_management):
        if edit_index==index:
            return True
        
def edit_book(book_management):
    
    for index,book in enumerate(book_management):
            print(f"Serial Number:{index+1}")
            print(f"Title:{book['Title']}\nISBN:{book['ISBN']}\nAuthor's:{book['Authors']}\nprice:{book['Price']}\nPub_Year:{book['Year']}\nQuantity:{book['Quantity']}\nState:{book['State']}\n-----------------------------\n")
            
    edit_index=int(input('Please select serial number to Edit:'))
    flag=serach_index(edit_index,book_management)
    

    if flag==True:
        while True:
            Edit_info=input('Please specify which info do you want to edit(Title/Author/ISBN/Quantity/Price/Year) or 0 to exit').capitalize()
            try:
                if Edit_info=='Title':
                    book_management[edit_index-1]['Title']=input('Edit Title')
                elif Edit_info=='Author':
                    book_management[edit_index-1]['Authors']=input('Edit Author name(Separate with "," for more than one author):').split(',')
                elif Edit_info=='ISBN':
                    book_management[edit_index-1]['ISBN']=int(input("Edit ISBN Number:"))
                elif Edit_info=='Quantity':
                    book_management[edit_index-1]['Quantity']=int(input('Edit Quantity:'))
                elif Edit_info=='Price':
                    book_management[edit_index-1]['Price']=format(float(input('Edit Price:')),".2f")
                elif Edit_info=='Year':
                    book_management[edit_index-1]['Year']=input('Edit Year:')
                elif Edit_info=='0':
                    break
                else:
                    print('Wrong Choice')
            except IndexError:
                print('Invalid Serial')
    else:
        print("Invalid Serial")