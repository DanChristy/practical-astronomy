#!/usr/bin/python3

import lib.pa_datetime as PD

def testCivilTimeToDecimalHours(hours, minutes, seconds):
	print("\n___CivilTimeToDecimalHours___")
	decimalHours = PD.CivilTimeToDecimalHours(hours,minutes,seconds)

	print("Decimal hours for {hours}:{minutes}:{seconds} is {decimalHours}".format(hours=hours, minutes=minutes, seconds=seconds, decimalHours=decimalHours))

	revertHours,revertMinutes,revertSeconds = PD.DecimalHoursToCivilTime(decimalHours)

	print("Converting {decimalHours} back to Civil Time gives {hours}:{minutes}:{seconds}".format(decimalHours=decimalHours, hours=revertHours, minutes=revertMinutes, seconds=revertSeconds))

	print("   The hour part of {dH} is {hourPart}".format(dH=decimalHours, hourPart=PD.DecimalHourHour(decimalHours)))
	print("The minutes part of {dH} is {minutesPart}".format(dH=decimalHours, minutesPart=PD.DecimalHourMinutes(decimalHours)))
	print("The seconds part of {dH} is {secondsPart}".format(dH=decimalHours, secondsPart=PD.DecimalHourSeconds(decimalHours)))

def testLocalCivilTimeToUniversalTime(hours, minutes, seconds, isDaylightSavings, zoneCorrection, day, month, year):
	print("\n___LocalCivilTimeToUniversalTime___")
	print("INPUT:")
	print(" [Local Civil Time] {hours}:{minutes}:{seconds}".format(hours=hours,minutes=minutes,seconds=seconds))
	print(" Daylight Savings = {isDS}".format(isDS=isDaylightSavings))
	print(" Zone Correction = {zoneCorrection}".format(zoneCorrection=zoneCorrection))
	print(" [Local Date] {month}/{day}/{year}".format(month=month,day=day,year=year))

	utHours,utMinutes,utSeconds,gwDay,gwMonth,gwYear = PD.LocalCivilTimeToUniversalTime(hours,minutes,seconds,isDaylightSavings,zoneCorrection,day,month,year)

	print("OUTPUT:")
	print(" [UTC] {hours}:{minutes}:{seconds}".format(hours=utHours,minutes=utMinutes,seconds=utSeconds))
	print(" [Greenwich Date] {month}/{day}/{year}".format(month=gwMonth,day=gwDay,year=gwYear))

	revertLCTHours,revertLCTMinutes,revertLCTSeconds,revertDay,revertMonth,revertYear = PD.UniversalTimeToLocalCivilTime(utHours,utMinutes,utSeconds,isDaylightSavings,zoneCorrection,gwDay,gwMonth,gwYear)

	print("REVERT:")
	print(" [Local Civil Time] {hours}:{minutes}:{seconds}".format(hours=revertLCTHours,minutes=revertLCTMinutes,seconds=revertLCTSeconds))
	print(" [Local Date] {month}/{day}/{year}".format(month=revertMonth,day=revertDay,year=revertYear))

def testUniversalTimeToGreenwichSiderealTime(hours,minutes,seconds,day,month,year):
	print("\n___UniversalTimeToGreenwichSiderealTime___")
	print("INPUT:")
	print(" [UTC] {hours}:{minutes}:{seconds}".format(hours=hours,minutes=minutes,seconds=seconds))
	print(" [Greenwich Date] {month}/{day}/{year}".format(month=month,day=day,year=year))

	gstHours,gstMinutes,gstSeconds = PD.UniversalTimeToGreenwichSiderealTime(hours,minutes,seconds,day,month,year)

	print("OUTPUT:")
	print(" [Sidereal Time] {hours}:{minutes}:{seconds}".format(hours=gstHours,minutes=gstMinutes,seconds=gstSeconds))

	utHours,utMinutes,utSeconds,warningFlag = PD.GreenwichSiderealTimeToUniversalTime(gstHours,gstMinutes,gstSeconds,day,month,year)
	
	print("REVERT:")
	print(" [UTC] {hours}:{minutes}:{seconds}".format(hours=utHours,minutes=utMinutes,seconds=utSeconds))
	print(" [Warning Flag] {warningFlag}".format(warningFlag=warningFlag))

def testGreenwichSiderealTimeToLocalSiderealTime(hours,minutes,seconds,geographicalLongitude):
	print("\n___GreenwichSiderealTimeToLocalSiderealTime___")
	print("INPUT:")
	print(" [GST] {hours}:{minutes}:{seconds}".format(hours=hours,minutes=minutes,seconds=seconds))
	print(" [Geographical Longitude] {geogLong}".format(geogLong=geographicalLongitude))

	lstHours,lstMinutes,lstSeconds = PD.GreenwichSiderealTimeToLocalSiderealTime(hours,minutes,seconds,geographicalLongitude)

	print("OUTPUT:")
	print(" [Local Sidereal Time] {hours}:{minutes}:{seconds}".format(hours=lstHours,minutes=lstMinutes,seconds=lstSeconds))

	gstHours,gstMinutes,gstSeconds = PD.LocalSiderealTimeToGreenwichSiderealTime(lstHours,lstMinutes,lstSeconds,geographicalLongitude)

	print("REVERT:")
	print(" [GST] {hours}:{minutes}:{seconds}".format(hours=gstHours,minutes=gstMinutes,seconds=gstSeconds))


testCivilTimeToDecimalHours(18,31,27)

testLocalCivilTimeToUniversalTime(3,37,0,True,4,1,7,2013)

testUniversalTimeToGreenwichSiderealTime(14,36,51.67,22,4,1980)

testGreenwichSiderealTimeToLocalSiderealTime(4,40,5.23,-64)