from tkinter import *
import tkinter as tk
from tkinter import ttk,font,messagebox
class App():
    __ventana=None
    __altura=None
    __peso=None
    __imc=None
    __estado=None
    __contenedor2=None
    __cartel1=None
    __cartel2=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.resizable(0,0)
        self.__ventana.config(bg="white")
        self.__ventana.title("Calculadora de IMC")
        fuente=font.Font(weight="bold")
        fuente2=font.Font(size=13)
        self.__peso=IntVar()
        self.__altura=IntVar()
        self.__imc=StringVar()
        self.__estado=StringVar()
        self.contenedor=tk.Frame(self.__ventana,bg="white",borderwidth=4,relief="groove")
        self.separador1=ttk.Separator(self.contenedor,orient=HORIZONTAL)
        self.alturalbl=ttk.Label(self.contenedor,text="Altura:",font=fuente)
        self.pesolbl=ttk.Label(self.contenedor,text="Peso:",font=fuente)
        self.entrada1=ttk.Entry(self.contenedor,textvariable=self.__altura,width=40,font=fuente2)
        self.entrada2=ttk.Entry(self.contenedor,textvariable=self.__peso,width=40,font=fuente2)
        self.cmlbl=ttk.Label(self.contenedor,text="cm",font=fuente)
        self.kglbl=ttk.Label(self.contenedor,text="kg",font=fuente)
        self.separador2=ttk.Separator(self.contenedor,orient=HORIZONTAL)
        self.boton1=tk.Button(self.contenedor,text="Calcular",command=self.calcular,bg="#5cb85c",fg="white",font=fuente2)
        self.boton2=tk.Button(self.contenedor,text="Limpiar",command=self.limpiar2,bg="#5cb85c",fg="white",font=fuente2)
        opt={"padx":4,"pady":5}
        self.contenedor.pack(side=TOP)
        self.separador1.grid(column=0,row=0,pady=9)
        self.alturalbl.grid(column=0,row=1,pady=4)
        self.pesolbl.grid(column=0,row=2,**opt)
        self.entrada1.grid(column=1,row=1,columnspan=2,**opt)
        self.entrada2.grid(column=1,row=2,columnspan=2,**opt)
        self.cmlbl.grid(column=3,row=1,ipady=3,ipadx=3)
        self.kglbl.grid(column=3,row=2,ipady=4,ipadx=4)
        self.separador2.grid(column=0,row=3,pady=4)
        self.boton1.grid(column=1,row=4,padx=4,pady=4)
        self.boton2.grid(column=2,row=4,padx=4,pady=4)
        self.entrada1.focus_set()
        self.__ventana.mainloop()
    def calcular(self):
        if(self.entrada1.get()!="0" and self.entrada2.get()!="0"):
            resultado=None
            try:
                metros=float(self.entrada1.get())/100
                resultado=float(self.entrada2.get())/(metros*metros)
                if resultado<0:
                    raise ValueError
            except ValueError:
                messagebox.showerror(title="Error de tipo",message="Solo se admiten numeros positivos.")
            else:
                if(self.__contenedor2!=None):
                    self.limpiar1()
                self.__imc.set("Tu Indice de Masa Corporal es {:.2f} Kg/m2".format(resultado))
                colores={1:"#ffd059",2:"#94ff94",3:"#f7c6c3"}
                if(resultado<18.5):
                    self.__estado.set("Peso menor al normal")
                    color=colores[1]
                elif(resultado>=18.5 and resultado<25):
                    self.__estado.set("Peso normal")
                    color=colores[2]
                elif(resultado>=25.0 and resultado<30):
                    self.__estado.set("Peso superior al normal")
                    color=colores[1]
                else:
                    self.__estado.set("Obesidad")
                    color=colores[3]
                self.__contenedor2=tk.Frame(self.__ventana,bg=color,borderwidth=2)
                fuente=font.Font(size=10,weight="bold")
                self.__cartel1=tk.Label(self.__contenedor2,textvariable=self.__imc,fg="white",bg=color,font=fuente)
                self.__cartel2=tk.Label(self.__contenedor2,textvariable=self.__estado,fg="white",bg=color,font=fuente)
                self.__contenedor2.pack(side=BOTTOM)
                self.__cartel1.pack(side=TOP)
                self.__cartel2.pack(side=BOTTOM)
        else:
            messagebox.showerror(title="Error",message="Ingrese valores distintos de 0.")
    def limpiar1(self):
        self.__contenedor2.destroy()
        self.__cartel1.destroy()
        self.__cartel2.destroy()
    def limpiar2(self):
        self.limpiar1()
        self.__altura.set("0")
        self.__peso.set("0")