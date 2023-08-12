import doing
import todoing
import look


def operations():
    look.welcome()
    while(True):
        look.menu()
        match look.write_operation():
            case '0': # Exit
                look.bye()
                return
            case '1': # Create text
                text1 = doing.create_text(todoing.file_read(
                    todoing.way), look.title_input(), look.input_text_text())
                todoing.file_to_save(text1)
                look.ok_created()
                look.output_text(doing.find_text(
                    todoing.file_read(todoing.way), text1[0]))
            case '2': # Show text
                look.output_text(doing.find_text(
                    todoing.file_read(todoing.way), look.id_input()))
            case '3': # Show all textes
                look.output_all(doing.all_show(todoing.file_read(todoing.way)))
            case '4': # Show by sort date
                look.output_date(
                    doing.show_by_date(todoing.file_read(todoing.way), look.date_selected()))
            case '5': # Add text
                try:
                    text5 = doing.find_text(
                        todoing.file_read(todoing.way), look.id_input())
                    todoing.file_update(doing.add_text(todoing.file_read(
                        todoing.way), text5[0], look.title_input(), look.input_text_text()))
                    look.ok_changed()
                    look.output_text(doing.find_text(
                        todoing.file_read(todoing.way), text5[0]))
                except:
                    look.lost_id()
            case '6': # Delete text
                try:
                    todoing.file_update(doing.delete_text(
                        todoing.file_read(todoing.way), look.id_input()))
                    look.ok_deleted()
                except:
                    look.lost_id()
            case _:  # Mistake
                look.error_input()