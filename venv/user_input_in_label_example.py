from tkinter import *


class Input(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.entdat = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        self.ol = Label(text="Objective:")
        self.ol.pack(side=TOP)
        self.ew = Entry(textvariable=self.entdat)
        self.ew.pack(side=TOP)
        self.b = Button(text="OK", command=self.clicked)
        self.b.pack(side=TOP)

    def clicked(self):
        self.dat = Label(self, textvariable=self.entdat )
        self.dat.pack(side=TOP)
        # self.distroy_Widget()

    def distroy_Widget(self):
        pass
        # self.ew.destroy()
        # self.ol.destroy()
        # self.b.destroy()


def main():
    root = Tk()
    root.geometry("240x135+25+50")
    tm = Input(root)
    tm.pack(side=TOP)

    root.mainloop()

if __name__ == '__main__':
    main()