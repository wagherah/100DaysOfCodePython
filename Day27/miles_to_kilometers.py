import tkinter
window = tkinter.Tk()
window.geometry('400x200')
window.title('Mile to km Converter')

miles = ''
kilometers = 0

def calculate():
   
    miles =my_entry.get()
    kilometers = int(miles) * 1.6
    my_label2.config(text=kilometers)

my_entry = tkinter.Entry()
my_entry.grid(row=0, column=1)

my_label = tkinter.Label(text='Miles')
my_label.grid(row=0, column=2)

my_label1 = tkinter.Label(text='is equal to')
my_label1.grid(row=1, column=0) 

my_label2 = tkinter.Label(text=kilometers)
my_label2.grid(row=1, column=1)

my_label3 = tkinter.Label(text='kilometers')
my_label3.grid(row=1, column=2)


my_button = tkinter.Button(text='Calculate', command= calculate)
my_button.grid(row=2, column=1)

window.mainloop()