#!/usr/bin/python3

import unittest as UT
import lib.pa_datetime as PD

def test_gen(month,day,year):
	dayNumber = PD.CivilDateToDayNumber(month,day,year)
	print("Test input: {month}/{day}/{year}, test output: {dayNum}".format(month=month,day=day,year=year,dayNum=dayNumber))
	return dayNumber

class TestDayNumbers(UT.TestCase):
	def test_1_1_2000(self):
		self.assertEqual(test_gen(1,1,2000),1)

	def test_3_1_2000(self):
		self.assertEqual(test_gen(3,1,2000),61)
	
	def test_6_1_2003(self):
		self.assertEqual(test_gen(6,1,2003),152)

	def test_11_27_2009(self):
		self.assertEqual(test_gen(11,27,2009),331)


if __name__ == '__main__':
	UT.main()
