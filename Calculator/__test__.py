""" main and test file for calculator """

import numpy
from queue_n_stack import Queue, Stack
from function import Function, Operator
from calculator import Calculator

print("Stack test")
STACK = Stack()
for elem in range(2, 6):
    STACK.push(elem)
while not STACK.is_empty():
    print(STACK.pop())
    print("Elements left: " + str(STACK.size()))

print("\nQueue test")
QUEUE = Queue()
for elem in range(2, 6):
    QUEUE.push(elem)
while not QUEUE.is_empty():
    print(QUEUE.pop())
    print("Elements left: " + str(QUEUE.size()))

print("\nFunction test")
EXPONENTIAL_FUNC = Function(numpy.exp)
SIN_FUNC = Function(numpy.sin)
print(EXPONENTIAL_FUNC.execute(SIN_FUNC.execute(0)))

print("\nOperator test")
ADD_OP = Operator(numpy.add, 0)
MULTIPLY_OP = Operator(numpy.multiply, 1)
print(ADD_OP.execute(1, MULTIPLY_OP.execute(2, 3)))

print("\nCalculator test")
CALC = Calculator()
print("Calculator class test: " + str(CALC.functions['EXP'].execute(
    (CALC.operators['PLUSS'].execute(1, CALC.operators['GANGE'].execute(2, 3))))))
CALC.output_queue.push(1)
CALC.output_queue.push(2)
CALC.output_queue.push(3)
CALC.output_queue.push(CALC.operators['GANGE'])
CALC.output_queue.push(CALC.operators['PLUSS'])
CALC.output_queue.push(CALC.functions['EXP'])
print("RPN calculation: " + str(CALC.rpn_calculation()))
CALC.shunting_yard(
    [CALC.functions['EXP'], "(", 2, CALC.operators['GANGE'], 3, CALC.operators['PLUSS'], 1, ")"])
print("Through shunting_yard: " + str(CALC.rpn_calculation()))
print("\nFinished calculator:")
print("Exp(1 pluss 2 gange 3) = " +
      str(CALC.calculate_expression("Exp(1 pluss 2 gange 3)")))
print("sqrt(5 gange 3 pluss 10) = " +
      str(CALC.calculate_expression("sqrt(5 gange 3 pluss 10)")))
print("((15 DELE (7 MINUS (1 PLUSS 1))) GANGE 3) MINUS (2 PLUSS (1 PLUSS 1)) = " +
      str(CALC.calculate_expression("((15 DELE (7 MINUS (1 PLUSS 1))) GANGE 3) MINUS (2 PLUSS (1 PLUSS 1))")))
print("(-10 gange 1.5) gange -1 = " +
      str(CALC.calculate_expression("(-10 gange 1.5) gange -1")))
