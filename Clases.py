from tkinter import *
import tkinter.font
import tkinter as tk
#from PIL import Image, ImageDraw
from PIL import Image, ImageDraw, ImageFont



class AnadirClase(object):
    def __init__(self):
        self.__clases = list(range(8))
        self.__atr = list(range(8))
        self.__met = list(range(8))
        self.__dad = list(range(8))
        self.__son = list(range(8))
        self.__nameClass = list(range(8))
        self.__nameDad = list(range(8))
        self.__nameSon = list(range(8))
        self.__nameAtr = list(range(8))
        self.__nameMethod = list(range(8))
        self.__tablas = list(range(8))
        self.__tablas1 = list(range(8))
        self.__mostrarClass = list(range(8))
        self.__mostrarClass1 = list(range(8))
        self.__mostrarAtr = list(range(8))
        self.__mostrarAtr1 = list(range(8))
        self.__mostrarMet = list(range(8))
        self.__mostrarMet1 = list(range(8))
        self.__root = list(range(8))
        self.__mark = list(range(8))
        self.__i = 0
        self.__j = 0
        self.__k = 0
        self.__h = 0

    def crearClase(self):
        self.__clases[self.__j] = tk.Entry(marco, width = 20)
        self.__clases[self.__j].pack()
        self.__clases[self.__j].place(x = 20, y = 50 + 130*self.__j)
        self.__clases[self.__j].insert(0, "class")

        self.__atr[self.__j] = Text(marco, width = 20, height = 5)
        self.__atr[self.__j].pack()
        self.__atr[self.__j].place(x = 20, y = 80 + 130*self.__j)

        self.__met[self.__j] = Text(marco, width = 20, height = 5)
        self.__met[self.__j].pack()
        self.__met[self.__j].place(x = 200, y = 80 + 130*self.__j)

        self.__j += 1

    def crearHere(self):
        ext = None
        self.__dad[self.__k] = tk.Entry(marco, width = 20)
        self.__dad[self.__k].pack()
        self.__dad[self.__k].place(x = 500, y = 50 + 70*self.__k)
        self.__dad[self.__k].insert(0, "class")

        ext = tk.Label(marco, text="extends")
        ext.pack()
        ext.place(x = 640, y = 50 + 70*self.__k)

        self.__son[self.__k] = tk.Entry(marco, width = 20)
        self.__son[self.__k].pack()
        self.__son[self.__k].place(x = 700, y = 50 + 70*self.__k)
        self.__son[self.__k].insert(0, "class")

        self.__k += 1

    def obtenerDatos(self):
        self.__nameClass[self.__i] = self.__clases[self.__i].get()
        self.__nameAtr[self.__i] = self.__atr[self.__i].get('1.0', END)
        self.__nameMethod[self.__i] = self.__met[self.__i].get('1.0', END)

        if (self.__nameAtr[self.__i].count('public')) > 0 or (self.__nameAtr[self.__i].count('private')) > 0 or (self.__nameAtr[self.__i].count('protected')) > 0:
            print(str(self.__nameAtr[self.__i].count('public')))
            self.__nameAtr[self.__i] = self.__nameAtr[self.__i].replace('public', '+')
            self.__nameAtr[self.__i] = self.__nameAtr[self.__i].replace('private', '__')
            # self.__nameAtr[self.__i] = self.__nameAtr[self.__i].replace('protected', '#')

        if (self.__nameMethod[self.__i].count('public')) > 0 or (self.__nameMethod[self.__i].count('private')) > 0 or (self.__nameMethod[self.__i].count('protected')) > 0:
            self.__nameMethod[self.__i] = self.__nameMethod[self.__i].replace('public', '+')
            self.__nameMethod[self.__i] = self.__nameMethod[self.__i].replace('private', '__')
            # self.__nameMethod[self.__i] = self.__nameMethod[self.__i].replace('protected', '#')
        
        print(self.__nameAtr[self.__i])
        print(self.__nameMethod[self.__i])
        AnadirClase.devolverDatos(self)
        self.__i += 1
    
    def obtenerHere(self):
        self.__nameDad[self.__h] = self.__dad[self.__h].get()
        self.__nameSon[self.__h] = self.__son[self.__h].get()

        
        print(self.__nameDad[self.__h])
        AnadirClase.devolverHere(self)
        self.__h += 1

    def devolverDatos(self):
        self.__root[self.__i] = tk.Tk()
        self.__root[self.__i].title("Clase " + str(self.__i + 1))
        self.__root[self.__i].geometry("300x300")
        self.__root[self.__i].configure(background = "#ABCDEF")

        # aqui perro
        blanco = (0, 0, 0)
        image1 = Image.new("RGB", (400, 300), blanco)
        pintura = ImageDraw.Draw(image1)

        pintura.rectangle([10, 10, 250, 250], fill = 'white')
        pintura.line([10, 50, 250, 50], fill = "black")
        pintura.line([10, 150, 250, 150], fill = "black")


        lienzo = Canvas(self.__root[self.__i], width = 900, height = 500, background = "white")
        lienzo.grid(row = 0, column = 0)
        self.__tablas[self.__i] = lienzo.create_rectangle(10, 10, 250, 250, width = 3, fill = 'white')

        lienzo.create_line(10, 50, 250, 50, fill = "black")
        lienzo.create_line(10, 150, 250, 150, fill = "black")

        text_font = tkinter.font.Font(slant = "italic", family = "Helvetica", size = 20, weight = "bold")
        fonto=ImageFont.truetype("C:/Windows/Fonts/corbelli.ttf", 15)
        pintura.text((100, 30), str(self.__nameClass[self.__i]), font = fonto, fill = "black")
        pintura.text((50, 100), str(self.__nameAtr[self.__i]), font = fonto, fill = "black")
        pintura.text((60, 200), str(self.__nameMethod[self.__i]), font = fonto, fill = "black")

        self.__mostrarClass[self.__i] = lienzo.create_text(100, 30, font = text_font, text = str(self.__nameClass[self.__i]), fill = "black")
        self.__mostrarAtr[self.__i] = lienzo.create_text(50, 100, font = text_font, text = str(self.__nameAtr[self.__i]), fill = "black")
        self.__mostrarMet[self.__i] = lienzo.create_text(60, 200, font = text_font, text = str(self.__nameMethod[self.__i]), fill = "black")
        
        self.__mostrarClass1[self.__i] = lienzo.create_text(100, 30, font = text_font, text = str(self.__nameClass[self.__i]), fill = "black")
        self.__mostrarAtr1[self.__i] = lienzo.create_text(50, 100, font = text_font, text = str(self.__nameAtr[self.__i]), fill = "black")
        self.__mostrarMet1[self.__i] = lienzo.create_text(60, 200, font = text_font, text = str(self.__nameMethod[self.__i]), fill = "black")

        print(str(self.__nameClass[self.__i]))
        print(str(self.__nameAtr[self.__i]))

        filename = ""+str(self.__nameClass[self.__i])+".jpg"
        image1.save(filename)


    def devolverHere(self):
        p=0
        q=0
        self.__mark[self.__h] = tk.Tk()
        self.__mark[self.__h].title("Herencia " + str(self.__h + 1))
        self.__mark[self.__h].geometry("900x300")
        self.__mark[self.__h].configure(background = "#ABCDEF")

        lienzo = Canvas(self.__mark[self.__h], width = 900, height = 500, background = "white")
        lienzo.grid(row = 0, column = 0)

        self.__tablas[self.__h] = lienzo.create_rectangle(10, 10, 250, 250, width = 3, fill = 'white')

        lienzo.create_line(10, 50, 250, 50, fill = "black")
        lienzo.create_line(10, 150, 250, 150, fill = "black")


        lienzo.create_line(300, 110, 330, 140, fill = "black", width = 2)
        lienzo.create_line(300, 110, 330, 80, fill = "black", width = 2)
        lienzo.create_line(330, 80, 330, 140, fill = "black", width = 2)
        lienzo.create_line(330, 110, 400, 110, fill = "black", width = 2)

        
        self.__tablas1[self.__h] = lienzo.create_rectangle(500, 10, 740, 250, width = 3, fill = 'white')

        lienzo.create_line(500, 50, 740, 50, fill = "black")
        lienzo.create_line(500, 150, 740, 150, fill = "black")

        text_font = tkinter.font.Font(slant = "italic", family = "Helvetica", size = 20, weight = "bold")

        for i in range(8):
            if self.__nameDad[self.__h] == self.__nameClass[i]:
                p=i

        self.__mostrarClass[self.__h] = lienzo.create_text(100, 30, font = text_font, text = str(self.__nameClass[p]), fill = "black")
        self.__mostrarAtr[self.__h] = lienzo.create_text(50, 100, font = text_font, text = str(self.__nameAtr[p]), fill = "black")
        self.__mostrarMet[self.__h] = lienzo.create_text(60, 200, font = text_font, text = str(self.__nameMethod[p]), fill = "black")
        
        for j in range(8):
            if self.__nameSon[self.__h] == self.__nameClass[j]:
                q=j
        
        print(self.__nameSon[self.__h])
        
        self.__mostrarClass1[self.__h] = lienzo.create_text(600, 30, font = text_font, text = str(self.__nameClass[q]), fill = "black")
        self.__mostrarAtr1[self.__h] = lienzo.create_text(550, 100, font = text_font, text = str(self.__nameAtr[q]), fill = "black")
        self.__mostrarMet1[self.__h] = lienzo.create_text(560, 200, font = text_font, text = str(self.__nameMethod[q]), fill = "black")

        print(str(self.__nameClass[self.__h]))
        print(str(self.__nameAtr[self.__h]))
    
        
#Marco
marco = tk.Tk()
marco.title("Diagrama de clases")
marco.geometry("900x500")
marco.configure(background = "#ABCDEF")

#Objeto de la clase AñadirClase
obj = AnadirClase()

#Botones
btnCrear = Button(marco, text = "Crear Nueva Clase", command = obj.crearClase)
btnCrear.pack()
btnCrear.place(x = 20, y = 10)

btnHere = Button(marco, text = "Crear Nueva Herencia", command = obj.crearHere)
btnHere.pack()
btnHere.place(x = 500, y = 10)

btnEnviar = Button(marco, text = "Enviar", command = obj.obtenerDatos)
btnEnviar.pack()
btnEnviar.place(x = 300, y = 10)

btnEnviarHere = Button(marco, text = "Enviar herencia", command = obj.obtenerHere)
btnEnviarHere.pack()
btnEnviarHere.place(x = 780, y = 10)
mainloop()