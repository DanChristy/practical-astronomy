#!/usr/bin/python3

import lib.pa_datetime as DOE

easterMonth,easterDay,easterYear = DOE.GetDateOfEaster(2009)

print("{month}/{day}/{year}".format(month=easterMonth, day=easterDay, year=easterYear))
