#!/usr/bin/python3

import lib.pa_coordinate as PC
import unittest as UT

def getDecimalDegrees(degrees,minutes,seconds):
	resultDecimalDegrees = round(PC.AngleToDecimalDegrees(degrees,minutes,seconds),7)

	return resultDecimalDegrees

class TestAngleDecimalDegrees(UT.TestCase):
	def setUp(self):
		self.degrees = 182
		self.minutes = 31
		self.seconds = 27

	def test_angle_to_decimal_degrees(self):
		resultDecimalDegrees = getDecimalDegrees(self.degrees,self.minutes,self.seconds)

		print("[Angle] {degrees}d {minutes}m {seconds}s = [Decimal Degrees] {decimalDegrees}".format(degrees=self.degrees,minutes=self.minutes,seconds=self.seconds,decimalDegrees=resultDecimalDegrees))

		self.assertEqual(resultDecimalDegrees,182.5241667,"Decimal Degrees")

	def test_decimal_degrees_to_angle(self):
		resultDecimalDegrees = getDecimalDegrees(self.degrees,self.minutes,self.seconds)

		revertDegrees,revertMinutes,revertSeconds = PC.DecimalDegreesToAngle(resultDecimalDegrees)

		print("[Decimal Degrees] {decimalDegrees} = [Angle] {degrees}d {minutes}m {seconds}s".format(decimalDegrees=resultDecimalDegrees,degrees=revertDegrees,minutes=revertMinutes,seconds=revertSeconds))

		self.assertEqual(revertDegrees,182,"Angle Degrees")
		self.assertEqual(revertMinutes,31,"Angle Minutes")
		self.assertEqual(revertSeconds,27,"Angle Seconds")


if __name__ == '__main__':
	UT.main()
