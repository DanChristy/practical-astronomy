#include <iostream>
#include <string>
#include "julian.h"

using namespace std;

int main(int argc, char **argv)
{
	// defaults
	int inputMonth = 6;
	float inputDay = 19.75;
	int inputYear = 2009;

	// If a month, day, and year was specified on the command line, use that instead
	if (argc == 4) {
		inputMonth = atoi(argv[1]);
		inputDay = atof(argv[2]);
		inputYear = atoi(argv[3]);
	}

	CJulian julian;

	cout << std::fixed << "Julian date is " << julian.GreenwichToJulian(inputMonth, inputDay, inputYear) << endl;

	return 0;
}