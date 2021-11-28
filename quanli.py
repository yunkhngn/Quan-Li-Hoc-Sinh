#Đề: Quản lý học sinh
#            tên 
#           tuổi
#          lớp 
#            điểm toán, văn anh 
#        fuc: tính điểm trung bình 
#             tính năm sinh 

# import os
# clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
# clearConsole()
# #Clear console cho nó gọn

import datetime
from tkinter import *
from  tkinter import ttk


class Students:
    def __init__(self,stt, name, age, className, toan, van, anh):
        self.stt = stt
        self.name = name
        self.age = age
        self.className = className
        self.toan = toan
        self.van = van
        self.anh = anh
        
    def tinhTrungBinh(self):
        self.diemTrungBinh = (self.toan+self.van+self.anh)/3
        return self.diemTrungBinh
    
    def tinhNamSinh(self):
        x=datetime.datetime.now()
        self.namSinh= x.year - self.age
        return self.namSinh 


HocSinh = []

def NhapHocSinh():
    SoHocSinh = int(input('So hoc sinh: '))

    for i in range(SoHocSinh):
        STT = i+1
        Ten = str(input("Nổ cái tên: "))
        Tuoi = int(input("Tuổi? :"))
        Lop = str(input("Học lớp nào???: "))
        Toan = float(input("Điểm toán:  "))
        Van = float(input("Điểm văn: "))
        Anh = float(input("Điểm anh: "))
        print("")

        HocSinh.append(Students(STT, Ten, Tuoi, Lop, Toan,Van, Anh))

def LayHocSinh():
    HocSinhMuonCheck = int(input("Nhập số thứ tự: ")) - 1
    print("")
    print("Muốn lấy thông tin nào: ")
    print("[1] Tên")
    print("[2] Tuổi")
    print("[3] Lớp")
    print("[4] Điểm trung bình")
    print("[5] Năm sinh")
    option = int(input("Lựa chọn của bạn: "))
    print("")

    if option == 1:
        print(HocSinh[HocSinhMuonCheck].name)
    if option == 2:
        print(HocSinh[HocSinhMuonCheck].age)
    if option == 3:
        print(HocSinh[HocSinhMuonCheck].className)
    if option == 4:
        print(HocSinh[HocSinhMuonCheck].tinhTrungBinh())
    if option == 5:
        print(HocSinh[HocSinhMuonCheck].tinhNamSinh())

# while True:
#     print("[1] Nhập học sinh [2] Lấy học sinh")
#     luaChon = int(input("Lựa chọn của bạn: "))

#     if luaChon == 1:
#         NhapHocSinh()
#     if luaChon == 2:
#         LayHocSinh()

screen = Tk()
screen.geometry("950x500")
screen.maxsize(950, 450)
screen.minsize(950, 450)
screen.title("Phần mềm quản lí học sinh trường L")

#Row 0
titleLabel = Label(screen)
titleLabel.grid(columnspan = "13", row = "0", padx=5, pady=5)
titleLabel.config(text = "QUẢN LÍ HỌC SINH", font=("Segoe UI bold",15))

#Table row 1

game_frame = Frame(screen)
game_frame.grid(columnspan = "13", row = "1", padx=(30,0), pady=5)

tableData = ttk.Treeview(game_frame)

tableData['columns'] = ('stt', 'name', 'class', 'age', 'toan', 'van', 'anh', 'diemTB')

tableData.column("#0", width=0,  stretch=NO)
tableData.column("stt",anchor=CENTER, width=70)
tableData.column("name",anchor=CENTER, width=200)
tableData.column("class",anchor=CENTER, width=100)
tableData.column("age",anchor=CENTER, width=100)
tableData.column("toan",anchor=CENTER, width=100)
tableData.column("van",anchor=CENTER, width=100)
tableData.column("anh",anchor=CENTER, width=100)
tableData.column("diemTB",anchor=CENTER, width=100)


tableData.heading("#0",text="",anchor=CENTER)
tableData.heading("stt",text="STT",anchor=CENTER)
tableData.heading("name",text="Tên",anchor=CENTER)
tableData.heading("class",text="Lớp",anchor=CENTER)
tableData.heading("age",text="Tuổi",anchor=CENTER)
tableData.heading("toan",text="Điểm Toán",anchor=CENTER)
tableData.heading("van",text="Điểm Văn",anchor=CENTER)
tableData.heading("anh",text="Điểm Anh",anchor=CENTER)
tableData.heading("diemTB",text="Điểm TB",anchor=CENTER)

tableData.insert(parent='', index='end', iid=0, text='',
values=(1, 'Nguyễn Minh Đức', 'Lớp 11D0', '12', '10', '10', '10', '10'))

def insertData():
    stt =sttEntry.get()
    HocSinh[stt].name = nameEntry.get()
    HocSinh[stt].age = ageEntry.get()
    HocSinh[stt].className = classEntry.get()
    HocSinh[stt].toan = toanEntry.get()
    HocSinh[stt].van = vanEntry.get()
    HocSinh[stt].anh = anhEntry.get()
    HocSinh[stt].tinhTrungBinh()
    tableData.insert(parent='',index='end',iid=stt,text='',
    values=(HocSinh[stt].stt, str(HocSinh[stt].name), HocSinh[stt].className, HocSinh[stt].age, HocSinh[stt].toan, HocSinh[stt].van, HocSinh[stt].anh, HocSinh[stt].tinhTrungBinh()))

tableData.grid(row=1, column=0, columnspan=5, rowspan=5, padx=5, pady=5)
        
#Row 2
searchButton = Button(screen, width=7)
searchButton.grid(column = "0", row = "2", padx=(35,0), pady=(7,0))
searchButton.config(text="Search", font=("Segoe UI",12), relief=GROOVE, justify="center")

sttEntry = Entry(screen, width= "7")
sttEntry.grid(column = "1", row = "2", padx=0, pady=(7,0))
sttEntry.config(text="Stt", font=("Segoe UI",12), relief=GROOVE, justify="center")

nameEntry = Entry(screen, width= "25")
nameEntry.grid(column = "2", row = "2", padx=0, pady=(7,0))
nameEntry.config(text="Tên", font=("Segoe UI",12), relief=GROOVE, justify="center")

ageEntry = Entry(screen, width= 6)
ageEntry.grid(column = "3", row = "2", padx=0, pady=(7,0))
ageEntry.config(text="Tuổi", font=("Segoe UI",12), relief=GROOVE, justify="center")

classEntry = Entry(screen, width= 15)
classEntry.grid(column = "4", row = "2", padx=0, pady=(7,0))
classEntry.config(text="Lớp", font=("Segoe UI",12), relief=GROOVE, justify="center")

toanEntry = Entry(screen, width= 10)
toanEntry.grid(column = "5", row = "2", padx=0, pady=(7,0))
toanEntry.config(text="Toán", font=("Segoe UI",12), relief=GROOVE, justify="center")

vanEntry = Entry(screen, width= 10)
vanEntry.grid(column = "6", row = "2", padx=0, pady=(7,0))
vanEntry.config(text="Văn", font=("Segoe UI",12), relief=GROOVE, justify="center")

anhEntry = Entry(screen, width= 10)
anhEntry.grid(column = "7", row = "2", padx=0, pady=(7,0))
anhEntry.config(text="Anh", font=("Segoe UI",12), relief=GROOVE, justify="center")

#Row 3
exportLabel = Button(screen, width= "7")
exportLabel.grid(column = "0", row = "3", padx=(35,0), pady=(7,0))
exportLabel.config(text="Clear", font=("Segoe UI",12), relief=GROOVE, justify="center")

inputButton = Button(screen, width=7,)
inputButton.grid(column = "1", row = "3", padx=0, pady=(7,0))
inputButton.config(text="Input", font=("Segoe UI",12), relief=GROOVE, justify="center", command = insertData)

nameLabel = Label(screen, width= "25")
nameLabel.grid(column = "2", row = "3", padx=0, pady=(7,0))
nameLabel.config(text="Tên", font=("Segoe UI",12), relief=GROOVE, justify="center")

ageLabel = Label(screen, width= 6)
ageLabel.grid(column = "3", row = "3", padx=0, pady=(7,0))
ageLabel.config(text="Tuổi", font=("Segoe UI",12), relief=GROOVE, justify="center")

classLabel = Label(screen, width= 15)
classLabel.grid(column = "4", row = "3", padx=0, pady=(7,0))
classLabel.config(text="Lớp", font=("Segoe UI",12), relief=GROOVE, justify="center")

toanLabel = Label(screen, width= 10)
toanLabel.grid(column = "5", row = "3", padx=0, pady=(7,0))
toanLabel.config(text="Toán", font=("Segoe UI",12), relief=GROOVE, justify="center")

vanLabel = Label(screen, width= 10)
vanLabel.grid(column = "6", row = "3", padx=0, pady=(7,0))
vanLabel.config(text="Văn", font=("Segoe UI",12), relief=GROOVE, justify="center")

anhLabel = Label(screen, width= 10)
anhLabel.grid(column = "7", row = "3", padx=0, pady=(7,0))
anhLabel.config(text="Anh", font=("Segoe UI",12), relief=GROOVE, justify="center")

#CopyRight Label
copyRightLabel = Label(screen)
copyRightLabel.grid(columnspan = "13", row = "4", padx=(35,0), pady=(30,0))
copyRightLabel.config(text="Copyright © Khoa Nguyễn, supported by Copilot!", font=("Segoe UI light",10),bd="0", relief=GROOVE, justify="center")

screen.mainloop()
