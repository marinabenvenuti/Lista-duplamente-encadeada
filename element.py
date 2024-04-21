class Element:
    def __init__(self, value):
        self.__value = value
        self.__position = None
        self.__next = None
        self.__previous = None

    def get_value(self):
        return self.__value    

    def set_value(self, value):
        self.__value = value

    def get_next(self):
        return self.__next
    
    def set_next(self, next):
        self.__next = next
        
    def get_previous(self):
        return self.__previous
    
    def set_previous(self, previous):
        self.__previous = previous