// euler.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <stdio.h>
#include <iostream>
#include <algorithm>  

using namespace std;

bool isPrime(int a);

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
	cout << question5();

	int tmp;

	cin >> tmp;

	return 0;
}

