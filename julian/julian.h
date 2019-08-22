#ifndef JULIAN_H
#define JULIAN_H

/** Simple Greenwich Date structure (month, fractional day, year) */
struct GreenwichDate {
	int month;
	float day;
	int year;
};

/** This class provides functionality for working with Julian and Greenwich dates. */
class CJulian {
public:
	CJulian();

	/** Return a float representing the Julian date for the Greenwich month, day, and year specified.  */
	float GreenwichToJulian(int month, float day, int year);

	/** Return a GreenwichDate object for the Julian Date specified.  */
	GreenwichDate JulianToGreenwich(float julianDate);
};
#endif