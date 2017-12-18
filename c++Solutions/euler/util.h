#pragma once

#include <vector>

class Util {

	public:
		static long sum_of(int n);
		static std::vector<int> divisors(int n);
		static bool is_prime(int n);
		static std::vector<bool> sieve(int n);
		static int sum_of_divisors(int n);
};