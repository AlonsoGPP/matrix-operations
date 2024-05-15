from tkinter import Toplevel, Label, Frame, IntVar, Entry, Button, messagebox
import menu
import matrix
import matriz_operations
class Potencia: 
    def __init__(self):
        #Crea ventana nueva
        menu.gui_menu.withdraw()
        self.gui_trans_menu_dim = Toplevel()
        self.gui_trans_menu_dim.title("Potencia de Matriz")
        self.gui_trans_menu_dim.resizable(False, False)

        #crea frame donde van los componentes
        self.frame_menu_trans = Frame(self.gui_trans_menu_dim, highlightbackground='red', highlightthickness=1)
        self.frame_menu_trans.pack(fill='both', expand=True, padx=5, pady=5)
        Label(self.frame_menu_trans)
        Label(self.frame_menu_trans, text='Dimencion de Matriz:', font=('arial', 10, 'bold'))\
            .grid(row=3, column=1, columnspan=1)
        
        self.rows= IntVar()
        self.rows.set(2)
        
        Entry(self.frame_menu_trans, textvariable=self.rows, width=3).grid(row=4, column=2)
        

        self.cols=self.rows #igualamos

        self.pot_number=IntVar()
        self.pot_number.set(2)

        #OptionMenu(self.frame_menu_trans, self.cols, *range(2, 5)).grid(row=4, column=4)
        Label(self.frame_menu_trans, text="").grid(row=5, column=1)
        Label(self.frame_menu_trans, text="Potencia: ").grid(row=6, column=1)
        Entry(self.frame_menu_trans, textvariable=self.pot_number,width=3).grid(row=6, column=2)
        Button(self.frame_menu_trans, text='Ingresar', padx=16, pady=5, command=lambda:self.ingreso_matriz(self.rows,self.cols)).grid(row=7, column=4)

        self.gui_trans_menu_dim.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_trans_menu_dim.mainloop()
    def validar_campos_dim(self):
        try:
            self.rows.get()
            self.cols.get()
            self.pot_number.get()
        except Exception as e:
            messagebox.showerror(message=f"Error al ingresar dimenciones: {e}", title="Error")
            return False
        return True
    def ingreso_matriz(self,rows, cols):
        if(self.validar_campos_dim() is False):
           return
        self.gui_ingreso_matriz= Toplevel()
        matriz_1 = matrix.MatrizInput(rows,cols,self.gui_ingreso_matriz,0)
        
        frame_input_matriz = Frame(self.gui_ingreso_matriz, highlightbackground='red', highlightthickness=1)
        frame_input_matriz.pack(fill='both', expand=True, padx=5, pady=5)
        Button(frame_input_matriz,text="Calcular", width=8, command=lambda:self.procesar_matriz(matriz_1)).grid(row=1, column=1)
        self.gui_ingreso_matriz.protocol("WM_DELETE_WINDOW",menu.gui_menu.destroy)
        self.gui_ingreso_matriz.mainloop()
    def procesar_matriz(self,matriz_1:matrix.MatrizInput):
        matriz_a_value = matriz_1.get_matriz()
        if matriz_a_value is None:
            return
        self.salida_matriz(matriz_a_value)
    def salida_matriz(self, m1_val:list):
        self.gui_ingreso_matriz.destroy()
        self.gui_transp_salida = Toplevel()
        self.gui_transp_salida.title("Matriz Transpuesta")
        self.gui_transp_salida.resizable(False,False)

        self.frame_sum_salida = Frame(self.gui_transp_salida, highlightbackground='black', highlightthickness=1)
        self.frame_sum_salida.pack(fill='both', expand=True, padx=5, pady=5)
        rows_length = self.rows.get()
        cols_length = self.cols.get()
        def formatear_numero(numero)->str:
                return "{:.2f}".format(numero) if numero % 1 != 0 else "{:.0f}".format(numero)

        Label(self.frame_sum_salida, text="M. Ingresada:").grid(row=1,column=1)

        for i in range(rows_length):
            for j in range(cols_length):
                Label(self.frame_sum_salida,text=formatear_numero(m1_val[i][j]), bd=5).grid(row=i+1, column=j+2)
        pot_int=self.pot_number.get()
        Label(self.frame_sum_salida, text=f"A^{pot_int}: ").grid(row=cols_length*2,column=1)

        matriz_resultante =  self.calcular_mat_pow(m1_val,pot_int)

        for i in range(cols_length):
            for j in range(rows_length):
                Label(self.frame_sum_salida,text=formatear_numero(matriz_resultante[i][j]), bd=5).grid(row=i+cols_length*2, column=j+2)
        self.frame_btn_volver=Frame(self.gui_transp_salida)
        self.frame_btn_volver.pack(fill='both', expand=True, padx=5, pady=5)
        Button(self.frame_btn_volver, text="Volver", width=4, command=self.volver_menu).pack(side='bottom', anchor='e')

        self.gui_transp_salida.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_transp_salida.mainloop()
    def volver_menu(self):
        self.gui_ingreso_matriz.destroy()
        self.gui_trans_menu_dim.destroy()
        self.gui_transp_salida.destroy()
        menu.gui_menu.deiconify()
    def calcular_mat_pow(self, matriz_1, pot):
        return matriz_operations.MatrisOperations().mat_pow(matriz_1,pot)