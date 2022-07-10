from pdf2image import convert_from_path
from tkinter import *
import tkinter as tk 
import tkinter.filedialog as fd 
import tkinter.messagebox as mb
from tkinter import ttk

root = tk.Tk()
root.title('Converter from pdf to png')
root.geometry('700x350')

def choose_file(): 
    filetypes = (('Pdf file', '*.pdf'), ('Any file', '*'))
    filename = fd.askopenfilename(title='Open file', initialdir='/', 
    filetypes=filetypes)
    f = filename.split("/")
    global file_name
    file_name = f[-1]
    if file_name.endswith('.pdf'):
        show_info_choose_file_selected()
        label_text_changing()
    else:
        show_info_choose_file_fail()      
    
def show_info_choose_file_selected():
        msg = 'PDF file selected!'
        mb.showinfo('Information', msg)
        
def show_info_choose_file_fail():
        msg = "PDF file didn't select!\nRepeat attempt!"
        mb.showinfo('Warning', msg)
        window_choosing_file_fail()
        
def window_choosing_file_fail():
    answer = mb.askyesno(title='Warning', message='Do you want to continue file choosing?')
    if answer:
        choose_file()
        
def label_text_changing():
    text = 'File selected!'
    label.config(text=text)
    
btn_file = tk.Button(root, text='Choose file', command=choose_file)
btn_file.grid(row=1, column=0)

label = tk.Label(root, text="File didn't select...")
label.grid(row=2, column=0)

field_text = tk.Label(root, text = 'Select quality:')
field_text.grid(row=3, column=0)

var = IntVar()
var.set(3)
btn1 = Radiobutton(text='50 dpi', variable=var, value=0)
btn1.grid(row=4, column=0)
btn2 = Radiobutton(text='100 dpi', variable=var, value=1)
btn2.grid(row=5, column=0)
btn3 = Radiobutton(text='300 dpi', variable=var, value=2)
btn3.grid(row=6, column=0)
btn4 = Radiobutton(text='500 dpi', variable=var, value=3)
btn4.grid(row=7, column=0)
btn5 = Radiobutton(text='700 dpi', variable=var, value=4)
btn5.grid(row=8, column=0)

def choose_quality():
    global quality
    if var.get() == 0:
        quality = 50
    elif var.get() == 1:
        quality = 100
    elif var.get() == 2:
        quality = 300
    elif var.get() == 3:
        quality = 500
    elif var.get() == 4:
        quality = 700
     
def converting_error_file_name():
    msg = "You didn't select file"
    mb.showinfo('Warning', msg)

def converting_error_path():
    msg = "You didn't indicate path!\nRepeat attempt!"
    mb.showinfo('Warning', msg)
    
def func_converting():
    choose_quality()
    global images, image
    images = convert_from_path(f'{file_name}', quality)
    for i, image in enumerate(images):
        image.save(f'{path}/{file_name}_({i}).png')
        pb['maximum']= len(images)
        pb['value']= i+1
        root.update()
        a = len(images)
        x = round(((i+1)/(a)*100), 1)
        text = str('{y} % done...'.format(y = x))
        label_text_pb.config(text=text)
                   
def browse_btn():
    global path
    path = str
    path = fd.askdirectory()
    if path != "":
        show_info_brose_btn()
        func_label_bnt_dir_path()
    else: 
        show_info_brose_btn_fail()
        window_choosing_path_incdicating()
        
def show_info_brose_btn():
        msg = "Path selected!"
        mb.showinfo('Warning', msg)
        
def func_label_bnt_dir_path():
    text = 'Path indicated!!'
    label_bnt_dir_path.config(text=text)

def show_info_brose_btn_fail():
        msg = "Path didn't select!"
        mb.showinfo('Warning', msg) 
        
def window_choosing_path_incdicating():
    answer = mb.askyesno(title='Warning', message='Do you want to keep indicating path?')
    if answer:
        browse_btn()

btn_dir_path = tk.Button(root, text='Indicate a folder save path', command=browse_btn)
btn_dir_path.grid(row=9, column=0)
    
label_bnt_dir_path = tk.Label(root, text="Path didn't indicate...")
label_bnt_dir_path.grid(row=10, column=0)

def func_processing_error():
    try:
        func_converting()
    except Exception as e: 
        mb.showinfo('Warning', 'Mistake: '+str(e))

"""
lbl_from = tk.Label(root, text='From')
lbl_from.grid(row=4, column=0)
digit_var1 = tk.IntVar(root, value=0)
field_from = tk.Entry(root, textvariable=digit_var1)
field_from.grid(row=4, column=1)
lbl_to = tk.Label(root, text='to')
lbl_to.grid(row=4, column=2)
digit_var2 = tk.IntVar(root, value=0)
field_to = tk.Entry(root, textvariable=digit_var2)
field_to.grid(row=4, column=3)
"""

btn_converter = tk.Button(root, text='Converting', command=func_processing_error)
btn_converter.grid(row=11, column=0)

lbl_pb = tk.Label(root, text="Progress Bar")
lbl_pb.grid(row=12, column=0)
pb = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=280, value=0)
pb.grid(row=12, column=1)
root.update()

label_text_pb = tk.Label(root, text="Progress 0%")
label_text_pb.grid(row=13, column=1)

root.mainloop()



