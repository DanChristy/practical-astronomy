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

def testLocalCivilTimeToUniversalTime(hours, minutes, seconds, isDaylightSavings, zoneCorrection, day, month, year):
	print("INPUT:")
	print(" [Local Civil Time] {hours}:{minutes}:{seconds}".format(hours=hours,minutes=minutes,seconds=seconds))
	print(" Daylight Savings = {isDS}".format(isDS=isDaylightSavings))
	print(" Zone Correction = {zoneCorrection}".format(zoneCorrection=zoneCorrection))
	print(" [Local Date] {month}/{day}/{year}".format(month=month,day=day,year=year))

	myConvert = PC.CConvert()
	localCivilTime = PM.CivilTime(hours, minutes, seconds)
	localDate = PM.CivilDate(month, day, year)

	resultUT = myConvert.LocalCivilTimeToUniversalTime(localCivilTime, isDaylightSavings, zoneCorrection, localDate)

	print("OUTPUT:")
	print(" [UTC] {hours}:{minutes}:{seconds}".format(hours=resultUT.utHours,minutes=resultUT.utMinutes,seconds=resultUT.utSeconds))
	print(" [Greenwich Date] {month}/{day}/{year}".format(month=resultUT.gwMonth,day=resultUT.gwDay,year=resultUT.gwYear))


testCivilTimeToDecimalHours(18,31,27)
print("------")
testLocalCivilTimeToUniversalTime(3,37,0,True,4,1,7,2013)