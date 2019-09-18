#!/usr/bin/python3

import lib.pa_datetime as PD
import unittest as UT

def get_civil_time(hours,minutes,seconds):
	decimalHours = PD.civil_time_to_decimal_hours(hours,minutes,seconds)

	return round(decimalHours,8)

class test_civil_time(UT.TestCase):
	def setUp(self):
		self.hours = 18
		self.minutes = 31
		self.seconds = 27
		self.decimalHours = get_civil_time(self.hours,self.minutes,self.seconds)

	def test_civil_time_to_decimal_hours(self):
		print("Decimal hours for {hours}:{minutes}:{seconds} is {decimalHours}".format(hours=self.hours, minutes=self.minutes, seconds=self.seconds, decimalHours=self.decimalHours))

		self.assertEqual(self.decimalHours,18.52416667,"Decimal Hours")

	def test_decimal_hours_to_civil_time(self):
		revertHours,revertMinutes,revertSeconds = PD.decimal_hours_to_civil_time(self.decimalHours)
		print("Converting {decimalHours} back to Civil Time gives {hours}:{minutes}:{seconds}".format(decimalHours=self.decimalHours, hours=revertHours, minutes=revertMinutes, seconds=revertSeconds))

		self.assertEqual(revertHours,18,"Civil Time: Hours")
		self.assertEqual(revertMinutes,31,"Civil Time: Minutes")
		self.assertEqual(revertSeconds,27,"Civil Time: Seconds")

	def test_decimal_time_parts(self):
		hourPart = PD.decimal_hour_hour(self.decimalHours)
		minutesPart = PD.decimal_hour_minutes(self.decimalHours)
		secondsPart = PD.decimal_hour_seconds(self.decimalHours)

		print("The hour part of {dH} is {hourPart}".format(dH=self.decimalHours, hourPart=hourPart))
		print("The minutes part of {dH} is {minutesPart}".format(dH=self.decimalHours, minutesPart=minutesPart))
		print("The seconds part of {dH} is {secondsPart}".format(dH=self.decimalHours, secondsPart=secondsPart))

		self.assertEqual(hourPart,18,"Hour Part")
		self.assertEqual(minutesPart,31,"Minutes Part")
		self.assertEqual(secondsPart,27,"Seconds Part")

class test_local_civil_time(UT.TestCase):
	def setUp(self):
		self.hours = 3
		self.minutes = 37
		self.seconds = 0
		self.isDaylightSavings = True
		self.zoneCorrection = 4
		self.day = 1
		self.month = 7
		self.year = 2013

	def test_local_civil_time_to_universal_time(self):
		utHours,utMinutes,utSeconds,gwDay,gwMonth,gwYear = PD.local_civil_time_to_universal_time(self.hours,self.minutes,self.seconds,self.isDaylightSavings,self.zoneCorrection,self.day,self.month,self.year)

		print("[LCT]{hours}:{minutes}:{seconds} [DS]{isDS} [ZC]{zoneCorrection} [LD]{localMonth}/{localDay}/{localYear} = [UT]{utHours}:{utMinutes}:{utSeconds} [GWD]{gwMonth}/{gwDay}/{gwYear}".format(hours=self.hours,minutes=self.minutes,seconds=self.seconds,isDS=self.isDaylightSavings,zoneCorrection=self.zoneCorrection,localMonth=self.month,localDay=self.day,localYear=self.year,utHours=utHours,utMinutes=utMinutes,utSeconds=utSeconds,gwMonth=gwMonth,gwDay=gwDay,gwYear=gwYear))

		self.assertEqual(utHours,22,"UT Hours")
		self.assertEqual(utMinutes,37,"UT Minutes")
		self.assertEqual(utSeconds,0,"UT Seconds")
		self.assertEqual(gwDay,30,"Greenwich Day")
		self.assertEqual(gwMonth,6,"Greenwich Month")
		self.assertEqual(gwYear,2013,"Greenwich Year")

	def test_universal_time_to_local_civil_time(self):
		utHours,utMinutes,utSeconds,gwDay,gwMonth,gwYear = PD.local_civil_time_to_universal_time(self.hours,self.minutes,self.seconds,self.isDaylightSavings,self.zoneCorrection,self.day,self.month,self.year)

		revertLCTHours,revertLCTMinutes,revertLCTSeconds,revertDay,revertMonth,revertYear = PD.universal_time_to_local_civil_time(utHours,utMinutes,utSeconds,self.isDaylightSavings,self.zoneCorrection,gwDay,gwMonth,gwYear)

		print("[UT]{utHours}:{utMinutes}:{utSeconds} [DS]{isDS} [ZC]{zoneCorrection} [GWD]{gwMonth}/{gwDay}/{gwYear} = [LCT]{hours}:{minutes}:{seconds} [LD]{localMonth}/{localDay}/{localYear}".format(utHours=utHours,utMinutes=utMinutes,utSeconds=utSeconds,gwMonth=gwMonth,gwDay=gwDay,gwYear=gwYear,hours=revertLCTHours,minutes=revertLCTMinutes,seconds=revertLCTSeconds,isDS=self.isDaylightSavings,zoneCorrection=self.zoneCorrection,localMonth=self.month,localDay=self.day,localYear=self.year))

		self.assertEqual(revertLCTHours,3,"LCT Hours")
		self.assertEqual(revertLCTMinutes,37, "LCT Minutes")
		self.assertEqual(revertLCTSeconds,0, "LCT Seconds")
		self.assertEqual(revertDay,1,"Local Day")
		self.assertEqual(revertMonth,7,"Local Month")
		self.assertEqual(revertYear,2013,"Local Year")

class test_sidereal_time_universal_time(UT.TestCase):
	def setUp(self):
		self.utHours = 14
		self.utMinutes = 36
		self.utSeconds = 51.67
		self.greenwichDay = 22
		self.greenwichMonth = 4
		self.greenwichYear = 1980

	def test_universal_time_to_greenwich_sidereal_time(self):
		gstHours,gstMinutes,gstSeconds = PD.universal_time_to_greenwich_sidereal_time(self.utHours,self.utMinutes,self.utSeconds,self.greenwichDay,self.greenwichMonth,self.greenwichYear)
		
		print("[UT] {utHours}:{utMinutes}:{utSeconds} {gwMonth}/{gwDay}/{gwYear} = [GST] {gstHours}:{gstMinutes}:{gstSeconds}".format(utHours=self.utHours,utMinutes=self.utMinutes,utSeconds=self.utSeconds,gwMonth=self.greenwichMonth,gwDay=self.greenwichDay,gwYear=self.greenwichYear,gstHours=gstHours,gstMinutes=gstMinutes,gstSeconds=gstSeconds))

		self.assertEqual(gstHours,4,"GST Hours")
		self.assertEqual(gstMinutes,40,"GST Minutes")
		self.assertEqual(gstSeconds,5.23,"GST Seconds")

	def test_greenwich_sidereal_time_to_universal_time(self):
		gstHours,gstMinutes,gstSeconds = PD.universal_time_to_greenwich_sidereal_time(self.utHours,self.utMinutes,self.utSeconds,self.greenwichDay,self.greenwichMonth,self.greenwichYear)
		
		revertUTHours,revertUTMinutes,revertUTSeconds,statusMessage = PD.greenwich_sidereal_time_to_universal_time(gstHours,gstMinutes,gstSeconds,self.greenwichDay,self.greenwichMonth,self.greenwichYear)

		print("[GST] {gstHours}:{gstMinutes}:{gstSeconds} {gwMonth}/{gwDay}/{gwYear} = [UT] {utHours}:{utMinutes}:{utSeconds} [Status] {statusMsg}".format(gstHours=gstHours,gstMinutes=gstMinutes,gstSeconds=gstSeconds,gwMonth=self.greenwichMonth,gwDay=self.greenwichDay,gwYear=self.greenwichYear,utHours=revertUTHours,utMinutes=revertUTMinutes,utSeconds=revertUTSeconds,statusMsg=statusMessage))

		self.assertEqual(revertUTHours,14,"UT Hours")
		self.assertEqual(revertUTMinutes,36,"UT Minutes")
		self.assertEqual(revertUTSeconds,51.67,"UT Seconds")
		self.assertIn(statusMessage,["OK","Warning"],"Status Message")

class test_sidereal_time_local_time(UT.TestCase):
	def setUp(self):
		self.gstHours = 4
		self.gstMinutes = 40
		self.gstSeconds = 5.23
		self.geographicalLongitude = -64

	def test_greenwich_sidereal_time_to_local_sidereal_time(self):
		lstHours,lstMinutes,lstSeconds = PD.greenwich_sidereal_time_to_local_sidereal_time(self.gstHours,self.gstMinutes,self.gstSeconds,self.geographicalLongitude)

		print("[GST] {gstHours}:{gstMinutes}:{gstSeconds} [LON] {geogLon} = [LST] {lstHours}:{lstMinutes}:{lstSeconds}".format(gstHours=self.gstHours,gstMinutes=self.gstMinutes,gstSeconds=self.gstSeconds,geogLon=self.geographicalLongitude,lstHours=lstHours,lstMinutes=lstMinutes,lstSeconds=lstSeconds))

		self.assertEqual(lstHours,0,"LST Hours")
		self.assertEqual(lstMinutes,24,"LST Minutes")
		self.assertEqual(lstSeconds,5.23,"LST Seconds")

	def test_local_sidereal_time_to_greenwich_sidereal_time(self):
		lstHours,lstMinutes,lstSeconds = PD.greenwich_sidereal_time_to_local_sidereal_time(self.gstHours,self.gstMinutes,self.gstSeconds,self.geographicalLongitude)

		revertGSTHours,revertGSTMinutes,revertGSTSeconds = PD.local_sidereal_time_to_greenwich_sidereal_time(lstHours,lstMinutes,lstSeconds,self.geographicalLongitude)

		print("[LST] {lstHours}:{lstMinutes}:{lstSeconds} [LON] {geogLon} = [GST] {gstHours}:{gstMinutes}:{gstSeconds}".format(lstHours=lstHours,lstMinutes=lstMinutes,lstSeconds=lstSeconds,geogLon=self.geographicalLongitude,gstHours=revertGSTHours,gstMinutes=revertGSTMinutes,gstSeconds=revertGSTSeconds))

		self.assertEqual(revertGSTHours,4,"GST Hours")
		self.assertEqual(revertGSTMinutes,40,"GST Minutes")
		self.assertEqual(revertGSTSeconds,5.23,"GST Seconds")
	

if __name__ == '__main__':
	UT.main()
