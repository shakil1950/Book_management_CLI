
import add_book,view_book,search_book,remove_book,lent_book,view_lent_book,returned_book,edit_book

book_management=[
]


       
options="""
Options:
1.Add Book
2.View Book
3.Search Book
4.Remove Book
5.Lent Book
6.View Lent Book
7.Returned Book
8.Edit Book
0.Exit

"""   
while True:
    print(options)
    try:
        option=int(input('Enter Option:'))

        if option==1:
            add_book.add_book(book_management)
        elif option==2:
            view_book.view_book(book_management)
        elif option==3:
            search_book.search_book(book_management)
        elif option==4:
            remove_book.remove_book(book_management)
        elif option==5:
            lent_book.lent_book(book_management)
        elif option==6:
            view_lent_book.view_lent_book()
        elif option==7:
            returned_book.returned_book(book_management)
        elif option==8:
            edit_book.edit_book(book_management)
            
        elif option==0:
            break
        else:
            print("Invalid Option")
    except ValueError:
        print('Input Should be Only Number')

