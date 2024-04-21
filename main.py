from element import Element
from linked_list import LinkedList

if __name__ == '__main__':
    e1 = Element(22)
    e2 = Element(17)
    e3 = Element(13)
    e4 = Element(7)

    list = LinkedList(4)

    list.set_first(e1)
    list.add_next(e2)
    list.add_next(e3)
    list.add_previous(e4)
    print("Posição do cursor: ", list.get_cursor_position())

    for i in list.get_all():
        print(i.get_value())
