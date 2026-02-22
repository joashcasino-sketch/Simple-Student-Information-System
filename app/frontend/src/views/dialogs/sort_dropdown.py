import tkinter as tk

class SortDropdown:
    def __init__(self, parent, on_select_callback):
        self.parent = parent
        self.on_select_callback = on_select_callback
        self.dropdown_open = False
        self.dropdown_win = None
        self.sort_column = "Name"
        self.sort_reverse = False

        self.button = tk.Button(
            parent,
            text="Sort By ▾",
            font=("Lato", 10),
            bg="#85586F", fg="white",
            borderwidth=0, highlightthickness=0,
            relief="flat", cursor="hand2",
            command=self.toggle
        )

    def place(self, **kwargs):
        self.button.place(**kwargs)

    def toggle(self):
        if self.dropdown_open and self.dropdown_win:
            self.close()
            return

        x = self.button.winfo_rootx()
        y = self.button.winfo_rooty() + self.button.winfo_height()

        self.dropdown_win = tk.Toplevel(self.parent)
        self.dropdown_win.wm_overrideredirect(True)
        self.dropdown_win.geometry(f"120x180+{x}+{y}")
        self.dropdown_win.configure(bg="#85586F")

        options = ['ID Number', 'Name', 'Gender', 'Year Level', 'Program', 'College']
        for option in options:
            btn = tk.Button(
                self.dropdown_win,
                text=option,
                font=("Lato", 10),
                bg="#85586F", fg="white",
                activebackground="#642D48", activeforeground="white",
                borderwidth=0, relief="flat", cursor="hand2",
                anchor="w", padx=10,
                command=lambda o=option: self.select(o)
            )
            btn.pack(fill="x", pady=1)

        self.dropdown_open = True

    def select(self, option):
        self.button.config(text=f"{option} ▾")
        self.close()

        if option == self.sort_column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = option
            self.sort_reverse = False

        self.on_select_callback(self.sort_column, self.sort_reverse)

    def close(self):
        if self.dropdown_win:
            self.dropdown_win.destroy()
            self.dropdown_win = None
        self.dropdown_open = False