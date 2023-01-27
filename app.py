from tkinter import *
import random

root = Tk()
root.title("Random Countries")
root.geometry("1600x1600")
root.configure(background="pale green")

firstTime = True

title = Label(
    root, text="Random Countries and Capitals", font=("arial", 30), bg="pale green"
)
CountryAdder = Entry(root, font=("arial", 30))
CapitalAdder = Entry(root, font=("arial", 30))
title.place(relx=0.5, rely=0.05, anchor=CENTER)
CountryAdder.place(relx=0.45, rely=0.15, anchor=CENTER)
CapitalAdder.place(relx=0.45, rely=0.25, anchor=CENTER)

CountryList = []
CapitalList = []

CountryListLabel = Label(
    root, text="No Countries Added", font=("arial", 30), bg="pale green"
)
CapitalListLabel = Label(
    root, text="No Capitals Added", font=("arial", 30), bg="pale green"
)
CountryListLabel.place(relx=0.5, rely=0.35, anchor=CENTER)
CapitalListLabel.place(relx=0.5, rely=0.45, anchor=CENTER)


def Adder():
    global CountryList, CapitalList, firstTime
    if firstTime:
        CountryListLabel["text"] = ""
        CapitalListLabel["text"] = ""
        firstTime = False
    country = CountryAdder.get()
    capital = CapitalAdder.get()
    CountryList.append(country)
    CapitalList.append(capital)
    CountryAdder.delete(0, END)
    CapitalAdder.delete(0, END)
    CountryListLabel["text"] += f"{country}, "
    CapitalListLabel["text"] += f"{capital}, "

def Clear():
    global CountryList, CapitalList, firstTime
    CountryList = []
    CapitalList = []
    CountryListLabel["text"] = "No Countries Added"
    CapitalListLabel["text"] = "No Capitals Added"
    firstTime = True

ClearBTN = Button(
    root, text="Clear List", font=("arial", 20), command=Clear, bg="pale turquoise"
)
SubmitBTN = Button(
    root, text="Submit", font=("arial", 20), command=Adder, bg="pale turquoise"
)
ClearBTN.place(relx=0.65, rely=0.15, anchor=CENTER)
SubmitBTN.place(relx=0.65, rely=0.25, anchor=CENTER)
CountryDisplay = Label(root, font=("arial", 30), bg="pale green")
CapitalDisplay = Label(root, font=("arial", 30), bg="pale green")
CountryDisplay.place(relx=0.5, rely=0.65, anchor=CENTER)
CapitalDisplay.place(relx=0.5, rely=0.75, anchor=CENTER)


def CapitalCountryGenerator():
    RandomCountryIndex = random.randint(0, len(CountryList) - 1)
    RandomCapitalIndex = random.randint(0, len(CapitalList) - 1)
    RandomCountry = CountryList[RandomCountryIndex]
    RandomCapital = CapitalList[RandomCapitalIndex]
    CountryDisplay["text"] = f"Your Random Country Is {RandomCountry}"
    CapitalDisplay["text"] = f"Your Random Country Is {RandomCapital}"


TheBTN = Button(
    root,
    command=CapitalCountryGenerator,
    text="Display Random Countries and Capitals",
    font=("arial", 20),
    bg="pale turquoise",
)
TheBTN.place(relx=0.5, rely=0.55, anchor=CENTER)

root.mainloop()