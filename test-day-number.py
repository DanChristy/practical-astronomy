#!/usr/bin/python3

import lib.pa_datetime as PD
import lib.pa_models as PM

def checkDate(month,day,year):
	myDateTime = PD.CDateTime()

	dateToCheck = PM.CivilDate(month,day,year)

	dayNumber = myDateTime.CivilDateToDayNumber(dateToCheck)

	print("Day number for {month}/{day}/{year} is {daynum}".format(month=dateToCheck.month, day=dateToCheck.day, year=dateToCheck.year, daynum=dayNumber))

checkDate(1,1,2000)
checkDate(3,1,2000)
checkDate(6,1,2003)
checkDate(11,27,2009)