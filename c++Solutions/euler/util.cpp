#include "stdafx.h"
#include "util.h"

long Util::sum_of(int n) {
	return (n * (n + 1)) / 2;
}

std::vector<int> Util::divisors(int n) {

	std::vector<int> divisors = std::vector<int>();
	
	for (int i = 1, s = (n / 2) + 1; i < n; ++i) {
		if (n % i == 0) {
			divisors.push_back(i);
		}
	}

	divisors.push_back(n);

	return divisors;
}

int Util::sum_of_divisors(int n) {
	
	int total = 0;
	
	for (int i = 1, s = n / 2; i <= s; ++i) {
		if (n % i == 0) {
			total += i;
		}
	}

	return total;
}

bool Util::is_prime(int n) {
	if (n < 2) {
		return false;
	}

	if (n == 2) {
		return true;
	}

	if (n % 2 == 0) {
		return false;
	}

	for (int i = 3; (i * i) <= n; i += 2) {
		if (n % i == 0) {
			return false;
		}
	}

	return true;
}

std::vector<bool> Util::sieve(int n) {
		
		std::vector<bool> prime = std::vector<bool>();

		for (int p = 2; p * p <= n; ++p) {
			if (prime[p] == true) {
				for (int i = p * 2; i <= n; i += p) {
					prime[i] = false;
				}
			}
		}

		return prime;
};