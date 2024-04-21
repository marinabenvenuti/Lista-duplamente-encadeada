from element import Element
from linked_list import LinkedList

if __name__ == '__main__':
    #Elements Instantiation
    e1 = Element(22)
    e2 = Element(17)
    e3 = Element(13)
    e4 = Element(7)
    e5 = Element(75)
    e6 = Element(4)
    e7 = Element(36)

    #List Instantiation
    list = LinkedList(7)

    #Testing Functions
    list.set_first(e1)
    print("Cursor position on 1st step: ", list.get_cursor_position())

    list.add_in_position(0, e2)
    print("Cursor position on 2nd step: ", list.get_cursor_position())

    list.add_previous(e3)
    print("Cursor position on 3rd step: ", list.get_cursor_position())

    list.delete_last()
    print("Cursor position on 4th step: ", list.get_cursor_position())

    list.add_next(e7)
    print("Cursor position on 5th step: ", list.get_cursor_position())

    list.backward(1)
    print("Cursor position on 6th step: ", list.get_cursor_position())

    list.delete_current()
    print("Cursor position on 7th step: ", list.get_cursor_position())


    #Output
    print("-------End Result-------")
    for element in list.get_all():
        print(element.get_value())