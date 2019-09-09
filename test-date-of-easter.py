#!/usr/bin/python3

import lib.pa_datetime as DOE

myDateOfEaster = DOE.CDateTime()

easterDate = myDateOfEaster.GetDateOfEaster(2009)

print("{month}/{day}/{year}".format(month=easterDate.month, day=easterDate.day, year=easterDate.year))
