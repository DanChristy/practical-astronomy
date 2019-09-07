#!/usr/bin/python3

import lib.pa_conversions as PC
import lib.pa_models as PM

def testJulian(month,day,year):
	myConvert = PC.CConvert()

	dateToCheck = PM.CivilDate(month,day,year)

	julianDate = myConvert.GreenwichDateToJulianDate(dateToCheck)

	print("Julian Date for {month}/{day}/{year} is {julianDate}".format(month=dateToCheck.month, day=dateToCheck.day, year=dateToCheck.year, julianDate=julianDate))

	print("The day of the week for Julian Date {julianDate} is {dayOfWeek}".format(julianDate=julianDate, dayOfWeek=myConvert.JulianDateToWeekdayName(julianDate)))

	greenwichDate = myConvert.JulianDateToGreenwichDate(julianDate)

	print("Converting {julianDate} back to Greenwich Date gives {month}/{day}/{year}".format(julianDate=julianDate, month=greenwichDate.month, day=greenwichDate.day, year=greenwichDate.year))

	print("The day part of {julianDate} is {dayPart}".format(julianDate=julianDate, dayPart=myConvert.JulianDateDay(julianDate)))
	print("The month part of {julianDate} is {monthPart}".format(julianDate=julianDate, monthPart=myConvert.JulianDateMonth(julianDate)))
	print("The year part of {julianDate} is {yearPart}".format(julianDate=julianDate, yearPart=myConvert.JulianDateYear(julianDate)))

testJulian(6,19.75,2009)
