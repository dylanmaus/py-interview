# check if sequence of parens is correct

from collections import deque

test_cases = {
	'{{}([])}': True,
	'((((((((': False,
	'({[t]})': True,
	'[)))': False,
	'({)}': False,
	'}': False,
	')(){}{{{[]}}}': False,
	'{{{{[[[[()]]]]}}}}': True,
	'(': False,
	'{{()}': False,
	'asdf': True,
	'{asdfsdf[a](b)((c){d}[e]}[]': False
	}


def check_parens(input_string):
	stack = deque()
	if input_string[0] in [')', '}', ']']:
		return False
	else:
		for char in input_string:
			if char in ['(', '{', '[']:
				stack.append(char)
			elif char == ')':
				if stack[-1] == '(' and len(stack) > 0:
					stack.pop()
			elif char == '}':
				if stack[-1] == '{' and len(stack) > 0:
					stack.pop()
			elif char == ']':
				if stack[-1] == '[' and len(stack) > 0:
					stack.pop()

		if len(stack) == 0:
			return True
		else:
			return False

for test_case in list(test_cases):
	print(check_parens(test_case) == test_cases[test_case])






