#include <iostream>
#include <string>
#include "doe.h"

using namespace std;

int main(int argc, char **argv)
{
	float inputYear = 2019; // default to 2019

	// If a year was specified on the command line, use that instead
	if (argc == 2) {
		inputYear = strtof(argv[1], 0);
	}

	CDoe doe(inputYear);

	cout << "Easter date is " << doe.GetEaster() << endl;

	return 0;
}