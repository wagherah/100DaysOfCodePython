import tkinter

# creates a window
window = tkinter.Tk()
window.config(padx=20, pady=20)

def button_clicked():
    text = my_entry.get()
    my_label.config(text=text)

# creating title
window.title('First GUI Program')

window.minsize(width=500, height=300)

# a label
my_label = tkinter.Label(text='Im a Label')
# use to edit properties
# my_label.config(text='Updated text')
# place it on the screen
my_label.pack()

my_button = tkinter.Button(text="Save", command=button_clicked)
my_button.pack()

my_entry = tkinter.Entry()
my_entry.pack()


# it will keep the main window open
# should be in the end of screen
window.mainloop()
