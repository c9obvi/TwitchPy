from tkinter import *


def wins():
    label_ws.configure(text = "Your wins Today are: " + myWins.get(), font='Helvetica 10 bold' )

    kills = float(myKills.get())
    deaths = float(myDeaths.get())

    myKDA = kills/deaths

    label_KDA.configure(text="Your KDA is: %.3f " % myKDA, font='Helvetica 10 bold')



root = Tk()
root.geometry('350x175')
root.title("TwitchPy ScoreKeeper")
myKills = StringVar()
myDeaths = StringVar()
myWins = StringVar()



label_1 = Label(root, text="Wins", fg="Black").grid(row=0, sticky = E)
label_2 = Label(root, text="Kills", fg="Black").grid(row=1, sticky = E)
label_3 = Label(root, text="Deaths", fg="Black").grid(row=2, sticky = E)
entry_1 = Entry(root, textvariable = myWins).grid(row=0, column = 1)
entry_2 = Entry(root, textvariable = myKills).grid(row=1, column = 1)
entry_3 = Entry(root, textvariable = myDeaths).grid(row=2, column = 1)

label_ws = Label(root, text = "Enter Data and Update!")
label_ws.grid(row=0, column=3)
label_KDA = Label(root, text = "Enter K/D and Update!")
label_KDA.grid(row=1, column=3)

x = myKills.get()
y = myDeaths.get()




c = Checkbutton(root, text = "auto post for stream?")
c.grid(columnspan=2, row=3)



button_1 = Button(root, text = "Update", command= wins)
button_1.grid(row=4, column=1)



root.mainloop()