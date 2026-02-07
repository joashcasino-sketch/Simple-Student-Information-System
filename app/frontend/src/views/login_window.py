from tkinter import *
from PIL import Image, ImageTk

login = Tk()

#login window behaviour
login.geometry('1280x750')
login.resizable(False, False)
login.title('Sign in/Sign up')
login.configure(bg="#FFFFFF")

bg_image = Image.open("app/frontend/assets/bg.jpg")
bg_image = bg_image.resize((1680, 900))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(login, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame properties for the labels and entry
frame = Frame(login, width=500, height=500, bg='#85586F')
frame.place(relx=0.5, rely=0.5, anchor='center')    # Centers the frame
frame.grid_propagate(False)

#widgets within login window 
login_label = Label(frame, text='Welcome', font=('Roboto', 30, 'bold'), bg='#85586F', fg='#F8ECD1')
username_label = Label(frame, text='Username: ', font=('Times New Roman', 16), bg='#85586F', fg='#F8ECD1')
username_entry = Entry(frame, font=('Roboto', 16))
password_label = Label(frame, text='Password: ', font=('Times New Roman', 16), bg='#85586F', fg='#F8ECD1')
password_entry = Entry(frame, show='*', font=('Roboto', 16))
sign_in_button = Button(frame, text='Sign in', bg='#DEB6AB', fg="#000000")
sign_up_button = Button(frame, text='Sign up', bg='#DEB6AB', fg="#000000")

#Placement
login_label.grid(row=0, column=1)
username_label.grid(row=1, column=0, pady=10, sticky='e')
username_entry.grid(row=1, column=1, pady=10)
password_label.grid(row=2, column=0, pady=10, sticky='e')
password_entry.grid(row=2, column=1, pady=10)
sign_in_button.grid(row=3, column=1, pady=30)
sign_up_button.grid(row=3, column=0, pady=30)

login.mainloop()