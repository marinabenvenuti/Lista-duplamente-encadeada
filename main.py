from element import Element
from linked_list import LinkedList

if __name__ == '__main__':
    e1 = Element(22)
    e2 = Element(17)
    e3 = Element(8)
    e4 = Element(78)
    e5 = Element(13)

    list = LinkedList(2)
    
    list.set_first(e1)
    list.add_next(e2)
    print(list.list_all())
