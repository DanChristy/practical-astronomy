#ifndef SHARED_H
#include "shared.h"
#endif

#ifndef CONVERT_H
#define CONVERT_H

/** This class provides functionality for time conversions. */
class CConvert {
public:
	CConvert();

	/** Convert 12-hour general time to decimal time */
	float GeneralTimeToDecimal(GeneralTime generalTime, std::string period);

	/** Convert 24-hour general time to decimal time */
	float GeneralTimeToDecimal(GeneralTime generalTime);
};
#endif
