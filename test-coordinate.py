#!/usr/bin/python3

import lib.pa_coordinate as PC

def testAngleToDecimalDegrees(degrees,minutes,seconds):
	print("\n___AngleToDecimalDegrees___")
	print("INPUT:")
	print(" [Angle] {degrees}d {minutes}m {seconds}s".format(degrees=degrees,minutes=minutes,seconds=seconds))

	resultDecimalDegrees = PC.AngleToDecimalDegrees(degrees,minutes,seconds)

	print("OUTPUT:")
	print(" [Decimal Degrees] {decimalDegrees}".format(decimalDegrees=resultDecimalDegrees))

	revertDegrees,revertMinutes,revertSeconds = PC.DecimalDegreesToAngle(resultDecimalDegrees)

	print("REVERT:")
	print(" [Angle] {degrees}d {minutes}m {seconds}s".format(degrees=revertDegrees,minutes=revertMinutes,seconds=revertSeconds))

testAngleToDecimalDegrees(182,31,27)