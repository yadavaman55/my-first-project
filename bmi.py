import tkinter as tk
from tkinter import messagebox
import datetime
import matplotlib.pyplot as plt

# File to store BMI history
FILE_NAME = "bmi_data.txt"

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0: 
            messagebox.showerror("Error", "Weight and Height must be positive")
            return

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi}\nCategory: {category}")

        # Save data
        save_data(weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Function to save data
def save_data(weight, height, bmi, category):
    with open(FILE_NAME, "a") as file:
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        file.write(f"{date},{weight},{height},{bmi},{category}\n")

# Function to show history
def show_history():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()
            if data.strip() == "":
                messagebox.showinfo("History", "No data found")
            else:
                messagebox.showinfo("BMI History", data)
    except FileNotFoundError:
        messagebox.showinfo("History", "No data file found")

# Function to show graph
def show_graph():
    try:
        dates = []
        bmi_values = []

        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                dates.append(parts[0])
                bmi_values.append(float(parts[3]))

        if len(bmi_values) == 0:
            messagebox.showinfo("Graph", "No data to plot")
            return

        plt.plot(dates, bmi_values, marker='o')
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("BMI Value")
        plt.title("BMI Trend")
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        messagebox.showerror("Error", "No data available")

# GUI Setup
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("350x400")

tk.Label(root, text="Advanced BMI Calculator", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Weight (kg)").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (m)").pack()
entry_height = tk.Entry(root)
entry_height.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

tk.Button(root, text="View History", command=show_history).pack(pady=5)
tk.Button(root, text="Show Graph", command=show_graph).pack(pady=5)

tk.Label(root, text="Python Mini Project", fg="gray").pack(side="bottom")

root.mainloop()