from tkinter import  Frame,Label,StringVar,Entry,Button
class MatrizInput:
     ABCEDARIO = 'abcdefghijklmnopqrstuvwxyz'

     def __init__(self, rows, cols, wind, id_name):
        print("llegue")
        self.gui_input_matriz = wind
        self.gui_input_matriz.title("Ingreso Matriz")
        self.gui_input_matriz.resizable(False,False)

        self.frame_input_matriz = Frame(self.gui_input_matriz, highlightbackground='red', highlightthickness=1)
        self.frame_input_matriz.pack(fill='both', expand=True, padx=5, pady=5)

        Label(self.frame_input_matriz, text=f"Ingrese Matriz {MatrizInput.ABCEDARIO[id_name].upper()} : ").grid(row=1, column=1)

        self.text_var=[]#lista
        self.entries=[]
        self.matriz_int = []
        
        self.get_rows, self.get_cols = (rows.get(),cols.get())
        for i in range(self.get_rows):
            print(i)
            self.text_var.append([])#se añade una lista a la lista
            self.entries.append([])
            for j in range(self.get_cols):
                if(i==0):
                    Label(self.frame_input_matriz,text=MatrizInput.ABCEDARIO[j]).grid(row=2, column=j+2)
                self.text_var[i].append(StringVar())
                self.entries[i].append(Entry(self.frame_input_matriz, textvariable=self.text_var[i][j], width=3))
                self.entries[i][j].grid(row=i + 3, column=j + 2)
                Label(self.frame_input_matriz, text=i + 1).grid(row=i + 3, column=1, sticky='e')
     def get_matriz(self):
        self.mat_value = []
        for i in range(self.get_rows):
            self.mat_value.append([])
            for j in range(self.get_cols):
                self.mat_value[i].append(int(self.text_var[i][j].get()))
        return self.mat_value
     def get_element(self,f,c):
         return int(self.text_var[f][c].get())
     def get_fila(self, fila):
         fila_text_vars = self.text_var[fila-1]
         fila_int=[]
         for i in range(len(fila_text_vars)):
             fila_int.append((fila_text_vars[i]).get())
    
    

    