#include "stdafx.h"

int Euler::problem_3() {
	uint64 target = 600851475143;
	int upper_bound = round(sqrt(target));

	int highest = 0;

	for (int i = 1; i < upper_bound; i++) {
		if (target % i == 0) {
			if (Util::is_prime(i)) {
				highest = i;
			}
		}
	}

	return highest;
}

int Euler::problem_5() {

	std::vector<int> primes = {2, 11, 13, 17, 19};

	int initial = 2520;

	for (int &prime : primes) {
		initial *= prime;
	}

	return initial;
}

int Euler::problem_9() {
	
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

int Euler::problem_12_threads() {

	std::vector<long> triangles;

	for (int i = 1; i < 20000; ++i) {
		triangles.push_back(Util::sum_of(i));
	}

	std::size_t const halfPoint = triangles.size() / 2;

	std::vector<long> lo(triangles.begin(), triangles.begin() + halfPoint);
	std::vector<long> hi(triangles.begin() + halfPoint, triangles.end());

	std::vector<long> loLo(lo.begin(), lo.begin() + (lo.size() / 2));
	std::vector<long> hiLo(lo.begin() + (lo.size() / 2), lo.end());
	std::vector<long> loHi(hi.begin(), hi.begin() + (hi.size() / 2));
	std::vector<long> hiHi(hi.begin() + (hi.size() / 2), hi.end());

	auto checkFactors = [] (std::vector<long> vec) -> long {		

		for (long &triangle : vec) {
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
	};

	//std::future<long> futures[] = { std::async(checkFactors, hiLo), std::async(checkFactors, loHi),
	//	                            std::async(checkFactors, hiHi), std::async(checkFactors, loLo) };

	//for (unsigned int i = 0; i < 4; ++i) {
	//	std::future<long> future = futures[i];
	//}

	//for (std::future<long> tFuture : futures) {
	//	
	//	long result = tFuture.get();

	//	if (result != 0) {
	//		return result;
	//	}
	//}

	return 0;
}

int Euler::problem_12() {

	std::vector<long> triangles;

	for (int i = 12000; i < 20000; ++i) {
		triangles.push_back(Util::sum_of(i));
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

int Euler::problem_14() {
	
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

int Euler::problem_19() {

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

int Euler::problem_21() {
	int total = 0;

	for (int i = 1; i < 10000; ++i) {
		int n1 = Util::sum_of_divisors(i);
		int n2 = Util::sum_of_divisors(Util::sum_of_divisors(i));

		if (n2 == i && i < n1) {
			total += i + n1;
		}
	}

	return total;

}

int Euler::problem_22() {

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

	for (unsigned int i = 0; i < vec.size(); ++i) {
		
		std::string s = vec[i];
		
		int strTotal = 0;
		
		for (char &c : s) {
			strTotal += c - 64;
		}	

		total += strTotal * (i+1);
	}

	return total;
}

int main() {

	std::cout << Euler::problem_21() << std::endl;
	int holder;

	std::cin >> holder;

	return 0;
}