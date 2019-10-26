use crate::lib::macros;
use crate::lib::util as utils;

/// Gets the date of Easter for the year specified.
///
/// ## Arguments
///
/// input_year -- Year for which you'd like the date of Easter.
///
/// ## Returns
///
/// month, day, year
pub fn get_date_of_easter(input_year: u32) -> (u32, u32, u32) {
    let year = input_year as f64;

    let a = year % 19.0;
    let b = (year / 100.0).floor();
    let c = year % 100.0;
    let d = (b / 4.0).floor();
    let e = b % 4.0;
    let f = ((b + 8.0) / 25.0).floor();
    let g = ((b - f + 1.0) / 3.0).floor();
    let h = ((19.0 * a) + b - d - g + 15.0) % 30.0;
    let i = (c / 4.0).floor();
    let k = c % 4.0;
    let l = (32.0 + 2.0 * (e + i) - h - k) % 7.0;
    let m = ((a + (11.0 * h) + (22.0 * l)) / 451.0).floor();
    let n = ((h + l - (7.0 * m) + 114.0) / 31.0).floor();
    let p = (h + l - (7.0 * m) + 114.0) % 31.0;

    let day = p + 1.0;
    let month = n;

    return (month as u32, day as u32, year as u32);
}

/// Calculate day number for a date.
///
/// ## Arguments
///
/// month, day, year
///
/// ## Returns
///
/// day_number
pub fn civil_date_to_day_number(mut month: u32, day: u32, year: u32) -> u32 {
    if month <= 2 {
        month = month - 1;
        month = if utils::is_leap_year(year) {
            month * 62
        } else {
            month * 63
        };
        month = (month as f64 / 2.0).floor() as u32;
    } else {
        month = ((month as f64 + 1.0) * 30.6).floor() as u32;
        month = if utils::is_leap_year(year) {
            month - 62
        } else {
            month - 63
        };
    }

    return month + day;
}

/// Convert a Civil Time (hours,minutes,seconds) to Decimal Hours
pub fn civil_time_to_decimal_hours(hours: u32, minutes: u32, seconds: u32) -> f64 {
    return macros::hms_dh(hours, minutes, seconds);
}

/// Convert Decimal Hours to Civil Time
///
/// ## Returns
///
/// hours (u32), minutes (u32), seconds (u32)
pub fn decimal_hours_to_civil_time(decimal_hours: f64) -> (u32, u32, u32) {
    let hours = macros::dh_hour(decimal_hours);
    let minutes = macros::dh_min(decimal_hours);
    let seconds = macros::dh_sec(decimal_hours);

    return (hours, minutes, seconds);
}
