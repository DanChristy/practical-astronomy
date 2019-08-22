#!/usr/bin/python3

import ctypes

julianlib = ctypes.cdll.LoadLibrary('./julianshared.so')

class Julian(object):
	def __init__(self):
		#julianlib.CJulian_new.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_int]
		julianlib.CJulian_new.restype = ctypes.c_void_p

		julianlib.CJulian_GreenwichToJulian.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_int]
		julianlib.CJulian_GreenwichToJulian.restype = ctypes.c_float

		self.obj = julianlib.CJulian_new()

	def GreenwichToJulian(self, month, day, year):
		return julianlib.CJulian_GreenwichToJulian(self.obj, month, day, year)

julian = Julian()
julianDate = julian.GreenwichToJulian(6, 19.75, 2009)

print ("Julian date for 6/19.75/2009 is {julianDate}".format(julianDate=julianDate))