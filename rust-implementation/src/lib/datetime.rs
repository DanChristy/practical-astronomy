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

/// Convert local Civil Time to Universal Time
///
/// ## Returns
///
/// UT hours, UT mins, UT secs, GW day, GW month, GW year
pub fn local_civil_time_to_universal_time(
    lct_hours: u32,
    lct_minutes: u32,
    lct_seconds: u32,
    is_daylight_savings: bool,
    zone_correction: i32,
    local_day: u32,
    local_month: u32,
    local_year: u32,
) -> (u32, u32, u32, u32, u32, u32) {
    let lct = civil_time_to_decimal_hours(lct_hours, lct_minutes, lct_seconds);

    let daylight_savings_offset = if is_daylight_savings == true { 1 } else { 0 };

    let ut_interim = lct - daylight_savings_offset as f64 - zone_correction as f64;
    let gday_interim = local_day as f64 + (ut_interim / 24.0);

    let jd = macros::cd_jd(gday_interim, local_month, local_year);

    let g_day = macros::jdc_day(jd) as f64;
    let g_month = macros::jdc_month(jd);
    let g_year = macros::jdc_year(jd);

    let ut = 24.0 * (g_day - g_day.floor());

    return (
        macros::dh_hour(ut),
        macros::dh_min(ut),
        macros::dh_sec(ut),
        g_day.floor() as u32,
        g_month,
        g_year,
    );
}

/// Convert Universal Time to local Civil Time
///
/// ## Returns
///
/// LCT hours, LCT minutes, LCT seconds, day, month, year
pub fn universal_time_to_local_civil_time(
    ut_hours: u32,
    ut_minutes: u32,
    ut_seconds: u32,
    is_daylight_savings: bool,
    zone_correction: i32,
    gw_day: u32,
    gw_month: u32,
    gw_year: u32,
) -> (u32, u32, u32, u32, u32, u32) {
    let dst_value = if is_daylight_savings == true { 1 } else { 0 };
    let ut = macros::hms_dh(ut_hours, ut_minutes, ut_seconds);
    let zone_time = ut + zone_correction as f64;
    let local_time = zone_time + dst_value as f64;
    let local_jd_plus_local_time =
        macros::cd_jd(gw_day as f64, gw_month, gw_year) + (local_time / 24.0);
    let local_day = macros::jdc_day(local_jd_plus_local_time) as f64;
    let integer_day = local_day.floor();
    let local_month = macros::jdc_month(local_jd_plus_local_time);
    let local_year = macros::jdc_year(local_jd_plus_local_time);

    let lct = 24.0 * (local_day - integer_day as f64);

    return (
        macros::dh_hour(lct),
        macros::dh_min(lct),
        macros::dh_sec(lct),
        integer_day as u32,
        local_month,
        local_year,
    );
}
