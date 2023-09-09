from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


def save():
    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()
    new_dict = {
        website: {
            'email': email,
            'password': pwd,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details that you entered: \nEmail: {email}\nPassword: {pwd}\nIs it ok to save?")
    #     if is_ok:
    #         with open("data.txt", "a") as data_file:
    #             data_file.write(f"{website} | {email} | {pwd}\n")
    #             website_entry.delete(0, END)
    #             email_entry.delete(0, END)
    #             pwd_entry.delete(0, END)
    #             website_entry.focus()
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_dict, data_file, indent=4)
        else:
            data.update(new_dict)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            pwd_entry.delete(0, END)
            website_entry.focus()


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pwd_entry.insert(0, password)
    pyperclip.copy(password)


def search():
    search_entry = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if search_entry in data:
            messagebox.showinfo(title=search_entry, message=f"Email: {data[search_entry]['email']}\nPassword: {data[search_entry]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_entry} exists.")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=logo)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_btn = Button(text="Search", width=11, command=search)
search_btn.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=37)
email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, 'abc@gmail.com' )

pwd_label = Label(text="Password:")
pwd_label.grid(column=0, row=3)
pwd_entry = Entry(width=22)
pwd_entry.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", width=11, command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=34, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
