''' Use a Class to rewrite the Ceaser Code
Created 22-6-2019
Author - Finn McCool
UTF8
Python 3.7.3 64-bit('base':conda)'''

import tkinter as tk
from tkinter.font import Font

HEIGHT = 620
WIDTH = 470
img = 'kaiser.png'

class CaeserApp:

    def __init__(self): 

        self.root = tk.Tk()
        self.root.title('Caeser Code')
        FONT = Font(family='Arial',size=12,weight='bold')

        self.canvas = tk.Canvas(self.root,width=WIDTH,height=HEIGHT)
        self.canvas.pack()
        backdrop = tk.PhotoImage(file=img)
        backdrop_label = tk.Label(self.root,image=backdrop)
        backdrop_label.place(relwidth=1,relheight=1)

        message_frame = tk.Frame(self.root, bg='#33334d', bd=5)
        message_frame.place(
                            relx=0.5,
                            rely=0.1,
                            relwidth=0.75,
                            relheight=0.05,
                            anchor='n')
        self.message_text = tk.Entry(message_frame,
                            bg='#ffffff',
                            font=FONT)
        self.message_text.place( 
                            relheight=1,
                            relwidth=1)

        offset_frame = tk.Frame(self.root, bg='#33334d', bd=5)
        offset_frame.place(
                        relx=0.5,
                        rely=0.75,
                        relwidth=0.75,
                        relheight=0.05,
                        anchor='n')

        self.offset_text = tk.Entry(offset_frame,
                       bg='#ffffff',
                       font=FONT)               
        self.offset_text.place(relheight=1,relwidth=0.25)          

        clear_button = tk.Button(offset_frame,
                            text='Clear',
                            bg='grey',
                            font=('Arial',11))
        clear_button.place(
            relheight=1,
            relwidth=0.3,
            relx=0.35)   
        clear_button.configure(command=self.clear_input)

        generate_code_button = tk.Button(offset_frame,
                                text="Generate",
                                bg='grey',
                                font=('Arial',11))
        generate_code_button.place(
            relheight=1,
            relwidth=0.3,
            relx=0.7)        
        generate_code_button.configure(command=self.generate_code)

        coded_frame = tk.Frame(self.root, bg='#33334d', bd=5)
        coded_frame.place(
            relx=0.5,
            rely=0.8,
            relwidth=0.75,
            relheight=0.1,
            anchor='n')

        self.cypher_text = tk.Label(coded_frame,
                        bg='#ffffff',
                        relief='raised',
                        font=FONT,
                        anchor='nw',
                        justify='left',
                        bd=5)
        self.cypher_text.place(
                relheight=1,
                relwidth=1,)        
        
        
        self.root.mainloop()  


    def clear_input(self):
        self.message_text.delete(0, 'end')
        self.offset_text.delete(0, 'end')
        #self.cypher_text.delete(0,'end')
    
    def generate_code(self):
        message = str(self.message_text.get())
        key = int(self.offset_text.get())
        alphabet1 = ''.join(chr(x) for x in range(32, 127))
        alphabet2 = alphabet1[key:]+alphabet1[:key]
        coded_message = ''
        for i in range(len(message)):
            x = alphabet1.find(message[i])
            coded_message += (alphabet2[x])
        self.cypher_text.config(text=coded_message)       

Caeser = CaeserApp()

