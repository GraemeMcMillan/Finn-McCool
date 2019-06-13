#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python 3.7.3
"""
Created on Mon Jun 10 00:08:11 2019

@author: finnmccool

A Tkinter programme to accept a user message 
and offset integer to generate an encrypted
version using the Caeser cypher system.
Based on the UTF-8 character set.
"""
import tkinter as tk
from tkinter import font


# create variables for the H & W of the root windo
HEIGHT = 500
WIDTH = 600

'''Here's where the functions go to manage the data'''


def clear_input():
    message_text.delete(0, 'end')
    offset_text.delete(0, 'end')


def caesar_code():
    message = str(message_text.get())
    key = int(offset_text.get())
    alphabet1 = ''.join(chr(x) for x in range(32, 127))
    alphabet2 = alphabet1[key:]+alphabet1[:key]
    coded_message = ''
    for i in range(len(message)):
        x = alphabet1.find(message[i])
        coded_message += (alphabet2[x])
    cypher.config(text=coded_message)


'''Create the root window etc.'''
root = tk.Tk()
root.title('Ceaser Code')

# Create the canvas to draw on
canvas = tk.Canvas(root,
                   height=HEIGHT,
                   width=WIDTH,
                   relief='sunken')
canvas.pack()

# Add a backdrop
backdrop = tk.PhotoImage(file='caeser.png')
backdrop_label = tk.Label(root, image=backdrop)
backdrop_label.place(relwidth=1, relheight=1)

'''Create the frame to get the user's message'''
# Create a frame
message_frame = tk.Frame(root, bg='#9999ff', bd=5)
message_frame.place(
    relx=0.5,
    rely=0.1,
    relwidth=0.75,
    relheight=0.1,
    anchor='n')
# Enter the tect to convert
message_text = tk.Entry(message_frame,
                        bg='#ffffff',
                        font=('Arial',14))
message_text.place(
    relheight=1,
    relwidth=1)

'''Create a similar frame for the offset to be applied'''
# Create a frame
offset_frame = tk.Frame(root, bg='#9999ff', bd=5)
offset_frame.place(
    relx=0.5,
    rely=0.25,
    relwidth=0.75,
    relheight=0.1,
    anchor='n')
# Enter the tect to convert
offset_text = tk.Entry(offset_frame,
                       bg='#ffffff',
                       font=('Arial',11))
offset_text.place(
    relheight=1,
    relwidth=0.25)

# Button to initiate conversion
offset_button = tk.Button(offset_frame,
                          text="Generate",
                          bg='grey',
                          font=('Arial',11))
offset_button.configure(command=caesar_code)
offset_button.place(
    relheight=1,
    relwidth=0.3,
    relx=0.7)
#Button to clear the input
clear_button = tk.Button(offset_frame,
                         text='Clear',
                         bg='grey',
                         font=('Arial',11))
clear_button.configure(command=clear_input)
clear_button.place(
    relheight=1,
    relwidth=0.3,
    relx=0.35)

'''Now make a Bottom Frame to show the output'''
bottom_frame = tk.Frame(root, bg='#9999ff', bd=5)
bottom_frame.place(
    relx=0.5,
    rely=0.6,
    relwidth=0.75,
    relheight=0.2,
    anchor='n')

# The converted message
cypher = tk.Label(bottom_frame,
                  bg='#ffffff',
                  relief='raised',
                  font=('Courier',12),
                  anchor='nw',
                  justify='left',
                  bd=5)

cypher.place(
    relheight=1,
    relwidth=1,)


root.mainloop()
