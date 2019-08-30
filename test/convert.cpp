#include <iostream>
#include <string>
#include "../src/include/convert.h"

using namespace std;

int main(int argc, char **argv)
{
	CConvert convert;

	cout << "Decimal time for 18:31:27 is " << convert.GeneralTimeToDecimal(18, 31, 27) << endl;
	cout << "Decimal time for 6:31:27 PM is " << convert.GeneralTimeToDecimal(6, 31, 27, "PM") << endl;

	return 0;
}
