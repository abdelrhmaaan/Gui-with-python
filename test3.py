from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as tb
import re

# Function to toggle between registration, sign-in, and project details sections
def toggle_registration_sign_in():
    if registration_frame.winfo_viewable():
        registration_frame.pack_forget()
        sign_in_frame.pack()
    else:
        sign_in_frame.pack_forget()
        registration_frame.pack()

def register_user():
    # Perform registration logic here

    # After successful registration, navigate to the project details frame
    registration_frame.pack_forget()
    project_details_frame.pack()

def validate_registration_email(P):
    is_valid = bool(re.match(r'\w+@\w+\.\w+', P))
    if is_valid:
        registration_email_validation_label.config(text="Valid Email", foreground="green")
    else:
        registration_email_validation_label.config(text="Invalid Email", foreground="red")
    return True

def validate_sign_in_email(P):
    # Add your validation logic for the sign-in email here
    return True

def validate_sign_in_password(P):
    # Add your validation logic for the sign-in password here
    return True

root = tb.Window(title='Crowd-Funding', themename='darkly')
root.iconbitmap(r'imges\python.ico')
root.geometry('500x500')

# Create a frame for registration widgets
registration_frame = Frame(root)

reg_title = tb.Label(registration_frame, text='Register', bootstyle='primary', font=('Helvetica', 30))
reg_title.pack(pady=40)

name_label = tb.Label(registration_frame, text='Name:')
name_label.pack()
name_ent = tb.Entry(registration_frame, bootstyle='success')
name_ent.pack()

email_label = tb.Label(registration_frame, text='Email:')
email_label.pack()

validate_registration_email_func = root.register(validate_registration_email)
registration_email_entry = tb.Entry(registration_frame, bootstyle='success', validate="key", validatecommand=(validate_registration_email_func, "%P"))
registration_email_entry.pack()

# Add password, confirm password, and other form fields as needed

# Label to display email validation status for registration
registration_email_validation_label = tb.Label(registration_frame, text="", foreground="black")
registration_email_validation_label.pack()

# Create a frame for sign-in widgets (initially hidden)
sign_in_frame = Frame(root)

# Add sign-in widgets to the sign-in frame
sign_in_title = tb.Label(sign_in_frame, text='Sign In', bootstyle='primary', font=('Helvetica', 30))
sign_in_title.pack(pady=40)

sign_in_email_label = tb.Label(sign_in_frame, text='Email:')
sign_in_email_label.pack()

validate_sign_in_email_func = root.register(validate_sign_in_email)
sign_in_email_entry = tb.Entry(sign_in_frame, bootstyle='success', validate="key", validatecommand=(validate_sign_in_email_func, "%P"))
sign_in_email_entry.pack()

sign_in_password_label = tb.Label(sign_in_frame, text='Password:')
sign_in_password_label.pack()

validate_sign_in_password_func = root.register(validate_sign_in_password)
sign_in_password_entry = tb.Entry(sign_in_frame, bootstyle='success', validate="key", validatecommand=(validate_sign_in_password_func, "%P"))
sign_in_password_entry.pack()

# Create a frame for project details (initially hidden)
project_details_frame = Frame(root)

# Add project details widgets to the project details frame
sign_in_email_label = tb.Label(project_details_frame, text='Project Title:')
sign_in_email_label.pack()
sign_in_email_entry = tb.Entry(project_details_frame, bootstyle='success')
sign_in_email_entry.pack()

sign_in_email_label1 = tb.Label(project_details_frame, text='Project Desc:')
sign_in_email_label1.pack()
sign_in_email_entry1 = tb.Entry(project_details_frame, bootstyle='success')
sign_in_email_entry1.pack()

sign_in_email_label1 = tb.Label(project_details_frame, text='Total Traget:')
sign_in_email_label1.pack()
sign_in_email_entry1 = tb.Entry(project_details_frame, bootstyle='success')
sign_in_email_entry1.pack()

register_button = tb.Button(project_details_frame, text="Add Product", bootstyle='success')
register_button.pack(pady=10)
# You can create your project details form here
# Add a "Sign in" link label
sign_in_label = tb.Label(registration_frame, text="Already have an account? Sign in", foreground="blue", cursor="hand2")
sign_in_label.pack(pady=10)
sign_in_label.bind("<Button-1>", lambda event: toggle_registration_sign_in())

# Add a "Register" button to complete registration and navigate to project details
register_button = tb.Button(registration_frame, text="Register", bootstyle='success', command=register_user)
register_button.pack()

# Initially, display the registration frame
registration_frame.pack()

root.mainloop()
