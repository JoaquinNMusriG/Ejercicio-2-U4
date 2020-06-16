from tkinter import ttk,Tk,StringVar
from tkinter.constants import *
import requests

class Aplicacion():
    __ventana=None
    __dolar=None
    __peso=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('380x140')
        self.__ventana.title('Conversor de moneda')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 12", relief='sunken')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="dólares").grid(column=2, row=0, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=0, row=1, sticky=E)
        ttk.Label(mainframe, text="pesos").grid(column=2, row=1, sticky=W)

        self.__dolar = StringVar()
        self.__peso = StringVar()
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=2, row=2, sticky=W)
        self.entrada=ttk.Entry(mainframe, textvariable=self.__dolar)
        self.entrada.grid(column=1, row=0, sticky=W)
        self.entrada.bind('<Return>', self.calcular)
        self.respuesta = ttk.Label(mainframe, textvariable=self.__peso)
        self.respuesta.grid(column=1, row=1, sticky=(W, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.__ventana.mainloop()

    def calcular(self, evento):
        try:
            valorD = float(self.entrada.get())
            r = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
            x = r.json()
            dolar = float(x[0]['casa']['venta'].replace(',','.'))
            self.__peso.set('{:0.2f}'.format(valorD*dolar))
        except ValueError:
            print('No es un numero.')
