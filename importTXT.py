from data_input import address_book 

file_name = 'Address_book.txt'

def database_creator (file_name):
    global address_book
    file = open(file_name, 'r')
    data = file.readlines()
    keys_contact = data[0].strip().split(';')
    del data[0]
    for lines in data:
        users_info = lines.strip().split(';')
        new_line = dict(zip(keys_contact, users_info))
        new_key = new_line.pop('Id')
        address_book[new_key] = new_line
    file.close()
    return address_book