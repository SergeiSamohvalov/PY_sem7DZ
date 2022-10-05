from data_input import address_book 

file_name = 'Address_book.txt'

def data_export(file_name):
    file = open(file_name, 'w')
    get_keys = address_book['1']
    first_line = "Id;"+ ";".join(get_keys.keys())
    file.write(first_line+'\n')
    for item in address_book.keys():
        new_line = str(item)+';' + ';'.join(values for values in address_book[item].values())
        file.write(new_line+'\n')
    file.close()
    return address_book