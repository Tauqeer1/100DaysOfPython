from tkinter import *
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
WHITE = "#ffffff"
BLACK = "#000000"
GRAY = "#635d5c"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_to_file(filename, text):
    with open(filename, 'a') as text_file:
        text_file.write(text)

def save_data():
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()

    if len(website_value) == 0 or len(email_value) == 0 or len(password_value) == 0:
        messagebox.showerror(title="Error", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_value,
                                       message=f"These are the details entered: \n Email: {email_value} \n "
                                               f"Password: {password_value} \n Is it ok to save ?")
        print(is_ok)
        if is_ok:
            text_to_write = f"{website_value} | {email_value} | {password_value}\n"
            write_to_file("data.txt", text_to_write)
            messagebox.showinfo("Success", "Data saved!")
            clear_form()

def clear_form():
    website_input.delete(0, END)
    password_input.delete(0, END)

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

website_input = Entry(width=35, bg=WHITE, fg=BLACK, relief="flat", highlightcolor=GRAY, highlightthickness=1, insertbackground=BLACK)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)


email_label = Label(text="Email/Username:", bg=WHITE, fg=BLACK, pady=5)
email_label.grid(row=2, column=0)

email_input = Entry(width=35, bg=WHITE, fg=BLACK, relief="flat", highlightcolor=GRAY, highlightthickness=1, insertbackground=BLACK)
email_input.insert(0, "tauqeer.shakir@yahoo.com")
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", bg=WHITE, fg=BLACK, pady=5)
password_label.grid(row=3, column=0)

password_input = Entry(width=21, bg=WHITE, fg=BLACK, show="*", relief="flat", highlightcolor=GRAY, highlightthickness=1, insertbackground=BLACK)
password_input.grid(row=3, column=1)

password_generate_button = Button(text="Generate Password", highlightbackground=WHITE, width=11, relief="raised")
password_generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightbackground=WHITE, relief="raised", command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()