import math
import string

class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)  
    def pop(self):
        return self.items.pop() 
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items) == 0 
    def peek(self):
        return self.items[-1]
        
def order(operator):
    if operator == '(' or operator == ')':
        return 3
    elif operator == '^':
        return 2
    elif operator == '*' or operator == '/':
        return 1
    elif operator == '-' or operator == '+':
        return 1
        
def reverse(string):
    rev = []
    for chr in string [::-1]:
        if chr == ')':
            rev.append('(')
        elif chr == '(':
            rev.append(')')
        else:
            rev.append(chr)
    return rev
    
def convert(infix):
    op = Stack()
    num = Stack()
    aux = reverse(infix)
    for chr in aux:
        if (chr.isalnum()==True):
            num.push(chr)
        elif (chr.isalpha()==True):
            num.push(chr)
        elif chr == '(':
            op.push(chr)
        elif ((chr=='+')or(chr=='-')or(chr=='*')or(chr=='/')) and op.is_empty()==True:
            op.push(chr)
        elif ((chr=='+')or(chr=='-')or(chr=='*')or(chr=='/')) and op.is_empty()==False:
            if order(op.peek())>order(chr):
                op.push(chr)
            elif order(op.peek())<=order(chr):
                num.push(op.pop())
                op.push(chr)
        elif chr == ')':
            while op.peek() != '(':
                num.push(op.pop())
            op.pop()           
    for item in op.items:
        num.push(op.pop())
    while num.is_empty() == False:
        print(num.pop(),end="")
                
inp = input()
convert(inp)
