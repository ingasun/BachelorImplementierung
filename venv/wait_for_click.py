import tkinter as tk


def get_input():
    global user_input
    user_input = box.get()
    box.delete("0", "end")
    print('in funktion', user_input)
    var_1.set(1)


root = tk.Tk()
...
var_1 = tk.IntVar()
box = tk.Entry(root)
button = tk.Button(root, text="Click Me", command=get_input)
button.place(relx=.5, rely=.5, anchor="c")
box.place(relx=.5, rely=.5, anchor="c")

print("waiting...")
button.wait_variable(var_1)
print(user_input)
print("done waiting.")
print('warte jetzt wieder')
button.wait_variable(var_1)
print(user_input)
# ok, sieht aus als würde jetzt immer der aktuelle Wert im Entry benutzt - das ist doch super
# hier könnten jetzt die einzelnen Funktionen aufgerufen werden oder das button wait wird einfach im code benutzt
print('genug gewartet')
root.mainloop()