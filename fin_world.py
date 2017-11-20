#****************************************************************
# caps quiz - d.e.Howe kingston ont. 2017 October
# quiz logic when finished may offer mult. lists to quiz with
#****************************************************************

from tkinter import *

import random
import copy

import csv   # getting my lists from csv files so I do not need to store data in script


with open('world_caps.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    countrys = []
    capitals = []
    for row in readCSV:
        country = row[0]
        capital = row[1]

        countrys.append(country)
        capitals.append(capital)

   # print(countrys)
   # print(capitals)

#print(len(countrys))
#print(len(capitals))
 # getting my lists from csv files so I do not need to store data in script


short_list = ['1','2','3','4','5']  # not sure i need the dummy fields?


score = 0
count = 0

cap = copy.copy(capitals)

new_list = copy.copy(capitals)
states = copy.copy(countrys)


#****************************************************************
# caps quiz - d.e.Howe kingston ont. 2017 October
# function ShowChoice
# START
#****************************************************************



def ShowChoice():
    global count
    global score
    x = v.get()
    
    if x == cap[count]:
        score = score + 1
          
    count = count + 1
    root.destroy()       
    
#****************************************************************
# caps quiz - d.e.Howe kingston ont. 2017 October
# function ShowChoice
# END
#****************************************************************

    
while count < 197:

#****************************************************************
# caps quiz - d.e.Howe kingston ont. 2017 October
# shuffle my newlist a copy of the original cap[] list
# then pull the top five from the list that are now random
# these are now my choices for the user - since i want to insert the correct answer
# I need to be sure it is not already in the random list i check and if it is
# I replace it with next off shuffled list so I can then insert the correct answer at random
#****************************************************************
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
    root.geometry("500x500+290+90")
    
    Label(root,text="\nThe Capital of " + states[count] + " is?\n", font=18).grid(row=2,column=0)
    
    v = StringVar()


    for i in range(5):
    
        b = Radiobutton(root, text =short_list[i], variable=v,command=ShowChoice, value=short_list[i],font=18,indicatoron=0)
        b.grid(row= i+4,column=1, sticky=W)
        
    gif_one = Text(root,height=8, width=25)
    photo=PhotoImage(file='./unflag.png')
    gif_one.image_create(END, image=photo)
    gif_one.grid(row=10,column=0)
   
 
    Label(root,text='   Score = '+ str(score),font=24).grid(row=10,column=2,sticky=W)
    Label(root,text='\n You have: ' + str(score) + ' of ' + str(count) + ' correct.\n\n',font=24).grid(row=12,column=0,sticky=W)

    if count > 0:
        Label(root,text=' or: ' + str(int(100 * score/count)) + ' Percent',font=24).grid(row=12,column=1,sticky=W)

    done = Button(root,text =' QUIT  ',command=quit).grid(row=16,column=1) 


    root.bind('<Return>',ShowChoice)

    mainloop()


