import tkinter as tk
from tkinter import messagebox,simpledialog
root=tk.Tk()
root.withdraw()
h=simpledialog.askfloat("身長","あなたの身長を入力してください")/100
w=simpledialog.askfloat("体重","あなたの体重を入力してください")
bmi=w/(h*h)
messagebox.showinfo("BMI",f"あなたのBMIは{bmi}です")
