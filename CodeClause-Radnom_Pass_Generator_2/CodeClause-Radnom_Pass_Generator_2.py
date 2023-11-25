import random as r

import string
from tkinter import *


class Generator:

    def __init__(self):
        self.root = Tk()
        self.root['bg'] = 'blue'
        self.root.title('Password Generator')
        self.root.wm_iconbitmap('pass.ico')

        self.label1 = Label(text='Enter Password Length :', fg='white', bg='blue', font=('terminal', 15))
        self.label1.grid(row=0, column=0, padx=5, pady=5)

        self.entry = Entry(bg='white', width=15, fg='blue', font=('terminal', 15))
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        self.txt = Text(height=8, width=40, font=('terminal', 15))
        self.txt.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.btn1 = Button(text='Generate', bg='blue', fg='white', borderwidth=0, font=('terminal', 15),
                           command=self.button_click)
        self.btn1.grid(row=2, column=1, padx=50, pady=20, sticky='e')

        self.btn2 = Button(text='Reset', bg='blue', fg='white', borderwidth=0, font=('terminal', 15),
                           command=self.reset_btn)
        self.btn2.grid(row=2, column=0, padx=50, pady=5, sticky='w')

        self.root.bind('<Return>', self.pass_click)
        self.root.bind('<Escape>', self.reset_click)

        self.root.mainloop()

    def random_key(self, length):
        char = string.ascii_letters + string.digits + string.punctuation
        ran = ''.join(r.choice(char) for _ in range(length))
        return ran

    def button_click(self):
        try:
            if int(self.entry.get()) == 0:
                self.txt.insert('1.0', 'Unable to generate 0 lenth password\n')
            else:
                random_pass = self.random_key(int(self.entry.get()))
                self.txt.delete('1.0', END)
                self.txt.insert('1.0', f'Generated Password\nPassword: {str(random_pass)}\n')
                self.entry.delete(0, END)
        except ValueError as e:
            self.txt.delete('1.0', END)
            self.txt.insert('1.0', f'Please Enter "Numerics" only {str(e)}')
            self.entry.delete(0, END)

        except Exception as a:
            self.txt.delete('1.0', END)
            self.txt.insert('1.0', str(a))
            self.entry.delete(0, END)

    def reset_btn(self):
        self.entry.delete(0, END)
        self.txt.delete('0.0', END)

    def pass_click(self, event):
        self.button_click()

    def reset_click(self, event):
        self.reset_btn()


Generator()
