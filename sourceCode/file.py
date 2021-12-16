from tkinter import *
from tkinter import messagebox
from datetime import datetime
import requests

WINDOWCOLOUR = "#152D35"
CANVASCOLOUR = "#BFD8B8"
TEXTCOLOUR = "black"
API_KEY = "<YOUR_API_KEY>" # insert your API Key here, inside double quotes
OPTEDTYPE = []
SHEETY_ENDPOINT = "<YOUR_SHEETY_ENDPOINT_HERE>" # insert your Sheety endpoint here, relevant to your google sheet

window = Tk()
window.config(padx=20, pady=25, bg=WINDOWCOLOUR)
window.title("Expense report")

canvas = Canvas(width=500, height=450, bg=CANVASCOLOUR, highlightthickness=0)
canvas.create_text(264, 60, text="💸 Expense report 💸", font={"Comic Sans MS", 40, "bold"}, fill=TEXTCOLOUR)

moneyImg = PhotoImage(file="images/picture.crdownload")
canvas.create_image(280, 299, image=moneyImg)

canvas.grid(column=0, row=0)


def display_selected():
    choice = variable.get()
    OPTEDTYPE.append(choice)
    print(OPTEDTYPE[0])


def successMsg():
    headers = {
        "x-app-key": API_KEY,
    }
    sheetyEndPoint = SHEETY_ENDPOINT
    todayDate = datetime.now().date().strftime('%d-%m-%Y')
    remarks = remarksEntry.get()
    moneyToAdd = moneyReceipt.get()
    print(moneyToAdd)
    typeOfexpense = OPTEDTYPE[0]
    amountOfExpense = float(moneyEntry.get())
    print(amountOfExpense)

    sheetInputs = {
        "expSummary": {
            "date": todayDate,
            "particulars": remarks,
            "receipts": moneyToAdd,
            typeOfexpense: amountOfExpense
        }
    }
    response = requests.post(url=sheetyEndPoint, json=sheetInputs, headers=headers)
    print(response.text)

    messagebox.showinfo(title="Good job", message="Successfully entered")
    OPTEDTYPE.clear()


def exitApp():
    window.destroy()


choices = ['home', 'stationary', 'vacation', 'medicines', 'food', 'online', 'fuel', 'receipts']

# setting variable for Integers
variable = StringVar()
variable.set("Choose")

# creating widget
dropdown = OptionMenu(
    window,
    variable,
    *choices,
    command=display_selected
)

print(OPTEDTYPE)

dropdown.config(bg="white", highlightthickness=0, width=20)
# positioning widget
dropdown.place(x=189, y=89)

moneyReceipts = Label(text="Money received: ", width=15, bg=CANVASCOLOUR, fg=TEXTCOLOUR)
moneyReceipts.place(x=83, y=130)

moneyReceipt = Entry(width=25)
moneyReceipt.place(x=190, y=130)

money = Label(text="Total expense: ", width=15, bg=CANVASCOLOUR, fg=TEXTCOLOUR)
money.place(x=87, y=160)

moneyEntry = Entry(width=25, state="normal")
moneyEntry.place(x=190, y=160)

specialRemarks = Label(text="Special Remarks: ", width=15, bg=CANVASCOLOUR, fg=TEXTCOLOUR)
specialRemarks.place(x=80, y=190)

remarksEntry = Entry(width=25)
remarksEntry.place(x=190, y=190)

submitButton = Button(text="Enter", width=20, command=successMsg)
submitButton.config(bg="white")
submitButton.place(x=192, y=220)

exitApplication = Button(text="Exit application", width=20, command=exitApp)
exitApplication.config(bg="#345B63", fg="white")
exitApplication.place(x=192, y=248)
window.mainloop()
