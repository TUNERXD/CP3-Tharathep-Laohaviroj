# import
from tkinter import ttk
import tkinter as tk

# information

# For men: 10 x weight (kg) + 6.25 x height (cm) – 5 x age (y) + 5 (kcal / day)
# For women: 10 x weight (kg) + 6.25 x height (cm) – 5 x age (y) -161 (kcal / day)
# sedentary = 1.2
# lightly_active = 1.375
# moderately_active = 1.550
# very_active = 1.725
# extra_active = 1.9
# protein = * 0.3 then / 4


# functions
def buildmuscle(event):

    sedentary = 1.2
    lightly_active = 1.375
    moderately_active = 1.550
    very_active = 1.725
    extra_active = 1.9

    sex = sex_result.get()
    activity = active_result.get()
    weight = weight_input.get()
    height = height_input.get()
    age = age_input.get()

    if sex == "Male":
        bmr = round(float(10 * float(weight)) + (6.25 * int(height)) - (5 * int(age)) + 5, 0)

        if activity == "Sedentary":
            calorie = round(float((((bmr * sedentary) + 500) * 0.3)/4), 0)
            result_result.configure(text=calorie, fg="Green")
        elif activity == "Lightly active":
            calorie = round(float((((bmr * lightly_active) + 500) * 0.3)/4), 0)
            result_result.configure(text=calorie, fg="Green")
        elif activity == "Moderately active":
            calorie = round(float(((bmr * moderately_active + 500) * 0.3)/4), 0)
            result_result.configure(text=calorie, fg="Green")
        elif activity == "Very active":
            calorie = round(float((((bmr * very_active) + 500) * 0.3)/4), 0)
            result_result.configure(text=calorie, fg="Green")
        elif activity == "Extra active":
            calorie = round(float((((bmr * extra_active) + 500) * 0.3)/4), 0)
            result_result.configure(text=calorie, fg="Green")

    elif sex == "Female":
        bmr = round(float(10 * float(weight)) + (6.25 * int(height)) - (5 * int(age)) - 161, 0)

        if activity == "Sedentary":
            calorie = round(float((((bmr * sedentary) + 500) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Green")
        elif activity == "Lightly active":
            calorie = round(float((((bmr * lightly_active) + 500) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Green")
        elif activity == "Moderately active":
            calorie = round(float(((bmr * moderately_active + 500) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Green")
        elif activity == "Very active":
            calorie = round(float((((bmr * very_active) + 500) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Green")
        elif activity == "Extra active":
            calorie = round(float((((bmr * extra_active) + 500) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Green")


def loseweight(event):

    sedentary = 1.2
    lightly_active = 1.375
    moderately_active = 1.550
    very_active = 1.725
    extra_active = 1.9

    sex = sex_result.get()
    activity = active_result.get()
    weight = weight_input.get()
    height = height_input.get()
    age = age_input.get()

    if sex == "Male":
        bmr = round(float(10 * float(weight)) + (6.25 * int(height)) - (5 * int(age)) + 5, 0)

        if activity == "Sedentary":
            calorie = round(float((((bmr * sedentary) * 0.9) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")
        elif activity == "Lightly active":
            calorie = round(float((((bmr * lightly_active) * 0.9) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")
        elif activity == "Moderately active":
            calorie = round(float((((bmr * moderately_active) * 0.8) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")
        elif activity == "Very active":
            calorie = round(float((((bmr * very_active) * 0.8) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")
        elif activity == "Extra active":
            calorie = round(float((((bmr * extra_active) * 0.8) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")

    elif sex == "Female":
        bmr = round(float(10 * float(weight)) + (6.25 * int(height)) - (5 * int(age)) - 161, 0)

        if activity == "Sedentary":
            calorie = round(float((((bmr * sedentary) * 0.9) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")
        elif activity == "Lightly active":
            calorie = round(float((((bmr * lightly_active) * 0.9) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")
        elif activity == "Moderately active":
            calorie = round(float((((bmr * moderately_active) * 0.9) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")
        elif activity == "Very active":
            calorie = round(float((((bmr * very_active) * 0.8) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")
        elif activity == "Extra active":
            calorie = round(float((((bmr * extra_active) * 0.8) * 0.4) / 4), 0)
            result_result.configure(text=calorie, fg="Red")


def maintainweight(event):

    sedentary = 1.2
    lightly_active = 1.375
    moderately_active = 1.550
    very_active = 1.725
    extra_active = 1.9

    sex = sex_result.get()
    activity = active_result.get()
    weight = weight_input.get()
    height = height_input.get()
    age = age_input.get()

    if sex == "Male":
        bmr = round(float(10 * float(weight)) + (6.25 * int(height)) - (5 * int(age)) + 5, 0)

        if activity == "Sedentary":
            calorie = round(float(((bmr * sedentary) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")
        elif activity == "Lightly active":
            calorie = round(float(((bmr * lightly_active) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")
        elif activity == "Moderately active":
            calorie = round(float(((bmr * moderately_active) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")
        elif activity == "Very active":
            calorie = round(float(((bmr * very_active) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")
        elif activity == "Extra active":
            calorie = round(float(((bmr * extra_active) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")

    elif sex == "Female":
        bmr = round(float(10 * float(weight)) + (6.25 * int(height)) - (5 * int(age)) - 161, 0)

        if activity == "Sedentary":
            calorie = round(float(((bmr * sedentary) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")
        elif activity == "Lightly active":
            calorie = round(float(((bmr * lightly_active) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")
        elif activity == "Moderately active":
            calorie = round(float(((bmr * moderately_active) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")
        elif activity == "Very active":
            calorie = round(float(((bmr * very_active) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")
        elif activity == "Extra active":
            calorie = round(float(((bmr * extra_active) * 0.3) / 4), 0)
            result_result.configure(text=calorie, fg="Blue")


mainWindow = tk.Tk()

# Title
title_label = tk.Label(mainWindow, text="Protein Intake Calculator")
title_label.grid(row=0, column=0)

# Function Buttons
build_muscle_button = tk.Button(mainWindow, text="Build Muscle", width=15, fg="Green")
build_muscle_button.grid(row=2, column=0)
build_muscle_button.bind('<Button-1>', buildmuscle)

lose_weight_button = tk.Button(mainWindow, text="Lose Weight", width=15, fg="Red")
lose_weight_button.grid(row=3, column=0)
lose_weight_button.bind('<Button-1>', loseweight)

maintain_weight_button = tk.Button(mainWindow, text="Maintain Weight", width=15, fg="Blue")
maintain_weight_button.grid(row=4, column=0)
maintain_weight_button.bind('<Button-1>', maintainweight)

# information Input

age_label = tk.Label(mainWindow, text="Age: ")
age_label.grid(row=1, column=4)
age_input = tk.Entry(mainWindow, width=18)
age_input.grid(row=1, column=5)

sex_label = tk.Label(mainWindow, width=15, text="Sex: ")
sex_label.grid(row=2, column=4)
choices = ["Male", "Female"]
sex_choices = tk.StringVar(mainWindow)
sex_result = ttk.Combobox(mainWindow, values=choices, width=15)
sex_result.grid(row=2, column=5)

height_label = tk.Label(mainWindow, text="Height(cm): ")
height_label.grid(row=3, column=4)
height_input = tk.Entry(mainWindow, width=18)
height_input.grid(row=3, column=5)

weight_label = tk.Label(mainWindow, text="Weight(Kg.): ")
weight_label.grid(row=4, column=4)
weight_input = tk.Entry(mainWindow, width=18)
weight_input.grid(row=4, column=5)

active_label = tk.Label(mainWindow, width=15, text="Activity level: ")
active_label.grid(row=5, column=4)

# Activity Levels
choices = ["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"]
active_choices = tk.StringVar(mainWindow)
active_result = ttk.Combobox(mainWindow, values=choices, width=15)
active_result.grid(row=5, column=5)
active_title = tk.Label(mainWindow, text="Activity Level:", fg="Blue")
active_title.grid(row=7, column=0)
active_label2 = tk.Label(mainWindow, text="Sedentary (Little or no exercise)")
active_label2.grid(row=8, column=0)
active_label3 = tk.Label(mainWindow, text="Lightly active (Light exercise/sports 3-5 days a week)")
active_label3.grid(row=9, column=0)
active_label4 = tk.Label(mainWindow, text="Moderately active (Moderate exercise/sports 3-5 days a week)")
active_label4.grid(row=10, column=0)
active_label5 = tk.Label(mainWindow, text="Very active (Hard exercise/sports 6-7 days a week)")
active_label5.grid(row=11, column=0)
active_label6 = tk.Label(mainWindow, text="Extra active (Hard exercise/sports 6-7 days a week, plus physical job)")
active_label6.grid(row=12, column=0)

# Result
result_label = tk.Label(mainWindow, text="Result --> Protein in grams")
result_label.grid(row=6, column=5)
result_result = tk.Label(mainWindow, text="Protein:")
result_result.grid(row=7, column=5)
mainWindow.mainloop()
