#include <iostream>
#include <string>
#include <vector>
#include "doe.h"

CDoe::CDoe()
{
	// no initialization needed, for now
}

std::string CDoe::GetEaster(float year)
{
	int a = (int)year % 19;
	int b = (int)year / 100;
	int c = (int)year % 100;
	int d = b / 4;
	int e = b % 4;
	int f = (b + 8) / 25;
	int g = (b - f + 1) / 3;
	int h = ((19 * a) + b - d - g + 15) % 30;
	int i = c / 4;
	int k = c % 4;
	int l = (32 + 2 * (e + i) - h - k) % 7;
	int m = (a + (11 * h) + (22 * l)) / 451;
	int n = (h + l - (7 * m) + 114) / 31;
	int p = (h + l - (7 * m) + 114) % 31;
	int day = p + 1;
	int month = n;

	return std::to_string(month) + "/" + std::to_string(day) + "/" + std::to_string((int)year);
}

extern "C"
{
	CDoe *CDoe_new()
	{
		return new CDoe();
	}

	char *CDoe_GetEaster(CDoe *doe, float year)
	{
		std::string easterString = doe->GetEaster(year);

		return easterString.data();
	}
}
