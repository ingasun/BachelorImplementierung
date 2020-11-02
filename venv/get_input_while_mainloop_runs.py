from tkinter import *
from tkinter import ttk
from time import time, sleep

root = Tk()
loop = 0
block = BooleanVar(root, False)


while loop < 5:

    print('loop')

    # vielleicht lieber ne extra function für das label
    def label_behaviour():
        instruction_label.config(text="new text")

    def user_data():
        print(instruction_label['text'])
        # instruction_label.destroy()
        user_input = data.get()
        print(user_input)
        instruction_label.config(text="new text")
        # wird für eine sekunde angezeigt
        root.update_idletasks()
        sleep(5)
        print(instruction_label['text'])
        block.set(False)

    lb = ttk.Label(root, text='hier was eingeben')
    instruction_label = ttk.Label(root, text='Nächste Eingabe bitte')
    data = ttk.Entry(root)
    bt = ttk.Button(root, text='Ok', command=user_data)

    lb.grid(row=0, column=1)
    instruction_label.grid(row=1)
    data.grid(row=0, column=2)
    bt.grid(row=0, column=3)
    block.set(True)

    root.wait_variable(block)
    loop += 1

print ('left loop')
# Ändert sich erst nach while Schleife
#root.update_idletasks()
root.mainloop()