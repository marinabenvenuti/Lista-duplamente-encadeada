class Element:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value

    def get_next(self):
        return self.__next
    
    def set_next(self, next):
        self.__next = next