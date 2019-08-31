#!/usr/bin/python3

import ctypes

convertlib = ctypes.cdll.LoadLibrary('./convertshared.so')

class GeneralTime(ctypes.Structure):
	_fields_ = [("hours", ctypes.c_int), ("minutes", ctypes.c_int), ("seconds", ctypes.c_int)]

class Convert(object):
	def __init__(self):
		convertlib.CConvert_new.restype = ctypes.c_void_p

		convertlib.CConvert_General12HourTimeToDecimal.argtypes = [ctypes.c_void_p, GeneralTime, ctypes.c_char_p]
		convertlib.CConvert_General12HourTimeToDecimal.restype = ctypes.c_float

		convertlib.CConvert_General24HourTimeToDecimal.argtypes = [ctypes.c_void_p, GeneralTime]
		convertlib.CConvert_General24HourTimeToDecimal.restype = ctypes.c_float

		self.obj = convertlib.CConvert_new()

	def convertGeneral12HourTimeToDecimal(self, generalTime, period):
		periodArgInput = bytes(period,'utf-8')
		periodArg = ctypes.create_string_buffer(periodArgInput)

		return convertlib.CConvert_General12HourTimeToDecimal(self.obj, generalTime, periodArg)

	def convertGeneral24HourTimeToDecimal(self, generalTime):
		return convertlib.CConvert_General24HourTimeToDecimal(self.obj, generalTime)


convert = Convert()

generalTime = GeneralTime()
generalTime.hours = 18
generalTime.minutes = 31
generalTime.seconds = 27

print ("Decimal time for 18:31:27 is {decimalTime}".format(decimalTime=convert.convertGeneral24HourTimeToDecimal(generalTime)))

generalTime.hours = generalTime.hours - 12
print ("Decimal time for 6:31:27 PM is {decimalTime}".format(decimalTime=convert.convertGeneral12HourTimeToDecimal(generalTime,"PM")))
