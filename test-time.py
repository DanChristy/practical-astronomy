#!/usr/bin/python3

import lib.pa_datetime as PD
import lib.pa_models as PM

def testCivilTimeToDecimalHours(hours, minutes, seconds):
	print("\n___CivilTimeToDecimalHours___")
	myDateTime = PD.CDateTime()
	timeToCheck = PM.CivilTime(hours, minutes, seconds)

	decimalHours = myDateTime.CivilTimeToDecimalHours(timeToCheck)

	print("Decimal hours for {hours}:{minutes}:{seconds} is {decimalHours}".format(hours=timeToCheck.hours, minutes=timeToCheck.minutes, seconds=timeToCheck.seconds, decimalHours=decimalHours))

	civilTime = myDateTime.DecimalHoursToCivilTime(decimalHours)

	print("Converting {decimalHours} back to Civil Time gives {hours}:{minutes}:{seconds}".format(decimalHours=decimalHours, hours=civilTime.hours, minutes=civilTime.minutes, seconds=civilTime.seconds))

	print("   The hour part of {dH} is {hourPart}".format(dH=decimalHours, hourPart=myDateTime.DecimalHourHour(decimalHours)))
	print("The minutes part of {dH} is {minutesPart}".format(dH=decimalHours, minutesPart=myDateTime.DecimalHourMinutes(decimalHours)))
	print("The seconds part of {dH} is {secondsPart}".format(dH=decimalHours, secondsPart=myDateTime.DecimalHourSeconds(decimalHours)))

def testLocalCivilTimeToUniversalTime(hours, minutes, seconds, isDaylightSavings, zoneCorrection, day, month, year):
	print("\n___LocalCivilTimeToUniversalTime___")
	print("INPUT:")
	print(" [Local Civil Time] {hours}:{minutes}:{seconds}".format(hours=hours,minutes=minutes,seconds=seconds))
	print(" Daylight Savings = {isDS}".format(isDS=isDaylightSavings))
	print(" Zone Correction = {zoneCorrection}".format(zoneCorrection=zoneCorrection))
	print(" [Local Date] {month}/{day}/{year}".format(month=month,day=day,year=year))

	myDateTime = PD.CDateTime()
	localCivilTime = PM.CivilTime(hours, minutes, seconds)
	localDate = PM.CivilDate(month, day, year)

	resultUT = myDateTime.LocalCivilTimeToUniversalTime(localCivilTime, isDaylightSavings, zoneCorrection, localDate)

	print("OUTPUT:")
	print(" [UTC] {hours}:{minutes}:{seconds}".format(hours=resultUT.utHours,minutes=resultUT.utMinutes,seconds=resultUT.utSeconds))
	print(" [Greenwich Date] {month}/{day}/{year}".format(month=resultUT.gwMonth,day=resultUT.gwDay,year=resultUT.gwYear))

	universalTime = PM.CivilTime(resultUT.utHours,resultUT.utMinutes,resultUT.utSeconds)
	greenwichDate = PM.CivilDate(resultUT.gwMonth,resultUT.gwDay,resultUT.gwYear)
	revertLocalCivilTimeOutput = myDateTime.UniversalTimeToLocalCivilTime(universalTime,isDaylightSavings,zoneCorrection,greenwichDate)

	print("REVERT:")
	print(" [Local Civil Time] {hours}:{minutes}:{seconds}".format(hours=revertLocalCivilTimeOutput.utHours,minutes=revertLocalCivilTimeOutput.utMinutes,seconds=revertLocalCivilTimeOutput.utSeconds))
	print(" [Local Date] {month}/{day}/{year}".format(month=revertLocalCivilTimeOutput.gwMonth,day=revertLocalCivilTimeOutput.gwDay,year=revertLocalCivilTimeOutput.gwYear))

def testUniversalTimeToGreenwichSiderealTime(hours,minutes,seconds,day,month,year):
	print("\n___UniversalTimeToGreenwichSiderealTime___")
	print("INPUT:")
	print(" [UTC] {hours}:{minutes}:{seconds}".format(hours=hours,minutes=minutes,seconds=seconds))
	print(" [Greenwich Date] {month}/{day}/{year}".format(month=month,day=day,year=year))

	myDateTime = PD.CDateTime()
	universalTime = PM.CivilTime(hours, minutes, seconds)
	greenwichDate = PM.CivilDate(month, day, year)

	resultSiderealTime = myDateTime.UniversalTimeToGreenwichSiderealTime(universalTime, greenwichDate)

	print("OUTPUT:")
	print(" [Sidereal Time] {hours}:{minutes}:{seconds}".format(hours=resultSiderealTime.hours,minutes=resultSiderealTime.minutes,seconds=resultSiderealTime.seconds))

	revertUniversalTime = myDateTime.GreenwichSiderealTimeToUniversalTime(resultSiderealTime, greenwichDate)
	
	print("REVERT:")
	print(" [UTC] {hours}:{minutes}:{seconds}".format(hours=revertUniversalTime.hours,minutes=revertUniversalTime.minutes,seconds=revertUniversalTime.seconds))

def testGreenwichSiderealTimeToLocalSiderealTime(hours,minutes,seconds,geographicalLongitude):
	print("\n___GreenwichSiderealTimeToLocalSiderealTime___")
	print("INPUT:")
	print(" [GST] {hours}:{minutes}:{seconds}".format(hours=hours,minutes=minutes,seconds=seconds))
	print(" [Geographical Longitude] {geogLong}".format(geogLong=geographicalLongitude))

	myDateTime = PD.CDateTime()
	greenwichSiderealTime = PM.CivilTime(hours, minutes, seconds)

	resultLocalSiderealTime = myDateTime.GreenwichSiderealTimeToLocalSiderealTime(greenwichSiderealTime, geographicalLongitude)

	print("OUTPUT:")
	print(" [Local Sidereal Time] {hours}:{minutes}:{seconds}".format(hours=resultLocalSiderealTime.hours,minutes=resultLocalSiderealTime.minutes,seconds=resultLocalSiderealTime.seconds))

	revertGST = myDateTime.LocalSiderealTimeToGreenwichSiderealTime(resultLocalSiderealTime,geographicalLongitude)

	print("REVERT:")
	print(" [GST] {hours}:{minutes}:{seconds}".format(hours=revertGST.hours,minutes=revertGST.minutes,seconds=revertGST.seconds))


testCivilTimeToDecimalHours(18,31,27)

testLocalCivilTimeToUniversalTime(3,37,0,True,4,1,7,2013)

testUniversalTimeToGreenwichSiderealTime(14,36,51.67,22,4,1980)

testGreenwichSiderealTimeToLocalSiderealTime(4,40,5.23,-64)