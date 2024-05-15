from tkinter import Tk, Frame,Label,Button
from tkinter.constants import BOTH
import suma, mult, trans, determinante, potencia, inversa, rango
gui_menu = Tk() 
gui_menu.geometry("500x500")
gui_menu.resizable(False,False)
frame_menu = Frame(gui_menu, highlightbackground='black', highlightthickness=1)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)
class Menu:
    def __init__(self):
        self.label = Label(frame_menu, text="Menu de Operaciones")
        self.sum_btn=Button(frame_menu,text="Sumar Matriz", command=suma.Suma)
        self.mul_btn=Button(frame_menu, text="Multplicar Matriz", command=mult.Mult)
        self.trans_btn=Button(frame_menu, text="Transpuesta Matriz", command=trans.Transpuesta)
        self.det_btn=Button(frame_menu, text="Determinante Matriz", command=determinante.Determinante)
        self.pot_btn=Button(frame_menu, text="Potencia de Matriz", command=potencia.Potencia)
        self.inv_btn=Button(frame_menu, text="Inversa de Matriz", command=inversa.Inversa)
        self.rank_btn=Button(frame_menu, text="Rango de Matriz", command=rango.Rango)
        self._packing()
        gui_menu.mainloop()
    def _packing(self):
        self.label.pack()
        self.sum_btn.pack()
        self.mul_btn.pack()
        self.trans_btn.pack()
        self.det_btn.pack()
        self.pot_btn.pack()
        self.inv_btn.pack()
        self.rank_btn.pack()