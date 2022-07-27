from scipy.sparse import data
import numpy as np
import tkinter as tk
from Detector_Edad import preparar_rostro

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.winfo_screenmmwidth
        ancho_ventana = 400
        alto_ventana = 400
        x_ventana = self.master.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.master.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.master.geometry(posicion)

        self.pack()
        self.create_widgets()
        self.Preparar

    def create_widgets(self):
        self.Preparar = tk.Button(self)
        self.Preparar["text"] = "Detectar Rango De Edad Del Individuo"
        self.Preparar["command"] = preparar_rostro
        self.Preparar.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()