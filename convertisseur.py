from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Convertisseur de Monnaie')

frame1 = Frame(root, padx = 60, pady = 30)
frame1.pack()

label = Label(frame1, text = "Convertisseur de Monnaie", font = 'TimesNewRoman 24', fg = 'black', bd = 2)
label.pack(side = TOP)

frame2 = Frame(frame1, pady = 15)
frame2.pack()

frame3 = Frame(frame2, pady = 10)
frame3.pack()

frame4 = Frame(frame2, pady = 10)
frame4.pack()

#Label(frame3, text = "Dollars", font = 'TimesNewRoman 16').pack(side = LEFT)
d1 = Entry(frame3, font = 'TimesNewRoman 16', fg = 'black', bg = '#ddd', bd = 2, relief = RIDGE)
d1.pack(side = RIGHT)

#Label(frame4, text = "Euros ", font = 'TimesNewRoman 16').pack(side = LEFT)
d2 = Entry(frame4, font = 'TimesNewRoman 16', fg = 'black', bg = '#ddd', bd = 2, relief = RIDGE)
d2.pack(side = RIGHT)

frame5 = Frame(frame1)
frame5.pack()

devise = ttk.Combobox(frame3, values=["Dollar", "Yen", "Euro", "Livre"], font = 'TimesNewRoman 16')
devise.pack(side = RIGHT)
devise.current(0)

devise_2 = ttk.Combobox(frame4, values=["Dollar", "Yen", "Euro", "Livre"], font = 'TimesNewRoman 16')
devise_2.pack(side = RIGHT)
devise_2.current(0)

def convertir(t1,t2):
    global devise
    global devise_2
    global d1
    global d2
    historique = ""
    nbr_1 = d1.get()
    nbr_2 = d2.get()
    if len(str(nbr_2)) > 0 and len(str(nbr_1)) > 0:
        d1.delete(0,'end')
        d2.delete(0,'end')
    elif len(str(nbr_1)) != 0:
        d2.insert(0,str(int(nbr_1) * t1))
        historique = str(nbr_1) + " " + devise.get() + " = " + d2.get() + " " + devise_2.get() + "\n"
        f = open("Historique.csv","a")
        f.write(historique)
        f.close()
    elif len(str(nbr_2)) != 0:
        d1.insert(0,str(int(nbr_2) * t2))
        historique = str(nbr_2) + " " + devise_2.get() + " = " + d1.get() + " " + devise.get() + "\n"
        f = open("Historique.csv","a")
        f.write(historique)
        f.close()
    
def appel_convertir():
    global d1
    global d2
    global devise
    select1 = devise.get()
    select2 = devise_2.get()
    for i in ["Dollar", "Yen", "Euro", "Livre"]:
        if select1 == i and select2 == i:
            convertir(1,1)
            
    for i in ["Yen", "Euro", "Livre"]:
        if select1 == "Dollar" and select2 == i:
            if i == "Yen":
                convertir(130.27,0.0077)
            elif i == "Euro":
                convertir(0.92,1.09)
            elif i == "Livre":
                convertir(0.81,1.23)

    for i in ["Dollar", "Euro", "Livre"]:
        if select1 == "Yen" and select2 == i:
            if i == "Dollar":
                convertir(130.27,0.0077)
            elif i == "Euro":
                convertir(0.0071,141.74)
            elif i == "Livre":
                convertir(0.0062,160.42)

    for i in ["Dollar", "Yen", "Livre"]:
        if select1 == "Euro" and select2 == i:
            if i == "Dollar":
                convertir(1.09,0.92)
            elif i == "Yen":
                convertir(141.74,0.0071)
            elif i == "Livre":
                convertir(0.88,1.13)

    for i in ["Dollar", "Euro", "Yen"]:
        if select1 == "Livre" and select2 == i:
            if i == "Dollar":
                convertir(1.23,0.81)
            elif i == "Yen":
                convertir(160.42,0.0062)
            elif i == "Euro":
                convertir(1.13,0.88)

def reset():
    global d1
    global d2
    d1.delete(0,'end')
    d2.delete(0,'end')

Button(frame5, text = "Convertir", font = 'TimesNewRoman 15', padx = 5, command = appel_convertir).pack(side = LEFT)
Button(frame5, text = "Reset", font = 'TimesNewRoman 15', padx = 5, command = reset).pack(side = RIGHT)

root.mainloop()