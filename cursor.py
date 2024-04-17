class Cursor:       #Should the cursor actually be another class (?)
    def __init__(self, linked_list: object) -> None:
        self.__list = linked_list       #Every cursor should be associated with a linked_list
        self.__pointer = None
    
    def get_pointer(self):
        return self.__pointer
    
    def set_pointer(self, address):
        self.__pointer = address

    def go_to_start(self):
        self.set_pointer(self.__list.start())

    def go_to_end(self):
        self.set_pointer(self.__list.end())

    def forward(self, times):   #How many times the cursor should go forward
        pass

    def backward(self, times):  #How many times the cursor should go backwards
        pass