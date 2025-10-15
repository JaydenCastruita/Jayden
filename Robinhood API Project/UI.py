from logging import root
import tkinter as tk

class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Robinhood Login")
        self.root.geometry("300x200")
        # self.root.configure(background='pink')

        self.username_label = tk.Label(self.root, text="Username:", font=("Times New Roman", 14))
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root, font=("Times New Roman", 14))
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:", font=("Times New Roman", 14))
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*", font=("Times New Roman", 14))
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", font=("Times New Roman", 14), command=self.login)
        self.login_button.pack()

        self.credentials = None

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.credentials = (self.username, self.password)
        self.root.destroy()

    def cancel(self):
        self.credentials = (None, None)
        self.root.destroy()

    def run(self):
        self.root.mainloop()
        return self.credentials

# LoginApp().run()

# root = tk.Tk()

# root.title("Robinhood Login")
# root.geometry("300x200")

# username_label = tk.Label(root, text="Username:", font=("Times New Roman", 14))
# username_label.pack()

# username_entry = tk.Entry(root, font=("Times New Roman", 14))
# username_entry.pack()

# password_label = tk.Label(root, text="Password:", font=("Times New Roman", 14))
# password_label.pack()

# def hide_text():
#     password_entry = tk.Entry(root, show="*", font=("Times New Roman", 14))
#     password_entry.pack()
    

# # password_entry = tk.Entry(root, show="*", font=("Times New Roman", 14))
# # password_entry.pack()

# login_button = tk.Button(root, text="Login", font=("Times New Roman", 14))
# login_button.pack()

# root.mainloop()