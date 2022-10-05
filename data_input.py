address_book = {}

def new_contact ():
    global address_book
    last_id = max([int(item) for item in address_book.keys()])
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone: ")
    description = input("Comment: ")
    new_id = last_id + 1
    new_entry = {'First name': first_name, 'Last name': last_name, 'Phone': phone_number, 'Comment':description}
    address_book[new_id] = new_entry
    return address_book

def find_contact ():
    global address_book
    first_name = input("First name: ")
    last_name = input("Last name: ")
    result = 0
    for i in address_book.values():
        if first_name in i.values() and last_name in i.values():
            for j in i.keys():
                print (j + ": " + i[j])
                result+=1
    if result==0:
        print ("Контакта не существует, проверьте правильность ввода данных")
    return address_book

def delete_contact ():
    global address_book
    id_contact = input("Contact ID to be deleted: ")
    del address_book[id_contact]
    return None