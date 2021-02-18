#COVID 19 DIGITAL TESTING KIT
#Getting and processing the data
import pandas
import sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
dataOne = pandas.read_csv("Cleaned-Data.csv")
stageTwo = dataOne[["Fever", "Tiredness", "Dry-Cough","Difficulty-in-Breathing","Sore-Throat","Pains","Nasal-Congestion", "Runny-Nose", "Diarrhea"]]
severities = []
contact = []
for i in dataOne.index:
    if (dataOne["Severity_Mild"][i]) == 1:
        severities.append(1)
    elif (dataOne["Severity_Moderate"][i]) == 1:
        severities.append(1)
    elif (dataOne["Severity_None"][i]) == 1:
        severities.append(0)
    else:
        severities.append(1)
    if (dataOne["Contact_Dont-Know"][i]) == 1:
        contact.append(0.5)
    elif (dataOne["Contact_No"][i]) == 1:
        contact.append(0)
    else:
        contact.append(1)
dataTwo = {
    "Fever":dataOne["Fever"].values,
    "Tiredness": dataOne["Tiredness"].values,
    "Dry-Cough": dataOne["Dry-Cough"].values,
    "Difficulty-in-Breathing": dataOne["Difficulty-in-Breathing"].values,
    "Sore-Throat": dataOne["Sore-Throat"].values,
    "Pains": dataOne["Pains"].values,
    "Nasal-Congestion": dataOne["Nasal-Congestion"].values,
    "Runny-Nose": dataOne["Runny-Nose"].values,
    "Diarrhea": dataOne["Diarrhea"].values,
    "Contact": contact,
    "Corona": severities
}
stage3 = pandas.DataFrame.from_dict(dataTwo)
stage4 = stage3[["Fever","Tiredness","Dry-Cough","Difficulty-in-Breathing","Sore-Throat","Pains","Nasal-Congestion","Runny-Nose","Diarrhea","Contact"]]
stage42 = stage3["Corona"]

training_data, validation_data, training_labels, validation_labels = train_test_split(stage4.values, stage42.values,test_size = 0.2, random_state = 2)

print("DATA PROCESS DONE")
theBest = 0
k_list =[]
accuracies = []
select = 0
classifier = LogisticRegression()
classifier.fit(training_data,training_labels)
howGood = (classifier.score(validation_data,validation_labels))
print("Accuracy is: " + str(howGood)+"%")


#The GUI


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
running = True
window = Tk()
#"Fever","Tiredness","Dry-Cough","Difficulty-in-Breathing","Sore-Throat","Pains","Nasal-Congestion","Runny-Nose","Diarrhea","Contact"
fever_str_var = tk.StringVar()
tired_str_var = tk.StringVar()
dc_str_var = tk.StringVar()
dib_str_var = tk.StringVar()
st_str_var = tk.StringVar()
pains_str_var = tk.StringVar()
nc_str_var = tk.StringVar()
rn_str_var = tk.StringVar()
diarrhea_str_var = tk.StringVar()
contact_str_var = tk.StringVar()


window.title("COVID-19 Digital Test by Abdulaziz Albastaki")
window.geometry("350x400")
heading = Label(text="Welcome to Aziz's virtual detection center!", bg="blue", fg="white", height="2", width="50")
heading.pack()
welcome = Label(window, text="Hello! I'll detect the status of COVID-19 in you.")
welcome.place(x=0, y=40)

#FEVER
fever = Label(window, text="Fever?")
fever.place(x=0, y=70)
fever_combobox = ttk.Combobox(window, textvariable=fever_str_var, values=["Yes", "No"])
fever_combobox.place(x=100, y=70)

#Tiredness
tiredness = Label(window, text="Tiredness?")
tiredness.place(x=0, y=100)
tired_combobox = ttk.Combobox(window, textvariable=tired_str_var, values=["Yes", "No"])
tired_combobox.place(x=100, y=100)

#Dry Cough
dc = Label(window, text="Dry Cough?")
dc.place(x=0, y=130)
dc_combobox = ttk.Combobox(window, textvariable=dc_str_var, values=["Yes", "No"])
dc_combobox.place(x=100, y=130)

#Difficulty-in-Breathing
dib = Label(window, text="Breathing Difficulty?")
dib.place(x=0, y=160)
dib_combobox = ttk.Combobox(window, textvariable=dib_str_var, values=["Yes", "No"])
dib_combobox.place(x=100, y=160)

#Sore Throat
sthroat = Label(window, text="Sore Throat?")
sthroat.place(x=0, y=190)
sthroat_combobox = ttk.Combobox(window, textvariable=st_str_var, values=["Yes", "No"])
sthroat_combobox.place(x=100, y=190)

#Pain
pains = Label(window, text="Any Pain?")
pains.place(x=0, y=220)
pains_combobox = ttk.Combobox(window, textvariable=pains_str_var, values=["Yes", "No"])
pains_combobox.place(x=100, y=220)

#Stuffy Nose
nasalcongestion = Label(window, text="Stuffy Nose?")
nasalcongestion.place(x=0, y=250)
stuffynose_combobox = ttk.Combobox(window, textvariable=nc_str_var, values=["Yes", "No"])
stuffynose_combobox.place(x=100, y=250)

#Runny Nose
runnynose = Label(window, text="Runny Nose?")
runnynose.place(x=0, y=280)
runnynose_combobox = ttk.Combobox(window, textvariable=rn_str_var, values=["Yes", "No"])
runnynose_combobox.place(x=100, y=280)

#Diarrhea
diarrhea = Label(window, text="Diarrhea?")
diarrhea.place(x=0, y=310)
diarrhea_combobox = ttk.Combobox(window, textvariable=diarrhea_str_var, values=["Yes", "No"])
diarrhea_combobox.place(x=100, y=310)

#Contact
contact2 = Label(window, text="Any Conact?")
contact2.place(x=0, y=340)
contact_combobox = ttk.Combobox(window, textvariable=contact_str_var, values=["Yes","Don't know", "No"])
contact_combobox.place(x=100, y=340)


entryboxes = [fever_combobox, tired_combobox, dc_combobox, dib_combobox, sthroat_combobox, pains_combobox,stuffynose_combobox,runnynose_combobox,diarrhea_combobox,contact_combobox]
entryboxesText = ["Fever", "Tiredness", "Dry Cough", "Breathing Difficulty", "Sore Throat", "Pain","Stuffy Nose","Runny Nose","Diarrhea","Contact"]


def clear():
    for i in entryboxes:
        i.delete(0, END)

output = Text(window, width = 75, height = 6, wrap=WORD, background = "red")

def apply():
    proceed = "True"
    string = ("You have left the following blank: ")
    count = 0
    for i in entryboxes:
        if i.get() == "":
            proceed = "False"
            string += "\n " + entryboxesText[count]
        count += 1
    if proceed == "True":
        values = []
        for i in entryboxes:
            if i.get() == "Yes":
                values.append(1.0)
            elif i.get() == "No":
                values.append(0.0)
            else:
                values.append(0.5)
        result = classifier.predict([values])
        resultfinal = ""
        print(result)
        if result == [0]:
            resultfinal = "NEGATIVE"
        else:
            resultfinal = "POSITIVE"
        #resultfinal = resultfinal
        print("Percentage is "+str(classifier.predict_proba([values])))
        messagebox.showinfo("Thank you!", "Your status of COVID-19 is: " + resultfinal)
    else:
        messagebox.showinfo("Oops!", string)


def exit():
    running = False
    window.destroy()


submit = Button(window, text="SUBMIT", width=6, command=apply, bg="red").place(x=10, y=370)
clearButton = Button(window, text="CLEAR", width=6, command=clear, bg="red").place(x=75, y=370)
exitButton = Button(window, text="EXIT", width=6, command=exit, bg="red").place(x=140, y=370)

window.mainloop()