'''
libmanager is a Library management software for schools, colleges or public libraries.
created by - Gitanshu Sankhla
date - 25 oct 2022
github - https://github.com/gitanshu18/libmanager

*NOTE: this file only contains backend elements and functionality of project. Frontend file is app.py .

'''

import tkinter
import mysql.connector as ms
from tkinter import *
from tkinter import messagebox,ttk
import datetime as dt
from fpdf import FPDF

# connecting sql database and creating cursor

db = ms.connect(
    host='localhost',
    user='root',
    password='',
    database='libman'
)

if db.is_connected():
    print('database connected.')
else:
    print("error while connecting database.")
    
cur = db.cursor()

# function to add data from entry fields to database.
def add_data(tree,libbookname, libauthor, lissueddate, lreturnexp, lissuedby, lissuerclass, lreturnact, lmobile,lprn):
    try:
        qry = 'insert into libdata(bookname, author, issued_date, exp_return, issued_by, issuer_class, return_act, mobile, PRN_No)'+'values("{}","{}","{}","{}","{}","{}","{}",{}, {})'.format(libbookname, libauthor, lissueddate, lreturnexp, lissuedby, lissuerclass, lreturnact, lmobile,lprn)
        cur.execute(qry)
        db.commit()
        record= [libbookname, libauthor, lissueddate, lreturnexp, lissuedby, lissuerclass, lreturnact, lmobile, lprn]
        # adding data to tree
        
        # getting last index
        count = len(tree.get_children())-1
        tree.insert('', count,iid=record[8] ,text='',values=(record[8],record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
        
        messagebox.showinfo('db', 'data inserted successfully to database.')
         # removing all items form tree
        for item in tree.get_children():
            tree.delete(item)
        # adding updating items in treeview
        cur.execute("select * from libdata")
        data = cur.fetchall()
        upt_count = 0
        for record in data:
            tree.insert('', upt_count,iid=record[8] ,text='',values=(record[8],record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
            upt_count =+1
    except ms.errors.IntegrityError as ex:
        messagebox.showerror("duplicacy error","PRN already exist.\n {}".format(ex))  
        print(ex)
    
#  function to preview the data in textbox 
def preview_data(widget, libbookname, libauthor, lissueddate, lreturnexp, lissuedby, lissuerclass, lreturnact, lmobile, lprn):
    widget.delete(1.0,END)
    data = '''
        NATIONAL PUBLIC LIBRARY
        
    Book : {}
    Author : {}
    Issue on : {}
    Must return on: {}
    Issuer name : {}
    Issuer class : {}
    Actual return on : {}
    Mobile no. : {}
    PRN No. : {}
    '''.format(libbookname, libauthor, lissueddate, lreturnexp, lissuedby, lissuerclass, lreturnact, lmobile, lprn)
    widget.insert(END, data)
    
# function to delete data from tree and database
def del_data(tree,bookname, author, issued_date, return_exp, issued_by, issuer_class,return_act, mobile,prn):
    try:
        qry = 'delete from libdata where PRN_No = {}'.format(prn)
        cur.execute(qry)
        db.commit()
        tree.delete(prn)
        bookname.delete(0,END)
        author.delete(0,END)
        issued_date.delete(0,END)
        return_exp.delete(0,END)
        issued_by.delete(0,END)
        issuer_class.delete(0,END)
        return_act.delete(0,END)
        mobile.delete(0,END)
        
        messagebox.showinfo('db', 'data deleted successfully.')
    except tkinter.TclError:
        messagebox.showerror("error","data does not exist.")
    
# function to update record in database and also in tree
def update_data(tree,libbookname, libauthor, lissueddate, lreturnexp, lissuedby, lissuerclass, lreturnact, lmobile, lprn):
    # updating item in db
    qry = 'update libdata set bookname = "{}", author = "{}", issued_date = "{}", exp_return = "{}", issued_by = "{}", issuer_class = "{}", return_act = "{}", mobile = {} where PRN_No = {}'.format(libbookname, libauthor, lissueddate, lreturnexp, lissuedby, lissuerclass, lreturnact, lmobile,lprn)
    cur.execute(qry)
    db.commit()
    messagebox.showinfo('db', 'data updated successfully in database.')
    # removing all items form tree
    for item in tree.get_children():
      tree.delete(item)
    # adding updating items in treeview
    cur.execute("select * from libdata")
    data = cur.fetchall()
    count = 0
    for record in data:
        tree.insert('', count,iid=record[8] ,text='',values=(record[8],record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
        count =+1
    
# function to retrieve data from database to input widget using PRN no.
def fetch(widget,libbookname, libauthor, lissueddate, lreturnexp, lissuedby, lissuerclass, lreturnact, lmobile, lprn):
    # checking prn validity
    prns = []
    cur.execute('select PRN_No from libdata')
    for i in cur:
        for k in i:
            prns.append(k)
    if int(lprn) in prns:
        qry = 'select * from libdata where PRN_No = {}'.format(lprn)
        cur.execute(qry)
        data = []
        for item in cur:
            for i in item:
                data.append(i)
        libbookname.delete(0,END)
        libauthor.delete(0,END)
        lissueddate.delete(0,END)
        lreturnexp.delete(0,END)
        lissuedby.delete(0,END)
        lissuerclass.delete(0,END)
        lreturnact.delete(0,END)
        lmobile.delete(0,END)
        
        libbookname.insert(END,data[0])
        libauthor.insert(END,data[1])
        lissueddate.insert(END,data[2])
        lreturnexp.insert(END,data[3])
        lissuedby.insert(END,data[4])
        lissuerclass.insert(END,data[5])
        lreturnact.insert(END,data[6])
        lmobile.insert(END,data[7])
        
        widget.delete(1.0,END)
        predata = '''
              NATIONAL PUBLIC LIBRARY

        Book : {}
        Author : {}
        Issue on : {}
        Must return on: {}
        Issuer name : {}
        Issuer class : {}
        Actual return on : {}
        Mobile no. : {}
        PRN No. : {}
        '''.format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],lprn)
        widget.insert(END, predata)
    else:
        messagebox.showerror('Fetch error', "PRN does'nt exist.")
    
# function to clear preview and inputs.
def clearpre(widget,libbookname, libauthor, lissuedby, lissuerclass, lreturnact, lmobile, lprn):
    widget.delete(1.0, END)
    libbookname.delete(0,END)
    libauthor.delete(0,END)
    lissuedby.delete(0,END)
    lissuerclass.delete(0,END)
    lreturnact.delete(0,END)
    lmobile.delete(0,END)
    lprn.delete(0,END)

# function to make receipt for late fine 
def makereceipt(libbookname, libauthor, lissueddate, lreturnexp, lissuedby, lissuerclass, lreturnact, lmobile, lprn):
    import os 
    # total fine calculating algorithm
    raiseby = 10
    expectedreturn = dt.datetime.strptime(lreturnexp, "%d/%m/%Y")
    actual_return = dt.datetime.strptime(lreturnact, "%d/%m/%Y")
    delta = actual_return - expectedreturn 
    print(delta)
    if delta.days < 0:
        fine = 0
    else:
        fine =  delta.days*raiseby
    
    # making pdf  
    width = 21
    height = 14.85

    pdf = FPDF('L',"cm","A5")
    pdf.set_margins(1.0,1.0,1.0)
    pdf.add_page()
    # making page border using rectangle function
    pdf.rect(1,1,width-2, height-6)

    pdf.add_font('alger', '', "C:\\Windows\\Fonts\\ALGER.ttf")
    pdf.set_font('alger', '', 23)
    pdf.text(5.5,2,'NATIONAL PUBLIC LIBRARY')
    pdf.set_font('times', "", 16)
    pdf.text(8.4,2.6,"Receipt for late fine")
    # personal details
    pdf.set_font('times', "", 12)
    pdf.text(2,4,"Name :")
    pdf.text(2,4.5,"Class :")
    pdf.text(2,5,"Mobile :")
    pdf.text(2,5.5,"PRN NO. :")

    pdf.text(4,4,lissuedby.capitalize())
    pdf.text(4,4.5,lissuerclass)
    pdf.text(4,5,lmobile)
    pdf.text(4,5.5,lprn)


    # book details
    pdf.text(10,4,"Book :")
    pdf.text(10,4.5,"Author :")

    pdf.text(12,4,libbookname.capitalize())
    pdf.text(12,4.5,libauthor.capitalize())

    # issue details
    pdf.text(7,6,"Borrowing Period:  "+lissueddate+" - "+ lreturnact)
    pdf.text(8.2,6.8,"Expected Return: "+lreturnexp)
    if delta.days > 0:
        pdf.text(6,8,"You have been charge for late return of book by {} days.".format(delta.days))
    else:
        pdf.text(8,8,"You have return book on time")
    pdf.text(9,9,"Total fine:"+ str(fine))
    # giving name to pdf and creating it in working directory
    pdf.output("receipts/{}{}.pdf".format(lprn,lissuedby))
    # opening receipts
    os.system('cmd /c "cd receipts & start {}{}.pdf"'.format(lprn,lissuedby))

# retrieve data from database and show it to rows of tree.
def showdatatotree(tree):
    cur.execute("select * from libdata")
    data = cur.fetchall()
    count = 0
    for record in data:
        tree.insert('', count,iid=record[8] ,text='',values=(record[8],record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]))
        count +=1
    