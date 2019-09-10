import math
from . import pa_models

## This class provides functions for working with coordinate systems.
class CCoordinate(object):
	def __init__(self):
		pass

	## \brief Convert an Angle (degrees, minutes, and seconds) to Decimal Degrees
	def AngleToDecimalDegrees(self, angle):
		A = abs(angle.seconds)/60
		B = (abs(angle.minutes)+A)/60
		C = abs(angle.degrees)+B
		D = -(C) if angle.degrees < 0 or angle.minutes < 0 or angle.seconds < 0 else C

		return D
	
	## \brief Convert Decimal Degrees to an Angle (degrees, minutes, and seconds)
	def DecimalDegreesToAngle(self, decimalDegrees):
		unsignedDecimal = abs(decimalDegrees)
		totalSeconds = unsignedDecimal * 3600
		seconds2dp = round(totalSeconds % 60, 2)
		correctedSeconds = 0 if seconds2dp == 60 else seconds2dp
		correctedRemainder = totalSeconds + 60 if seconds2dp == 60 else totalSeconds
		minutes = math.floor(correctedRemainder/60) % 60
		unsignedDegrees = math.floor(correctedRemainder / 3600)
		signedDegrees = -1 * unsignedDegrees if decimalDegrees < 0 else unsignedDegrees

		return pa_models.Angle(signedDegrees,minutes,math.floor(correctedSeconds))
