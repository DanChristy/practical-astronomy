#!/usr/bin/python3

import lib.pa_datetime as PD
import unittest as UT

def get_julian_date(month,day,year):
	return PD.greenwich_date_to_julian_date(day,month,year)

class test_julian(UT.TestCase):
	def setUp(self):
		self.inputMonth = 6
		self.inputDay = 19.75
		self.inputYear = 2009

	def test_greenwich_to_julian(self):
		julianDate = get_julian_date(self.inputMonth,self.inputDay,self.inputYear)
		print("Julian Date for {month}/{day}/{year} is {julianDate}".format(month=self.inputMonth, day=self.inputDay, year=self.inputYear, julianDate=julianDate))
		
		self.assertEqual(julianDate,2455002.25,"Conversion to Julian Date")

	def test_day_of_week(self):
		julianDate = get_julian_date(self.inputMonth,self.inputDay,self.inputYear)
		dayOfWeek = PD.julian_date_to_weekday_name(julianDate)
		print("The day of the week for Julian Date {julianDate} is {dayOfWeek}".format(julianDate=julianDate, dayOfWeek=dayOfWeek))
		
		self.assertEqual(dayOfWeek,"Friday","Get Day of Week")

	def test_julian_to_greenwich(self):
		julianDate = get_julian_date(self.inputMonth,self.inputDay,self.inputYear)
		day,month,year = PD.julian_date_to_greenwich_date(julianDate)	
		print("Converting {julianDate} back to Greenwich Date gives {month}/{day}/{year}".format(julianDate=julianDate, month=month, day=day, year=year))
		
		self.assertEqual(month,6,"Month")
		self.assertEqual(day,19.75,"Day")
		self.assertEqual(year,2009,"Year")

	def test_day_part(self):
		julianDate = get_julian_date(self.inputMonth,self.inputDay,self.inputYear)
		dayPart=PD.julian_date_day(julianDate)
		print("The day part of {julianDate} is {dayPart}".format(julianDate=julianDate, dayPart=dayPart))	
		
		self.assertEqual(dayPart,19.75,"Day part")

	def test_month_part(self):
		julianDate = get_julian_date(self.inputMonth,self.inputDay,self.inputYear)
		monthPart=PD.julian_date_month(julianDate)
		print("The month part of {julianDate} is {monthPart}".format(julianDate=julianDate, monthPart=monthPart))	
		
		self.assertEqual(monthPart,6,"Month part")

	def test_year_part(self):
		julianDate = get_julian_date(self.inputMonth,self.inputDay,self.inputYear)
		yearPart=PD.julian_date_year(julianDate)
		print("The year part of {julianDate} is {yearPart}".format(julianDate=julianDate, yearPart=yearPart))	
		
		self.assertEqual(yearPart,2009,"Year part")


if __name__ == '__main__':
	UT.main()
