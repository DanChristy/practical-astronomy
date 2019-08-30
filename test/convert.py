#!/usr/bin/python3

import ctypes

convertlib = ctypes.cdll.LoadLibrary('./convertshared.so')

class Convert(object):
	def __init__(self):
		convertlib.CConvert_new.restype = ctypes.c_void_p

		convertlib.CConvert_General12HourTimeToDecimal.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
		convertlib.CConvert_General12HourTimeToDecimal.restype = ctypes.c_float

		convertlib.CConvert_General24HourTimeToDecimal.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
		convertlib.CConvert_General24HourTimeToDecimal.restype = ctypes.c_float

		self.obj = convertlib.CConvert_new()

	def convertGeneral12HourTimeToDecimal(self, hours, minutes, seconds, period):
		periodArgInput = bytes(period,'utf-8')
		periodArg = ctypes.create_string_buffer(periodArgInput)

		return convertlib.CConvert_General12HourTimeToDecimal(self.obj, hours, minutes, seconds, periodArg)

	def convertGeneral24HourTimeToDecimal(self, hours, minutes, seconds):
		return convertlib.CConvert_General24HourTimeToDecimal(self.obj, hours, minutes, seconds)


convert = Convert()
print ("Decimal time for 18:31:27 is {decimalTime}".format(decimalTime=convert.convertGeneral24HourTimeToDecimal(18,31,27)))
print ("Decimal time for 6:31:27 PM is {decimalTime}".format(decimalTime=convert.convertGeneral12HourTimeToDecimal(6,31,27,"PM")))
