def view_lent_book():

    with open('Lent_book.csv','r') as fp:
        print('---------------------------')
        for book in fp.readlines():
            
            print(book.strip())
    