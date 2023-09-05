from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]


    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website_write = website_entry.get()
    email_write = email_username_entry.get()
    password_write = password_entry.get()

    if len(website_write)==0 or len(password_write)==0 or len(email_write)==0:
        messagebox.showinfo(title="Somethings wrong!", message=f"please write all fields")
    else:
        is_ok = messagebox.askokcancel(title=website_write,message=f"These are the details entered: \nEmail:{email_write}"
                                                               f"\nPassword:{password_write}\n Is it ok to save?" )
        if is_ok:
            with open("password.txt",mode="a") as file:
                file.write(f"{website_write} | {email_write} | {password_write}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)
#Label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
e_mail_label=Label(text="Email/Username :")
e_mail_label.grid(row=2, column=0)
password_label = Label(text="Password :")
password_label.grid(row=3,column=0)

#Entries
website_entry= Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(row=2,column=1,columnspan=2)
email_username_entry.insert(0,"berkay.karabas091@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password = Button(text="Generate Password",command=generator)
generate_password.grid(column=2,row=3)

add_button = Button(width=35,text="Add",command=save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()