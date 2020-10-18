import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


class StartPage(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.hallo = 'hey beauty'
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.entry1 = tk.Entry(self, width=7, borderwidth=5)
        self.entry1.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        calculate_button = tk.Button(self, text="Get Text",
                                     command=self.get_text)
        calculate_button.pack()
        # mal schauen ob es in stringvar gespeichert werden kann
        var = tk.StringVar()
        self.x = tk.Entry(self, width=7, borderwidth=5, textvariable=var)
        label = tk.Label(self, bg='blue', text=self.x)
        label.pack()

    def get_text(self):
        self.content = (self.x.get())
        #self.text.append(entry)
        #self.update()
        #print(self.text)


class PageTwo(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        page1 = self.controller.get_page(PageOne)
        label = tk.Label(self, bg='blue', text=page1.entry1.get())
        label.pack()


app = SeaofBTCapp()
app.mainloop()