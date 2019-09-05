#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include "include/julian.h"

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

float CJulian::GreenwichToJulian(GreenwichDate greenwichDate)
{
	float y = greenwichDate.year;
	float m = greenwichDate.month;
	float d = greenwichDate.day;
	float yd = (m < 3) ? (y - 1) : y;
	float md = (m < 3) ? (m + 12) : m;
	float A = floor(yd / 100);
	float B = (isGregorian(m, d, y)) ? (2 - A + floor((A / 4))) : 0;
	float C = (yd < 0) ? floor((365.25 * yd) - .75) : floor(365.25 * yd);
	float D = floor(30.6001 * (md + 1));
	float JD = B + C + D + d + (float)1720994.5;

	return JD;
}

GreenwichDate CJulian::JulianToGreenwich(float julianDate)
{
	float l = floor(julianDate + 0.5);
	float F = julianDate + 0.5 - l;
	float A = floor((l - 1867216.25) / 36524.25);
	float B = (l > 2299160) ? l + 1 + A - floor(A / 4) : l;
	float C = B + 1524;
	float D = floor((C - 122.1) / 365.25);
	float E = floor(365.25 * D);
	float G = floor((C - E) / 30.6001);

	float d = C - E + F - floor(30.6001 * G);
	float m = (G < 13.5) ? G - 1 : G - 13;
	float y = (m > 2.5) ? D - 4716 : D - 4715;

	GreenwichDate greenwichDate(m, d, y);

	return greenwichDate;
}

std::string CJulian::GetDayOfWeek(float julianDate)
{
	float workingJulian = (int)(julianDate - 0.5) + 0.5;
	float n = (int)(workingJulian + 1.5) % 7;

	std::string dayName = "";
	switch ((int)n) {
	case 0:
		dayName = "Sunday";
		break;
	case 1:
		dayName = "Monday";
		break;
	case 2:
		dayName = "Tuesday";
		break;
	case 3:
		dayName = "Wednesday";
		break;
	case 4:
		dayName = "Thursday";
		break;
	case 5:
		dayName = "Friday";
		break;
	case 6:
		dayName = "Saturday";
		break;
	default:
		break;
	}

	return dayName;
}

extern "C"
{
	CJulian *CJulian_new()
	{
		return new CJulian();
	}

	float CJulian_GreenwichToJulian(CJulian *julian, GreenwichDate greenwichDate)
	{
		return julian->GreenwichToJulian(greenwichDate);
	}

	GreenwichDate CJulian_JulianToGreenwich(CJulian *julian, float julianDate)
	{
		return julian->JulianToGreenwich(julianDate);
	}

	char *CJulian_GetDayOfWeek(CJulian *julian, float julianDate)
	{
		std::string dayName = julian->GetDayOfWeek(julianDate);

		return dayName.data();
	}
}