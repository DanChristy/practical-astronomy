#!/usr/bin/python3

import lib.pa_date_of_easter as DOE

myDateOfEaster = DOE.CDateOfEaster()

easterDate = myDateOfEaster.GetDateOfEaster(2009)

print("{month}/{day}/{year}".format(month=easterDate.month, day=easterDate.day, year=easterDate.year))
