import math

## @brief Convert an Angle (degrees, minutes, and seconds) to Decimal Degrees
def AngleToDecimalDegrees(degrees, minutes, seconds):
	A = abs(seconds)/60
	B = (abs(minutes)+A)/60
	C = abs(degrees)+B
	D = -(C) if degrees < 0 or minutes < 0 or seconds < 0 else C

	return D

## @brief Convert Decimal Degrees to an Angle (degrees, minutes, and seconds)
## @returns degrees, minutes, seconds
def DecimalDegreesToAngle(decimalDegrees):
	unsignedDecimal = abs(decimalDegrees)
	totalSeconds = unsignedDecimal * 3600
	seconds2dp = round(totalSeconds % 60, 2)
	correctedSeconds = 0 if seconds2dp == 60 else seconds2dp
	correctedRemainder = totalSeconds + 60 if seconds2dp == 60 else totalSeconds
	minutes = math.floor(correctedRemainder/60) % 60
	unsignedDegrees = math.floor(correctedRemainder / 3600)
	signedDegrees = -1 * unsignedDegrees if decimalDegrees < 0 else unsignedDegrees

	return signedDegrees,minutes,math.floor(correctedSeconds)
