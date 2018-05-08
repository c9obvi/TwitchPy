from tkinter import *
from tkinter import ttk
from numpy import *


#!!!!!Frame & Variables are below!!!!!

root = Tk()
#root.iconbitmap(root, default = "TpyICO.ico" )
root.geometry('460x175')
root.title("TwitchPy KD Session- By ShareFire.net")

myKills = StringVar()
myDeaths = StringVar()
myWins = StringVar()
sessionKills = IntVar()
kills = float
deaths = float
x = StringVar()

KS = float
DS = float
SKDR = float
#-----------------------------------------------------------------------------------------

#-----Session Tracking Arrays "lists" below -----------------------------------------

#Kills List
seshk = []

#Deaths List
seshd = []

#-----------LEFT-Side    INPUT/ENTRIES   &  labels----------------------------------------

label_1 = Label(root, text="Wins:", fg="Black").grid(row=0, sticky = E)
label_2 = Label(root, text="Kills:", fg="Black").grid(row=1, sticky = E)
label_3 = Label(root, text="Deaths:", fg="Black").grid(row=2, sticky = E)

entry_1 = Entry(root, textvariable = myWins)
entry_1.grid(row=0, column = 1)
entry_2 = Entry(root, textvariable = myKills)
entry_2.grid(row=1, column = 1)
entry_3 = Entry(root, textvariable = myDeaths)
entry_3.grid(row=2, column = 1)

# in case of empty entry fields-------------------------------------------------------------
"""if not entry_1.get():
    entry_1 = "0"
if not entry_2.get():
    entry_2 = "0"
if myDeaths.get():
    entry_3 = "0" """""
#entry_1.insert(0, string= "0")
entry_2.insert(0, string= "0")
entry_3.insert(0, string= "0")

#---------Checkbox for auto post/delete-------------
c = Checkbutton(root, text = "auto post for stream?")
c.grid(columnspan=2, row=3)



#---------------------------------RIGHT-Side labels------------------
label_ws = Label(root, text = "Enter Data and Update!")
label_ws.configure(font='Helvetica 10 bold', fg= "Darkorange")
label_ws.grid(row=0, column=3)

label_KDA = Label(root, text = "Enter K/D and Update!")
label_KDA.grid(row=1, column=3)
label_KDA.configure(font='Helvetica 10 bold', fg= "#73b8d2")

label_killCount = Label(root, text = "Kills this session", font= 'Helvetica 10 bold', fg= "Darkgreen")
label_killCount.grid(row=3, column=3)


label_deathCount = Label(root, text = "Deaths this session", font= 'Helvetica 10 bold', foreground= "Red")
label_deathCount.grid(row=4, column=3)

label_SessionCount = Label(root, text = "K/D this session", font= 'Helvetica 10 bold', foreground= "Black")
label_SessionCount.grid(row=5, column=3)

#Checkbox for auto post/delete. needs function built in..
c = Checkbutton(root, text = "auto post for stream?")
c.grid(columnspan=2, row=3)


#functions are listed below

def wins():
    label_ws.configure(text = "Your wins Today are: " + myWins.get(), font='Helvetica 10 bold' )
    return ;

def KDfunc():

    kills = int(myKills.get())
    deaths = int(myDeaths.get())
    try:
        myKDA = kills/deaths
    except ZeroDivisionError:
        myKDA = kills/1

    label_KDA.configure(text="Your KDA that game: %.3f " % myKDA, font='Helvetica 10 bold')

    seshk.append(kills)
    seshd.append(deaths)

    return;


#----------clear entry boxs -------------------------------#

def clearEntry():
   entry_2.delete(0,END)
   entry_2.insert(0, string="0")

   entry_3.delete(0, END)
   entry_3.insert(0, string="0")
   return;


#--------------Session Functions--------------------
# attempting to make array work with sum and concatenating the sum into session stats.
def sessionTrack():

    label_killCount.configure(text="Kills this session: " + str(sum(seshk)))
    label_deathCount.configure(text="Deaths this session: " + str(sum(seshd)))

    kills = int(sum(seshk))
    deaths = int(sum(seshd))


    try:
        myKDA = kills / deaths
    except ZeroDivisionError:
        myKDA = kills/1

    label_SessionCount.configure(text="K/D This Session: %.3f " % myKDA, font='Helvetica 10 bold')

    return;

    #------------------------------------------joining all functions?-----------------
def action():

    wins()
    KDfunc()
    clearEntry()
    sessionTrack()

    return;



#----------------------Session K & D --------------------------


#------------BUTTON-------------------------

button_1 = ttk.Button(root, text = "Update", command= action)
button_1.grid(row=4, column=1)

root.mainloop()