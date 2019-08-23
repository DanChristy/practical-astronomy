#!/usr/bin/python3

import ctypes

doelib = ctypes.cdll.LoadLibrary('./doeshared.so')

class Doe(object):
	def __init__(self, year):
		doelib.CDoe_new.argtypes = [ctypes.c_float]
		doelib.CDoe_new.restype = ctypes.c_void_p

		doelib.CDoe_GetEaster.argtypes = [ctypes.c_void_p]
		doelib.CDoe_GetEaster.restype = ctypes.c_char_p
		
		self.obj = doelib.CDoe_new(year)

	def getEaster(self):
		return doelib.CDoe_GetEaster(self.obj)

doe = Doe(2019)
dateOfEaster = doe.getEaster()
print ("Easter date is {easterDate}".format(easterDate=dateOfEaster.decode('utf-8')))