from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#ffffff"
BLACK = "#000000"
GRAY = "#635d5c"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = ''.join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_to_json(filename, data_dict):
    try:
        with open(filename, 'r') as data_json_file:
            # Reading old data
            data = json.load(data_json_file)
    except FileNotFoundError:
        with open(filename, 'w') as data_json_file:
            # Saving updated data to file
            json.dump(data_dict, data_json_file, indent=4)
    else:
        # Updating old data with new data
        data.update(data_dict)
        with open(filename, 'w') as data_json_file:
            # Saving updated data to file
            json.dump(data, data_json_file, indent=4)

def save_data():
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()

    if len(website_value) == 0 or len(email_value) == 0 or len(password_value) == 0:
        messagebox.showerror(title="Error", message="Please make sure you haven't left any fields empty!")
    else:
        data_dict = {
            website_value: {
                "email": email_value,
                "password": password_value
            }
        }
        write_to_json('data.json', data_dict)
        messagebox.showinfo("Success", "Data saved!")
        clear_form()

def clear_form():
    website_input.delete(0, END)
    password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_value = website_input.get()
    try:
        with open('data.json', 'r') as data_json_file:
            data = json.load(data_json_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File found!")
    else:
        try:
            find_obj = data[website_value]
        except KeyError:
            messagebox.showerror(title="Error", message=f"No details for the {website_value} exists!")
        else:
            messagebox.showinfo(title=website_value,
                                message=f"Email: {find_obj['email']} \n Password: {find_obj['password']}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:", bg=WHITE, fg=BLACK, pady=5)
website_label.grid(row=1, column=0)

website_input = Entry(width=21, bg=WHITE, fg=BLACK, relief="flat", highlightcolor=GRAY, highlightthickness=1, insertbackground=BLACK)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=1)

search_button = Button(text="Search", highlightbackground=WHITE, width=11, relief="raised", command=find_password)
search_button.grid(row=1, column=2)


email_label = Label(text="Email/Username:", bg=WHITE, fg=BLACK, pady=5)
email_label.grid(row=2, column=0)

email_input = Entry(width=35, bg=WHITE, fg=BLACK, relief="flat", highlightcolor=GRAY, highlightthickness=1, insertbackground=BLACK)
email_input.insert(0, "tauqeer.shakir@yahoo.com")
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", bg=WHITE, fg=BLACK, pady=5)
password_label.grid(row=3, column=0)

password_input = Entry(width=21, bg=WHITE, fg=BLACK, relief="flat", highlightcolor=GRAY, highlightthickness=1, insertbackground=BLACK)
password_input.grid(row=3, column=1)

password_generate_button = Button(text="Generate Password", highlightbackground=WHITE, width=11, relief="raised", command=generate_password)
password_generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightbackground=WHITE, relief="raised", command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()