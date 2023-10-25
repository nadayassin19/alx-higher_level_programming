#!/usr/bin/python3
"""It's a module of the class Node"""


class Node:
    """it defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """initialize data & next node

        Args:
            data (int): data value
            next_node (node): node value
        """
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """a property to retrieve data
        """
        return (self._data)

    @data.setter
    def data(self, value):
        """it's a method to set data
        """
        if type(self._data) != int:
            raise TypeError("data must be an integer")
        else:
            self._data = value

    @property
    def next_node(self):
        """a property to retrieve next node
        """
        return (self._next_node)

    @next_node.setter
    def next_node(self, value):
        """it's a method to set next node
        """
        if value is not None or type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """it's a class to defines a singly linked list
    """
    def __init__(self):
        """initialize a new singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """it's a method to insert a new Node

        Args:
            value (Node): the new node to be inserted
        """
        new = Node(value)
        if self.__head is None:
            new._next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """it's used to print the new singly linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
