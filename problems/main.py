def question_1():
	list_numbs = []
	
	for i in range(1, 1000):
		if i % 3 == 0 and i % 5 == 0:
			list_numbs.append(i)
		elif i % 3 == 0:
			list_numbs.append(i)
		elif i % 5 == 0:
			list_numbs.append(i)
	
	result = sum(list_numbs)
	
	print(result)
	
	
def question_2():
	last = 1
	last_2 = 1
	
	sums = []
	
	while last < 4000000:
		fib = last + last_2
		
		last = last_2
		last_2 = fib
		
		if fib % 2 == 0:
			sums.append(fib)
	
	print(sum(sums))


def question_3():
	target = 600851475143


def main():
	question_3()

main()