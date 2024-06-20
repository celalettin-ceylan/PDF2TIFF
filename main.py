from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from app import *



main_window = create_main_window(title="PDF to TIFF", geometry='400x150')

s1_frame = Frame(main_window)
s2_frame = Frame(main_window)

selected_file = StringVar()
target_directory = StringVar()

create_butons_area(window=s1_frame, selected_file=selected_file, target_directory=target_directory)
create_entries_area(window=s1_frame, selected_file=selected_file, target_directory=target_directory)
create_run_button(window=s2_frame, selected_file=selected_file, target_directory=target_directory)

s1_frame.pack(pady=(10,5), padx=5, anchor='w')
s2_frame.pack(pady=(5,5), padx=5, anchor='w')

main_window.mainloop()
