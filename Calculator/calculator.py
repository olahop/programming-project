""" main class calculator """

import re
import numbers
import numpy
from function import Function, Operator
from queue_n_stack import Queue, Stack


class Calculator:
    """ RPN calculator """

    functions = None
    operators = None
    output_queue = None

    def __init__(self):
        """ define supported functions and operators and link them to numpy functions """
        self.functions = {'EXP': Function(numpy.exp), 'LOG': Function(numpy.log), 'SIN': Function(
            numpy.sin), 'COS': Function(numpy.cos), 'SQRT': Function(numpy.sqrt)}
        self.operators = {'PLUSS': Operator(numpy.add, 0), 'GANGE': Operator(
            numpy.multiply, 1), 'DELE': Operator(numpy.divide, 1), 'MINUS': Operator(
                numpy.subtract, 0)}
        self.output_queue = Queue()

    def rpn_calculation(self):
        """ calculates the output_queue """
        number_stack = Stack()
        while not self.output_queue.is_empty():
            element = self.output_queue.pop()
            if isinstance(element, numbers.Number):
                number_stack.push(element)
            elif isinstance(element, Function):
                stack_element = number_stack.pop()
                result = element.execute(stack_element)
                number_stack.push(result)
            elif isinstance(element, Operator):
                stack_element_top = number_stack.pop()
                stack_element_bottom = number_stack.pop()
                result = element.execute(stack_element_bottom, stack_element_top)
                number_stack.push(result)
        return number_stack.pop()

    def shunting_yard(self, input_queue):
        """ transform and adds RPN text to the output_queue """
        operator_stack = Stack()
        for elem in input_queue:
            if isinstance(elem, numbers.Number):
                self.output_queue.push(elem)
            elif isinstance(elem, Function) or elem == "(":
                operator_stack.push(elem)
            elif elem == ")":
                top_of_stack_elem = operator_stack.pop()
                while top_of_stack_elem != "(" and (not operator_stack.is_empty()):
                    self.output_queue.push(top_of_stack_elem)
                    top_of_stack_elem = operator_stack.pop()
            else:
                while not operator_stack.is_empty():
                    top_of_stack = operator_stack.peek()
                    if isinstance(top_of_stack, Function) \
                            or (isinstance(top_of_stack, Operator) \
                                and elem.strength <= top_of_stack.strength):
                        top_of_stack_elem = operator_stack.pop()
                        self.output_queue.push(top_of_stack_elem)
                    else:
                        break
                operator_stack.push(elem)
        while not operator_stack.is_empty():
            self.output_queue.push(operator_stack.pop())

    def txt_parser(self, txt):
        """ parses txt to shunting_yard input array """
        input_queue = []
        upper_case = txt.upper()
        iterator = 0
        while iterator <= len(upper_case):
            functions = "|".join(["^" + func for func in self.functions])
            func_check = re.search(functions, upper_case[iterator:])
            operators = "|".join(["^" + operator for operator in self.operators])
            operator_check = re.search(operators, upper_case[iterator:])
            bracket_check = re.search("^[()]+", upper_case[iterator:])
            num_check = re.search("^[-0123456789.]+", upper_case[iterator:])
            if func_check:
                input_queue.append(self.functions[func_check.group()])
                iterator += func_check.end(0)
            elif operator_check:
                input_queue.append(self.operators[operator_check.group()])
                iterator += operator_check.end(0)
            elif bracket_check:
                input_queue.append(bracket_check.group()[0])
                iterator += 1
            elif num_check:
                input_queue.append(float(num_check.group()))
                iterator += num_check.end(0)
            elif iterator >= len(upper_case):
                break
            else:
                iterator += 1
        return input_queue

    def calculate_expression(self, txt):
        """ the functioning main of the calculator """
        input_queue = self.txt_parser(txt)
        self.shunting_yard(input_queue)
        return self.rpn_calculation()
