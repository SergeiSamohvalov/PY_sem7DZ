import data_input

def to_do (action):
    if action == 1:
        data_input.new_contact()
    if action == 2:
        data_input.find_contact()
    if action == 3:
        data_input.delete_contact()