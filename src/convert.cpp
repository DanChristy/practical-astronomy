#include <iostream>
#include <string>
#include <vector>
#include "include/convert.h"

CConvert::CConvert()
{
	// no initialization needed, for now
}

float CConvert::GeneralTimeToDecimal(GeneralTime generalTime, std::string period)
{
	float step1 = this->GeneralTimeToDecimal(generalTime);

	float returnValue = (period == "PM") ? step1 + 12 : step1;

	return returnValue;
}

float CConvert::GeneralTimeToDecimal(GeneralTime generalTime)
{
	float step1 = (float)generalTime.seconds / 60;
	float step2 = ((float)generalTime.minutes + step1) / 60;
	float returnValue = step2 + (float)generalTime.hours;

	return returnValue;
}

extern "C"
{
	CConvert *CConvert_new()
	{
		return new CConvert();
	}

	float CConvert_General12HourTimeToDecimal(CConvert *convert, GeneralTime generalTime, char *period)
	{
		return convert->GeneralTimeToDecimal(generalTime, period);
	}

	float CConvert_General24HourTimeToDecimal(CConvert *convert, GeneralTime generalTime)
	{
		return convert->GeneralTimeToDecimal(generalTime);
	}
}
