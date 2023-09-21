import math
import string

class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        return self.items[-1]
    
def reverse(equation):
    
        
def order(operator):
    if operator == '(' or operator ==')':
        return 3
    elif operator == '^':
        return 2
    elif operator == '*' or operator == '/':
        return 1
    elif operator == '-' or operator == '+':
        return 0
    
def infix2prefix(infix):
    opStack = Stack()
    outStack = Stack()
    aux_stack = Stack()
    infixrev = reverse(infix)

    for chr in infixrev:
        if (chr.isalnum() == True):
            outStack.push(chr)
        elif(chr.isalpha() == True):
            outStack.push(chr)
        elif chr == '(':
            opStack.push(chr)
        elif ((chr == '+') or (chr == '-') or (chr == '*') or (chr == '/')) and opStack.is_empty() == True:
            opStack.push(chr)
        elif ((chr == '+') or (chr == '-') or (chr == '*') or (chr == '/')) and opStack.is_empty() == False:
            if order(opStack.peek())>order(chr):
                opStack.push(chr)
            elif order(opStack.peek())<=order(chr):
                outStack.push(opStack.pop())
                opStack.push(chr)
        elif chr == ")":
            if opStack.is_empty() == True:
                opStack.push(chr)
            if opStack.is_empty() == False:
                while opStack.peek != '(':
                    outStack.push(opStack.pop())
    
    for item in opStack.items:
        outStack.push(opStack.pop())

    while outStack.is_empty() == False:
        print(outStack.pop(),end='')


A = "(9+1)*(((1+2)+3)+4)"
revA = reverse(A)
print(revA)

"""
    (9+1)*(((1+2)+3)+4)
"""
