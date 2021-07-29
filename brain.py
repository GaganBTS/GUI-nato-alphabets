import pandas
from tkinter import messagebox


def nato_produce(text):
    data = pandas.read_csv("nato_phonetic_alphabet.csv")

    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

    word = text.upper()
    if " " in word:
        messagebox.showerror(title="INVALID",message="Don't include any spaces")
    else:
     try:
        output_list = [phonetic_dict[letter] for letter in word]
     except:
        messagebox.showerror(title="INVALID", message="please enter alphabets only")
     else:
        return output_list