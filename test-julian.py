#!/usr/bin/python3

import lib.pa_conversions as PC
import lib.pa_shared as PS

def testJulian(month,day,year):
	myConvert = PC.CConvert()

	dateToCheck = PS.CivilDate(month,day,year)

	julianDate = myConvert.GreenwichDateToJulianDate(dateToCheck)

	print("Julian Date for {month}/{day}/{year} is {julianDate}".format(month=dateToCheck.month, day=dateToCheck.day, year=dateToCheck.year, julianDate=julianDate))

	greenwichDate = myConvert.JulianDateToGreenwichDate(julianDate)

	print("Converting {julianDate} back to Greenwich Date gives {month}/{day}/{year}".format(julianDate=julianDate, month=greenwichDate.month, day=greenwichDate.day, year=greenwichDate.year))

testJulian(6,19.75,2009)
