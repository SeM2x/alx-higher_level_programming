#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Represents a Node"""

    def __init__(self, data, next_node=None):
        """initialized a Node instance"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns data"""
        return self.__data

    @data.setter
    def data(self, value):
        """selt data to value"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """returns next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """selt next_node to value"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a SinglyLinkedList"""

    def __init__(self):
        """initialized a SinglyLinkedList instance"""
        self.__head = None

    def __str__(self):
        """returns a string to print"""

        string = ""
        node = self.__head
        while (node is not None):
            string += str(node.data)
            if node.next_node is not None:
                string += '\n'
            node = node.next_node
        return string

    def sorted_insert(self, value):
        """inserts a node in the sorted list"""

        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            if self.__head.data > node.data:
                node.next_node = self.__head
                self.__head = node
            else:
                tail = self.__head
                while (tail.next_node is not None
                        and tail.next_node.data < node.data):
                    tail = tail.next_node

                node.next_node = tail.next_node
                tail.next_node = node
