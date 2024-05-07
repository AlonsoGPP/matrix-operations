from tkinter import Toplevel,Frame, Label,Entry,IntVar,Button
import numpy as np
import menu
import matrix
class Mult:
    def __init__(self) -> None:
        menu.gui_menu.withdraw()
        self.gui_mul_menu_dim = Toplevel()
        self.gui_mul_menu_dim.title("Multiplicacion De Matrices")
        self.gui_mul_menu_dim.resizable(False, False)

        self.frame_menu_sum = Frame(self.gui_mul_menu_dim, highlightbackground='red', highlightthickness=1)
        self.frame_menu_sum.pack(fill='both', expand=True, padx=5, pady=5)
        #matriz A
        Label(self.frame_menu_sum, text='Dimencion de Matriz: A', font=('arial', 10, 'bold'))\
            .grid(row=3, column=1)
        
        self.rows= IntVar()
        self.rows.set(2)
        
       
        Entry(self.frame_menu_sum, textvariable=self.rows, width=3).grid(row=4, column=2)
        
        Label(self.frame_menu_sum, text="x").grid(row=4, column=3)

        self.cols=IntVar()
        self.cols.set(2)
        entryca=Entry(self.frame_menu_sum, textvariable=self.cols,width=3)
        entryca.bind('<Leave>',self.reflejar_contenido)
        entryca.grid(row=4, column=4)
        Label(self.frame_menu_sum, text="").grid(row=5,column=1)
        
        #MatrizB
        self.rows_b= IntVar()
        self.rows_b.set(2)
        Label(self.frame_menu_sum, text='Dimencion de Matriz: B', font=('arial', 10, 'bold'))\
                    .grid(row=6, column=1, )
        #Label(self.frame_menu_sum, text="[n]").grid(row=7, column=2)
        entryfb=Entry(self.frame_menu_sum,state='readonly' ,textvariable=self.rows_b,width=3)
        entryfb.bind('<Leave>',self.reflejar_contenido)
        entryfb.grid(row=7, column=2)
        self.cols_b= IntVar()
        self.cols_b.set(2)
        Label(self.frame_menu_sum, text="x").grid(row=7, column=3)

        Entry(self.frame_menu_sum, textvariable=self.cols_b,width=3).grid(row=7, column=4)

        Button(self.frame_menu_sum, text='Ingresar', padx=16, pady=5, command=lambda:self.ingreso_matriz(self.rows,self.cols,self.rows_b, self.cols_b))\
            .grid(row=89, column=4)

        self.gui_mul_menu_dim.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_mul_menu_dim.mainloop()
    def reflejar_contenido(self,event):
        try:
            if(self.cols.get()):
                contenido=self.cols.get()
                self.rows_b.set(contenido)
        except Exception as e:
            print("Error", e)
            #self.cols.set(0)
    def ingreso_matriz(self,rows, cols,rows_b, cols_b):
       self.gui_ingreso_matriz= Toplevel()
       m1 = matrix.MatrizInput(rows,cols,self.gui_ingreso_matriz,0)
       m2= matrix.MatrizInput(rows_b,cols_b,self.gui_ingreso_matriz,1)
       frame_input_matriz = Frame(self.gui_ingreso_matriz, highlightbackground='red', highlightthickness=1)
       frame_input_matriz.pack(fill='both', expand=True, padx=5, pady=5)
       Button(frame_input_matriz,text="Calcular", width=8, command=lambda:self.procesar_matriz(m1,m2)).grid(row=1, column=1)
       self.gui_mul_menu_dim.protocol("WM_DELETE_WINDOW",menu.gui_menu.destroy)
       self.gui_ingreso_matriz.mainloop()
    def procesar_matriz(self,m1:matrix.MatrizInput,m2:matrix.MatrizInput):
        try:
            matriz_a_value = m1.get_matriz()
            matrix_b_value = m2.get_matriz()
            
        except Exception as e:
            print('Hubo un error',e)
        self.salida_matriz(matriz_a_value, matrix_b_value)

    def salida_matriz(self, m1_val:list, m2_val:list):
        #self.gui_ingreso_matriz.destroy()
        self.gui_mul_salida = Toplevel()
        self.gui_mul_salida.title("Multiplicacion Salida")
        self.gui_mul_salida.resizable(False,False)

        self.frame_sum_salida = Frame(self.gui_mul_salida, highlightbackground='black', highlightthickness=1)
        self.frame_sum_salida.pack(fill='both', expand=True, padx=5, pady=5)
        rows_length_a = self.rows.get()
        cols_length_a = self.cols.get()
        rows_length_b = self.rows_b.get()
        cols_length_b = self.cols_b.get()

       

        Label(self.frame_sum_salida, text="Matriz A:").grid(row=1,column=1)

        for i in range(rows_length_a):
            for j in range(cols_length_a):
                Label(self.frame_sum_salida,text=m1_val[i][j], bd=5).grid(row=i+1, column=j+2)

        Label(self.frame_sum_salida, text='Matriz B:', underline=0)\
            .grid(row=1, column=cols_length_a+2)
        
        for i in range(rows_length_b):
            for j in range(cols_length_b):
                Label(self.frame_sum_salida,text=m2_val[i][j], bd=5).grid(row=i+1, column=j+cols_length_b*2+2)

        Label(self.frame_sum_salida, text="Producto:").grid(row=cols_length_b*2,column=1)

        matriz_resultante_mul =  self.calcular_mul(m1_val, m2_val)
        
        rows_mat_resul, cols_mat_resl=rows_length_a,cols_length_b
       
        for i in range(rows_mat_resul):
            for j in range(cols_mat_resl):
                Label(self.frame_sum_salida,text=matriz_resultante_mul[i][j], bd=5).grid(row=i+cols_mat_resl*2, column=j+2)
        self.frame_btn_volver=Frame(self.gui_mul_salida)
        self.frame_btn_volver.pack(fill='both', expand=True, padx=5, pady=5)
        Button(self.frame_btn_volver, text="Volver", width=4, command=self.volver_menu).pack(side='bottom', anchor='e')

        self.gui_mul_salida.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_mul_salida.mainloop()
    def calcular_mul(self,m1_val,m2_val)->list:
         product_matriz = np.matmul(m1_val,m2_val)
         return product_matriz
    def volver_menu(self):
        self.gui_ingreso_matriz.destroy()
        self.gui_mul_menu_dim.destroy()
        self.gui_mul_salida.destroy()
        menu.gui_menu.deiconify()
