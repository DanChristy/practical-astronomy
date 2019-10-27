use crate::lib::util as utils;

/// Convert a Civil Time (hours,minutes,seconds) to Decimal Hours
///
/// Original macro name: HMSDH
pub fn hms_dh(hours: u32, minutes: u32, seconds: u32) -> f64 {
    let f_hours = hours as f64;
    let f_minutes = minutes as f64;
    let f_seconds = seconds as f64;

    let a = f_seconds.abs() / 60.0;
    let b = (f_minutes.abs() + a) / 60.0;
    let c = f_hours.abs() + b;

    return if f_hours < 0.0 || f_minutes < 0.0 || f_seconds < 0.0 {
        -c
    } else {
        c
    };
}

/// Return the hour part of a Decimal Hours
///
/// Original macro name: DHHour
pub fn dh_hour(decimal_hours: f64) -> u32 {
    let a = decimal_hours.abs();
    let b = a * 3600.0;
    let c = utils::round_f64(b - 60.0 * (b / 60.0).floor(), 2);
    // let d = if c == 60.0 { 0.0 } else { c };
    let e = if c == 60.0 { b + 60.0 } else { b };

    return if decimal_hours < 0.0 {
        -(e / 3600.0).floor() as u32
    } else {
        (e / 3600.0).floor() as u32
    };
}

/// Return the minutes part of a Decimal Hours
///
/// Original macro name: DHMin
pub fn dh_min(decimal_hours: f64) -> u32 {
    let a = decimal_hours.abs();
    let b = a * 3600.0;
    let c = utils::round_f64(b - 60.0 * (b / 60.0).floor(), 2);
    let e = if c == 60.0 { b + 60.0 } else { b };

    return ((e / 60.0).floor() % 60.0) as u32;
}

/// Return the seconds part of a Decimal Hours
///
/// Original macro name: DHSec
pub fn dh_sec(decimal_hours: f64) -> u32 {
    let a = decimal_hours.abs();
    let b = a * 3600.0;
    let c = utils::round_f64(b - 60.0 * (b / 60.0).floor(), 2);
    let d = if c == 60.0 { 0.0 } else { c };

    return d as u32;
}

/// Convert a Greenwich Date/Civil Date (day,month,year) to Julian Date
///
/// Original macro name: CDJD
pub fn cd_jd(day: f64, month: u32, year: u32) -> f64 {
    let f_day = day as f64;
    let f_month = month as f64;
    let f_year = year as f64;

    let y = if f_month < 3.0 { f_year - 1.0 } else { f_year };
    let m = if f_month < 3.0 {
        f_month + 12.0
    } else {
        f_month
    };

    let mut b: f64 = 0.0;

    if f_year > 1582.0 {
        let a = (y / 100.0).floor();
        b = 2.0 - a + (a / 4.0).floor();
    } else {
        if f_year == 1582.0 && f_month > 10.0 {
            let a = (y / 100.0).floor();
            b = 2.0 - a + (a / 4.0).floor();
        } else {
            if f_year == 1582.0 && f_month == 10.0 && f_day >= 15.0 {
                let a = (y / 100.0).floor();
                b = 2.0 - a + (a / 4.0).floor();
            } else {
                b = 0.0;
            }
        }
    }

    let c = if y < 0.0 {
        ((365.25 * y) - 0.75).floor()
    } else {
        (365.25 * y).floor()
    };

    let d = (30.6001 * (m + 1.0)).floor();

    return b + c + d + f_day + 1720994.5;
}

/// Returns the day part of a Julian Date
///
/// Original macro name: JDCDay
pub fn jdc_day(julian_date: f64) -> f64 {
    let i = (julian_date + 0.5).floor();
    let f = julian_date + 0.5 - i;
    let a = ((i - 1867216.25) / 36524.25).floor();
    let b = if i > 2299160.0 {
        i + 1.0 + a - (a / 4.0).floor()
    } else {
        i
    };
    let c = b + 1524.0;
    let d = ((c - 122.1) / 365.25).floor();
    let e = (365.25 * d).floor();
    let g = ((c - e) / 30.6001).floor();

    return c - e + f - (30.6001 * g).floor();
}

/// Returns the month part of a Julian Date
///
/// Original macro name: JDCMonth
pub fn jdc_month(julian_date: f64) -> u32 {
    let i = (julian_date + 0.5).floor();
    let f = julian_date + 0.5 - i;
    let a = ((i - 1867216.25) / 36524.25).floor();
    let b = if i > 2299160.0 {
        i + 1.0 + a - (a / 4.0).floor()
    } else {
        i
    };
    let c = b + 1524.0;
    let d = ((c - 122.1) / 365.25).floor();
    let e = (365.25 * d).floor();
    let g = ((c - e) / 30.6001).floor();

    let return_value = if g < 13.5 { g - 1.0 } else { g - 13.0 };

    return return_value as u32;
}

/// Returns the year part of a Julian Date
///
/// Original macro name: JDCYear
pub fn jdc_year(julian_date: f64) -> u32 {
    let i = (julian_date + 0.5).floor();
    let f = julian_date + 0.5 - i;
    let a = ((i - 1867216.25) / 36524.25).floor();
    let b = if i > 2299160.0 {
        i + 1.0 + a - (a / 4.0).floor()
    } else {
        i
    };
    let c = b + 1524.0;
    let d = ((c - 122.1) / 365.25).floor();
    let e = (365.25 * d).floor();
    let g = ((c - e) / 30.6001).floor();
    let h = if g < 13.5 { g - 1.0 } else { g - 13.0 };

    let return_value = if h > 2.5 { d - 4716.0 } else { d - 4715.0 };

    return return_value as u32;
}
