from tkinter import*
import string
import random
import pyperclip
def generate():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_lenght=int(lenght_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_lenght))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_lenght))

    if choice.get()==3:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets+numbers+special_characters,password_lenght))      

    #password=random.sample(all,password_lenght)
    #passwordField.insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)
root=Tk()
root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times newroman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid(pady=10)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lenghtLabel=Label(root,text='Password Lenght',font=('Font'),bg='gray20',fg='white')
lenghtLabel.grid(pady=5)

lenght_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font,command=generate)
lenght_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=5)

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=5)

root.mainloop()



