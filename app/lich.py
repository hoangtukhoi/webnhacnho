from tkinter import *
from tkcalendar import Calendar
import datetime

root = Tk()
root.geometry("450x450")
x = datetime.datetime.now()
lich = Calendar(root,locale='vi_VN',font = ("Times New Roman", 18), selectmode = 'day',
			year = x.year, month = x.month,
			day = x.day)

lich.pack(pady = 10)
def show_date():
    selected_date = lich.get_date()
    print(selected_date)


# Tạo một nút để hiển thị ngày được chọn
btn = Button(root ,text="Chọn ngày", command=show_date)
btn.pack()
root.mainloop()