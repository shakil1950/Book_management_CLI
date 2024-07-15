contact_book=[
    # {
    #   'name': 'shakil', 
    #   'phone': '01770959030',
    #   'email': 'shakil@gmail.com'   
    # },
    # {'name': 'Afsana', 
    #  'phone': '01500000000', 
    #  'email': 'afsana@gmail.com'
    #  },
    # {'name': 'Maruf', 
    #  'phone': '017709568635', 
    #  'email': 'maruf@gmail.com'
    #  },
    # {'name': 'Zurin', 
    #  'phone': '0145879654758', 
    #  'email': 'zurin@gmail.com'
    #  }
]


def contact_add():
    name=input('Enter Name:')
    phone=input('Enter Phone Number:')
    email=input('Enter Email:')
    
    contact={
        'name':name,
        'phone':phone,
        'email':email
    }
    
    contact_book.append(contact)

def view_all_contact():
    for contact in contact_book:
        print(f"Name:{contact['name']} \nPhone:{contact['phone']}\nEmail:{contact['email']}")
        print('---------------------------------------------------------------------')


def search_contact():
    while True:
        search_key=input("Type somthing for search:")
        for contact in contact_book:
            if search_key in contact['name'] or search_key in contact['phone'] or search_key in contact['email']:
                print(f"Name:{contact['name']} \nPhone:{contact['phone']}\nEmail:{contact['email']}")
                print('---------------------------------------------------------------------')
        
        found=input("Do You want to search continue(Y/N):??")
        if found.upper()=='N':
            break
        else:
            continue


def remove_contact():
    
    for index, contact in enumerate(contact_book):
        print(f'Contact Serial ==> {index+1} <==')
        print(f"Name:{contact['name']} \nPhone:{contact['phone']}\nEmail:{contact['email']}")
        print('---------------------------------------------------------------------')

    contact_serial=int(input('Enter Contact Serial  Number:'))
    contact_book.pop(contact_serial-1)

def update_contact():
    
    for index,contact in enumerate(contact_book):
        print(f'Contact Serial ==> {index+1} <==')
        print(f"Name:{contact['name']} \nPhone:{contact['phone']}\nEmail:{contact['email']}")
        print('---------------------------------------------------------------------')
    
    contact_serial=int(input('Enter Contact Serial  Number:'))
    while True:
        key_input=input("Which Information Do you want to Update(Name/Phone/Email) or 0 for exit").lower()
        
        
        if key_input=='name':
            contact_book[contact_serial-1]['name']=input("Enter Name").capitalize()
        elif key_input=='phone':
            contact_book[contact_serial-1]['phone']=input('Enter Phone Number').capitalize()
        elif key_input=='email':
            contact_book[contact_serial-1]['email']=input('Enter Email').capitalize()
        elif key_input=='0':
            break
        else:
            print('Invalid Key')

def backup_contact():
        with open('backup_contact.csv','w') as fp:
            for contact in contact_book:
                line=f"Name:{contact['name']} \nPhone:{contact['phone']}\nEmail:{contact['email']}\n-----------------\n"
                fp.write(line)
         
        
         

def restore_contact():
    restore_list=[]
    with open('backup_contact.csv','r') as fp:
        for line in fp.readlines():
            
            if len(line.strip().split(':'))==1:
                contact={
                    'name':restore_list[0],
                    'phone':restore_list[1],
                    'email':restore_list[2]   
                }
                contact_book.append(contact)
                restore_list=[]
                print(contact_book)
               
            else:
                restore_list.append(line.strip().split(':')[1])
                   

choice_list="""
Options
---------------------------------
1.Create Contact
2.View Contact
3.Search Contact
4.Remove Contact
5.Update Contact
6.Backup Contact
7.Restore Contact
0.Exit
"""
while True:
    print(choice_list)
    choice=int(input("Enter Your Option:"))
    if choice==1:
        contact_add()
    elif choice==2:
        view_all_contact()
    elif choice==3:
        search_contact()
    elif choice==4:
        remove_contact()
    elif choice==5:
        update_contact()
    elif choice==6:
        backup_contact()
    elif choice==7:
        restore_contact()
    elif choice==0:
        break
    else:
        print('Wrong Choice !!')
