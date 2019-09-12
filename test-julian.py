#!/usr/bin/python3

import lib.pa_datetime as PD

def testJulian(month,day,year):
	julianDate = PD.GreenwichDateToJulianDate(day,month,year)

	print("Julian Date for {month}/{day}/{year} is {julianDate}".format(month=month, day=day, year=year, julianDate=julianDate))

	print("The day of the week for Julian Date {julianDate} is {dayOfWeek}".format(julianDate=julianDate, dayOfWeek=PD.JulianDateToWeekdayName(julianDate)))

	day,month,year = PD.JulianDateToGreenwichDate(julianDate)

	print("Converting {julianDate} back to Greenwich Date gives {month}/{day}/{year}".format(julianDate=julianDate, month=month, day=day, year=year))

	print("The day part of {julianDate} is {dayPart}".format(julianDate=julianDate, dayPart=PD.JulianDateDay(julianDate)))
	print("The month part of {julianDate} is {monthPart}".format(julianDate=julianDate, monthPart=PD.JulianDateMonth(julianDate)))
	print("The year part of {julianDate} is {yearPart}".format(julianDate=julianDate, yearPart=PD.JulianDateYear(julianDate)))

testJulian(6,19.75,2009)
