import sys
from pathlib import Path
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage

backend_path = Path(__file__).resolve().parent.parent.parent.parent / "backend" / "src"
sys.path.insert(0, str(backend_path))

from login_handler import handle_sign_in, handle_sign_up

OUTPUT_PATH = Path(__file__).resolve().parent
ASSETS_PATH = OUTPUT_PATH.parent.parent.parent / "frontend" / "assets" / "frame0"
LOGO_PATH = Path(__file__).resolve().parent.parent.parent / "assets" / "logo.png"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("409x425")
window.configure(bg = "#F8ECD1")
window.title("    Login Panel")

icon = PhotoImage(file=str(LOGO_PATH))
window.iconphoto(True, icon)

canvas = Canvas(
    window,
    bg = "#F8ECD1",
    height = 425,
    width = 409,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    204.0,
    231.0,
    image=image_image_1
)

canvas.create_text(
    30.0,
    38.0,
    anchor="nw",
    text="Welcome\n",
    fill="#000000",
    font=("Inter SemiBold", 45 * -1, "bold")
)

canvas.create_text(
    85.0,
    189.0,
    anchor="nw",
    text="username:",
    fill="#000000",
    font=("Inter Light", 13 * -1)
)

canvas.create_text(
    85.0,
    258.0,
    anchor="nw",
    text="password:\n",
    fill="#000000",
    font=("Inter Light", 13 * -1)
)

# use for later
invalid_message = Label(
    window,  # parent widget
    text="*Invalid username or password",
    fg="#FF0101",
    bg="#F8ECD1",  # Match your window background
    font=("Inter Light", 10)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_sign_in(username_entry, password_entry),
    relief="flat"
)
button_1.place(
    x=95.0,
    y=340.0,
    width=92.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_sign_up(username_entry, password_entry),
    relief="flat"
)
button_2.place(
    x=223.0,
    y=341.0,
    width=92.0,
    height=51.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    245.0,
    197.0,
    image=entry_image_1
)
username_entry = Entry(
    bd=0,
    bg="#DEB6AB",
    fg="#000716",
    highlightthickness=0
)
username_entry.place(
    x=180.0,
    y=184.0,
    width=130.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    245.0,
    267.0,
    image=entry_image_2
)
password_entry = Entry(
    bd=0,
    bg="#DEB6AB",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
password_entry.place(
    x=180.0,
    y=253.0,
    width=130.0,
    height=26.0
)

canvas.create_rectangle(
    35.0,
    113.0,
    373.0000491078099,
    114.98250744712803,
    fill="#85586F",
    outline="")
window.resizable(False, False)
window.mainloop()
