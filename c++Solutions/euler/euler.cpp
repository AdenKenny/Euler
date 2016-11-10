#include "stdafx.h"

int Euler::question3() {
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

int Euler::question5() {

	std::vector<int> primes = {2, 11, 13, 17, 19};

	int initial = 2520;

	for (int &prime : primes) {
		initial *= prime;
	}

	return initial;
}

int Euler::question9() {
	
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

int Euler::question12() {

	std::vector<long> triangles;

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

int Euler::question14() {
	
	int maxLen = 0;
	int retVal = 0;

	for (int i = 1; i < 1000000; ++i) {
				
		int len = 0;
		uint64 numb = i;
		auto lambda = [&numb] (uint64) -> uint64 {
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

int Euler::question19() {

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

int Euler::question22() {

	std::vector<std::string> vec;

	std::ifstream file("p022_names.txt");
	std::string input;	
	while (std::getline(file, input)) {
		
	}

	std::stringstream ss(input);

	std::string token;

	while (std::getline(ss, token, ',')) {
		vec.push_back(token);
	}

	for (std::string &s : vec) {
		s.erase(std::remove(s.begin(), s.end(), '\"'), s.end());
	}

	std::sort(vec.begin(), vec.end());

	long total = 0;

	for (int i = 0; i < vec.size(); ++i) {
		
		std::string s = vec[i];
		
		int strTotal = 0;
		
		for (char &c : s) {
			strTotal += c - 64;
		}	

		total += strTotal * (i+1);
	}

	return total;
}

long Euler::sumOf(int n) {
	return (n * (n + 1)) / 2;
}

bool Euler::isPrime(int n) {
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

int main() {

	Euler e = Euler();

	std::cout << e.question22() << std::endl;
	int holder;

	std::cin >> holder;

	return 0;
}