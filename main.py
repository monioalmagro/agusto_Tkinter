import tkinter as tk


from testing_bg import (func_reporte_1, func_reporte_2, func_reporte_3, 
                        func_reporte_4, func_reporte_5, func_reporte_6)


class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("Scrip para Agusto")
        self.label1=tk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")

        self.boton1=tk.Button(self.ventana1, text="boton1", command=self.reporte1)
        self.boton1.grid(column=0, row=1)

        self.boton2=tk.Button(self.ventana1, text="boton2", command=self.reporte2)
        self.boton2.grid(column=0, row=2)

        self.boton3=tk.Button(self.ventana1, text="boton3", command=self.reporte3)   
        self.boton3.grid(column=1, row=1)

        self.boton4=tk.Button(self.ventana1, text="boton4", command=self.reporte4)
        self.boton4.grid(column=1, row=2)

        self.boton5=tk.Button(self.ventana1, text="boton5", command=self.reporte5)
        self.boton5.grid(column=2, row=1)

        self.boton6=tk.Button(self.ventana1, text="boton6", command=self.reporte6)
        self.boton6.grid(column=2, row=2)

        self.ventana1.mainloop()


    def reporte1(self):
        func_reporte_1()
        
    def reporte2(self):
        func_reporte_2()
    
    def reporte3(self):
        func_reporte_3()    
    
    def reporte4(self):
        func_reporte_4()

    def reporte5(self):
        func_reporte_5()

    def reporte6(self):
        func_reporte_6()


aplicacion1=Aplicacion()
