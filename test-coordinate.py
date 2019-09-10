#!/usr/bin/python3

import lib.pa_coordinate as PC
import lib.pa_models as PM

def testAngleToDecimalDegrees(degrees,minutes,seconds):
	print("\n___AngleToDecimalDegrees___")
	print("INPUT:")
	print(" [Angle] {degrees}d {minutes}m {seconds}s".format(degrees=degrees,minutes=minutes,seconds=seconds))

	myCoordinate = PC.CCoordinate()
	inputAngle = PM.Angle(degrees,minutes,seconds)
	resultDecimalDegrees = myCoordinate.AngleToDecimalDegrees(inputAngle)

	print("OUTPUT:")
	print(" [Decimal Degrees] {decimalDegrees}".format(decimalDegrees=resultDecimalDegrees))

	revertAngle = myCoordinate.DecimalDegreesToAngle(resultDecimalDegrees)

	print("REVERT:")
	print(" [Angle] {degrees}d {minutes}m {seconds}s".format(degrees=revertAngle.degrees,minutes=revertAngle.minutes,seconds=revertAngle.seconds))

testAngleToDecimalDegrees(182,31,27)