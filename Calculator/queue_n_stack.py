""" contains a standard queue and stack """


class Container:
    """ super class to the queue and stack """

    items = []

    def __init__(self):
        """ init """
        self.items = []

    def size(self):
        """ Return number of elements in self.items """
        return len(self.items)

    def is_empty(self):
        """ Check if self.items is empty """
        if self.items:
            return False
        return True

    def push(self, item):
        """Add item to end of self.items"""
        self.items.append(item)

    def pop(self):
        """Pop off the correct element of self.items, and return it"""

    def peek(self):
        """Return the top element without removing it"""


class Queue(Container):
    """ container subclass queue """

    def peek(self):
        return self.items[0]

    def pop(self):
        """Pop off the first element """
        assert not self.is_empty()
        return self. items.pop(0)


class Stack(Container):
    """ container subclass stack """

    def peek(self):
        return self.items[self.size()-1]

    def pop(self):
        """Pop off the first element """
        assert not self.is_empty()
        return self.items.pop(self.size()-1)
