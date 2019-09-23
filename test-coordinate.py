#!/usr/bin/python3

import lib.pa_coordinate as PC
import unittest as UT

def get_decimal_degrees(degrees,minutes,seconds):
	resultDecimalDegrees = round(PC.angle_to_decimal_degrees(degrees,minutes,seconds),7)

	return resultDecimalDegrees

class test_angle_decimal_degrees(UT.TestCase):
	def setUp(self):
		self.degrees = 182
		self.minutes = 31
		self.seconds = 27

	def test_angle_to_decimal_degrees(self):
		resultDecimalDegrees = get_decimal_degrees(self.degrees,self.minutes,self.seconds)

		print("[Angle] {degrees}d {minutes}m {seconds}s = [Decimal Degrees] {decimalDegrees}".format(degrees=self.degrees,minutes=self.minutes,seconds=self.seconds,decimalDegrees=resultDecimalDegrees))

		self.assertEqual(resultDecimalDegrees,182.5241667,"Decimal Degrees")

	def test_decimal_degrees_to_angle(self):
		resultDecimalDegrees = get_decimal_degrees(self.degrees,self.minutes,self.seconds)

		revertDegrees,revertMinutes,revertSeconds = PC.decimal_degrees_to_angle(resultDecimalDegrees)

		print("[Decimal Degrees] {decimalDegrees} = [Angle] {degrees}d {minutes}m {seconds}s".format(decimalDegrees=resultDecimalDegrees,degrees=revertDegrees,minutes=revertMinutes,seconds=revertSeconds))

		self.assertEqual(revertDegrees,182,"Angle Degrees")
		self.assertEqual(revertMinutes,31,"Angle Minutes")
		self.assertEqual(revertSeconds,27,"Angle Seconds")

class test_right_ascension_hour_angle(UT.TestCase):
	def setUp(self):
		self.ra_hours = 18
		self.ra_minutes = 32
		self.ra_seconds = 21
		self.lct_hours = 14
		self.lct_minutes = 36
		self.lct_seconds = 51.67
		self.is_daylight_saving = False
		self.zone_correction = -4
		self.local_day = 22
		self.local_month = 4
		self.local_year = 1980
		self.geographical_longitude = -64

	def test_right_ascension_to_hour_angle(self):
		hour_angle_hours,hour_angle_minutes,hour_angle_seconds = PC.right_ascension_to_hour_angle(self.ra_hours,self.ra_minutes,self.ra_seconds,self.lct_hours,self.lct_minutes,self.lct_seconds,self.is_daylight_saving,self.zone_correction,self.local_day,self.local_month,self.local_year,self.geographical_longitude)

		print("[RA] {ra_hours}:{ra_minutes}:{ra_seconds} [LCT] {lct_hours}:{lct_minutes}:{lct_seconds} [DS] {is_daylight_saving} [ZC] {zone_correction} [LD] {local_month}/{local_day}/{local_year} [LON] {geographical_longitude} = [HA] {hour_angle_hours}:{hour_angle_minutes}:{hour_angle_seconds}".format(ra_hours=self.ra_hours,ra_minutes=self.ra_minutes,ra_seconds=self.ra_seconds,lct_hours=self.lct_hours,lct_minutes=self.lct_minutes,lct_seconds=self.lct_seconds,is_daylight_saving=self.is_daylight_saving,zone_correction=self.zone_correction,local_month=self.local_month,local_day=self.local_day,local_year=self.local_year,geographical_longitude=self.geographical_longitude,hour_angle_hours=hour_angle_hours,hour_angle_minutes=hour_angle_minutes,hour_angle_seconds=hour_angle_seconds))

		self.assertEqual(hour_angle_hours,9,"Hour Angle Hours")
		self.assertEqual(hour_angle_minutes,52,"Hour Angle Minutes")
		self.assertEqual(hour_angle_seconds,23.66,"Hour Angle Seconds")

	def test_hour_angle_to_right_ascension(self):
		hour_angle_hours,hour_angle_minutes,hour_angle_seconds = PC.right_ascension_to_hour_angle(self.ra_hours,self.ra_minutes,self.ra_seconds,self.lct_hours,self.lct_minutes,self.lct_seconds,self.is_daylight_saving,self.zone_correction,self.local_day,self.local_month,self.local_year,self.geographical_longitude)

		right_ascension_hours,right_ascension_minutes,right_ascension_seconds = PC.hour_angle_to_right_ascension(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,self.lct_hours,self.lct_minutes,self.lct_seconds,self.is_daylight_saving,self.zone_correction,self.local_day,self.local_month,self.local_year,self.geographical_longitude)

		print("[HA] {hour_angle_hours}:{hour_angle_minutes}:{hour_angle_seconds} [LCT] {lct_hours}:{lct_minutes}:{lct_seconds} [DS] {is_daylight_saving} [ZC] {zone_correction} [LD] {local_month}/{local_day}/{local_year} [LON] {geographical_longitude} = [RA] {ra_hours}:{ra_minutes}:{ra_seconds}".format(hour_angle_hours=hour_angle_hours,hour_angle_minutes=hour_angle_minutes,hour_angle_seconds=hour_angle_seconds,lct_hours=self.lct_hours,lct_minutes=self.lct_minutes,lct_seconds=self.lct_seconds,is_daylight_saving=self.is_daylight_saving,zone_correction=self.zone_correction,local_month=self.local_month,local_day=self.local_day,local_year=self.local_year,geographical_longitude=self.geographical_longitude,ra_hours=right_ascension_hours,ra_minutes=right_ascension_minutes,ra_seconds=right_ascension_seconds))

		self.assertEqual(right_ascension_hours,18,"Right Ascension Hours")
		self.assertEqual(right_ascension_minutes,32,"Right Ascension Minutes")
		self.assertEqual(right_ascension_seconds,21,"Right Ascension Seconds")

class test_equatorial_coordinates_horizon_coordinates(UT.TestCase):
	def setUp(self):
		self.hour_angle_hours = 5
		self.hour_angle_minutes = 51
		self.hour_angle_seconds = 44
		self.declination_degrees = 23
		self.declination_minutes = 13
		self.declination_seconds = 10
		self.geographical_latitude = 52

	def test_equatorial_coordinates_to_horizon_coordinates(self):
		azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds = PC.equatorial_coordinates_to_horizon_coordinates(self.hour_angle_hours,self.hour_angle_minutes,self.hour_angle_seconds,self.declination_degrees,self.declination_minutes,self.declination_seconds,self.geographical_latitude)

		print("[HA] {ha_hours}:{ha_minutes}:{ha_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s [LON] {geog_lat} = [AZ] {azimuth_degrees}d {azimuth_minutes}m {azimuth_seconds}s [ALT] {altitude_degrees}d {altitude_minutes}m {altitude_seconds}s".format(ha_hours=self.hour_angle_hours,ha_minutes=self.hour_angle_minutes,ha_seconds=self.hour_angle_seconds,dec_degrees=self.declination_degrees,dec_minutes=self.declination_minutes,dec_seconds=self.declination_seconds,geog_lat=self.geographical_latitude,azimuth_degrees=azimuth_degrees,azimuth_minutes=azimuth_minutes,azimuth_seconds=azimuth_seconds,altitude_degrees=altitude_degrees,altitude_minutes=altitude_minutes,altitude_seconds=altitude_seconds))

		self.assertEqual(azimuth_degrees,283,"Azimuth Degrees")
		self.assertEqual(azimuth_minutes,16,"Azimuth Minutes")
		self.assertEqual(azimuth_seconds,15.7,"Azimuth Seconds")
		self.assertEqual(altitude_degrees,19,"Altitude Degrees")
		self.assertEqual(altitude_minutes,20,"Altitude Minutes")
		self.assertEqual(altitude_seconds,3.64,"Altitude Seconds")

	def test_horizon_coordinates_to_equatorial_coordinates(self):
		azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds = PC.equatorial_coordinates_to_horizon_coordinates(self.hour_angle_hours,self.hour_angle_minutes,self.hour_angle_seconds,self.declination_degrees,self.declination_minutes,self.declination_seconds,self.geographical_latitude)

		hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds = PC.horizon_coordinates_to_equatorial_coordinates(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,self.geographical_latitude)

		print("[AZ] {azimuth_degrees}d {azimuth_minutes}m {azimuth_seconds}s [ALT] {altitude_degrees}d {altitude_minutes}m {altitude_seconds}s [LON] {geog_lat} = [HA] {ha_hours}:{ha_minutes}:{ha_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s)".format(azimuth_degrees=azimuth_degrees,azimuth_minutes=azimuth_minutes,azimuth_seconds=azimuth_seconds,altitude_degrees=altitude_degrees,altitude_minutes=altitude_minutes,altitude_seconds=altitude_seconds,geog_lat=self.geographical_latitude,ha_hours=hour_angle_hours,ha_minutes=hour_angle_minutes,ha_seconds=hour_angle_seconds,dec_degrees=declination_degrees,dec_minutes=declination_minutes,dec_seconds=declination_seconds))

		self.assertEqual(hour_angle_hours,5,"Hour Angle Hours")
		self.assertEqual(hour_angle_minutes,51,"Hour Angle Minutes")
		self.assertEqual(hour_angle_seconds,44,"Hour Angle Seconds")
		self.assertEqual(declination_degrees,23,"Declination Degrees")
		self.assertEqual(declination_minutes,13,"Declination Minutes")
		self.assertEqual(declination_seconds,10,"Declination Seconds")

class test_ecliptic(UT.TestCase):
	def setUp(self):
		self.ecliptic_longitude_degrees = 139
		self.ecliptic_longitude_minutes = 41
		self.ecliptic_longitude_seconds = 10
		self.ecliptic_latitude_degrees = 4
		self.ecliptic_latitude_minutes = 52
		self.ecliptic_latitude_seconds = 31
		self.greenwich_day = 6
		self.greenwich_month = 7
		self.greenwich_year = 2009

	def test_mean_obliquity_of_the_ecliptic(self):
		g_day = 6
		g_month = 7
		g_year = 2009

		obliquity = PC.mean_obliquity_of_the_ecliptic(g_day,g_month,g_year)
		obliquity = round(obliquity,8)

		print("[Greenwich Date] {g_month}/{g_day}/{g_year} = [Obliquity] {obliquity}".format(g_month=g_month,g_day=g_day,g_year=g_year,obliquity=obliquity))

		self.assertEqual(obliquity,23.43805531,"Obliquity")

	def test_ecliptic_coordinate_to_equatorial_coordinate(self):
		ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds = PC.ecliptic_coordinate_to_equatorial_coordinate(self.ecliptic_longitude_degrees,self.ecliptic_longitude_minutes,self.ecliptic_longitude_seconds,self.ecliptic_latitude_degrees,self.ecliptic_latitude_minutes,self.ecliptic_latitude_seconds,self.greenwich_day,self.greenwich_month,self.greenwich_year)

		print("[LON] {lon_deg}d {lon_min}m {lon_sec}s [LAT] {lat_deg}d {lat_min}m {lat_sec}s [GD] {g_month}/{g_day}/{g_year} = [RA] {ra_hours}:{ra_minutes}:{ra_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s".format(lon_deg=self.ecliptic_longitude_degrees,lon_min=self.ecliptic_longitude_minutes,lon_sec=self.ecliptic_longitude_seconds,lat_deg=self.ecliptic_latitude_degrees,lat_min=self.ecliptic_latitude_minutes,lat_sec=self.ecliptic_latitude_seconds,g_month=self.greenwich_month,g_day=self.greenwich_day,g_year=self.greenwich_year,ra_hours=ra_hours,ra_minutes=ra_minutes,ra_seconds=ra_seconds,dec_degrees=dec_degrees,dec_minutes=dec_minutes,dec_seconds=dec_seconds))

		self.assertEqual(ra_hours,9,"RA Hours")
		self.assertEqual(ra_minutes,34,"RA Minutes")
		self.assertEqual(ra_seconds,53.4,"RA Seconds")
		self.assertEqual(dec_degrees,19,"Dec Degrees")
		self.assertEqual(dec_minutes,32,"Dec Minutes")
		self.assertEqual(dec_seconds,8.52,"Dec Seconds")

	def test_equatorial_coordinate_to_ecliptic_coordinate(self):
		ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds = PC.ecliptic_coordinate_to_equatorial_coordinate(self.ecliptic_longitude_degrees,self.ecliptic_longitude_minutes,self.ecliptic_longitude_seconds,self.ecliptic_latitude_degrees,self.ecliptic_latitude_minutes,self.ecliptic_latitude_seconds,self.greenwich_day,self.greenwich_month,self.greenwich_year)

		ecl_long_deg,ecl_long_min,ecl_long_sec,ecl_lat_deg,ecl_lat_min,ecl_lat_sec = PC.equatorial_coordinate_to_ecliptic_coordinate(ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds,self.greenwich_day,self.greenwich_month,self.greenwich_year)

		print("[RA] {ra_hours}:{ra_minutes}:{ra_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s [GD] {g_month}/{g_day}/{g_year} = [LON] {lon_deg}d {lon_min}m {lon_sec}s [LAT] {lat_deg}d {lat_min}m {lat_sec}s".format(ra_hours=ra_hours,ra_minutes=ra_minutes,ra_seconds=ra_seconds,dec_degrees=dec_degrees,dec_minutes=dec_minutes,dec_seconds=dec_seconds,g_month=self.greenwich_month,g_day=self.greenwich_day,g_year=self.greenwich_year,lon_deg=ecl_long_deg,lon_min=ecl_long_min,lon_sec=ecl_long_sec,lat_deg=ecl_lat_deg,lat_min=ecl_lat_min,lat_sec=ecl_lat_sec))

		self.assertEqual(ecl_long_deg,139,"Ecliptic Longitude Degrees")
		self.assertEqual(ecl_long_min,41,"Ecliptic Longitude Minutes")
		self.assertEqual(ecl_long_sec,9.97,"Ecliptic Longitude Seconds")
		self.assertEqual(ecl_lat_deg,4,"Ecliptic Latitude Degrees")
		self.assertEqual(ecl_lat_min,52,"Ecliptic Latitude Minutes")
		self.assertEqual(ecl_lat_sec,30.99,"Ecliptic Latitude Seconds")

class test_galactic(UT.TestCase):
	def setUp(self):
		self.ra_hours = 10
		self.ra_minutes = 21
		self.ra_seconds = 0
		self.dec_degrees = 10
		self.dec_minutes = 3
		self.dec_seconds = 11

	def test_equatorial_coordinate_to_galactic_coordinate(self):
		gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec = PC.equatorial_coordinate_to_galactic_coordinate(self.ra_hours,self.ra_minutes,self.ra_seconds,self.dec_degrees,self.dec_minutes,self.dec_seconds)

		print("[EQ] [RA] {ra_hours}:{ra_minutes}:{ra_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s = [GAL] [LON] {gal_long_deg}d {gal_long_min}m {gal_long_sec}s [LAT] {gal_lat_deg}d {gal_lat_min}m {gal_lat_sec}s".format(ra_hours=self.ra_hours,ra_minutes=self.ra_minutes,ra_seconds=self.ra_seconds,dec_degrees=self.dec_degrees,dec_minutes=self.dec_minutes,dec_seconds=self.dec_seconds,gal_long_deg=gal_long_deg,gal_long_min=gal_long_min,gal_long_sec=gal_long_sec,gal_lat_deg=gal_lat_deg,gal_lat_min=gal_lat_min,gal_lat_sec=gal_lat_sec))

		self.assertEqual(gal_long_deg,232,"Galactic Longitude Degrees")
		self.assertEqual(gal_long_min,14,"Galactic Longitude Minutes")
		self.assertEqual(gal_long_sec,52.38,"Galactic Longitude Seconds")
		self.assertEqual(gal_lat_deg,51,"Galactic Latitude Degrees")
		self.assertEqual(gal_lat_min,7,"Galactic Latitude Minutes")
		self.assertEqual(gal_lat_sec,20.16,"Galactic Latitude Seconds")

	def test_galactic_coordinate_to_equatorial_coordinate(self):
		gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec = PC.equatorial_coordinate_to_galactic_coordinate(self.ra_hours,self.ra_minutes,self.ra_seconds,self.dec_degrees,self.dec_minutes,self.dec_seconds)

		ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds = PC.galactic_coordinate_to_equatorial_coordinate(gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec)

		print("[GAL] [LON] {gal_long_deg}d {gal_long_min}m {gal_long_sec}s [LAT] {gal_lat_deg}d {gal_lat_min}m {gal_lat_sec}s = [EQ] [RA] {ra_hours}:{ra_minutes}:{ra_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s".format(gal_long_deg=gal_long_deg,gal_long_min=gal_long_min,gal_long_sec=gal_long_sec,gal_lat_deg=gal_lat_deg,gal_lat_min=gal_lat_min,gal_lat_sec=gal_lat_sec,ra_hours=ra_hours,ra_minutes=ra_minutes,ra_seconds=ra_seconds,dec_degrees=dec_degrees,dec_minutes=dec_minutes,dec_seconds=dec_seconds))

		self.assertEqual(ra_hours,10,"Right Ascension Hours")
		self.assertEqual(ra_minutes,21,"Right Ascension Minutes")
		self.assertEqual(ra_seconds,0,"Right Ascension Seconds")
		self.assertEqual(dec_degrees,10,"Declination Degrees")
		self.assertEqual(dec_minutes,3,"Declination Degrees")
		self.assertEqual(dec_seconds,11,"Declination Seconds")

class test_object_angles(UT.TestCase):
	def setUp(self):
		self.ra_long_1_hour_deg = 5
		self.ra_long_1_min = 13
		self.ra_long_1_sec = 31.7
		self.dec_lat_1_deg = -8
		self.dec_lat_1_min = 13
		self.dec_lat_1_sec = 30
		self.ra_long_2_hour_deg = 6
		self.ra_long_2_min = 44
		self.ra_long_2_sec = 13.4
		self.dec_lat_2_deg = -16
		self.dec_lat_2_min = 41
		self.dec_lat_2_sec = 11
		self.hour_or_degree = "H"

	def test_angle_between_two_objects(self):

		angle_deg,angle_min,angle_sec = PC.angle_between_two_objects(self.ra_long_1_hour_deg,self.ra_long_1_min,self.ra_long_1_sec,self.dec_lat_1_deg,self.dec_lat_1_min,self.dec_lat_1_sec,self.ra_long_2_hour_deg,self.ra_long_2_min,self.ra_long_2_sec,self.dec_lat_2_deg,self.dec_lat_2_min,self.dec_lat_2_sec,self.hour_or_degree)

		print ("[OBJ 1] [RA LON] {ra_long_1_hour_deg}h/d {ra_long_1_min}m {ra_long_1_sec}s [DEC LAT] {dec_lat_1_deg}d {dec_lat_1_min}m {dec_lat_1_sec}s [OBJ 2] [RA LON] {ra_long_2_hour_deg}h/d {ra_long_2_min}m {ra_long_2_sec}s [DEC LAT] {dec_lat_2_deg}d {dec_lat_2_min}m {dec_lat_2_sec}s [TYPE] {hour_or_degree} = [ANGLE] {angle_deg}d {angle_min}m {angle_sec}s".format(ra_long_1_hour_deg=self.ra_long_1_hour_deg,ra_long_1_min=self.ra_long_1_min,ra_long_1_sec=self.ra_long_1_sec,dec_lat_1_deg=self.dec_lat_1_deg,dec_lat_1_min=self.dec_lat_1_min,dec_lat_1_sec=self.dec_lat_1_sec,ra_long_2_hour_deg=self.ra_long_2_hour_deg,ra_long_2_min=self.ra_long_2_min,ra_long_2_sec=self.ra_long_2_sec,dec_lat_2_deg=self.dec_lat_2_deg,dec_lat_2_min=self.dec_lat_2_min,dec_lat_2_sec=self.dec_lat_2_sec,hour_or_degree=self.hour_or_degree,angle_deg=angle_deg,angle_min=angle_min,angle_sec=angle_sec))

		self.assertEqual(angle_deg,23,"Angle Degrees")
		self.assertEqual(angle_min,40,"Angle Minutes")
		self.assertEqual(angle_sec,25.86,"Angle Seconds")

class test_rise_set(UT.TestCase):
	def setUp(self):
		self.ra_hours = 23
		self.ra_minutes = 39
		self.ra_seconds = 20
		self.dec_deg = 21
		self.dec_min = 42
		self.dec_sec = 0
		self.gw_date_day = 24
		self.gw_date_month = 8
		self.gw_date_year = 2010
		self.geog_long_deg = 64
		self.geog_lat_deg = 30
		self.vert_shift_deg = 0.5667

	def test_rising_and_setting(self):
		rise_set_status,ut_rise_hour,ut_rise_min,ut_set_hour,ut_set_min,az_rise,az_set = PC.rising_and_setting(self.ra_hours,self.ra_minutes,self.ra_seconds,self.dec_deg,self.dec_min,self.dec_sec,self.gw_date_day,self.gw_date_month,self.gw_date_year,self.geog_long_deg,self.geog_lat_deg,self.vert_shift_deg)

		print("[RA] {ra_hours}:{ra_minutes}:{ra_seconds} [DEC] {dec_deg}d {dec_min}m {dec_sec}s [GWD] {gw_date_month}/{gw_date_day}/{gw_date_year} [LON] {geog_long_deg} [LAT] {geog_lat_deg} [VS] {vert_shift_deg} = [STATUS] {rise_set_status} [UT] [RISE] {ut_rise_hour}:{ut_rise_min} [SET] {ut_set_hour}:{ut_set_min} [AZ] [RISE] {az_rise} [SET] {az_set}".format(ra_hours=self.ra_hours,ra_minutes=self.ra_minutes,ra_seconds=self.ra_seconds,dec_deg=self.dec_deg,dec_min=self.dec_min,dec_sec=self.dec_sec,gw_date_day=self.gw_date_day,gw_date_month=self.gw_date_month,gw_date_year=self.gw_date_year,geog_long_deg=self.geog_long_deg,geog_lat_deg=self.geog_lat_deg,vert_shift_deg=self.vert_shift_deg,rise_set_status=rise_set_status,ut_rise_hour=ut_rise_hour,ut_rise_min=ut_rise_min,ut_set_hour=ut_set_hour,ut_set_min=ut_set_min,az_rise=az_rise,az_set=az_set))

		self.assertEqual(rise_set_status,"OK","Rise/Set Status")
		self.assertEqual(ut_rise_hour,14,"UT Rise Hour")
		self.assertEqual(ut_rise_min,16,"UT Rise Minute")
		self.assertEqual(ut_set_hour,4,"UT Set Hour")
		self.assertEqual(ut_set_min,10,"UT Set Minute")
		self.assertEqual(az_rise,64.36,"AZ Rise")
		self.assertEqual(az_set,295.64,"AZ Set")

class test_precession(UT.TestCase):
	def setUp(self):
		self.ra_hour = 9
		self.ra_minutes = 10
		self.ra_seconds = 43
		self.dec_deg = 14
		self.dec_minutes = 23
		self.dec_seconds = 25
		self.epoch1_day = 0.923
		self.epoch1_month = 1
		self.epoch1_year = 1950
		self.epoch2_day = 1
		self.epoch2_month = 6
		self.epoch2_year = 1979

	def test_precession(self):
		corrected_ra_hour,corrected_ra_minutes,corrected_ra_seconds,corrected_dec_deg,corrected_dec_minutes,corrected_dec_seconds = PC.correct_for_precession(self.ra_hour,self.ra_minutes,self.ra_seconds,self.dec_deg,self.dec_minutes,self.dec_seconds,self.epoch1_day,self.epoch1_month,self.epoch1_year,self.epoch2_day,self.epoch2_month,self.epoch2_year)

		print("[RA] {ra_hour}:{ra_minutes}:{ra_seconds} [DEC] {dec_deg}d {dec_minutes}m {dec_seconds}s [EPOCH 1] {epoch1_month}/{epoch1_day}/{epoch1_year} [EPOCH 2] {epoch2_month}/{epoch2_day}/{epoch2_year} = [Corrected] [RA] {corrected_ra_hour}:{corrected_ra_minutes}:{corrected_ra_seconds} [DEC] {corrected_dec_deg}d {corrected_dec_minutes}m {corrected_dec_seconds}s".format(ra_hour=self.ra_hour,ra_minutes=self.ra_minutes,ra_seconds=self.ra_seconds,dec_deg=self.dec_deg,dec_minutes=self.dec_minutes,dec_seconds=self.dec_seconds,epoch1_day=self.epoch1_day,epoch1_month=self.epoch1_month,epoch1_year=self.epoch1_year,epoch2_day=self.epoch2_day,epoch2_month=self.epoch2_month,epoch2_year=self.epoch2_year,corrected_ra_hour=corrected_ra_hour,corrected_ra_minutes=corrected_ra_minutes,corrected_ra_seconds=corrected_ra_seconds,corrected_dec_deg=corrected_dec_deg,corrected_dec_minutes=corrected_dec_minutes,corrected_dec_seconds=corrected_dec_seconds))

		self.assertEqual(corrected_ra_hour,9,"Corrected Right Ascension Hour")
		self.assertEqual(corrected_ra_minutes,12,"Corrected Right Ascension Minutes")
		self.assertEqual(corrected_ra_seconds,20.18,"Corrected Right Ascension Seconds")
		self.assertEqual(corrected_dec_deg,14,"Corrected Declination Hour")
		self.assertEqual(corrected_dec_minutes,16,"Corrected Declination Minutes")
		self.assertEqual(corrected_dec_seconds,9.12,"Corrected Declination Seconds")

class test_nutation(UT.TestCase):
	def setUp(self):
		self.greenwich_day = 1
		self.greenwich_month = 9
		self.greenwich_year = 1988

	def test_nutation(self):
		nut_in_long_deg,nut_in_obl_deg = PC.nutation_in_ecliptic_longitude_and_obliquity(self.greenwich_day,self.greenwich_month,self.greenwich_year)

		nut_in_long_deg = round(nut_in_long_deg,9)
		nut_in_obl_deg = round(nut_in_obl_deg,7)

		print("[GWDATE] {greenwich_month}/{greenwich_day}/{greenwich_year} = [NUTATION] [LON] {nut_in_long_deg} [OBL] {nut_in_obl_deg}".format(greenwich_month=self.greenwich_month,greenwich_day=self.greenwich_day,greenwich_year=self.greenwich_year,nut_in_long_deg=nut_in_long_deg,nut_in_obl_deg=nut_in_obl_deg))

		self.assertEqual(nut_in_long_deg,0.001525808,"Nutation in Longitude (degrees)")
		self.assertEqual(nut_in_obl_deg,0.0025671,"Nutation in Obliquity (degrees)")

class test_aberration(UT.TestCase):
	def setUp(self):
		self.ut_hour = 0
		self.ut_minutes = 0
		self.ut_seconds = 0
		self.gw_day = 8
		self.gw_month = 9
		self.gw_year = 1988
		self.true_ecl_long_deg = 352
		self.true_ecl_long_min = 37
		self.true_ecl_long_sec = 10.1
		self.true_ecl_lat_deg = -1
		self.true_ecl_lat_min = 32
		self.true_ecl_lat_sec = 56.4

	def test_correct_for_aberration(self):
		apparent_ecl_long_deg,apparent_ecl_long_min,apparent_ecl_long_sec,apparent_ecl_lat_deg,apparent_ecl_lat_min,apparent_ecl_lat_sec = PC.correct_for_aberration(self.ut_hour,self.ut_minutes,self.ut_seconds,self.gw_day,self.gw_month,self.gw_year,self.true_ecl_long_deg,self.true_ecl_long_min,self.true_ecl_long_sec,self.true_ecl_lat_deg,self.true_ecl_lat_min,self.true_ecl_lat_sec)

		print("[Aberration] [UT] {ut_hour}:{ut_minutes}:{ut_seconds} [GWD] {gw_month}/{gw_day}/{gw_year} [ECL] [LON] {true_ecl_long_deg}d {true_ecl_long_min}m {true_ecl_long_sec}s [LAT] {true_ecl_lat_deg}d {true_ecl_lat_min}m {true_ecl_lat_sec}s = [Apparent ECL] [LON] {apparent_ecl_long_deg}d {apparent_ecl_long_min}m {apparent_ecl_long_sec}s [LAT] {apparent_ecl_lat_deg}d {apparent_ecl_lat_min}m {apparent_ecl_lat_sec}s".format(ut_hour=self.ut_hour,ut_minutes=self.ut_minutes,ut_seconds=self.ut_seconds,gw_month=self.gw_month,gw_day=self.gw_day,gw_year=self.gw_year,true_ecl_long_deg=self.true_ecl_long_deg,true_ecl_long_min=self.true_ecl_long_min,true_ecl_long_sec=self.true_ecl_long_sec,true_ecl_lat_deg=self.true_ecl_lat_deg,true_ecl_lat_min=self.true_ecl_lat_min,true_ecl_lat_sec=self.true_ecl_lat_sec,apparent_ecl_long_deg=apparent_ecl_long_deg,apparent_ecl_long_min=apparent_ecl_long_min,apparent_ecl_long_sec=apparent_ecl_long_sec,apparent_ecl_lat_deg=apparent_ecl_lat_deg,apparent_ecl_lat_min=apparent_ecl_lat_min,apparent_ecl_lat_sec=apparent_ecl_lat_sec))

		self.assertEqual(apparent_ecl_long_deg,352,"Apparent Ecliptic Longitude Degrees")
		self.assertEqual(apparent_ecl_long_min,37,"Apparent Ecliptic Longitude Minutes")
		self.assertEqual(apparent_ecl_long_sec,30.45,"Apparent Ecliptic Longitude Seconds")
		self.assertEqual(apparent_ecl_lat_deg,-1,"Apparent Ecliptic Latitude Degrees")
		self.assertEqual(apparent_ecl_lat_min,32,"Apparent Ecliptic Latitude Minutes")
		self.assertEqual(apparent_ecl_lat_sec,56.33,"Apparent Ecliptic Latitude Seconds")

class test_atmospheric_refraction(UT.TestCase):
	def setUp(self):
		self.true_ra_hour = 23
		self.true_ra_min = 14
		self.true_ra_sec = 0
		self.true_dec_deg = 40
		self.true_dec_min = 10
		self.true_dec_sec = 0
		self.coordinate_type = "TRUE"
		self.geog_long_deg = 0.17
		self.geog_lat_deg = 51.2036110
		self.daylight_saving_hours = 0
		self.timezone_hours = 0
		self.lcd_day = 23
		self.lcd_month = 3
		self.lcd_year = 1987
		self.lct_hour = 1
		self.lct_min = 1
		self.lct_sec = 24
		self.atmospheric_pressure_mbar = 1012
		self.atmospheric_temperature_celsius = 21.7

	def test_atmospheric_refraction(self):
		corrected_ra_hour,corrected_ra_min,corrected_ra_sec,corrected_dec_deg,corrected_dec_min,corrected_dec_sec = PC.atmospheric_refraction(self.true_ra_hour,self.true_ra_min,self.true_ra_sec,self.true_dec_deg,self.true_dec_min,self.true_dec_sec,self.coordinate_type,self.geog_long_deg,self.geog_lat_deg,self.daylight_saving_hours,self.timezone_hours,self.lcd_day,self.lcd_month,self.lcd_year,self.lct_hour,self.lct_min,self.lct_sec,self.atmospheric_pressure_mbar,self.atmospheric_temperature_celsius)

		print("[Refraction] [RA] {true_ra_hour}:{true_ra_min}:{true_ra_sec} [DEC] {true_dec_deg}d {true_dec_min}m {true_dec_sec}s [COORD TYPE] {coordinate_type} [GEOG LON/LAT] {geog_long_deg}d/{geog_lat_deg}d [DS HOURS] {daylight_saving_hours} [TZ HOURS] {timezone_hours} [LCD] {lcd_month}/{lcd_day}/{lcd_year} [LCT] {lct_hour}:{lct_min}:{lct_sec} [ATM] [PRESS MBR] {atmospheric_pressure_mbar} [TEMP C] {atmospheric_temperature_celsius} = [CORRECTED] [RA] {corrected_ra_hour}:{corrected_ra_min}:{corrected_ra_sec} [DEC] {corrected_dec_deg}d {corrected_dec_min}m {corrected_dec_sec}s".format(true_ra_hour=self.true_ra_hour,true_ra_min=self.true_ra_min,true_ra_sec=self.true_ra_sec,true_dec_deg=self.true_dec_deg,true_dec_min=self.true_dec_min,true_dec_sec=self.true_dec_sec,coordinate_type=self.coordinate_type,geog_long_deg=self.geog_long_deg,geog_lat_deg=self.geog_lat_deg,daylight_saving_hours=self.daylight_saving_hours,timezone_hours=self.timezone_hours,lcd_day=self.lcd_day,lcd_month=self.lcd_month,lcd_year=self.lcd_year,lct_hour=self.lct_hour,lct_min=self.lct_min,lct_sec=self.lct_sec,atmospheric_pressure_mbar=self.atmospheric_pressure_mbar,atmospheric_temperature_celsius=self.atmospheric_temperature_celsius,corrected_ra_hour=corrected_ra_hour,corrected_ra_min=corrected_ra_min,corrected_ra_sec=corrected_ra_sec,corrected_dec_deg=corrected_dec_deg,corrected_dec_min=corrected_dec_min,corrected_dec_sec=corrected_dec_sec))

		self.assertEqual(corrected_ra_hour,23,"Corrected RA Hours")
		self.assertEqual(corrected_ra_min,13,"Corrected RA Minutes")
		self.assertEqual(corrected_ra_sec,44.74,"Corrected RA Seconds")
		self.assertEqual(corrected_dec_deg,40,"Corrected Declination Degrees")
		self.assertEqual(corrected_dec_min,19,"Corrected Declination Minutes")
		self.assertEqual(corrected_dec_sec,45.76,"Corrected Declination Seconds")

class test_geocentric_parallax(UT.TestCase):
	def setUp(self):
		self.ra_hour = 22
		self.ra_min = 35
		self.ra_sec = 19
		self.dec_deg = -7
		self.dec_min = 41
		self.dec_sec = 13
		self.coordinate_type = "TRUE"
		self.equatorial_hor_parallax_deg = 1.019167
		self.geog_long_deg = -100
		self.geog_lat_deg = 50
		self.height_m = 60
		self.daylight_saving = 0
		self.timezone_hours = -6
		self.lcd_day = 26
		self.lcd_month = 2
		self.lcd_year = 1979
		self.lct_hour = 10
		self.lct_min = 45
		self.lct_sec = 0
	
	def test_corrections_for_geocentric_parallax(self):
		corrected_ra_hour,corrected_ra_min,corrected_ra_sec,corrected_dec_deg,corrected_dec_min,corrected_dec_sec = PC.corrections_for_geocentric_parallax(self.ra_hour,self.ra_min,self.ra_sec,self.dec_deg,self.dec_min,self.dec_sec,self.coordinate_type,self.equatorial_hor_parallax_deg,self.geog_long_deg,self.geog_lat_deg,self.height_m,self.daylight_saving,self.timezone_hours,self.lcd_day,self.lcd_month,self.lcd_year,self.lct_hour,self.lct_min,self.lct_sec)

		print("[Geocentric Parallax] [RA] {ra_hour}:{ra_min}:{ra_sec} [DEC] {dec_deg}d {dec_min}m {dec_sec}s [COORD TYPE] {coordinate_type} [EQ HOR PARA DEG] {equatorial_hor_parallax_deg} [GEOG] [LON] {geog_long_deg} [LAT] {geog_lat_deg} [HEIGHT] {height_m} [DS] {daylight_saving} [TZ] {timezone_hours} [LCD] {lcd_month}/{lcd_day}/{lcd_year} [LCT] {lct_hour}:{lct_min}:{lct_sec} = [CORRECTED] [RA] {corrected_ra_hour}:{corrected_ra_min}:{corrected_ra_sec} [DEC] {corrected_dec_deg}d {corrected_dec_min}m {corrected_dec_sec}s".format(ra_hour=self.ra_hour,ra_min=self.ra_min,ra_sec=self.ra_sec,dec_deg=self.dec_deg,dec_min=self.dec_min,dec_sec=self.dec_sec,coordinate_type=self.coordinate_type,equatorial_hor_parallax_deg=self.equatorial_hor_parallax_deg,geog_long_deg=self.geog_long_deg,geog_lat_deg=self.geog_lat_deg,height_m=self.height_m,daylight_saving=self.daylight_saving,timezone_hours=self.timezone_hours,lcd_day=self.lcd_day,lcd_month=self.lcd_month,lcd_year=self.lcd_year,lct_hour=self.lct_hour,lct_min=self.lct_min,lct_sec=self.lct_sec,corrected_ra_hour=corrected_ra_hour,corrected_ra_min=corrected_ra_min,corrected_ra_sec=corrected_ra_sec,corrected_dec_deg=corrected_dec_deg,corrected_dec_min=corrected_dec_min,corrected_dec_sec=corrected_dec_sec))

		self.assertEqual(corrected_ra_hour,22,"Corrected RA Hours")
		self.assertEqual(corrected_ra_min,36,"Corrected RA Minutes")
		self.assertEqual(corrected_ra_sec,43.22,"Corrected RA Seconds")
		self.assertEqual(corrected_dec_deg,-8,"Corrected Declination Degrees")
		self.assertEqual(corrected_dec_min,32,"Corrected Declination Minutes")
		self.assertEqual(corrected_dec_sec,17.4,"Corrected Declination Seconds")


if __name__ == '__main__':
	UT.main()
