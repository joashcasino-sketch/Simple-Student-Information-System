from tkinter import *

login = Tk()

login.geometry('500x560')
login.resizable(False, False)
login.title('Sign in/Sign up')
login.configure(bg='#85586F')

login_label = Label(login, text='Welcome', font=('Times New Roman', 30), bg='#85586F', fg='#F8ECD1')
username_label = Label(login, text='Username: ', font=('Times New Roman', 16), bg='#85586F', fg='#F8ECD1')
username_entry = Entry(login, font=('Times New Roman', 16))
password_label = Label(login, text='Password: ', font=('Times New Roman', 16), bg='#85586F', fg='#F8ECD1')
password_entry = Entry(login, show='*', font=('Times New Roman', 16))
sign_in_button = Button(login, text='Sign in', bg='#DEB6AB', fg="#000000")
sign_up_button = Button(login, text='Sign up', bg='#DEB6AB', fg="#000000")

#Placement
login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
sign_in_button.grid(row=3, column=1, columnspan=3)
sign_up_button.grid(row=3, column=0, columnspan=2)


login.mainloop()