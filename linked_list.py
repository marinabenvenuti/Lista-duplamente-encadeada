class LinkedList:
    def __init__(self) -> None:
        self.__start = None
        self.__end = None
        self.__counter = 0
        self.__cursor = None    #Every list should have a reference to its cursor (?)

    def list_all(self):
        if self.__is_empty():
            raise Exception
        else: 
            for i in range(self.__counter - 1):
                print(self.__start.value())
                self.__start = self.__start.get_next()

    def is_empty(self):
        if self.__start is None:
            return True
        else:
            return False

    def is_full(self):      #Technically a list is always full (?)
        pass

    def has(self, value):   #Searches for a element with given value, returns a boolean
        pass

    def which_index(self, value):    #Returns position of given value
        pass
