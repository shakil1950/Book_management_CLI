

def remove_book(book_management):
    try:
        while True:
            for index,book in enumerate(book_management):
                print(f"Serial Number:{index+1}")
                print(f"Title:{book['Title']}\nISBN:{book['ISBN']}\nAuthor's:{book['Authors']}\nprice:{book['Price']}\nPub_Year:{book['Year']}\nQuantity:{book['Quantity']}\nState:{book['State']}\n-----------------------------\n")
            
            remove_index=int(input('Please select serial number to remove:'))
            with open('book_add_list.csv','a') as fp:
                line=f"""State: Remove
                Title:{book_management[remove_index-1]['Title']}
                ISBN:{book_management[remove_index-1]['ISBN']}
                Author's:{book_management[remove_index-1]['Authors']}
                Price:{book_management[remove_index-1]['Price']}
                Year:{book_management[remove_index-1]['Year']}
                Quantity:{book_management[remove_index-1]['Quantity']}
                """
                fp.write(line)
            book_management.pop(remove_index-1)
            print('Book Remove Successfully!!!!!')
            delete_again=input("Do want to remove again(N/Y):").upper()
            if delete_again=='N':
                    break
            else:
                    continue
    except IndexError:
        print('No item left to remove')