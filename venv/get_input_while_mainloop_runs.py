from tkinter import *
from tkinter import ttk

root = Tk()
loop = 0
block = BooleanVar(root, False)

while loop < 2:

    print ('loop')

    def user_data():
        user_input = data.get()
        print (user_input)
        block.set(False)

    lb=ttk.Label(root, text="Enter data")
    instruction_label = ttk.Label(root, text='update label')
    data=ttk.Entry(root)
    bt=ttk.Button(root, text='Ok', command=user_data)

    lb.grid(row=0, column=1)
    instruction_label.grid(row=1)
    data.grid(row=0, column=2)
    bt.grid(row=0, column=3)

    block.set(True)
    root.wait_variable(block)
    loop += 1

print ('left loop')
root.mainloop()