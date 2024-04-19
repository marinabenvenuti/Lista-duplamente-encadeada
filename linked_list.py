class LinkedList:
    def __init__(self, size) -> None:
        self.__start = None
        self.__end = None
        self.__counter = 0
        self.__cursor = None    #Every list should have a reference to its cursor (?)
        self.__size = size
        
    def list_all(self):
        auxiliar = self.__start
        if self.is_empty():
            raise Exception
        else: 
            for i in range(self.__counter - 1):
                print(self.__start.value())
                self.__start = self.__start.get_next() 
            self.__start = auxiliar

    def is_empty(self):
        if self.__start is None:
            return True
        else:
            return False

    def is_full(self):      
        if self.__counter == self.__size:
            return True
        else:
            return False

    def has(self, value):   #Searches for a element with given value, returns a boolean
        pass

    def which_index(self, value):    #Returns position of given value
        pass
    
    def set_before_cursor(self, value): 
        pass
    
    def set_after_cursor(self, value): 
        pass
    
    def set_first(self, value):
        if self.__counter>0:
            value.set_next(self.__start)
            self.__start = value
        else:
            self.__start = value
        self.__counter += 1
    
    def set_last(self, value):
        if self.__counter>0:
            value.set_previous(self.__end)
            self.__end = value
        else:
            self.__start = value
            self.__end = value
        self.__counter += 1

    def add_in_position(self, position):
        pass
    
    def delete_actual_cursor(self):
        pass
    
    def delete_first(self):
        pass
    
    def delete_last(self):
        pass
    
    def delete_in_position(self, position):
        pass
    
    def delete_value(self, value):
        pass
        
    #cursor:
    def go_to_start(self):
        self.set_pointer(self.__list.start())

    def go_to_end(self):
        self.set_pointer(self.__list.end())

    def forward(self, times):   #How many times the cursor should go forward
        for i in range(times):
            aux = self.__cursor
            self.__cursor = self.__cursor.get_next()
            

    def backward(self, times):  #How many times the cursor should go backwards
        for i in range(times):
            aux = self.__cursor
            self.__cursor = self.__cursor.get_previous()
