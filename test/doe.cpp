#include <iostream>
#include <string>
#include "../src/include/doe.h"

using namespace std;

int main(int argc, char **argv)
{
	float inputYear = 2019; // default to 2019

	// If a year was specified on the command line, use that instead
	if (argc == 2) {
		inputYear = strtof(argv[1], 0);
	}

	CDoe doe;

	cout << "Easter date is " << doe.GetEaster(inputYear) << endl;

	return 0;
}
