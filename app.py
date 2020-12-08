import pymongo

__author__ = "Zayaan"

mongodb_uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(mongodb_uri)

database = client['MoneyManager']
collection = database['Users']

users = collection.find({})

#for user in users:
#    if user["Email"] == email:
#        print("There is already an existing account linked to this email address.")
#    else:
#        collection.insert_one({"Name" : username, "Email" : email})
#    print(user)




from tkinter import *


# set global variables
global username
global password
global username_entry
global password_entry
global main_screen
global username_verify
global password_verify



# create a GUI window 
main_screen = Tk()

# Function to clear the window
def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list


# Main account screen
def main_account_screen():
    # set the configuration of GUI window 
    main_screen.geometry("400x450")  
    # set the title of GUI window
    main_screen.title("Account Login")
    # create a Form label 
    Label(text="Money Manager", width="300", height="2", font=("Montserrat", 32)).pack() 
    # create Login Button 
    Button(text="Login", height="2", width="30", font=("Montserrat", 10), command = login).pack() 
    # create a register button
    Button(text="Register", height="2", width="30", font=("Montserrat", 10), command=register).pack()
    # start the GUI
    main_screen.mainloop()

# Set text variables
username = StringVar()
password = StringVar()
username_verify = StringVar()
password_verify = StringVar()

def register():

    # clear window
    widget_list = all_children(main_screen)
    for item in widget_list:
        item.pack_forget()

    # set the title of GUI window
    main_screen.title("Account Register")

    # Set label for user's instruction
    Label(main_screen, text="Please enter details below").pack()
    Label(main_screen, text="").pack()
    
    # Set username label
    username_lable = Label(main_screen, text="Username * ")
    username_lable.pack()

    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    username_entry = Entry(main_screen, textvariable=username)
    username_entry.pack()
   
    # Set password label
    password_lable = Label(main_screen, text="Password * ")
    password_lable.pack()
    
    # Set password entry
    password_entry = Entry(main_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(main_screen, text="").pack()
    
    # Set register button
    Button(main_screen, text="Register", width=10, height=1, command = register_user).pack()



def register_user():
    
    # get username and password
    username_info = username.get()
    password_info = password.get()
    print("Username: ", username_info)
    print("Password: ", password_info)
    
    # set a label for showing success information on screen     
    Label(main_screen, text="Registration Success", fg="green", font=("Montserrat", 10)).pack()
    
    # create Login Button 
    Button(text="Login", height="2", width="30", font=("Montserrat", 10), command = login).pack() 



# define login function
def login():

    # clear window
    widget_list = all_children(main_screen)
    for item in widget_list:
        item.pack_forget()

    main_screen.title("Login")
    Label(main_screen, text="Please enter details below to login").pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Username * ").pack()
    username_login_entry = Entry(main_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password * ").pack()
    password__login_entry = Entry(main_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command=login_verification).pack()

# define log in verfication function
def login_verification():
    print("working...")


# call the main_account_screen() function
main_account_screen()
