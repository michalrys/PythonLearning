# tylko do testu

# test setów

def cb_get_string_from_user(message_to_print):
    #TODO: must be string, else repeat
    #TODO: add check for names, surenames, nicks, address, ...
    string_input_from_user = input(f'>>> {message_to_print}: ')
    return string_input_from_user

z = cb_get_string_from_user('Pierwsze imię to')

print(z)