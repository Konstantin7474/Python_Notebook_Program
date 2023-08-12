import csv
import os


def file_read(way):
    textes = []
    if (os.path.exists(way)):
        with open(way, 'r') as f:
            reading = csv.reader(f, delimiter = ';')
            next(reading)
            for text in reading:
                textes.append(list(text))
        return textes
    else:
        with open(way, 'w') as f2:
            writing = csv.writer(f2, delimiter = ';')
            writing.writerow(header)
        return textes
    


def file_to_save(new_text):
    with open(way, 'a') as f:
        writing = csv.writer(f, delimiter = ';')
        writing.writerow(new_text)
    file_read(way)



def file_update(updated_textes):
    with open(way, 'w') as f:
        writing = csv.writer(f, delimiter = ';')
        writing.writerow(header)
        for text in updated_textes:
            writing.writerow(text)
    file_read(way)



current_dir = os.path.dirname(os.path.abspath(__file__))
way = os.path.join(current_dir, 'Notes.csv')



header = ['ID',
           'DATE',
           'TITLE',
           'NOTE']