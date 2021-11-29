import datetime
from tkinter import *
from  tkinter import ttk
from tkinter import messagebox
import numpy
import csv
import string
import tkinter.filedialog as filedialog

screen = Tk()
screen.geometry("950x500")
screen. resizable(width=False, height=False)
screen.title(" Phần mềm quản lí học sinh trường L")
screen.iconbitmap('icon.ico')

#Row 0
titleLabel = Label(screen)
titleLabel.grid(columnspan = "13", row = "0", padx=5, pady=(5,0))
titleLabel.config(text = "QUẢN LÍ HỌC SINH", font=("Segoe UI bold",15))

#Table row 1

table_frame = Frame(screen)
table_frame.grid(columnspan = "13", row = "1", padx=(30,0), pady=5)

tableScroll = Scrollbar(table_frame)
tableScroll.grid(row = "1", column = "8", sticky = "nsew")

tableData = ttk.Treeview(table_frame)

tableData['columns'] = ('stt', 'name', 'class', 'age', 'toan', 'van', 'anh', 'diemTB')
tableData.grid(row=1, column=0, columnspan=5, rowspan=5, padx=5, pady=5)

tableData.column("#0", width=0,  stretch=NO)
tableData.column("stt",anchor=CENTER, width=78)
tableData.column("name",anchor=CENTER, width=200)
tableData.column("class",anchor=CENTER, width=100)
tableData.column("age",anchor=CENTER, width=100)
tableData.column("toan",anchor=CENTER, width=100)
tableData.column("van",anchor=CENTER, width=100)
tableData.column("anh",anchor=CENTER, width=100)
tableData.column("diemTB",anchor=CENTER, width=110)


tableData.heading("#0",text="",anchor=CENTER)
tableData.heading("stt",text="STT",anchor=CENTER)
tableData.heading("name",text="Tên",anchor=CENTER)
tableData.heading("class",text="Lớp",anchor=CENTER)
tableData.heading("age",text="Tuổi",anchor=CENTER)
tableData.heading("toan",text="Điểm Toán",anchor=CENTER)
tableData.heading("van",text="Điểm Văn",anchor=CENTER)
tableData.heading("anh",text="Điểm Anh",anchor=CENTER)
tableData.heading("diemTB",text="Điểm TB",anchor=CENTER)


global count
data = []
count=0

def dtb():
    return round(float(float(toan_entry.get())+float(van_entry.get())+float(anh_entry.get()))/3, 2)

def inputData():
    global count
    tuoi = age_entry.get()
    nameCheck = name_entry.get()
    if float(toan_entry.get()) >10 or float(van_entry.get()) >10 or float(anh_entry.get()) >10 or float(toan_entry.get()) <0 or float(van_entry.get()) <0 or float(anh_entry.get()) <0:
        messagebox.showerror('Lỗi', 'Điểm không hợp lệ')
    elif isinstance(tuoi,int) == False or int(tuoi) < 0:
        messagebox.showerror('Lỗi', 'Tuổi không hợp lệ')
    else:
        tableData.insert(parent='',index='end',iid = count,text='',values=(stt_entry.get(), name_entry.get(), class_entry.get(), age_entry.get(), toan_entry.get(), van_entry.get(), anh_entry.get(), dtb()))
    
        count += 1

        data.append([stt_entry.get(), name_entry.get(), class_entry.get(), age_entry.get(), toan_entry.get(), van_entry.get(), anh_entry.get(), dtb()])

        stt_entry.delete(0,END)
        name_entry.delete(0,END)
        class_entry.delete(0,END)
        age_entry.delete(0,END)
        toan_entry.delete(0,END)
        van_entry.delete(0,END)
        anh_entry.delete(0,END)

def ExportData():
    global data

    Headers = ['stt', 'name', 'class', 'age', 'toan', 'van', 'anh', 'diemTB']

    dataWithHeaders = data
    dataWithHeaders.insert(0, Headers)
    dataCSV = numpy.array(dataWithHeaders)
    with open('Database/data.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(dataCSV)

def LoadData():
    global data, tableData, count
    count = 0

    path = filedialog.askopenfile()

    with open(path.name, 'r', newline='') as file:
        CSVdata = csv.reader(file, delimiter=',')
        for rows in CSVdata:
            data.append(rows)
        data.pop(0)
        
    for i in data:
        tableData.insert(parent='',index='end',iid = count,text='',values=(i[0], i[1],i[2] ,i[3], i[4], i[5], i[6], i[7]))
        count +=1

def deleteData():
    messagebox.askyesno('Ditmemay ấn cl', 'Cái này chưa code ấn cl à, code giúp tao với?')

Input_frame = Frame(screen)
Input_frame.grid(columnspan = "13", row = "2", padx=(10,0), pady=0)

menuLabel = Label(Input_frame, text = "MENU", font=("Segoe UI Bold",15))
menuLabel.grid(columnspan = "13", row = "2", padx=5, pady=5)

stt = Label(Input_frame,text="STT", font=("Segoe UI",10))
stt.grid(row=3,column=0,padx=5,pady=0)

name = Label(Input_frame,text="Tên", font=("Segoe UI",10))
name.grid(row=3,column=1,padx=5,pady=0)

className = Label(Input_frame,text="Lớp", font=("Segoe UI",10))
className.grid(row=3,column=2,padx=5,pady=0)

age = Label(Input_frame,text="Tuổi", font=("Segoe UI",10))
age.grid(row=3,column=3,padx=5,pady=0)

toan = Label(Input_frame,text="Điểm Toán", font=("Segoe UI",10))
toan.grid(row=3,column=4,padx=5,pady=0)

van = Label(Input_frame,text="Điểm Văn", font=("Segoe UI",10))
van.grid(row=3,column=5,padx=5,pady=0)

anh = Label(Input_frame,text="Điểm Anh", font=("Segoe UI",10))
anh.grid(row=3,column=6,padx=5,pady=0)

stt_entry = Entry(Input_frame, borderwidth=2, width = "6", font=("Segoe UI",12), justify="center", relief="groove")
stt_entry.grid(row=4,column=0,padx=3,pady=0)

name_entry = Entry(Input_frame,borderwidth=2, width = "33", font=("Segoe UI",12), justify="right", relief="groove")
name_entry.grid(row=4,column=1,padx=5,pady=0)

class_entry = Entry(Input_frame,borderwidth=2, width = "7", font=("Segoe UI",12), justify="center", relief="groove")
class_entry.grid(row=4,column=2,padx=5,pady=0)

age_entry = Entry(Input_frame,borderwidth=2, width="7", font=("Segoe UI",12), justify="center", relief="groove")
age_entry.grid(row=4,column=3,padx=5,pady=0)

toan_entry = Entry(Input_frame,borderwidth=2, width="7", font=("Segoe UI",12), justify="center", relief="groove")
toan_entry.grid(row=4,column=4,padx=5,pady=0)

van_entry = Entry(Input_frame,borderwidth=2, width="7", font=("Segoe UI",12), justify="center", relief="groove")
van_entry.grid(row=4,column=5,padx=5,pady=0)

anh_entry = Entry(Input_frame,borderwidth=2, width="7", font=("Segoe UI",12), justify="center", relief="groove")
anh_entry.grid(row=4,column=6,padx=5,pady=0)

Add_button = Button(Input_frame, text="Add", font=("Segoe UI",12), command=inputData, relief=GROOVE, justify="center", bd=2,width = 10)
Add_button.grid(row=4,column=7,columnspan=2,padx=0,pady=5)

Export_button = Button(Input_frame, width = 10, text = "Export", command = ExportData, font=("Segoe UI",12), relief=GROOVE, justify="center", bd=2)
Export_button.grid(row=5,column=7,columnspan=2,padx=0,pady=5)

Input_button = Button(Input_frame,width = 10, text = "Import",command= LoadData, font=("Segoe UI",12), relief=GROOVE, justify="center", bd=2)
Input_button.grid(row=5,column=5,columnspan=2,padx=5,pady=0)

Search_button = Button(Input_frame,width = 10, text = "Search", font=("Segoe UI",12), relief=GROOVE, justify="center", bd=2, command = deleteData)
Search_button.grid(row=5,column=2,columnspan=2,padx=0,pady=5)

Clear_button = Button(Input_frame,width = 10, text = "Clear", font=("Segoe UI",12), relief=GROOVE, justify="center", bd=2, command = deleteData)
Clear_button.grid(row=5,column=3,columnspan=3,padx=0,pady=5)


#CopyRight Label
copyRightLabel = Label(Input_frame)
copyRightLabel.grid(columnspan = "2", column = 0, row = "5", padx=(35,0), pady=(0,5))
copyRightLabel.config(text="Copyright © Khoa Nguyễn & Quang Ngo! For educational purposes only!", font=("Segoe UI light",9),bd="0", relief=GROOVE, justify="center")
screen.mainloop()
