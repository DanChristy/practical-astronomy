#ifndef JULIAN_H
#define JULIAN_H

struct GreenwichDate {
	int month;
	float day;
	int year;
};

/** This class provides functionality for determining the Julian date. */
class CJulian {
public:
	CJulian();

	/** Return a float representing the Julian date, for the Greenwich month, day, and year specified.  */
	float GreenwichToJulian(int month, float day, int year);

	GreenwichDate JulianToGreenwich(float julianDate);
};
#endif