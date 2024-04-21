class LinkedList:
    def __init__(self, size) -> None:
        self.__start = None
        self.__end = None
        self.__counter = 0
        self.__cursor = None
        self.__size = size

    #Function for cursor position
    def get_cursor_position(self):
        aux = self.__start
        position = 0
        while aux != self.__cursor:
            position += 1
            aux = aux.get_next()
        return position

    #Functions for debugging, returns all elements from the list
    def get_all(self):
        if self.is_empty():
            raise Exception("This list is empty!")
        else:
            aux = self.__start
            aux_list = []
            while aux is not None:
                aux_list.append(aux)
                aux = aux.get_next()
            return aux_list

    #Boolean functions
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
        if self.is_empty():
            raise Exception("This list is empty")
        else:
            aux = self.__start
            while aux != self.__end:
                if aux.get_value() == value:
                    return True
                aux = aux.get_next()
            return False

    def position_of(self, value):    #Returns position of given value
        if self.has(value):
            aux = self.__cursor
            self.__cursor = self.__start
            while self.__cursor != self.__end:
                if self.__cursor.get_value() == value:
                    position = self.get_cursor_position()
                    self.__cursor = aux
                    return position
                self.__cursor = self.__cursor.get_next()
            self.__cursor = aux

    #Addition Functions
    def set_first(self, element):   #Doesn't change the cursor, unless it's the first added element of the list
        if self.is_full():
            raise Exception("The list is already full!")
        elif self.__counter>0:
            element.set_next(self.__start)
            self.__start.set_previous(element)
            self.__start = element
        else:
            self.__start = element
            self.__cursor = self.__start
            self.__end = self.__start
            self.__counter += 1

    def set_last(self, element):    #Doesn't change the cursor
        if self.is_full():
            raise Exception("The list is already full!")
        if self.__counter > 0:
            element.set_previous(self.__end)
            self.__end = element
        else:
            self.__start = element
            self.__end = element
        self.__counter += 1

    def add_next(self, element):    #Cursor goes to the added element, a.k.a "next"
        if self.is_empty():
            self.__start = element
            self.__cursor = self.__start
        elif self.is_full():
            raise Exception("The list is already full!")
        else:
            if self.__cursor == self.__end:
                self.__end = element
            element.set_next(self.__cursor.get_next())
            self.__cursor.set_next(element)
            element.set_previous(self.__cursor)
            self.__cursor = element
        self.__counter += 1
    
    def add_previous(self, element):    #Doesn't change the cursor
        if self.is_full():
            raise Exception("The list is already full!")
        elif self.is_empty():
            raise Exception("The list is empty!")
        else:
            element.set_next(self.__cursor)
            element.set_previous(self.__cursor.get_previous())
            self.__cursor.set_previous(element)
        self.__counter += 1

    def add_in_position(self, position, element):   #Cursor mobility follows "add_next" logic
        if self.is_full():
            raise Exception("The list is alreay full!")
        elif self.is_empty():
            self.set_first(element)
        else:
            self.add_next(self.go_to_position(position-1))
        self.__counter += 1

    #Deletion Functions
    def delete_current(self):   #Cursor goes to the previous
        if self.is_empty():
            raise Exception("This list is already full!")
        else:
            self.__cursor.get_previous().set_next(self.__cursor.get_next())
            self.__cursor.get_next().set_previous(self.__cursor.get_previous())
        self.__cursor = self.__cursor.get_previous()
        self.__counter -= 1

    def delete_first(self):     #Doesn't change the cursor
        if self.is_empty():
            raise Exception("This list is already empty!")
        else:
            self.__start = self.__start.get_next()
        self.__counter -= 1
    
    def delete_last(self):      #Doesn't change the cursor
        if self.is_empty():
            raise Exception("This list is already empty!")
        else:
            self.__end = self.__end.get_previous()
        self.__counter -= 1
    
    def delete_in_position(self, position): #Cursor mobility follows "go_to_position" logic
        if self.is_empty():
            raise Exception("This list is already empty!")
        else:
            self.go_to_position(position -1)
            self.__cursor.set_next(self.__cursor.get_next(self.__cursor.get_next()))
            self.__counter -= 1
    
    def delete_by_value(self, value):
        if self.is_empty():
            raise Exception("This list is already empty!")
        else:
            self.delete_in_position(self.position_of(value))
        
    #Cursor functions
    def go_to_first(self):
        if self.is_empty():
            raise Exception("This list is empty!")
        self.__cursor = self.__start

    def go_to_position(self, position):
        if self.is_empty():
            raise Exception("This list is empty!")
        elif position > self.__counter:
            raise Exception("This position is empty!")
        else:
            times = self.get_cursor_position() - position
            if times > 0:
                self.backward(times)
            else:
                times = -times
                self.forward(times)

    def go_to_last(self):
        if self.is_empty():
            raise Exception("This list is empty!")
        else:
            self.__cursor = self.__end

    def forward(self, times):   #How many times the cursor should go forward
        if self.is_empty():
            raise Exception("This list is empty!")
        elif self.get_cursor_position() + times > self.__size - 1:
            raise Exception("This index is out of range!")
        else:
            for i in range(times):
                self.__cursor = self.__cursor.get_next()

    def backward(self, times):  #How many times the cursor should go backwards
        if self.is_empty():
            raise Exception("This list is empty!")
        elif self.get_cursor_position() - times < 0:
            raise Exception("This index is out of range!")
        else:
            for i in range(times):
                self.__cursor = self.__cursor.get_previous()
