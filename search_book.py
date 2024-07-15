def search_book(book_management):
    while True:
        search_key=input('Search Your Desire Book:').lower()
        flag=False
        for index,book in enumerate(book_management):
            if search_key in str(book['ISBN']).lower() or search_key in book['Title'].lower() or search_key in [author.lower() for author in book['Authors']]:
                print(f"Serial Number:{index+1}")
                print(f"Title:{book['Title']}\nISBN:{book['ISBN']}\nAuthor's:{book['Authors']}\nprice:{book['Price']}\nPub_Year:{book['Year']}\nQuantity:{book['Quantity']}\nState:{book['State']}\n-----------------------------\n")
                flag=True
        if flag==False:
            print("Opps Sorry!!! Book not Found")   
        search_again=input("Do want To Search Again(N/Y):").upper()
        if search_again=='N':
            break
        else:
            continue