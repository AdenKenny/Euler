#include "stdafx.h"
#include <vector>
#include <stdio.h>
#include <iostream>
#include <algorithm>  
#include <unordered_map>

typedef unsigned __int64 uint;

using namespace std;

bool isPrime(int a);
long sumOf(int a);

int question3() {
	long long target = 600851475143;
	int upperBound = sqrt(target);

	int highest = 0;

	for (int i = 1; i < upperBound; i++) {
		if (target % i == 0) {
			if (isPrime(i)) {
				highest = i;
			}
		}
	}

	return highest;
}

int question5() {

	vector<int> primes = {2, 11, 13, 17, 19};

	int initial = 2520;

	for (int &prime : primes) {
		initial *= prime;
	}

	return initial;
}

int question9() {
	
	for (int a = 1; a < 500; ++a) {
		for (int b = 1; b < 500; ++b) {
			for (int c = 1; c < 500; ++c) {
				if ((a + b + c) == 1000) {
					
					auto lambda = [&a, &b, &c] (int, int, int) {
						int sum = (a * a) + (b * b);
						if ((a * a) + (b * b) == (c * c)) {
							return true;
						}

						return false;
					};
					
					if (lambda(a, b, c)) {
						return (a * b * c);
					}
				}
			}
		}
	}
	
	return 0;
}

int question12() {

	vector<long> triangles;

	for (int i = 12000; i < 20000; ++i) {
		triangles.push_back(sumOf(i));
	}

	for (long &triangle : triangles) {
		int factors = 0;

		for (long i = 1; i < (triangle / 2) + 1; ++i) {
			if (triangle % i == 0) {
				factors++;
			}
		}

		if (factors >= 500) {
			return triangle;
		}
	}

	return 0;
}

int question14() {
	
	int maxLen = 0;
	int retVal = 0;

	for (int i = 1; i < 1000000; ++i) {
				
		int len = 0;
		uint numb = i;
		auto lambda = [&numb] (uint) {
			if (numb % 2 == 0) {
				return numb / 2;
			}
			else {
				return (3 * numb) + 1;
			}
		};

		while (numb != 1) {
			numb = lambda(numb);
			len++;
		}

		if (len > maxLen) {
			maxLen = len;
			retVal = i;
		}
	}
	
	return retVal;
}

int question19() {

	int totalDays = 0;
	for (int i = 1901; i <= 2000; ++i) {
		if (i % 4 == 0) {
			totalDays += 366;
		}

		else {
			totalDays += 365;
		}
	}

	int numbSundays = 0;
	for (int i = 1; i <= totalDays; ++i) {
		if (i % 7 == 0) {
			numbSundays++;
		}
	}

	return numbSundays;
}

int question20() {
	int target = 100;

	uint sum = 0;
	for(int i = 1; i < target; ++i) {
		for(int j = 1; j < i; ++j) {
			sum += j
		}
	}

	return 0;
}

long sumOf(int n) {
	return (n * (n + 1)) / 2;
}

bool isPrime(int number) {
	if (number < 2) {
		return false;
	}

	if (number == 2) {
		return true;
	}

	if (number % 2 == 0) {
		return false;
	}

	for (int i = 3; (i * i) <= number; i += 2) {
		if (number % i == 0) {
			return false;
		}
	}

	return true;
}

int main() {
	cout << question19();

	int tmp;

	cin >> tmp;

	return 0;
}

