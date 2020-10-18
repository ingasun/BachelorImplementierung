import tkinter


class Prompt:
    def button_action(self):
        self.my_entry = self.ent.get()  # this is the variable I wanna use in another function
        print(self.my_entry)

    def __init__(self, master):
        self.lbl = tkinter.Label(master, text="Write Something")
        self.ent = tkinter.Entry(master)
        self.btn = tkinter.Button(master, text="Get That Something", command=self.button_action)
        self.lbl.pack()
        self.ent.pack()
        self.btn.pack()


root = tkinter.Tk()
root.title("Widget Example")
prompt = Prompt(root)
# mal sehen ob es hier abgerufen werden kann -> nein scheinbar nicht
# man kommt erst an die Werte wenn das Fenster weg ist
root.mainloop()

bla = prompt.my_entry
print(bla)
# prompt.my_entry