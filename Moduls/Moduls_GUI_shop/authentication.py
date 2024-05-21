from tkmacosx import Button
from canvas import root, frame


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",   # background color
        fg="white",   # font color
        bd=0,
        width=90,
        height=40,
        command=register
    )

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        fg='white',
        width=90,
        height=40,
        command=login
    )

    frame.create_window(350, 260, window=register_button)


def register():
    print("Register")


def login():
    print('Login')
