from copy import deepcopy
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