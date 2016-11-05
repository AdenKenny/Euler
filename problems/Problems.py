import math
from problems import Util

"""
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def question_1() -> int:
	list_numbs = []
	
	for i in range(1, 1000):
		if i % 3 == 0 and i % 5 == 0:
			list_numbs.append(i)
		elif i % 3 == 0:
			list_numbs.append(i)
		elif i % 5 == 0:
			list_numbs.append(i)
	
	return sum(list_numbs)
	
"""
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""


def question_2() -> int:
	last = 1
	last_2 = 1
	
	sums = []
	
	while last < 4000000:
		fib = last + last_2
		
		last = last_2
		last_2 = fib
		
		if fib % 2 == 0:
			sums.append(fib)
	
	return sum(sums)

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def question_3() -> int:
	target = 600851475143
	upper_bound = int(math.sqrt(target))
	
	highest = 0
	
	for i in range(1, upper_bound):
		if target % i == 0:
			if Util.Util.is_prime(i):
				highest = i
	
	return highest

"""
A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.
"""


def question_4() -> int:
	
	highest = 0
	
	for i in range(100, 999):
		for j in range(100, 999):
			prod = i * j
			if Util.Util.is_pal(prod):
				if prod > highest:
					highest = prod
	
	return highest
	
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def question_5() -> int:
	
	primes = (2, 11, 13, 17, 19)

	initial = 2520
		
	for prime in primes:
		initial *= prime
		
	return initial
		

def question_6() -> int:
	
	target = 100
	
	sum_of_squares = 0
	
	for i in range(1, target + 1):
		sum_of_squares += (i * i)

	sum_of_numbers = (target * (target + 1)) / 2
		
	print(sum_of_numbers)

	return (sum_of_numbers * sum_of_numbers) - sum_of_squares


def question_7() -> int:
	
	numb = 0
	target = 10001
	
	for i in range(2, 1000000):
		if Util.Util.is_prime(i):
			numb += 1
			if numb == target:
				return i
			
			
def question_8() -> int:
	num = 0  # Number omitted as is 1000 digits.

	prod = 1
	max_prod = 0
	
	num_str = str(num)
	
	length = len(num_str)
	
	for i in range(1, length - 13 + 1):
		prod = 1
		for j in range(i, i + 13):
			prod *= int(num_str[j - 1: j])
			
			if prod > max_prod:
				max_prod = prod
	
	return max_prod


def question_9() -> int:
	pass


def main():
	print(question_8())

main()