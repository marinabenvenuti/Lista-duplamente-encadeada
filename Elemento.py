class Elemento:
    def __init__(self, id):
        self.__id = id
        self.__anterior = None
        self.__proximo = None
        
    @property
    def id(self):
        return self.__id
    
    @property
    def anterior(self):
        return self.__anterior
    
    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior
        
    @property
    def proximo(self):
        return self.__proximo
    
    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo
        


