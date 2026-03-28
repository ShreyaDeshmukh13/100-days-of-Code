from tkinter import Tk, Canvas , PhotoImage , Entry , Label , Button , END , messagebox
from random import choice , randint , shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
               'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
               'V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','^','&','*','+','(',')']


    password_letters = [choice(letters)for _ in range(randint(8,10))]
    password_symbols = [choice(symbols)for _ in range(randint(2,4))]
    password_numbers= [choice(numbers)for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = Email_input.get()
    password = password_input.get()
    new_data = {website : {
        "email" : email ,
        "password" : password ,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "OOPS" , message = "Plase make sure you haven' t left any fields empty")

    else:
        try:
           with open ("data.json" , "r") as file:
               #Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data,file, indent =4)
        else:
            # Updating old data with new data
            data.update(new_data)


            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(data , file,indent =4)

        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)

    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(width = 200 , height = 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo_img )
canvas.grid(column =1 , row=0)

website_label = Label(text="Website:" , font=("New Times Roman",10) )
website_input = Entry(width =30)
website_input.grid(column=1,row=1 , columnspan = 2 , sticky="w")
website_input.focus()
website_label.grid(column=0,row=1)

Email_label = Label(text="Email/Username:" , font=("New Times Roman",10) )
Email_input = Entry(width =50)
Email_input.grid(column=1,row=2 ,columnspan = 2,sticky="w")
Email_input.insert(0,'shreya@email.com')
Email_label.grid(column=0,row=2)

password_label = Label(text="Password:" , font=("New Times Roman",10) )
password_input = Entry(width =30)
password_input.grid(column=1,row=3,sticky="w")
password_label.grid(column=0,row=3)

generate_password_button = Button(text="Generate Password",command = generate_password)
generate_password_button.grid(column=2,row=3 )

add_button = Button(text = "Add" , width = 36 , command = save_password)
add_button.grid(row =4 , column=1 , columnspan = 2 , sticky="w")

search_button = Button(text = "Search" )
search_button.grid(column=2,row=1)







window.mainloop()