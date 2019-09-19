""" calculator execution helper class """

import numbers


class Function:
    """ function class """

    func = None

    def __init__(self, func):
        """ init """
        self.func = func

    def execute(self, element):
        """ checks if input element is a number """
        if not isinstance(element, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element)
        return result


class Operator:
    """ operator class """

    operation = None
    strength = None

    def __init__(self, operation, strength):
        """ init """
        self.operation = operation
        self.strength = strength

    def execute(self, element_1, element_2):
        """ execute the operation with the input elements """
        if not (isinstance(element_1, numbers.Number) and isinstance(element_2, numbers.Number)):
            raise TypeError("Cannot execute func if element is not a number")
        return self.operation(element_1, element_2)
