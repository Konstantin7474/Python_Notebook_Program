
from datetime import datetime



def create_text(textes: list, title: str, text_text: str):
    text_id = new_id(textes)
    text = [text_id, get_time(), title, text_text]
    return text



def find_text(textes: list, text_id: str):
    for text in textes:
        if text_id in text:
            return text
        

def all_show(textes: list):
    non_empty_textes = [text for text in textes if text] 
    return non_empty_textes




def show_by_date(textes: list, selected_date: str):
    filtered_textes = []
    for text in textes:
        print("Debug:", text)
        if len(text) >= 2: 
            if selected_date in text[1]:
                filtered_textes.append(text)
        else:
            print("Invalid format:", text)
    return filtered_textes



def add_text(textes: list, text_id: str, new_title: str, new_text: str):
    new_id_value = new_id(textes)  
    added_text = [new_id_value, get_time(), new_title, new_text]
    textes.append(added_text)  
    textes.sort()  
    return textes



def delete_text(textes: list, text_id: str):
    text = find_text(textes, text_id)
    textes.remove(text)
    return textes



def new_id(textes: list):
    if (textes != []):
        return '1'
    else:
        return str(int(textes[-1][0])+ 1)
        


def get_time():
    now = datetime.now()
    now_f = now.strftime("%d/%m/%Y-%H:%M:%S")
    return now_f
    
