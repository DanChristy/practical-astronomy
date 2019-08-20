#!/usr/bin/python3

import ctypes

julianlib = ctypes.cdll.LoadLibrary('./julianshared.so')

class Julian(object):
	def __init__(self, month, day, year):
		julianlib.CJulian_new.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_int]
		julianlib.CJulian_new.restype = ctypes.c_void_p

		julianlib.CJulian_GetJulian.argtypes = [ctypes.c_void_p]
		julianlib.CJulian_GetJulian.restype = ctypes.c_float

		self.obj = julianlib.CJulian_new(month, day, year)

	def getJulian(self):
		return julianlib.CJulian_GetJulian(self.obj)

julian = Julian(6, 19.75, 2009)
julianDate = julian.getJulian()

print ("Julian date is {julianDate}".format(julianDate=julianDate))