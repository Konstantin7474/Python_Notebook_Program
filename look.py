def welcome():
    print('\nYou are welcome to NOTES')


def bye():
    print('\nBYE!')



def menu():
    print("""
    MENU:
    1 - Create note
    2 - Show note
    3 - Show all notes
    4 - Show by date
    5 - Add note
    6 - Delete note
    0 - EXIT
    """)



def write_operation():
    return input('Input command: ')


def id_input():
    return input('Input Note ID:')



def date_selected():
    return input('Input the date of the Notes: dd/mm/yyyy  ')



def title_input():
    return input ('Input Note title: ')



def input_text_text():
    return input('Input Note text: ')



def output_text(text):
    try:
        print('\n -----------------------',
              f'\nID: {text[0]}\nDATE: {text[1]}\nTITLE: {text[2]}\nNOTE: {text[3]}\n',
              '-----------------------')
    except:
        lost_id()


def output_all(textes):
    non_empty_textes = [text for text in textes if text] 
    if non_empty_textes:
        if len(non_empty_textes) > 1:
            print(f'\nFound {len(non_empty_textes)} Notes:')
        else:
            print(f'\nFind {len(non_empty_textes)} Note: ')
        for text in non_empty_textes:
            print('\n -----------------------',
                  f'\nID: {text[0]}\nDATE: {text[1]}\nTITLE: {text[2]}\nNOTE: {text[3]}\n',
                  '-----------------------')
    else:
        print('\nERROR! NOTES ARE EMPTY',
              '\nCREATE YOUR FIRST NOTE')




def output_date(textes):
    if(textes != []):
        if(len(textes) > 1):
            print(f'\nFound {len(textes)} Notes:')
        else:
            print(f'\nFind {len(textes)} Note: ')
        for text in textes:
            print('\n -----------------------',
              f'\nID: {text[0]}\nDATE: {text[1]}\nTITLE: {text[2]}\nNOTE: {text[3]}\n',
              '-----------------------')
    else:
        print('\nERROR! NOTES NOT FOUND',
              '\nCHECK YOUR DATE INPUT')



def ok_created():
    print('\nNOTE CREATED SUCCESSFULLY')



def ok_changed():
    print('\nNOTE CHANGED SUCCESSFULLY')


def ok_deleted():
    print('\nNOTE DELETED SUCCESSFULLY')


def error_input():
    print('\nINPUT ERROR! PLEASE TRY AGAIN')


def lost_id():
    print('\nERROR! NOTE NOT FOUND',
          '\nOR CHECK YOUR ID INPUT')
    
