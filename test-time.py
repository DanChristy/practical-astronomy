#!/usr/bin/python3

import lib.pa_conversions as PC
import lib.pa_models as PM

def testCivilTimeToDecimalHours(hours, minutes, seconds):
	myConvert = PC.CConvert()
	timeToCheck = PM.CivilTime(hours, minutes, seconds)

	decimalHours = myConvert.CivilTimeToDecimalHours(timeToCheck)

	print("Decimal hours for {hours}:{minutes}:{seconds} is {decimalHours}".format(hours=timeToCheck.hours, minutes=timeToCheck.minutes, seconds=timeToCheck.seconds, decimalHours=decimalHours))

	civilTime = myConvert.DecimalHoursToCivilTime(decimalHours)

	print("Converting {decimalHours} back to Civil Time gives {hours}:{minutes}:{seconds}".format(decimalHours=decimalHours, hours=civilTime.hours, minutes=civilTime.minutes, seconds=civilTime.seconds))

	print("   The hour part of {dH} is {hourPart}".format(dH=decimalHours, hourPart=myConvert.DecimalHourHour(decimalHours)))
	print("The minutes part of {dH} is {minutesPart}".format(dH=decimalHours, minutesPart=myConvert.DecimalHourMinutes(decimalHours)))
	print("The seconds part of {dH} is {secondsPart}".format(dH=decimalHours, secondsPart=myConvert.DecimalHourSeconds(decimalHours)))

testCivilTimeToDecimalHours(18,31,27)
