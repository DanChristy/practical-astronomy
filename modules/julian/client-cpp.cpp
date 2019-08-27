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

	float julianDate = julian.GreenwichToJulian(inputMonth, inputDay, inputYear);

	cout << std::fixed << "Julian date for " << inputMonth << "/" << inputDay << "/" << inputYear << " is " << julianDate << endl;

	cout << "The day of the week for " << inputMonth << "/" << inputDay << "/" << inputYear << " is " << julian.GetDayOfWeek(julianDate) << std::endl;

	GreenwichDate greenwichDate = julian.JulianToGreenwich(julianDate);

	cout << std::fixed << "Converting back to Greenwich Date gives " << greenwichDate.month << "/" << greenwichDate.day << "/" << greenwichDate.year << std::endl;

	return 0;
}