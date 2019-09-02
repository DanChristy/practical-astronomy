#include <iostream>
#include <math.h>
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

GeneralTime CConvert::DecimalToGeneralTime(float decimalTime)
{
	float total_seconds = decimalTime * 3600;
	float seconds_2_dp = floor(((int)total_seconds % 60) * 1000) / 1000;
	float corrected_seconds = (seconds_2_dp == 60) ? 0 : seconds_2_dp;
	float corrected_remainder = (seconds_2_dp == 60) ? total_seconds + 60 : total_seconds;
	float minutes = int(floor(corrected_remainder / 60)) % 60;
	float hours = floor(corrected_remainder / 3600);
	hours = (decimalTime < 0) ? (-1 * hours) : hours;
	float seconds = corrected_seconds;

	GeneralTime generalTime((int)hours, (int)minutes, (int)seconds);

	return generalTime;
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

	GeneralTime CConvert_DecimalToGeneralTime(CConvert *convert, float decimalTime)
	{
		return convert->DecimalToGeneralTime(decimalTime);
	}
}
