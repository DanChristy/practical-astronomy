#ifndef SHARED_H
#include "shared.h"
#endif

#ifndef JULIAN_H
#define JULIAN_H

/** This class provides functionality for working with Julian and Greenwich dates. */
class CJulian {
public:
	CJulian();

	/** Return a float representing the Julian date for the Greenwich month, day, and year specified.  */
	float GreenwichToJulian(GreenwichDate greenwichDate);

	/** Return a GreenwichDate object for the Julian Date specified.  */
	GreenwichDate JulianToGreenwich(float julianDate);

	/** Return the day of the week (e.g., "Sunday") for the Julian Date specified. */
	std::string GetDayOfWeek(float julianDate);
};
#endif