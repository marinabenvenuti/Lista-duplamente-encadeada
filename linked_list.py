class LinkedList:
    def __init__(self, size) -> None:
        self.__start = None
        self.__end = None
        self.__counter = 0
        self.__cursor = None
        self.__size = size

    def list_all(self):
        aux = self.__start
        if self.is_empty():
            raise Exception("This list is empty!")
        else: 
            for i in range(2):
                print(self.__start.get_value())
                self.__start = self.__start.get_next() 
            self.__start = aux

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

    def position_of(self, value):    #Returns position of given value
        pass
    
    def set_first(self, element):
        if self.is_full():
            raise Exception("The list is already full!")
        elif self.__counter>0:
            element.set_next(self.__start)
            self.__start.set_previous(element)
            self.__start = element
        else:
            self.__start = element
        self.__cursor = self.__start
        self.__counter += 1
    
    def set_last(self, element):
        if self.is_full():
            raise Exception
        if self.__counter>0:
            element.set_previous(self.__end)
            self.__end = element
        else:
            self.__start = element
            self.__end = element
        self.__counter += 1

    def add_next(self, element):
        if self.is_empty():
            self.__start = element
            self.__cursor = self.__start
        elif self.is_full():
            raise Exception("The list is already full!")
        else:
            element.set_next(self.__cursor.get_next())
            self.__cursor.set_next(element)
            element.set_previous(self.__cursor)
        self.__counter += 1
    
    def add_previous(self, element): 
        if self.is_full():
            raise Exception
        elif self.is_empty():
            raise Exception
        else:
            element.set_next(self.__cursor)
            element.set_previous(self.__cursor.get_previous())
            self.__cursor_set_previous(element)
            self.__counter += 1

    def add_in_position(self, position, element):
        if self.is_full():
            raise Exception
    
    def delete_current(self):
        if self.is_empty():
            raise Exception
        else:
            pass
    def delete_first(self):
        if self.is_empty():
            raise Exception
    
    def delete_last(self):
        if self.is_empty():
            raise Exception
    
    def delete_in_position(self, position):
        if self.is_empty():
            raise Exception
    
    def delete_by_value(self, value):
        if self.is_empty():
            raise Exception
        
    #cursor functions:
    def go_to_first(self):
        if self.is_empty():
            raise Exception
        self.__cursor = self.__start()

    def go_to_last(self):
        if self.is_empty():
            raise Exception
        self.__cursor = self.__end()

    def forward(self, times):   #How many times the cursor should go forward
        for i in range(times):
            aux = self.__cursor
            self.__cursor = self.__cursor.get_next()

    def backward(self, times):  #How many times the cursor should go backwards
        for i in range(times):
            aux = self.__cursor
            self.__cursor = self.__cursor.get_previous()
