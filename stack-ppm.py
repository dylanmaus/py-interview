'''
Implement a stack that has the following methods:
push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack
max(), which returns the maximum value in the stack currently
constant time
'''

# LIFO

from collections import deque

stack = deque()

'''
stack.append(1)
stack.append(2)
stack.append(5)
'''

def push(s, v):
	s.append(v)
	# return s

'''pop already a part of Python standard lib'''



push(stack, 1)
push(stack, 2)
push(stack, 3)

m = max(stack)
print(m)