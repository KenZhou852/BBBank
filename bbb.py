from tkinter import *
from tkinter import ttk
import SplitsInfo
import functions

splits_filepath = "Desktop/splits.csv"
splits = SplitsInfo.SplitsInfo(splits_filepath)

root = Tk()
root.title("Bank of BB")
root.geometry("325x500")
root.configure(background='#e7c7ff')

ttk.Style().configure('TFrame', background="#e7c7ff")
ttk.Style().configure('TLabel', background="#e7c7ff", foreground="#301934")
ttk.Style().configure('MenuBar.TFrame', background="#b168e8")
ttk.Style().configure('TButton', background="#B388FF", foreground="#301934")
ttk.Style().configure('Function.TButton', background="#e7c7ff")

functions.main(root, splits)

root.mainloop()