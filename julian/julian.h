#ifndef JULIAN_H
#define JULIAN_H

/** This class provides functionality for determining the Julian date. */
class CJulian {
private:
	int greenwich_month;
	float greenwich_day;
	int greenwich_year;

public:
	CJulian(int month, float day, int year);

	/** Return a float representing the Julian date, for the month, day, and year specified at init.  */
	float GetJulian();
};
#endif