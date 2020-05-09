# caps quiz - d.e.Howe kingston ont. 2017 October

from tkinter import *
import random
import copy

cap = ['Ottawa', 'Edmonton', 'Victoria', 'Winnipeg', 'Fredericton',
       'St. Johns', 'Halifax', 'Toronto', 'Charlottetown',
       'Quebec City', 'Regina', 'Whitehorse',
       'Iqaluit',  'Yellowknife']
states = ['Canada',  'Alberta',  'British Columbia',  'Manitoba',
          'New Brunswick', 'Newfoundland and Labrador',
          'Nova Scotia', 'Ontario', 'Prince Edward Island',
          'Quebec', 'Saskatchewan', 'Yukon', 'Nunavut',
          'Northwest Territories']

short_list = [' ',  ' ', ' ', ' ', ' ']

score = 0
count = 0

new_list = copy.copy(cap)


def ShowChoice():
    global count
    global score
    x = v.get()
    if x == cap[count]:
        score = score + 1
    count = count + 1
    root.destroy()

while count < 14:

    random.shuffle(new_list)

    for i in range(5):
        short_list[i] = new_list[i]
    for i in range(5):
        if short_list[i] == cap[count]:
            short_list[i] = new_list[5]
    from random import randint
    r = randint(0,  4)

    short_list[r] = cap[count]
    root = Tk()
    Label(root, text="The Capital of " +
          states[count] + " is?\n",  font=32).grid(row=2, column=0)
    v = StringVar()
    for i in range(5):
        b = Radiobutton(root,  text=short_list[i],  variable=v,
                        command=ShowChoice, value=short_list[i],
                        font=22, indicatoron=0)
        b.grid(row=i+4, column=2, sticky=W)
    gif_one = Text(root, height=12,  width=40)
    photo = PhotoImage(file='./canflag.gif')
    gif_one.image_create(END,  image=photo)
    gif_one.grid(row=9, column=0)
    Label(root, text='   Score = ' + str(score),
          font=18).grid(row=10, column=0, sticky=W)

    Label(root, text=' You have: ' + str(score) +
          ' of ' + str(count) + ' correct.').grid(row=11, column=0)

    done = Button(root, text=' QUIT  ', command=quit).grid(row=10, column=2)
    root.bind('<Return>',  ShowChoice)

    mainloop()
