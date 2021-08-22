import random
import tkinter
from tkinter import messagebox
import pass_generator

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_length = random.randint(8, 13)
    symbol_count = random.randint(1, 4)
    numbers_count = random.randint(1, 5)
    letters_count = password_length - symbol_count - numbers_count

    generated_password = pass_generator.generate_password(letters_count, symbol_count, numbers_count)
    print(generated_password)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_entry.get()
    name = name_entry.get()
    password = password_entry.get()

    if len(website) < 5 or len(name) < 5 or len(password) < 8:
        messagebox.showinfo(title="Error", message="Something goes wrong!\nDid you enter all required info?")
        return

    is_ok = messagebox.askokcancel(title=website,
                                   message=f"Is everything OK?\nwebsite: {website}\nname: {name}\npassword: {password}")

    if is_ok:
        with open("saves.csv", "a") as save_file:
            save_file.write(f"{website} | {name} | {password_entry.get()}\n")
            website_entry.delete(0, tkinter.END)
            # name_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

if __name__ == "__main__":

    window = tkinter.Tk()
    window.title("Password Manager")
    window.config(width=200, height=200, padx=40, pady=30, bg=YELLOW)

    canvas = tkinter.Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
    padlock_img = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=padlock_img)
    canvas.grid(column=1, row=0)

    website_label = tkinter.Label()
    website_label.config(text="Website:", bg=YELLOW)
    website_label.grid(column=0, row=1)

    name_label = tkinter.Label()
    name_label.config(text="Email/Username:", bg=YELLOW)
    name_label.grid(column=0, row=2)

    password_label = tkinter.Label()
    password_label.config(text="Password:", bg=YELLOW)
    password_label.grid(column=0, row=3)

    website_entry = tkinter.Entry(width=50)
    website_entry.grid(column=1, row=1, columnspan=2)
    website_entry.focus()

    name_entry = tkinter.Entry(width=50)
    name_entry.grid(column=1, row=2, columnspan=2)
    name_entry.insert(0, "yourname@mailbox.com")

    password_entry = tkinter.Entry(width=32)
    password_entry.grid(column=1, row=3)

    generate_button = tkinter.Button()
    generate_button.config(text="Generate Password", command=generate_password)
    generate_button.grid(column=2, row=3)

    add_button = tkinter.Button()
    add_button.config(text="Add", width=43, command=add_password)
    add_button.grid(column=1, row=4, columnspan=2)

    window.mainloop()
