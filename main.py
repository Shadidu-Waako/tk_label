from tkinter import *

my_window = Tk()

# 2.INTRODUCTION TO TKINTER LABEL WIDGET

# label_1 = Label(my_window, text='Hello World')
# label_1.pack()
# label_2 = Label(my_window, text='Hello World, how are you today?')
# label_2.pack()

# label_3 = Label(my_window, text='I am label three')
# label_4 = Label(my_window, text='I am label four')
# label_3.pack()
# label_4.pack()


# HOW TO SET THE TITLE OF A PYTHON TKINTER WINDOW

# my_window.title('Demo')


# 3.TKINTER OBJECTS


# 4. TKINTER EVENTS AND MAINLOOP

# first_name = input('Please enter your first name: ')
# second_name = input('Please enter your second name: ')
# full_name = first_name + ' ' + second_name
# print('Hello', full_name)
#
# for i in range(1000):
#     print(i)
#     print(i * 2)
#     print(i * 3)


# 5. HOW TO SET THE BACKGROUND COLOR OF A PYTHON TKINTER WINDOW

# my_window.title('Demo1')
# my_window.config(background='light blue')
# my_window.config(bg='red')
#
# # light green
# my_window.config(bg='#00ff00')
# # dark green
# my_window.config(bg='#007700')
# # yellow
# my_window.config(bg='#ffff00')
# # orange
# my_window.config(bg='#ff7700')
# # white
# my_window.config(bg='#ffffff')
# # black
# my_window.config(bg='#000000')
#
# my_window.config(bg='#88324f')


# # 6. SETTING THE SIZE OF A TKINTER WINDOW

# my_window.config(width=400, height=200, bg='#94d42b')


# # 7. HOW TO SET THE LOCATION OF A PYTHON TKINTER WINDOW
# my_window.geometry('200x100')
# my_window.geometry('200x100+0+0')
# my_window.geometry('200x200+1000+200')


# 8. CREATING A FIXED SIZE WINDOW

# my_window.geometry('400x200')
# my_window.resizable(width=False, height=False)


# # 9. HOW TO SET A WINDOW IN THE CENTER OF THE SCREEN
# width_of_window = 500
# height_of_window = 500
#
# screen_width = my_window.winfo_screenwidth()
# screen_height = my_window.winfo_screenheight()
#
# x_coordinate = (screen_width/2) - (width_of_window/2)
# y_coordinate = (screen_height/2) - (height_of_window/2)
#
# my_window.geometry('%dx%d+%d+%d' % (width_of_window, height_of_window, x_coordinate, y_coordinate))


# 11. SETTING THE FONT TYPE, FONT COLOUR AND FONT SIZE OF A LABEL

# # label_1 = Label(my_window, text='Hello World', bg='blue', fg='white')
# label_1 = Label(my_window, text='Red text in Times Font', fg='red', font='Times')
# label_2 = Label(my_window, text='Green text in Broadway Font', fg='green', font='Broadway')
# label_3 = Label(my_window, text='Blue text in Verdana Font', fg='blue', font='Verdana 32 bold italic')
# label_1.pack()
# label_2.pack()
# label_3.pack()


# 12. SETTING THE WIDTH OF A TKINTER LABEL
# label_1 = Label(my_window, text='Hello World', bg='red', fg='white', font='Times 32', width=20)
# label_2 = Label(my_window, text='Hello World', bg='green', fg='white', font='Times 32', width=30)
# label_3 = Label(my_window, text='Hello World', bg='blue', fg='white', font='Times 32', width=40)
# label_1.pack()
# label_2.pack()
# label_3.pack()


# 13. DISPLAYING MULTIPLE LINES OF TEXT IN A LABEL
# label_1 = Label(my_window, text='Line 1 of text\nLine 2 of text\nLine 3 of text', font='Times 32', width=20)
# label_1.pack()


# 14. SETTING THE RELIEF AND BORDER OF A LABEL
# label_1 = Label(my_window, text='Hello World', bd=8, relief='solid', font='Times 32')
# label_2 = Label(my_window, text='Hello World', bd=8, relief='raised', font='Times 32')
# label_3 = Label(my_window, text='Hello World', bd=8, relief='sunken', font='Times 32')
# label_4 = Label(my_window, text='Hello World', bd=8, relief='ridge', font='Times 32')
# label_5 = Label(my_window, text='Hello World', bd=8, relief='groove', font='Times 32')
# label_6 = Label(my_window, text='Hello World', bd=8, relief='flat', font='Times 32')
# label_1.pack()
# label_2.pack()
# label_3.pack()
# label_5.pack()
# label_6.pack()


# 15. SETTING THE HEIGHT OF A TKINTER LABEL
# label_1 = Label(my_window, text='Hello World\nHello World', bd=3, relief='solid', font='Times 32', height=2)
# label_1.pack()


# 16. POSITIONING TEXT WITHIN A PYTHON TKINTER LABEL
# my_window.geometry('400x250')
#
# label_1 = Label(my_window,
#                 text='spacer')
# label_2 = Label(my_window,
#                 text='Hello World\nHello World',
#                 bd=3,
#                 relief='solid',
#                 font='Times 32',
#                 width=15,
#                 height=4,
#                 anchor=W)
# label_1.pack()
# label_2.pack()


# 17. HOW TO PAD TEXT AROUND THE TEXT OF A LABEL
# my_window.geometry('400x250')
#
# label_1 = Label(my_window,
#                 text='spacer')
# label_2 = Label(my_window,
#                 text='Hello World',
#                 bd=3,
#                 relief='solid',
#                 font='Times 32',
#                 pady=30)
# label_3 = Label(my_window,
#                 text='spacer')
# label_4 = Label(my_window,
#                 text='Hello World',
#                 bd=3,
#                 relief='solid',
#                 font='Times 32',
#                 padx=20)
# label_1.pack()
# label_2.pack()
# label_3.pack()
# label_4.pack()


# HOW TO JUSTIFY TEXT WITHIN A TKINTER LABEL
# my_window.geometry('400x250')
#
# label_1 = Label(my_window,
#                 text='spacer')
# label_2 = Label(my_window,
#                 text='Text\nText Text\nText Text Text',
#                 bd=3,
#                 relief='solid',
#                 font='Times 32',
#                 justify=RIGHT)
# label_3 = Label(my_window,
#                 text='spacer')
# label_4 = Label(my_window,
#                 text='Text\nText Text\nText Text Text',
#                 bd=3,
#                 relief='solid',
#                 font='Times 32',
#                 justify=LEFT)
# label_1.pack()
# label_2.pack()
# label_3.pack()
# label_4.pack()


# HOW TO ANCHOR AND JUSTIFY TEXT IN A PYTHON TKINTER LABEL
# my_window.geometry('400x250')
#
# label_1 = Label(my_window,
#                 text='spacer')
# label_2 = Label(my_window,
#                 text='Text\nText Text\nText Text Text',
#                 bd=3,
#                 relief='solid',
#                 font='Times 32',
#                 width=15,
#                 height=4,
#                 anchor=SW,
#                 justify=RIGHT)
# label_3 = Label(my_window,
#                 text='spacer')
# label_4 = Label(my_window,
#                 text='Text\nText Text\nText Text Text',
#                 bd=3,
#                 relief='solid',
#                 font='Times 32',
#                 width=15,
#                 height=4,
#                 anchor=SW,
#                 justify=LEFT)
# label_1.pack()
# label_2.pack()
# label_3.pack()
# label_4.pack()


# 20. HOW TO ACCESS THE OPTIONS OF A PYTHON TKINTER LABEL
# label_1 = Label(my_window,
#                 bd=8,
#                 relief='solid',
#                 font='Times 22 bold',
#                 bg='red',
#                 fg='white',
#                 text='Hello World')
# label_1.pack()


# DYNAMICALLY ALTERING A PYTHON TKINTER LABEL
# label_1 = Label(my_window,
#                 bd=8,
#                 relief='solid',
#                 font='Times 22 bold',
#                 bg='red',
#                 fg='white',
#                 text='Hello World')
# label_1.pack()
# # changing what's defined in the label to this
# label_1['bd'] = 16
# label_1['bg'] = 'blue'
# label_1['relief'] = 'ridge'
# label_1['text'] = 'Uganda'
# label_1['font'] = 'Mistral 32 bold'
# label_1['padx'] = 16
# label_1['width'] = 20


# 22. PYTHON TKINTER KEYS METHOD FOR A LABEL
# label_1 = Label(my_window,
#                 bd=8,
#                 relief='solid',
#                 font='Times 22 bold',
#                 bg='red',
#                 fg='white',
#                 text='Hello World')
# label_1.pack()
# # print(label_1.keys())
# for item in label_1.keys():
#     print(item, ':', label_1[item])


# 23. USING STRINGVAR AND TEXTVARIABLE WITH A PYTHON TKINTER LABEL
# var_1 = StringVar()
# label_1 = Label(my_window,
#                 relief='solid',
#                 font='Times 22 bold',
#                 textvariable=var_1)
# label_1.pack()
# var_1.set('Hi')


# 24. THE PYTHON TKINTER STRINGVAR SET METHOD
var_1 = StringVar()
label_1 = Label(my_window,
                relief='solid',
                font='Times 22 bold')
label_2 = Label(my_window,
                relief='solid',
                font='Times 22 bold',
                textvariable=var_1)
label_1.pack()
label_2.pack()
label_1['text'] = 'Text put here using key/value pairs approach'
var_1.set('Using textvariable and StringVar()')

my_window.mainloop()
