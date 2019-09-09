#!/usr/bin/python3

import lib.pa_datetime as PD
import lib.pa_models as PM

def testJulian(month,day,year):
	myDateTime = PD.CDateTime()

	dateToCheck = PM.CivilDate(month,day,year)

	julianDate = myDateTime.GreenwichDateToJulianDate(dateToCheck)

	print("Julian Date for {month}/{day}/{year} is {julianDate}".format(month=dateToCheck.month, day=dateToCheck.day, year=dateToCheck.year, julianDate=julianDate))

	print("The day of the week for Julian Date {julianDate} is {dayOfWeek}".format(julianDate=julianDate, dayOfWeek=myDateTime.JulianDateToWeekdayName(julianDate)))

	greenwichDate = myDateTime.JulianDateToGreenwichDate(julianDate)

	print("Converting {julianDate} back to Greenwich Date gives {month}/{day}/{year}".format(julianDate=julianDate, month=greenwichDate.month, day=greenwichDate.day, year=greenwichDate.year))

	print("The day part of {julianDate} is {dayPart}".format(julianDate=julianDate, dayPart=myDateTime.JulianDateDay(julianDate)))
	print("The month part of {julianDate} is {monthPart}".format(julianDate=julianDate, monthPart=myDateTime.JulianDateMonth(julianDate)))
	print("The year part of {julianDate} is {yearPart}".format(julianDate=julianDate, yearPart=myDateTime.JulianDateYear(julianDate)))

testJulian(6,19.75,2009)
