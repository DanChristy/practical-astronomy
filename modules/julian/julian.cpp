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

GreenwichDate CJulian::JulianToGreenwich(float julianDate)
{
	GreenwichDate greenwichDate;

	int l = julianDate + 0.5;
	float F = julianDate + 0.5 - l;
	int A = ((float)l - 1867216.25) / 36524.25;
	int B = (l > 2299160) ? l + 1 + A - (int)(A / 4) : l;
	int C = B + 1524;
	int D = (C - 122.1) / 365.25;
	int E = 365.25 * D;
	int G = (C - E) / 30.6001;

	float d = C - E + F - (int)(30.6001 * G);
	int m = ((float)G < 13.5) ? G - 1 : G - 13;
	int y = ((float)m > 2.5) ? D - 4716 : D - 4715;

	greenwichDate.month = m;
	greenwichDate.day = d;
	greenwichDate.year = y;

	return greenwichDate;
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

	GreenwichDate CJulian_JulianToGreenwich(CJulian *julian, float julianDate)
	{
		return julian->JulianToGreenwich(julianDate);
	}
}