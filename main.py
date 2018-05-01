from tkinter import *
from tkinter import ttk
from numpy import *

#the update button funtion, including KDA calculation.

def wins():
    label_ws.configure(text = "Your wins Today are: " + myWins.get(), font='Helvetica 10 bold' )

    kills = float(myKills.get())
    deaths = float(myDeaths.get())

    myKDA = kills/deaths

    label_KDA.configure(text="Your KDA is: %.3f " % myKDA, font='Helvetica 10 bold')

    seshk.append(kills)

    x = str(sum(seshk))

    return;

    #clear entry boxs -------------------------------#

def clearEntry():
   entry_2.delete(0,END)
   entry_3.delete(0,END)

   return;


#--------------Session Functions--------------------
# attempting to make array work with sum and concatenating the sum into session stats.
def sessionTrack():

    label_killCount.configure(text= "Your kills this session are: updating here" + x.get(), font='Helvetica 10 bold')

    return;

    #------------------------------------------joining all functions?-----------------
def action():
    wins()
    clearEntry()
    sessionTrack()

    return;





#-----------------------------------------------------------------------------------------

#!!!!!Frame & Variables are below!!!!!

root = Tk()
#root.iconbitmap(root, default = "TpyICO.ico" )
root.geometry('600x175')
root.title("TwitchPy ScoreKeeper")
myKills = StringVar()
myDeaths = StringVar()
myWins = StringVar()
sessionKills = IntVar()


#-----Session Tracking Variables below -----------------------------------------

seshk = []


#-----------LEFT-Side    INPUT/ENTRIES   &  labels----------------------------------------

label_1 = Label(root, text="Wins", fg="Black").grid(row=0, sticky = E)
label_2 = Label(root, text="Kills", fg="Black").grid(row=1, sticky = E)
label_3 = Label(root, text="Deaths", fg="Black").grid(row=2, sticky = E)

entry_1 = Entry(root, textvariable = myWins)
entry_1.grid(row=0, column = 1)
entry_2 = Entry(root, textvariable = myKills)
entry_2.grid(row=1, column = 1)
entry_3 = Entry(root, textvariable = myDeaths)
entry_3.grid(row=2, column = 1)

#---------------------------------RIGHT-Side labels------------------
label_ws = Label(root, text = "Enter Data and Update!")
label_ws.configure(font='Helvetica 10 bold', fg= "#ea9b2c")
label_ws.grid(row=0, column=3)

label_KDA = Label(root, text = "Enter K/D and Update!")
label_KDA.grid(row=1, column=3)
label_KDA.configure(font='Helvetica 10 bold', fg= "#73b8d2")

label_killCount = Label(root, text = "Kills this session", font= 'Helvetica 10 bold', fg= "Green")
label_killCount.grid(row=3, column=3)


label_deathCount = Label(root, text = "Deaths this session", font= 'Helvetica 10 bold', foreground= "Red")
label_deathCount.grid(row=4, column=3)



#----------------------Session K & D --------------------------





#Checkbox for auto post/delete
c = Checkbutton(root, text = "auto post for stream?")
c.grid(columnspan=2, row=3)

#------------BUTTON-------------------------

button_1 = ttk.Button(root, text = "Update", command= action)
button_1.grid(row=4, column=1)



root.mainloop()