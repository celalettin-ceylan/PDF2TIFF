from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from imageextract import pdf_to_tiff

def select_file(vars: StringVar):
    selectedFile = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[('pdf file', '*.pdf')])
    vars.set(selectedFile)

def select_directory(vars: StringVar):
    selectedDirectory = filedialog.askdirectory()
    vars.set(selectedDirectory)

def create_main_window(title="PDF to Image", geometry='300x300'):
    window = Tk()
    window.title(title)
    window.geometry(geometry)
    return window

def create_butons_area(window : Frame, selected_file: StringVar, target_directory: StringVar):
    s0_column_frame = Frame(window)
    file_button = Button( s0_column_frame,
                     text="Select File", 
                     padx=3, 
                     pady=3, 
                     bg="#FF8A08", 
                     fg="#000000", 
                     command=lambda: select_file(selected_file)).pack(anchor='w', pady=(5,5))

    directory_button = Button(s0_column_frame,
                     text="Select Directory", 
                     padx=3, 
                     pady=3, 
                     bg="#FF8A08", 
                     fg="#000000", 
                     command=lambda: select_directory(target_directory)).pack(anchor='w', pady=(5,5))
    s0_column_frame.grid(row=0, column=0, ipadx=10)

def create_entries_area(window: Frame, selected_file: StringVar, target_directory: StringVar):
    s1_column_frame = Frame(window)
    file_entry = Entry(s1_column_frame,
                     textvariable=selected_file, 
                     fg="#000000",
                     border=1,
                     width=30,
                     font=("Verdana",10)).pack(ipadx=5,ipady=5, pady=(5,5))
    directory_entry = Entry(s1_column_frame,
                     textvariable=target_directory, 
                     fg="#000000",
                     border=1,
                     width=30,
                     font=("Verdana",10)).pack(ipadx=5,ipady=5, pady=(5,5))
    s1_column_frame.grid(row=0, column=1, ipadx=10)

def create_run_button(window:Frame,  selected_file: StringVar, target_directory: StringVar):
    runButton = Button(window,
                    text="Run", 
                     padx=3, 
                     pady=3, 
                     bg="#C40C0C", 
                     fg="#000000",
                     width=20,
                     command=lambda: run_job(selected_file, target_directory)).grid(row=1,column=1)

def run_job(selected_file: StringVar, target_directory: StringVar):
    str_selected_file = selected_file.get()
    str_target_directory = target_directory.get()
    pdf_to_tiff(str_selected_file, str_target_directory)
    messagebox.showinfo("PDF2TIFF", "Converting is finishing...")