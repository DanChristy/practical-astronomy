#!/usr/bin/python3

import ctypes

doelib = ctypes.cdll.LoadLibrary('./doeshared.so')

class Doe(object):
	def __init__(self):
		doelib.CDoe_new.restype = ctypes.c_void_p

		doelib.CDoe_GetEaster.argtypes = [ctypes.c_void_p, ctypes.c_float]
		doelib.CDoe_GetEaster.restype = ctypes.c_char_p
		
		self.obj = doelib.CDoe_new()

	def getEaster(self, year):
		return doelib.CDoe_GetEaster(self.obj, year)

doe = Doe()
dateOfEaster = doe.getEaster(2019)
print ("Easter date is {easterDate}".format(easterDate=dateOfEaster.decode('utf-8')))