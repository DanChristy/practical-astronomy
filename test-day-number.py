#!/usr/bin/python3

import lib.pa_datetime as PD

def checkDate(month,day,year):
	dayNumber = PD.CivilDateToDayNumber(month,day,year)

	print("Day number for {month}/{day}/{year} is {daynum}".format(month=month, day=day, year=year, daynum=dayNumber))

checkDate(1,1,2000)
checkDate(3,1,2000)
checkDate(6,1,2003)
checkDate(11,27,2009)