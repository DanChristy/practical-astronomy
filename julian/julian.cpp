#include <iostream>
#include <string>
#include <vector>
#include "julian.h"

bool isGregorian(int month, int day, int year)
{
	// Dates > Oct 15 1582 are Gregorian

	if (year > 1582)
		return true;

	if (year < 1582)
		return false;

	if (month > 10)
		return true;

	if (month < 10)
		return false;

	return (day > 15) ? true : false;
}

CJulian::CJulian(int month, float day, int year)
{
	this->greenwich_month = month;
	this->greenwich_day = day;
	this->greenwich_year = year;
}

float CJulian::GetJulian()
{
	int y = this->greenwich_year;
	int m = this->greenwich_month;
	float d = this->greenwich_day;
	int yd = (m < 3) ? (y - 1) : y;
	int md = (m < 3) ? (m + 12) : m;
	int A = yd / 100;
	int B = (isGregorian(m, d, y)) ? (2 - A + (A / 4)) : 0;
	int C = (yd < 0) ? (365.25 * (float)yd) - .75 : 365.25 * yd;
	int D = 30.6001 * (md + 1);
	float JD = B + C + D + d + (float)1720994.5;

	return JD;
}

extern "C"
{
	CJulian *CJulian_new(int month, float day, int year)
	{
		return new CJulian(month, day, year);
	}

	float CJulian_GetJulian(CJulian *julian)
	{
		return julian->GetJulian();
	}
}