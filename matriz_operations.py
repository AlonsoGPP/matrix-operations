from copy import deepcopy
import numpy as np
class MatrisOperations:
    def get_row(self, mt:list, fila_n):
        return mt[fila_n-1]
    def get_col(self, mt:list, col_n):
        col=[]
        for m in mt:
            col.append(m[col_n-1])
        return col
    def get_element_at(self, mt , f, c):
        return self.get_row(mt,f)[c-1]
    def copy_mat(self, mt):
        return deepcopy(mt)
    def row_column_remover(self,mt,fila,columna):
        copy_mt = self.copy_mat(mt)
        copy_mt = self.rm_row(copy_mt,fila)
        copy_mt = self.rm_column(copy_mt,columna)
        return copy_mt
    def rm_row(self, mt, row):
        del mt[row-1]
        return mt
    def rm_column(self, mt, column):
        for row in mt:
            del row[column-1]
        return mt
    def cofactor(self, mt, fila,columna):
        b=self.row_column_remover(mt, fila,columna)
        cofact = (-1)**(fila+columna)*self.determinante(b)
        return cofact
    def matriz_identidad(self,dimension):
        matriz=[]
        for i in range(dimension):
            col=[]
            for j in range(dimension):
                if i==j:
                    col.append(1)
                else:
                    col.append(0)
            matriz.append(col)
        return matriz
    def determinante(self, mt:list):
        rows_n=len(mt)
        colums_n=len(mt[0])
        if(rows_n==2 and colums_n==2):
            return self.get_element_at(mt, 1, 1)*self.get_element_at(mt, 2, 2 )-(self.get_element_at(mt, 1,2)\
                                                                                 *self.get_element_at(mt,2,1))
        total = 0
        for col in  range(colums_n):
           total+=self.get_element_at(mt,1,col+1)*self.cofactor(mt,1,col+1)
        return total
    def calcular_mul(self,m1_val:list,m2_val:list):
         product_matriz = np.matmul(m1_val,m2_val)
         return product_matriz
    def mat_pow(self, m1_value:list, pot_value)->list:
        if pot_value==1:
            return m1_value
        elif pot_value==0:
            return self.matriz_identidad(len(m1_value))
        result=deepcopy(m1_value)
        for _ in range(pot_value-1):
            result=self.calcular_mul(m1_value,result)
        return result
    def transpuesta(self,m1):
        filas = len(m1)
        columnas = len(m1[0])
        transpuesta = []

        for i in range(columnas):
            transpuesta.append([])
        #rellena usando j como iterador sobre una matriz precreada    
        for i in range(filas):
            for j in range(columnas):
                transpuesta[j].append(m1[i][j])
            
                

        return transpuesta
    def intercambiar_filas(self, matriz, i, j):
        
        matriz[i], matriz[j] = matriz[j], matriz[i]

    def multiplicar_fila_por_escalar(self, matriz, fila, escalar):
   
        for i in range(len(matriz[0])):
            matriz[fila][i] *= escalar

    def sumar_filas_multiplicadas(self,matriz, fila_destino, fila_origen, escalar):
        
        for i in range(len(matriz[0])):
            matriz[fila_destino][i] += matriz[fila_origen][i] * escalar

 
    def scalar_mul(self, a, scalar):
        
        return [[elem * scalar for elem in row] for row in a]
    def inversa(self, mt): 
        #retorna la inversa de una matriz usando formula
        coord = self.get_element_at    

        def adj():
            adj_matrix = []

            for x in range(1, len(mt[0])+1):
                row = []
                for y in range(1, len(mt)+1):
                    row.append(self.cofactor(mt, x, y))
                adj_matrix.append(row)
            return self.transpuesta(adj_matrix)
                
        if len(mt) == 2 and len(mt[0]) == 2:
            div = 1 / self.determinante(mt)
            pre_inverse = []
            pre_inverse.append([coord(mt,2,2) , -1*coord(mt,1,2)])
            pre_inverse.append([-1*coord(mt,2,1), coord(mt,1,1)])
            
            return self.scalar_mul(pre_inverse, div)

        adj_matrix = adj()
        div = 1 / self.determinante(mt)

        return self.scalar_mul(adj_matrix, div) 
    
    def rango_matriz(self, matriz):
        """
        Función para calcular el rango de una matriz utilizando eliminación gaussiana.
        """
        #  eliminación gaussiana
        for i in range(len(matriz)):
            # verifica si el elemento es 0, para intercambiar
            if matriz[i][i] == 0:
                for j in range(i+1, len(matriz)):
                    if matriz[j][i] != 0:
                        matriz[i], matriz[j] = matriz[j], matriz[i]
                        break
                    

            # hacer 0 los elemento no pivotes
            for j in range(i+1, len(matriz)):
                if matriz[i][i] != 0:
                    escalar = -matriz[j][i] / matriz[i][i]
                    for k in range(i, len(matriz[0])):
                        matriz[j][k] += escalar * matriz[i][k]

        # recuentio de número de filas no nulas
        rango = sum(1 for fila in matriz if any(fila))
        return rango