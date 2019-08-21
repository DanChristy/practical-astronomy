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

CJulian::CJulian()
{
	// No initialization needed, for now.
}

float CJulian::GreenwichToJulian(int month, float day, int year)
{
	int y = year;
	int m = month;
	float d = day;
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
	CJulian *CJulian_new()
	{
		return new CJulian();
	}

	float CJulian_GreenwichToJulian(CJulian *julian, int month, float day, int year)
	{
		return julian->GreenwichToJulian(month, day, year);
	}
}