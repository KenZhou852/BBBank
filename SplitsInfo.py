import csv
import os
from pathlib import Path

class SplitsInfo:
    def __init__(self, filepath):
        self.splits = {}
        self.filepath=filepath

        with open(os.path.join(Path.home(), self.filepath)) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                row[1] = int(row[1])
                self.splits[row[0]] = row[1]

        self.sort()
        
    def sort(self):
        self.splits = dict(sorted(self.splits.items(), key=lambda item: item[1], reverse=True))

    def add_splits(self, names, amount):
        payees = [name.get().lower() for name in names if name.get() != ""]
        amount_per_person = int(amount.get()) // len(payees)
        namelist = [name.lower() for name in self.splits.keys()]
        

        for payee in payees:
            if payee in namelist:
                self.splits[payee] += amount_per_person
            else:
                self.splits[payee] = amount_per_person
        self.update_splits()

    def pay_splits(self, name, amount):
        if name.get().lower() in self.splits.keys():
            self.splits[name.get().lower()] -= int(amount.get())
            if self.splits[name.get().lower()] <= 0:
                self.splits.pop(name.get().lower())

    def update_splits(self):
        with open(os.path.join(Path.home(), self.filepath), mode="w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for key in self.splits:
                writer.writerow([key, self.splits[key]])

    def get_split(self):
        return self.splits