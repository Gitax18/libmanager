"""
libmanager is a Library management software for schools, colleges or public libraries.
created by - Gitanshu Sankhla
date - 25 oct 2022
github - https://github.com/gitanshu18/libmanager

*NOTE: this file only contains frontend elements of project. Backend file is functions_utilities.
"""
from functions_utilities import *
from tkinter import *
from tkinter import messagebox, ttk
import datetime as dt

# making project UI
root = Tk()

# setting root window properties
root.geometry('1300x720+10+10')
root.iconbitmap('images//icon.ico')
root.grid_propagate(False)
root.pack_propagate(False)
root.config(bg='#00d4ff')
root.title('Libmanager')

# changing notebook default style, (Removing borders)
style=ttk.Style()
style.layout("TNotebook", [])
style.configure("TNotebook", highlightbackground="#848a98",tabmargins=0)

# making notebook
nb = ttk.Notebook(root,style="TNotebook")

# creating tabs 
maintab = Frame(nb, bg="#00d4ff")
pretab = Frame(nb, bg="#00d4ff")

# adding tabs to notebook
nb.add(maintab, text="  Home  ")
nb.add(pretab, text="  Data  ")
nb.pack(fill='both')

# creating page header
heading =  Label(maintab, text="LIBMANAGER", borderwidth=1, relief=SOLID, font=("Calibri", 30, "bold"), padx=50, bg='#ff3c54', fg='#020024')
heading.pack(fill="both", pady=(0,50))

# creating main frame to store two frames one for inputs and one for treeview(user data preview)
container = Frame(maintab, bg='white')
container.pack(fill='both')
parent_width = container.winfo_width() # in px
child_widths = parent_width/2
# creating sub frames of container frame
inputframe = Frame(container, borderwidth=2, bg="#00d4ff")
inputframe.pack(side=LEFT, expand=True, fill='both')
inputframe.config(width=child_widths)

previewframe = Frame(container, borderwidth=2, bg="#00d4ff")
previewframe.pack(side=RIGHT, expand=True, fill='both')
previewframe.config(width=child_widths)

# content of inputframe

Label(inputframe, text='BOOK NAME : ', padx=5, pady=10, justify=LEFT,bg='#00d4ff',font=('Calibri', 15,'roman')).grid(row=0, column=0,padx=50)
bookname = Entry(inputframe, width=40, font=('Calibri', 15,'roman'))
bookname.grid(row=0, column=1,padx=0)

Label(inputframe, text='AUTHOR : ', padx=5, pady=10, justify=LEFT,bg='#00d4ff',font=('Calibri', 15,'roman')).grid(row=1, column=0,padx=50)
author = Entry(inputframe, width=40, font=('Calibri', 15,'roman'))
author.grid(row=1, column=1,padx=0)

Label(inputframe, text='ISSUED DATE : ', padx=5, pady=10, justify=LEFT,bg='#00d4ff',font=('Calibri', 15,'roman')).grid(row=2, column=0,padx=50)
issued_date = Entry(inputframe, width=40, font=('Calibri', 15,'roman'))
issued_date.grid(row=2, column=1,padx=0)

Label(inputframe, text='EXPECTED RETURN : ', padx=5, pady=10, justify=LEFT,bg='#00d4ff',font=('Calibri', 15,'roman')).grid(row=3, column=0,padx=50)
return_exp = Entry(inputframe, width=40, font=('Calibri', 15,'roman'))
return_exp.grid(row=3, column=1,padx=0)

Label(inputframe, text='ISSUED BY : ', padx=5, pady=10, justify=LEFT,bg='#00d4ff',font=('Calibri', 15,'roman')).grid(row=4, column=0,padx=50)
issued_by = Entry(inputframe, width=40, font=('Calibri', 15,'roman'))
issued_by.grid(row=4, column=1,padx=0)

Label(inputframe, text='ISSUER CLASS : ', padx=5, pady=10,  justify=LEFT,bg='#00d4ff',font=('Calibri', 15,'roman')).grid(row=5, column=0,padx=50)
issuer_class = Entry(inputframe, width=40, font=('Calibri', 15,'roman'))
issuer_class.grid(row=5, column=1,padx=0)

Label(inputframe, text='RETURN (ACTUAL) : ', padx=5, pady=10, justify=LEFT,bg='#00d4ff',font=('Calibri', 15,'roman')).grid(row=6, column=0,padx=50)
return_act= Entry(inputframe, width=40, font=('Calibri', 15,'roman'))
return_act.grid(row=6, column=1,padx=0)

Label(inputframe, text='MOBIlE NO. : ', padx=5, pady=10, justify=LEFT,bg='#00d4ff',font=('Calibri', 15,'roman')).grid(row=7, column=0,padx=50)
mobile = Entry(inputframe, width=40, font=('Calibri', 15,'roman'))
mobile.grid(row=7, column=1,padx=0)

Label(inputframe, text='PRN NO. : ', padx=5, pady=10, justify=LEFT,bg='#00d4ff',font=('Calibri', 15,'roman')).grid(row=8, column=0,padx=50)
prn = Entry(inputframe, width=40, font=('Calibri', 15,'roman'))
prn.grid(row=8, column=1,padx=0)

# changing entry border
bookname.config(borderwidth=2, relief=SOLID)
author.config(borderwidth=2, relief=SOLID)
issued_date.config(borderwidth=2, relief=SOLID)
return_exp.config(borderwidth=2, relief=SOLID)
issued_by.config(borderwidth=2, relief=SOLID)
issuer_class.config(borderwidth=2, relief=SOLID)
return_act.config(borderwidth=2, relief=SOLID)
mobile.config(borderwidth=2, relief=SOLID)
prn.config(borderwidth=2, relief=SOLID)

# contents of preview frame.
preview_scroll = Scrollbar(previewframe)
preview_scroll.pack(side=RIGHT, fill=Y)

preview = Text(previewframe, yscrollcommand=preview_scroll.set ,bg="#ffffff", fg='#000000', width=40, height=13, font=("Calibri", 16, 'bold'), bd=3, relief=SOLID)
preview.pack(padx=150)
preview_scroll.config(command=preview.yview)

btnframe = Frame(maintab, height=20, bd=3, bg='#00d4ff')
btnframe.pack(pady=10)

# Buttons (add data, preview data, delete data, update data, download receipt)
add_data_btn = Button(btnframe, text="Add Data", height=2, width=13, padx=5, command=lambda: add_data(tree,bookname.get(),author.get(),issued_date.get(), return_exp.get(), issued_by.get(), issuer_class.get(),return_act.get(), mobile.get(),prn.get()))
add_data_btn.grid(row=0, column=0, padx=20, pady=30)

pre_data_btn = Button(btnframe, text="Preview Data", height=2, width=13, padx=5, command=lambda: preview_data(preview,bookname.get(),author.get(),issued_date.get(), return_exp.get(), issued_by.get(), issuer_class.get(),return_act.get(), mobile.get(),prn.get()))
pre_data_btn.grid(row=0, column=1, padx=20, pady=30)

del_data_btn = Button(btnframe, text="Delete Data", height=2, width=13, padx=5, command=lambda: del_data(tree,bookname, author, issued_date, return_exp, issued_by, issuer_class,return_act, mobile,prn.get()))
del_data_btn.grid(row=0, column=2, padx=20, pady=30)

upd_data_btn = Button(btnframe, text="Update Data", height=2, width=13, padx=5, command=lambda: update_data(tree,bookname.get(),author.get(),issued_date.get(), return_exp.get(), issued_by.get(), issuer_class.get(),return_act.get(), mobile.get(),prn.get()))
upd_data_btn.grid(row=0, column=3, padx=20, pady=30)

fetch_btn = Button(btnframe, text="Fetch Data", height=2, width=13, padx=5, command=lambda: fetch(preview,bookname,author,issued_date, return_exp, issued_by, issuer_class,return_act, mobile,prn.get()))
fetch_btn.grid(row=0, column=4, padx=20, pady=30)

clr_btn = Button(btnframe, text="Clear Preview", height=2, width=13, padx=5, command=lambda: clearpre(preview,bookname,author, issued_by, issuer_class,return_act, mobile,prn) )
clr_btn.grid(row=0, column=5, padx=20, pady=30)

down_rec_btn = Button(btnframe, text="Download Receipt", height=2, width=13, padx=5, command=lambda: makereceipt(bookname.get(),author.get(),issued_date.get(), return_exp.get(), issued_by.get(), issuer_class.get(),return_act.get(), mobile.get(),prn.get()))
down_rec_btn.grid(row=0, column=6, padx=20, pady=30)

# setting defaults values of issue date and expected return date.
issuedate = dt.date.today().strftime("%d/%m/%Y")
returndate = dt.datetime.strptime(issuedate, '%d/%m/%Y') + dt.timedelta(days=7)

issued_date.insert(0, issuedate)
return_exp.insert(0, returndate.strftime('%d/%m/%Y'))

# Creating content for Data Tab.

# making treeview to show tabular data retrieving from database
# making scrollbar for tree
tree_scroll = Scrollbar(pretab)
tree_scroll.pack(side=RIGHT, fill=Y)
# making columns identities 
columns = ('PNR','bookname', 'author', 'issued-date', 'exp-return', 'issued-by', 'issuer-class', 'act-return', 'mobile')
# creating treeview widget
tree = ttk.Treeview(pretab, height=30, show='headings', columns=columns, yscrollcommand=tree_scroll.set, selectmode=BROWSE)
tree_scroll.config(command=tree.yview)

# making columns in our widget
tree.column('PNR', width=15,minwidth=15, anchor=CENTER)
tree.column('bookname', width=15,minwidth=15, anchor=CENTER)
tree.column('author', width=15,minwidth=15, anchor=CENTER)
tree.column('issued-date', width=15,minwidth=15, anchor=CENTER)
tree.column('exp-return', width=15,minwidth=15, anchor=CENTER)
tree.column('issued-by', width=15,minwidth=15, anchor=CENTER)
tree.column('issuer-class', width=15,minwidth=15, anchor=CENTER)
tree.column('act-return', width=15,minwidth=15, anchor=CENTER)
tree.column('mobile', width=15,minwidth=15, anchor=CENTER)

# giving headings to above created columns
tree.heading('PNR', text='PNR')
tree.heading('bookname', text='Bookname')
tree.heading('author', text='Author')
tree.heading('issued-date', text='Issued on')
tree.heading('exp-return', text='Return (Expected)')
tree.heading('issued-by', text='Issuer Name')
tree.heading('issuer-class', text='Issuer Class')
tree.heading('act-return', text='Return (Actual)')
tree.heading('mobile', text='Mobile')

def ondoubleclick(event):
    global tree 
    item = tree.focus()
    print(item)
    values = tree.item(item,'values')
    
    bookname.delete(0,END)
    author.delete(0,END)
    issued_date.delete(0,END)
    return_exp.delete(0,END)
    issued_by.delete(0,END)
    issuer_class.delete(0,END)
    return_act.delete(0,END)
    mobile.delete(0,END)
    prn.delete(0,END)
    
    prn.insert(0,values[0])
    bookname.insert(0,values[1])
    author.insert(0,values[2])
    issued_date.insert(0,values[3])
    return_exp.insert(0,values[4])
    issued_by.insert(0,values[5])
    issuer_class.insert(0,values[6])
    return_act.insert(0,values[7])
    mobile.insert(0,values[8])
    
    messagebox.showinfo("", "Data added to home tab successfully.")
    
tree.bind("<Double-1>", ondoubleclick)
tree.pack(side=TOP, fill='both')
# adding rows to treeview
showdatatotree(tree=tree)

root.mainloop()