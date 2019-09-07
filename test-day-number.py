#!/usr/bin/python3

import lib.pa_conversions as PC
import lib.pa_shared as PS

def checkDate(month,day,year):
	myConvert = PC.CConvert()

	dateToCheck = PS.CivilDate(month,day,year)

	dayNumber = myConvert.CivilDateToDayNumber(dateToCheck)

	print("Day number for {month}/{day}/{year} is {daynum}".format(month=dateToCheck.month, day=dateToCheck.day, year=dateToCheck.year, daynum=dayNumber))

checkDate(1,1,2000)
checkDate(3,1,2000)
checkDate(6,1,2003)
checkDate(11,27,2009)