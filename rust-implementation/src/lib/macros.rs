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
