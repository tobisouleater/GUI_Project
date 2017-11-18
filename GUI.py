"""
Toby Au
Final Project
Cross Platform - user customizable eBook
"""

from tkinter import *

"""
- render pages to look like a book
- Buttons : Previous / Next / Bookmark / Font Size / Page # / input page # /
- include a clock
"""

#write description about project in 3 lines and send to professor

#book = open(textfile .split())
"""
shelf = shelve.open('Books')
shelf['sample'] = book
shelf.close()
"""

def Next():
    #flips to next page
    return

def Previous():
    #flips to previous page
    return

def inputNum():
    #input page number and shows current page number
    return 

root = Tk()


Title = Label(root, text= 'Book Title')
Pagenum = Label(root, text= 5, anchor=N)
NextPage = Button(root, command= Next, text = 'Next')
PreviousPage = Button(root, command= Previous, text = 'Previous')
Book = Canvas(root, width=600, height=800, bg='gray83')

Book.create_text(300,30,fill="black",font="Times 20 italic bold",
                    text="Tkinter Project")

Title.pack()
NextPage.pack(anchor=NE)
PreviousPage.pack(anchor=NW)
Book.pack()


mainloop()
#Buttons : Previous / Next / Bookmark / Font Size / Page # / input page # 

