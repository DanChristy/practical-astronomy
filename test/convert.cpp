#include <iostream>
#include <string>
#include "../src/include/convert.h"

using namespace std;

int main(int argc, char **argv)
{
	CConvert convert;

	GeneralTime generalTime(18, 31, 27);

	cout << "Decimal time for 18:31:27 is " << convert.GeneralTimeToDecimal(generalTime) << endl;

	generalTime.hours -= 12;
	cout << "Decimal time for 6:31:27 PM is " << convert.GeneralTimeToDecimal(generalTime, "PM") << endl;

	return 0;
}
