from tkinter import Tk, Frame,Label,Button,messagebox,Menu
from tkinter.constants import BOTH
from PIL import ImageTk, Image
import suma, mult, trans, determinante, potencia, inversa, rango
gui_menu = Tk() 
gui_menu.geometry("500x500")
gui_menu.iconbitmap("assets/matrix-icon.ico")
gui_menu.resizable(False,False)
gui_menu.title("Matrix Solver")

def acerca_de():
    messagebox.showinfo("Acerca de", "Creado por: David Garcia Pariona\nCurso: Investigacion de Operaciones I")

#menu
barra_menu = Menu(gui_menu)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Acerca de", command=acerca_de)

menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=gui_menu.quit)

barra_menu.add_cascade(label="Ayuda", menu=menu_archivo)
gui_menu.config(menu=barra_menu)

main_image_path="assets/matrix-icon.jpg"
img = Image.open(main_image_path)
img = img.resize((100, 100), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)  
# frame_main.pack()

frame_title = Frame(gui_menu)
frame_title.pack(padx=5, pady=30)
label_img = Label(frame_title, image=img)
text_label = Label(frame_title, text="MATRIX SOLVER", pady=10)
label_img.image = img
label_img.pack()
text_label.pack()


frame_menu = Frame(gui_menu, highlightbackground='black', highlightthickness=1)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5 )
frame_buttons=Frame(frame_menu)
frame_buttons.pack()
class Menu:
    def __init__(self):
        self.label = Label(frame_buttons, text="Menu de Operaciones")
        self.sum_btn=Button(frame_buttons,text="Sumar Matriz", command=suma.Suma)
        self.mul_btn=Button(frame_buttons, text="Multplicar Matriz", command=mult.Mult)
        self.trans_btn=Button(frame_buttons, text="Transpuesta Matriz", command=trans.Transpuesta)
        self.det_btn=Button(frame_buttons, text="Determinante Matriz", command=determinante.Determinante)
        self.pot_btn=Button(frame_buttons, text="Potencia de Matriz", command=potencia.Potencia)
        self.inv_btn=Button(frame_buttons, text="Inversa de Matriz", command=inversa.Inversa)
        self.rank_btn=Button(frame_buttons, text="Rango de Matriz", command=rango.Rango)
        self._packing()
        gui_menu.mainloop()
    def _packing(self):
        padx_g=15
        pady_g=5
        self.label.grid(row=1, column=2, padx=padx_g, pady=pady_g)
        self.sum_btn.grid(row=2, column=1, padx=padx_g, pady=pady_g)
        self.mul_btn.grid(row=2, column=2, padx=padx_g, pady=pady_g)
        self.trans_btn.grid(row=2, column=3, padx=padx_g, pady=pady_g)
        self.det_btn.grid(row=3, column=1, padx=padx_g, pady=pady_g)
        self.pot_btn.grid(row=3, column=2, padx=padx_g, pady=pady_g)
        self.inv_btn.grid(row=3, column=3, padx=padx_g, pady=pady_g)
        self.rank_btn.grid(row=4, column=1, padx=padx_g, pady=pady_g)
