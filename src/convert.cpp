#include <iostream>
#include <string>
#include <vector>
#include "include/convert.h"

CConvert::CConvert()
{
	// no initialization needed, for now
}

float CConvert::GeneralTimeToDecimal(int hours, int minutes, int seconds, std::string period)
{
	float step1 = this->GeneralTimeToDecimal(hours, minutes, seconds);

	float returnValue = (period == "PM") ? step1 + 12 : step1;

	return returnValue;
}

float CConvert::GeneralTimeToDecimal(int hours, int minutes, int seconds)
{
	float step1 = (float)seconds / 60;
	float step2 = ((float)minutes + step1) / 60;
	float returnValue = step2 + (float)hours;

	return returnValue;
}

extern "C"
{
	CConvert *CConvert_new()
	{
		return new CConvert();
	}

	float CConvert_General12HourTimeToDecimal(CConvert *convert, int hours, int minutes, int seconds, char *period)
	{
		return convert->GeneralTimeToDecimal(hours, minutes, seconds, period);
	}

	float CConvert_General24HourTimeToDecimal(CConvert *convert, int hours, int minutes, int seconds)
	{
		return convert->GeneralTimeToDecimal(hours, minutes, seconds);
	}
}
