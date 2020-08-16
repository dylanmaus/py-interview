# Return the nth Fibonacci number
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacciRecursive(n):

	if n <= 2:
		return 1
	else:
		return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)


def fibonacciIterative(n):

	fibNums = []
	for i in range(0, n):
		if i <= 2:
			fibNums.append(i)
		else:
			fibNums.append(fibNums[i-1] + fibNums[i-2])

	return fibNums[n-1]


def fibonacciDynamic(n, memo):

	if n in memo:
		return memo[n]
	if n <= 2:
		f = 1
	else:
		f = fibonacciDynamic(n-1, memo) + fibonacciDynamic(n-2, memo)
		# print('hi')
	memo[n] = f
	print(memo)

	return f


def main():

	n = 10
	# f1 = fibonacciRecursive(n)
	# print(f1)
	# f2 = fibonacciIterative(n)
	# print(f2)
	memo = {}
	f3 = fibonacciDynamic(n, memo)
	print(f3)


if __name__ == '__main__':
	main()
	