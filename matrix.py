from tkinter import  Frame,Label,StringVar,Entry,Button, messagebox
class MatrizInput:
     ABCEDARIO = 'abcdefghijklmnopqrstuvwxyz'

     def __init__(self, rows, cols, wind, id_name):
        #print("llegue")
        self.gui_input_matriz = wind
        self.gui_input_matriz.title("Ingreso Matriz")
        #self.gui_input_matriz.resizable(False,False)

        self.frame_input_matriz = Frame(self.gui_input_matriz, highlightbackground='red', highlightthickness=1)
        self.frame_input_matriz.pack(fill='both', expand=True, padx=5, pady=5)

        Label(self.frame_input_matriz, text=f"Ingrese Matriz {MatrizInput.ABCEDARIO[id_name].upper()} : ").grid(row=1, column=1)

        self.text_var=[]#lista
        self.entries=[]
        self.matriz_int = []
        
        self.get_rows, self.get_cols = (rows.get(),cols.get())
        for i in range(self.get_rows):
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
            self.mat_value.append([])#añade nueva fila
            for j in range(self.get_cols):
                try:
                    valor:float = float(self.text_var[i][j].get())
                except Exception as e:
                    messagebox.showerror(message=f"Error en ingreso: {e}", title="Error")
                    return None
                self.mat_value[i].append(valor)
        return self.mat_value

    
    

    