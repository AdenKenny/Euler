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

#include "util.h"

typedef unsigned __int64 uint64;

class Euler {
	public:
		static int problem_3();
		static int problem_5();
		static int problem_9();
		static int problem_12();
		static int problem_12_threads();
		static int problem_14();
		static int problem_19();
		static int problem_21();
		static int problem_22();
};