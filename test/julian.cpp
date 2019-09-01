#include <iostream>
#include <string>
#include "../src/include/julian.h"

using namespace std;

int main(int argc, char **argv)
{
	// defaults
	GreenwichDate greenwichDate(6, 19.75, 2009);

	// If a month, day, and year was specified on the command line, use that instead
	if (argc == 4) {
		greenwichDate.month = atoi(argv[1]);
		greenwichDate.day = atof(argv[2]);
		greenwichDate.year = atoi(argv[3]);
	}

	CJulian julian;

	float julianDate = julian.GreenwichToJulian(greenwichDate);

	cout << std::fixed << "Julian date for " << greenwichDate.month << "/" << greenwichDate.day << "/" << greenwichDate.year << " is " << julianDate << endl;

	cout << "The day of the week for " << greenwichDate.month << "/" << greenwichDate.day << "/" << greenwichDate.year << " is " << julian.GetDayOfWeek(julianDate) << std::endl;

	GreenwichDate greenwichDateFromJulian = julian.JulianToGreenwich(julianDate);

	cout << std::fixed << "Converting back to Greenwich Date gives " << greenwichDateFromJulian.month << "/" << greenwichDateFromJulian.day << "/" << greenwichDateFromJulian.year << std::endl;

	return 0;
}