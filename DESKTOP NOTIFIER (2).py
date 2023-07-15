from tkinter import *
from plyer import notification
from tkinter import messagebox

BG_COLOR =  "#567189"

def noti_printer():
    title_text_entry = title_entry.get()
    message_entry = msg_entry.get()
    print("hehe")
    notification.notify(title=title_text_entry,
                        message= message_entry,
                        app_name= "Desktop Notifier",
                        timeout= 10)
    window.quit()



def timer():
    title_text_entry = title_entry.get().strip()
    message_entry = msg_entry.get().strip()
    time_unit_set = time_unit.get()
    time_set = int(time_entry.get())
    if len(title_text_entry) == 0 or len(message_entry) == 0:
        messagebox.showerror(title= "Error",message=("Please dont leave any fields empty").capitalize())
    else:
        if time_unit_set == "sec":
            window.after(time_set*1000,noti_printer)
        else:
            window.after(time_set*60000,noti_printer)
            print(time_set,"gg")



window = Tk()

window.title("Desktop Notifier")
window.config(bg=BG_COLOR,width=500,height= 250)
window.resizable(False,False)

#label desktop notifier
label = Label(text=("Desktop Notifier").upper())
label.config(bg=BG_COLOR,font=("arial",15),fg="gold")
label.grid(row=0,column=0,padx=20,pady=20)

#title label
title_label = Label(text="Title : ",bg=BG_COLOR,font=("arial",20,"normal"))
title_label.grid(row=1,column=0)

#message label
msg_label = Label(text="Message :",font=("arial",20,"normal"),bg=BG_COLOR)
msg_label.grid(row=2,column=0)

#time label
time_label = Label(text="Set Time :",font=("arial",20,"normal"),bg=BG_COLOR)
time_label.grid(row=3,column=0)

#entry for title of the screen
title_entry = Entry(width=50,)
title_entry.grid(row=1,column=1,pady=20,padx=10)
title_entry.focus()

# messsage entry
msg_entry = Entry(width=50)
msg_entry.grid(row=2,column=1,padx=20,pady=20)


#time countdown spinbox
time_entry = Spinbox(width=5,from_=1,to=60,increment=1,font=("arial",15))
time_entry.grid(row=3,column=1,pady=20,padx=10)

#notification button
noti_but = Button(text="Set Notification",width=20,font=("arial",15),command=timer)
noti_but.grid(row=4,column=1,pady=20,padx=20)
noti_but.config(padx=10,borderwidth=10,relief="ridge",fg="gold",bg="#181D31")

time_unit = StringVar(value="sec")
#min radio
min_rad = Radiobutton(text="min",bg=BG_COLOR,variable=time_unit,value="min")
min_rad.place(x=450,y=210)

#sec radio
sec_rad = Radiobutton(text="sec",bg=BG_COLOR,variable=time_unit,value="sec")
sec_rad.place(x=500,y=210)

window.mainloop()