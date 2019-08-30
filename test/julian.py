#!/usr/bin/python3

import ctypes

julianlib = ctypes.cdll.LoadLibrary('./julianshared.so')

class GreenwichDate(ctypes.Structure):
	_fields_ = [("month", ctypes.c_int), ("day", ctypes.c_float), ("year", ctypes.c_int)]

class Julian(object):
	def __init__(self):
		julianlib.CJulian_new.restype = ctypes.c_void_p

		julianlib.CJulian_GreenwichToJulian.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_int]
		julianlib.CJulian_GreenwichToJulian.restype = ctypes.c_float

		julianlib.CJulian_JulianToGreenwich.argtypes = [ctypes.c_void_p, ctypes.c_float]
		julianlib.CJulian_JulianToGreenwich.restype = GreenwichDate

		julianlib.CJulian_GetDayOfWeek.argtypes = [ctypes.c_void_p, ctypes.c_float]
		julianlib.CJulian_GetDayOfWeek.restype = ctypes.c_char_p
		
		self.obj = julianlib.CJulian_new()

	def GreenwichToJulian(self, month, day, year):
		return julianlib.CJulian_GreenwichToJulian(self.obj, month, day, year)

	def JulianToGreenwich(self, julianDate):
		return julianlib.CJulian_JulianToGreenwich(self.obj, julianDate)

	def GetDayOfWeek(self, julianDate):
		return julianlib.CJulian_GetDayOfWeek(self.obj, julianDate)

julian = Julian()
julianDate = julian.GreenwichToJulian(6, 19.75, 2009)
greenwichDate = julian.JulianToGreenwich(julianDate)

print("Julian date for 6/19.75/2009 is {julianDate}".format(julianDate=julianDate))

print("Day of the week for 6/19.75/2009 is {dayName}".format(dayName=julian.GetDayOfWeek(julianDate).decode('utf-8')))

print("Converting back to Greenwich Date gives {gwMonth}/{gwDay}/{gwYear}".format(gwMonth=greenwichDate.month, gwDay=greenwichDate.day, gwYear=greenwichDate.year))
