// euler.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <stdio.h>
#include <iostream>

using namespace std;

bool isPrime(int a);

long long question3() {
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
	cout << question3();

	return 0;
}

