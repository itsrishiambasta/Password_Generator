import random  # Importing the random module to generate random choices
import string  # Importing string module to get alphabets, digits, and symbols
import tkinter as tk  # Importing tkinter and giving it an alias 'tk' for GUI creation
from tkinter import messagebox  # Importing messagebox from tkinter for popup messages

# Function to generate a random password based on user input
def generate_password():  # Defining a function named 'generate_password'
    try:  # Start of a try block to handle errors
        length = length_entry.get()  # Getting the user input for password length from the entry field
        if not length.isdigit():  # Checking if the entered value is a number
            messagebox.showerror("Error", "Enter a valid number!")  # Displaying an error message if input is invalid
            return  # Exiting the function
        
        length = int(length)  # Converting the input string to an integer
        if length <= 0:  # Checking if the number is greater than 0
            messagebox.showerror("Error", "Enter a number greater than 0!")  # Displaying an error message
            return  # Exiting the function
        
        characters = string.ascii_letters + string.digits + string.punctuation  # Combining all character types
        password = ''.join(random.choice(characters) for _ in range(length))  # Generating a password of given length
        password_entry.delete(0, tk.END)  # Clearing any previous password from the entry field
        password_entry.insert(0, password)  # Displaying the newly generated password in the entry field
    except Exception as e:  # Handling any unexpected errors
        messagebox.showerror("Error", "Something went wrong!")  # Displaying a generic error message

# Function to copy the generated password to the clipboard
def copy_to_clipboard():  # Defining a function named 'copy_to_clipboard'
    password = password_entry.get()  # Retrieving the password from the entry field
    if password:  # Checking if there is a password to copy
        root.clipboard_clear()  # Clearing the clipboard content
        root.clipboard_append(password)  # Copying the password to the clipboard
        root.update()  # Updating the clipboard
        messagebox.showinfo("Success", "Password copied!")  # Displaying a success message
    else:  # If there is no password to copy
        messagebox.showwarning("Warning", "Generate a password first!")  # Displaying a warning message

# GUI Setup
root = tk.Tk()  # Creating the main application window
root.title("Simple Password Generator")  # Setting the title of the window
root.geometry("400x200")  # Setting the window size (width x height)
root.resizable(False, False)  # Disabling resizing of the window

# Widgets (GUI Elements)
tk.Label(root, text="Enter password length:").pack(pady=5)  # Creating a label asking for password length
length_entry = tk.Entry(root)  # Creating an entry field for user to input password length
length_entry.pack(pady=5)  # Displaying the entry field with padding

generate_button = tk.Button(root, text="Generate", command=generate_password)  # Creating a button to generate password
generate_button.pack(pady=5)  # Displaying the button with padding

password_entry = tk.Entry(root, width=30)  # Creating an entry field to display the generated password
password_entry.pack(pady=5)  # Displaying the entry field with padding

copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)  # Creating a button to copy password to clipboard
copy_button.pack(pady=5)  # Displaying the button with padding

root.mainloop()  # Running the Tkinter event loop to keep the application running
