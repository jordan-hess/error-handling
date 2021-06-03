from tkinter import *
import os




username = ["jordieboy123@gmail.com", "itsurgirlzozo234@gmail.com", "jadenjohnmayer@gmail.com", "thapelototsi@gmail.com"]
password = ["plantsvzombies", "mathisbae", "manenburgtaxi", "samora"]

username = input("Please enter your username : ")
password = input("Please enter your password : ")
print("Greetings,", username, "you are now logged in now with a password")

command = input("Please type a command :")
if command == "log off":
    print("You have now been logged off again",username)
    username == ""
    password == ""

username = input("Please enter your username : ")
password = input("Please enter your password : ")

while (username != "username" and password != "password"):

    print(" Sorry username and password incorrect please re-enter for validation ")
    username = input("Please enter your username : ")
    password = input("Please enter your password : ")

else:
    print ("Greetings, ", username, "you are now logged in now with your password")


    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)

    def login():
        global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

main_screen.mainloop()
