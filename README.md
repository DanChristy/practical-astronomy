# practical-astronomy

Implementation, in Python 3, of algorithms from "[Practical Astronomy with your Calculator or Spreadsheet](https://www.amazon.com/Practical-Astronomy-your-Calculator-Spreadsheet/dp/1108436072)" by Peter Duffett-Smith.  API documentation is published [here](https://jfcarr-astronomy.github.io/practical-astronomy/).

If you're interested in this topic, please buy the book!  It provides far more detail and context.

## Done

### Date/Time Functions

Type | Description
-----|------------
Calculate | Date of Easter
Convert | Civil Date to Day Number
Convert | Greenwich Date <-> Julian Date
Convert | Julian Date to Day-of-Week
Extract | Day, Month, and Year parts of Julian Date
Convert | Civil Time <-> Decimal Hours
Extract | Hour, Minutes, and Seconds parts of Decimal Hours
Convert | Local Civil Time <-> Universal Time
Convert | Universal Time <-> Greenwich Sidereal Time
Convert | Greenwich Sidereal Time <-> Local Sidereal Time

### Coordinate Functions

Type | Description
-----|------------
Convert | Angle <-> Decimal Degrees
Convert | Right Ascension <-> Hour Angle
Convert | Equatorial Coordinates <-> Horizon Coordinates
Calculate | Obliquity of the Ecliptic
Convert | Ecliptic Coordinates <-> Equatorial Coordinates
Convert | Equatorial Coordinates <-> Galactic Coordinates
Calculate | Angle between two objects
Calculate | Rising and Setting times for an object
Calculate | Precession (corrected coordinates between two epochs)
Calculate | Nutation (in ecliptic longitude and obliquity) for a Greenwich date
Calculate | Effects of aberration for ecliptic coordinates
Calculate | RA and Declination values, corrected for atmospheric refraction and geocentric parallax
Calculate | Heliographic coordinates
Calculate | Carrington rotation number
Calculate | Selenographic (lunar) coordinates (sub-Earth and sub-Solar)

### Sun Functions

Type | Description
-----|------------
Calculate | Approximate and precise positions of the Sun
Calculate | Sun's distance and angular size
Calculate | Local sunrise and sunset
Calculate | Morning and evening twilight
Calculate | Equation of time
Calculate | Solar elongation

### Planet Functions

Type | Description
-----|------------
Calculate | Approximate and precise position of planet
Calculate | Visual aspects of planet (distance, angular diameter, phase, light time, position angle of bright limb, and apparent magnitude)
Calculate | Position of comet (elliptical and parabolic)
Calculate | Binary star orbit data

### Moon Functions

Type | Description
-----|------------
Calculate | Approximate position of Moon
