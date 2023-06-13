import string
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class PasswordGenerator:

    def __init__(self, master: Tk) -> None:
        self.window = master
        self.window.bind('<Return>', self.generate_password)

        self.label = ttk.Label(text='Length of the password')
        self.label.place(x=60, y=50)

        self.entry = ttk.Entry(self.window)
        self.entry.place(x=210, y=50)

        self.first_value = IntVar()
        self.first_check = ttk.Checkbutton(self.window, text='Use digits', variable=self.first_value, cursor='hand2', onvalue=1, offvalue=0)
        self.first_check.place(x=60, y=80)

        self.second_value = IntVar()
        self.second_check = ttk.Checkbutton(self.window, text='Use punctuation marks', variable=self.second_value, cursor='hand2', onvalue=3, offvalue=2)
        self.second_check.place(x=60, y=110)

        self.reset_button = ttk.Button(self.window, text='Reset', command=self.reset, cursor='hand2')
        self.reset_button.place(x=260, y=80)

        self.reset_button = ttk.Button(self.window, text='Generate', command=self.generate_password, cursor='hand2')
        self.reset_button.place(x=260, y=110)


    def reset(self):
        self.entry.delete(0, END)
        self.first_value.set(0)
        self.second_value.set(2)

    def generate_password(self, event=None):
        self.symbols = string.ascii_letters
        self.second_entry = ttk.Entry(self.window, width=45)

        if self.entry.get():
            try:
                length = int(self.entry.get())

            except ValueError:
                messagebox.showerror('Value error', f'{self.entry.get()} is not a number')

            if self.first_value.get() == 1:
                self.symbols += string.digits
            if self.second_value.get() == 3:
                self.symbols += string.punctuation
                
            if length <= len(self.symbols):
                password = "".join(random.sample(self.symbols, length))

                self.second_entry.place(x=60, y=140)
                self.second_entry.insert(0, password)
                self.second_entry.config(state='readonly')
            else:
                messagebox.showwarning('Warning', 'Try something shorter')
        else:
            messagebox.showwarning('Warning', 'Enter length of the password')


if __name__ == '__main__':
    
    win = Tk()
    win.title('Password generator')
    win.geometry('400x250')
    win.resizable(0, 0)

    generator = PasswordGenerator(win)
    win.mainloop()