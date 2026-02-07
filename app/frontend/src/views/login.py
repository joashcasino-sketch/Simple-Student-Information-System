from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).resolve().parent
ASSETS_PATH = OUTPUT_PATH.parent.parent.parent / "frontend" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("409x425")
window.configure(bg = "#F8ECD1")

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
    62.0,
    38.0,
    anchor="nw",
    text="Login\n",
    fill="#000000",
    font=("Inter SemiBold", 40 * -1)
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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
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
    command=lambda: print("button_2 clicked"),
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
    195.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#DEB6AB",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=180.0,
    y=181.0,
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
entry_2 = Entry(
    bd=0,
    bg="#DEB6AB",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
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
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
