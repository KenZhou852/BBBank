from tkinter import *
from tkinter import ttk
import SplitsInfo

def handleClear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def handleExit(root,split):
    root.destroy()

def handleAddSplit(splits, names, amount, popupWindow, message):
    splits.add_splits(names, amount)
    for name in names:
        name.set("")
    amount.set("")
    message.set("")
    popupWindow.destroy()


def handlePaySplit(splits, name, amount, popupWindow):
    splits.pay_splits(name, amount)
    name.set("")
    amount.set("")
    popupWindow.destroy()

def setMax(amount, name, splits):
    if name.get().lower() in splits.get_split():
        amount.set(splits.get_split()[name.get()])

def payConfirmation(root, splits, name, amount):
    top = Toplevel(root, background="#e7c7ff")
    top.geometry("250x175")
    top.title("Bank of BB")
    top.grid()

    ttk.Label(top, text="Payment Summary", font=("arial",14, "bold")).grid(column=0, row=0, columnspan=3, pady=10, padx=20)
    
    if name.get() in splits.get_split():
        ttk.Label(top, text=("%s's Balance" % (name.get().title())), font=("arial", 12, "bold")).grid(column=0, row=1, columnspan=3, padx=20, pady=10)
        ttk.Label(top, text="{:,}".format(splits.get_split()[name.get()]), font=("arial", 11)).grid(column=0, row=2, padx=10)
        ttk.Label(top, text= "->", font=("arial", 11, "bold")).grid(column=1, row=2)
        ttk.Label(top, text="{:,}".format(splits.get_split()[name.get()]-int(amount.get())), font=("arial", 11)).grid(column=2, row=2, padx=10)
    else:
        ttk.Label(top, text="Person not found", font=("arial", 12, "bold"), foreground="#301934").grid(column=0, row=1, columnspan=3, padx=20, pady=10)
    
    Button(top, text="Confirm", command=lambda: handlePaySplit(splits, name, amount, top), background="lightgreen").grid(column=0, row=3, padx=10, pady=10)
    Button(top, text="Cancel", command=top.destroy, background="#f04654").grid(column=2, row=3, padx=10, pady=10)

def addConfirmation(root, splits, names, amount,message):
    top = Toplevel(root, background="#e7c7ff")
    top.geometry("250x380")
    top.title("Bank of BB")
    top.grid()

    party_list = [name.get() for name in names if name.get() != ""]
    party_size = len(party_list)
    party_list = ", ".join(party_list)

    ttk.Label(top, text="Split Summary", font=("arial",14, "bold")).grid(column=0, row=0, columnspan=2, pady=10, padx=20)

    ttk.Label(top, text=("Party"), font=("arial", 12, "bold")).grid(column=0, row=1, columnspan=2, padx=10, pady=3)
    ttk.Label(top, text=party_list, font=("arial", 11)).grid(column=0, row=2, columnspan=2, padx=10, pady=1)

    if message.get() != "":
        ttk.Label(top, text="Item Split", font=("arial",12,"bold")).grid(column=0, row=3, columnspan=2, padx=30, pady=5)
        ttk.Label(top, text=message.get(), font=("arial",11)).grid(column=0, row=4, columnspan=2, padx=30)

    ttk.Label(top, text="Amount", font=("arial", 12, "bold")).grid(column=0, row=5, columnspan=2, padx=30, pady=5)
    ttk.Label(top, text="{:,} total".format(int(amount.get())),font=("arial", 11)).grid(column=0, row=6, columnspan=2, padx=30)
    ttk.Label(top, text="{:,} mesos per person".format(int(amount.get())//party_size),font=("arial", 11)).grid(column=0, row=7, columnspan=2, padx=30)

    Button(top, text="Confirm", command=lambda: handleAddSplit(splits, names, amount, top, message), background="lightgreen").grid(column=0, row=8, padx=10, pady=10)
    Button(top, text="Cancel", command=top.destroy, background="#f04654").grid(column=1, row=8, padx=10, pady=10)

def handleShowAll(frame, splits):
    idx = 0
    for key in splits.get_split():
        ttk.Label(frame, text=(key.title()), font=("arial",12), width=10, borderwidth=3, background="#dab5f5", relief=GROOVE, foreground="#301934").grid(column=0, row=idx)
        ttk.Label(frame, text=str("{:,}".format(splits.get_split()[key])), width=15, font=("arial", 12), borderwidth=5, relief=GROOVE, background="white").grid(column=1, row=idx)
        idx+=1

def menuBar(root,splits):
    button_frm_top = ttk.Frame(root, padding=10, style="MenuBar.TFrame")
    button_frm_top.pack(side="top", fill=X)
    menu1 = ttk.Button(button_frm_top, text="Main", command=lambda:main(root,splits)).grid(column=0,row=0)
    menu2 = ttk.Button(button_frm_top, text="New Split", command=lambda:update(root,splits)).grid(column=1, row=0)
    menu3 = ttk.Button(button_frm_top, text="Pay", command=lambda:pay(root, splits)).grid(column=2, row=0)
    menu4 = ttk.Button(button_frm_top, text="Quit", command=lambda: handleExit(root, splits)).grid(column=3, row=0)

def main(root, splits):
    handleClear(root)
    menuBar(root,splits)

    main_frm = ttk.Frame(root, padding=25)
    main_frm.pack()

    button_frm_bot = ttk.Frame(root, padding=10)
    button_frm_bot.pack(side="bottom")
    btn1 = ttk.Button(button_frm_bot, text="Show All", command=lambda:handleShowAll(main_frm, splits), style="Function.TButton").grid(column=0, row=0)
    btn2 = ttk.Button(button_frm_bot, text="Clear", command=lambda:handleClear(main_frm), style="Function.TButton").grid(column=1, row=0)
    handleShowAll(main_frm, splits)

def update(root, splits):
    handleClear(root)
    menuBar(root,splits)

    name_entries = []
    amount_var = StringVar()
    message = StringVar()

    main_frm = ttk.Frame(root, padding=25)
    main_frm.pack()

    ttk.Label(main_frm, text="Names", font=("arial", 12)).grid(column=0, row=0, padx=5)
    ttk.Label(main_frm, text="Amount", font=("arial", 12)).grid(column=0, row=6, pady=20, padx=5)
    ttk.Label(main_frm, text="Item Name\n (optional)", font=("arial",12)).grid(column=0, row=7)

    for i in range(6):
        name_var = StringVar()
        name_entries.append(name_var)
        ttk.Entry(main_frm, textvariable=name_var).grid(column=1, row=i)
    
    ttk.Entry(main_frm, textvariable=amount_var).grid(column=1, row=6)
    ttk.Entry(main_frm, textvariable=message).grid(column=1, row=7)

    update_btn = ttk.Button(root, text="Confirm", command=lambda:addConfirmation(root, splits,name_entries, amount_var, message), style="Function.TButton")
    update_btn.pack()

def pay(root, splits):
    handleClear(root)
    menuBar(root, splits)

    main_frm = ttk.Frame(root, padding=25)
    main_frm.pack()

    name = StringVar()
    amount= StringVar()

    ttk.Label(main_frm, text="Name", font=("arial", 12)).grid(column=0, row=0, padx=10)
    ttk.Entry(main_frm, textvariable=name).grid(column=1, row=0)

    ttk.Label(main_frm, text="Amount", font=("arial", 12)).grid(column=0, row=1, padx=10)
    ttk.Entry(main_frm, textvariable=amount).grid(column=1, row=1)
    ttk.Button(main_frm, text="MAX", command=lambda: setMax(amount, name, splits), style="Function.TButton").grid(column=2, row=1, padx=5)

    ttk.Button(root, text="Apply", command=lambda: payConfirmation(root, splits, name, amount), style="Function.TButton").pack()