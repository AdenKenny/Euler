#pragma once

#include <vector>
#include <stdio.h>
#include <iostream>
#include <algorithm>  
#include <fstream>
#include <string>
#include <sstream>
#include <thread>
#include <future>
#include <math.h>
#include <list>

typedef unsigned __int64 uint64;

class Euler {
private:
	long sumOf(int n);
	bool isPrime(int n);

public:
	int question3();
	int question5();
	int question9();
	int question12();
	int question12Threads();
	int question14();
	int question19();
	int question22();
};