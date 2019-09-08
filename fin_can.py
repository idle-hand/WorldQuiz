# caps quiz - d.e.Howe kingston ont. 2017 October
# quiz logic when finished may offer mult. lists to quiz with

from tkinter import *
import random
import copy

cap = ['Ottawa','Edmonton','Victoria','Winnipeg','Fredericton','St. Johns','Halifax','Toronto',
        'Charlottetown','Quebec City','Regina','Whitehorse','Iqaluit','Yellowknife']
states = ['Canada','Alberta','British Columbia','Manitoba','New Brunswick','Newfoundland and Labrador','Nova Scotia',
          'Ontario','Prince Edward Island','Quebec','Saskatchewan','Yukon','Nunavut','Northwest Territories']

short_list = [' ',' ',' ',' ',' ']

score = 0
count = 0

new_list = copy.copy(cap)

# caps quiz - d.e.Howe kingston ont. 2017 October
# function ShowChoice

def ShowChoice():
    global count
    global score
    x = v.get()
    
    if x == cap[count]:
        score = score + 1
          
    count = count + 1
    root.destroy()    

# function ShowChoice
    
while count < 14:

# caps quiz - d.e.Howe kingston ont. 2017 October
# shuffle my newlist a copy of the original cap[] list
# then pull the top five from the list that are now random
# these are now my choices for the user - since i want to insert the correct answer
# I need to be sure it is not already in the random list i check and if it is
# I replace it with next off shuffled list so I can then insert the correct answer at random

    random.shuffle(new_list)
   
    for i in range(5):
        short_list[i] = new_list[i]
    
    for i in range(5):
        if short_list[i] == cap[count]:
            short_list[i] = new_list[5]
    
    from random import randint
    r = randint(0, 4)

    short_list[r] = cap[count]
    
    root = Tk()
    root.geometry("700x500+290+90")
    #root.configure(background='white')
    #root["bg"] = "magenta"
   
    Label(root,text="The Capital of " + states[count] + " is?\n", font=32).grid(row=2,column=0)
    
    v = StringVar()
    
    for i in range(5):
      
        b = Radiobutton(root, text =short_list[i], variable=v,command=ShowChoice, value=short_list[i],font=22,indicatoron=0)
        b.grid(row= i+4,column=2, sticky=W)
        
    Label(root,text="\nYour Answer:", font=18).grid(row=12,column=0, sticky=W)

    gif_one = Text(root,height=13, width=40)
    photo=PhotoImage(file='./canflag.gif')
    gif_one.image_create(END, image=photo)
    gif_one.grid(row=9,column=0)
   
    Label(root,text='   Score = '+ str(score),font=18).grid(row=10,column=0,sticky=W)

    Label(root,text=' You have: ' + str(score) + ' of ' + str(count) + ' correct.').grid(row=11,column=0)

    if count > 0:
        Label(root,text=' or: ' + str(int(100 * score/count)) + ' Percent').grid(row=11,column=1,sticky=W)

    done = Button(root,text =' QUIT  ',command=quit).grid(row=10,column=2) 

    root.bind('<Return>',ShowChoice)

    mainloop()


