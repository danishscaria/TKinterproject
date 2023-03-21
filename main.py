from tkinter import*
from tkinter import ttk
root = Tk()
root.title("TPchange")
root.geometry("1000x500")
root.iconbitmap("./")
mbtn1 = Menubutton(root,text="Multimini 8",width=150,bg="#F3D2BE")
mbtn1.grid()
mbtn1.menu = Menu(mbtn1, tearoff = 0)
mbtn1["menu"] = mbtn1.menu
pythonVar = IntVar()
javaVar = IntVar()
phpVar = IntVar()
mbtn1.menu.add_checkbutton(label="Python", variable=pythonVar)
mbtn1.menu.add_checkbutton(label="Java", variable=javaVar)
mbtn1.menu.add_checkbutton(label="PHP", variable=phpVar,)
mbtn1.pack()
mbtn2 = Menubutton(root, text="Filter Sampler", width=150,bg="#F3D2BE")
mbtn2.menu = Menu(mbtn2, tearoff = 0)
mbtn2["menu"] = mbtn2.menu
pythonVar = IntVar()
javaVar = IntVar()
phpVar = IntVar()
mbtn2.menu.add_checkbutton(label="Python", variable=pythonVar)
mbtn2.menu.add_checkbutton(label="Java", variable=javaVar)
mbtn2.menu.add_checkbutton(label="PHP", variable=phpVar)
mbtn2.pack(pady=20)

mbtn3 = Menubutton(root, text="Nano Sampler", width=150,bg="#F3D2BE")

table = ttk.Treeview(root, columns=('column1', 'column2', 'column3', 'column4'), show='headings')
table.pack()

# Add column headings to the treeview
table.heading('column1', text='Column 1')
table.heading('column2', text='Column 2')
table.heading('column3', text='Column 3')
table.heading('column4', text='Column 4')

# Add 6 rows of data to the table
for i in range(6):
    table.insert('', 'end', values=('Row %s, Column 1' % (i+1), 'Row %s, Column 2' % (i+1), 'Row %s, Column 3' % (i+1), 'Row %s, Column 4' % (i+1)))
mbtn3.menu = Menu(mbtn3, tearoff = 0)
mbtn3["menu"] = mbtn3.menu
mbtn3.pack()
root.mainloop()



# import tkinter as tk
# from tkinter import*
#
# import tkinter as ttk
# root = tk.Tk()
# root.title("TPchange")
# root.geometry("1000x500")
# root.iconbitmap("./")
# # Create a list of options for the dropdown
# options = [table = ttk.Treeview(root, columns=('column1', 'column2', 'column3', 'column4'), show='headings')
# table.pack()
#
# # Add column headings to the treeview
# table.heading('column1', text='Column 1')
# table.heading('column2', text='Column 2')
# table.heading('column3', text='Column 3')
# table.heading('column4', text='Column 4')
#
# # Add 6 rows of data to the table
# for i in range(6):
#     table.insert('', 'end', values=('Row %s, Column 1' % (i+1), 'Row %s, Column 2' % (i+1), 'Row %s, Column 3' % (i+1), 'Row %s, Column 4' % (i+1)))
# ]
#
# # Create a Tkinter variable to store the selected option
# selected_option = tk.StringVar(root)
# selected_option.set(options[0]) # Set the default option
#
# # Create the dropdown button using the OptionMenu widget
# dropdown = tk.OptionMenu(root, selected_option, *options, )
# dropdown.pack()
#
# # Change the color of the dropdown button to pink
# dropdown.configure(background='pink')
#
# # Change the label of the dropdown button to 'multimini'
# dropdown.configure(text='multimini')
#
# root.mainloop()








