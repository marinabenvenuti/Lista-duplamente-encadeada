from Elemento import Elemento

class ListaDuplamEncad:
    def __init__(self):
        self.__contador = 0
        self.__inicio = None
        self.__fim = None
        self.__cursor = None
        
    @property
    def contador(self):
        return self.__contador
    
    @property
    def inicio(self):
        return self.__inicio
    
    @property
    def fim(self):
        return self.__fim
    
    @property
    def cursor(self):
        return self.__cursor
    
    @contador.setter
    def contador(self, contador):
        self.__contador = contador
        
    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio
        
    @inicio.setter
    def fim(self, fim):
        self.__fim = fim
        
    @cursor.setter
    def cursor(self, cursor):
        self.__cursor = cursor
        
    
    
    
    
e1 = Elemento(1)
e2 = Elemento(2)
e3 = Elemento(3)
e4 = Elemento(4)