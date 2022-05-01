from tkinter import *
import random

def dice_roll():
    dice_num_list = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    dice_num1 = random.choice(dice_num_list)
    dice_num2= random.choice(dice_num_list)
    dice.config(text=f"{dice_num1}{dice_num2}")
root = Tk()
root.title('Dice Simulator')
root.geometry('900x500')
root.minsize(900,500)
root.maxsize(900,500)

Label(root,text='Welcome to Dice Simulator',font=('arial',25,'bold')).pack(pady=20)

Button(root,text='Click to Roll',font=('arial',12,'bold'),command=dice_roll).pack()

frm = Frame(root,width=700,height=300)
frm.pack(pady=20)

dice = Label(frm,text='',font=('arial',200,'bold'))
dice.grid()


root.mainloop()

