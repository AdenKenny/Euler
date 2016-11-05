#include "stdafx.h"
#include <vector>
#include <stdio.h>
#include <iostream>
#include <algorithm>  

using namespace std;

bool isPrime(int a);
bool isPyTrip(int a, int b, int c);
int nextSeq(int n);

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
					if (isPyTrip(a, b, c)) {
						return (a * b * c);
					}
				}
			}
		}
	}
	
	return 0;
}

int question14() {
	
	int maxLen = 0;
	int retVal = 0;

	for (int i = 0; i < 1000000; i++) {
		
		int len = 0;
		int numb = i;
		while (numb != 1) {
			numb = nextSeq(numb);
			len++;
		}

		if (len > maxLen) {
			maxLen = len;
			retVal = i;
		}
	}
	
	

	return retVal;
}

int nextSeq(int numb) {
	
	if (numb % 2 == 0) {
		return numb / 2;
	}

	else {
		return (3 * numb) + 1;
	}
}

bool isPyTrip(int a, int b, int c) {
	
	int sum = (a * a) + (b * b);

	if (sum == (c * c)) {
		return true;
	}
	
	return false;
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
	cout << question14();

	int tmp;

	cin >> tmp;

	return 0;
}

