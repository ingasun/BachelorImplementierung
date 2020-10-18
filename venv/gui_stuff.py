from tkinter import*
# from PIL import ImageTk, Image

root = Tk()
root.title('Cooles Spiel')
root.geometry('900x900')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

viewerPane = LabelFrame(root)
actionPane = LabelFrame(root, bg="blue")

#frame = LabelFrame(root, text='This is my frame', padx=50, pady=50)
#frame.pack(padx=10, pady=10)
viewerPane.grid(row=0,column=0, sticky="nsew")
actionPane.grid(row=0,column=1, sticky="nsew")

button = Button(viewerPane, text='Wow')
button.pack()

root.mainloop()