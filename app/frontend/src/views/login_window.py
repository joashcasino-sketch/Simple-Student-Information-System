import sys
from pathlib import Path

# Add backend/src to path directly
backend_path = Path(__file__).resolve().parent.parent.parent.parent / "backend" / "src"
sys.path.insert(0, str(backend_path))

from tkinter import *
from PIL import Image, ImageTk
from test import handle_sign_in, handle_sign_up  # Now just import directly

login = Tk()

# Login window behaviour
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

# Widgets within login window 
login_label = Label(frame, text='Welcome', font=('Roboto', 30, 'bold'), bg='#85586F', fg='#F8ECD1')
username_label = Label(frame, text='Username: ', font=('Times New Roman', 16), bg='#85586F', fg='#F8ECD1')
username_entry = Entry(frame, font=('Roboto', 16))
password_label = Label(frame, text='Password: ', font=('Times New Roman', 16), bg='#85586F', fg='#F8ECD1')
password_entry = Entry(frame, show='*', font=('Roboto', 16))


# Callback function for successful login
def on_login_success(user_data):
    """
    Called when login is successful.
    Close login window and open main application.
    
    Args:
        user_data (dict): Dictionary containing user information
    """
    print(f"User logged in: {user_data['username']}")
    login.destroy()  # Close login window
    # TODO: Open your main application window here
    # For example: open_main_window(user_data)


# Create buttons with commands
sign_in_button = Button(
    frame, 
    text='Sign in', 
    bg='#DEB6AB', 
    fg="#000000",
    font=('Roboto', 12, 'bold'),
    cursor='hand2',
    command=lambda: handle_sign_in(username_entry, password_entry, on_login_success)
)

sign_up_button = Button(
    frame, 
    text='Sign up', 
    bg='#DEB6AB', 
    fg="#000000",
    font=('Roboto', 12, 'bold'),
    cursor='hand2',
    command=lambda: handle_sign_up(username_entry, password_entry)
)

# Placement
login_label.grid(row=0, column=1, pady=(20, 30))
username_label.grid(row=1, column=0, pady=10, padx=(10, 5), sticky='e')
username_entry.grid(row=1, column=1, pady=10, padx=(5, 10), sticky='w')
password_label.grid(row=2, column=0, pady=10, padx=(10, 5), sticky='e')
password_entry.grid(row=2, column=1, pady=10, padx=(5, 10), sticky='w')
sign_in_button.grid(row=3, column=1, pady=30, ipadx=20, ipady=5)
sign_up_button.grid(row=3, column=0, pady=30, ipadx=20, ipady=5)

# Bind Enter key to sign in
username_entry.bind('<Return>', lambda e: handle_sign_in(username_entry, password_entry, on_login_success))
password_entry.bind('<Return>', lambda e: handle_sign_in(username_entry, password_entry, on_login_success))

# Set focus to username entry on startup
username_entry.focus()

login.mainloop()