#include <iostream>
#include <string>
#include "../src/include/convert.h"

using namespace std;

int main(int argc, char **argv)
{
	CConvert convert;

	GeneralTime generalTime(18, 31, 27);

	float decimalTime = convert.GeneralTimeToDecimal(generalTime);
	cout << "Decimal time for 18:31:27 is " << decimalTime << endl;

	generalTime.hours -= 12;
	cout << "Decimal time for 6:31:27 PM is " << convert.GeneralTimeToDecimal(generalTime, "PM") << endl;

	GeneralTime generalTimeFromDecimal = convert.DecimalToGeneralTime(decimalTime);
	cout << "Converting back to general time gives " << generalTimeFromDecimal.hours << ":" << generalTimeFromDecimal.minutes << ":" << generalTimeFromDecimal.seconds << endl;

	return 0;
}
