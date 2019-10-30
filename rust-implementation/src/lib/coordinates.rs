use crate::lib::util as utils;

/// Convert an Angle (degrees, minutes, and seconds) to Decimal Degrees
pub fn angle_to_decimal_degrees(degrees: f64, minutes: f64, seconds: f64) -> f64 {
    let a = seconds.abs() / 60.0;
    let b = (minutes.abs() + a) / 60.0;
    let c = degrees.abs() + b;
    let d = if degrees < 0.0 || minutes < 0.0 || seconds < 0.0 {
        -c
    } else {
        c
    };

    return d;
}

/// Convert Decimal Degrees to an Angle (degrees, minutes, and seconds)
///
/// ## Returns
/// degrees, minutes, seconds
pub fn decimal_degrees_to_angle(decimal_degrees: f64) -> (f64, f64, f64) {
    let unsigned_decimal = decimal_degrees.abs();
    let total_seconds = unsigned_decimal * 3600.0;
    let seconds_2_dp = utils::round_f64(total_seconds % 60.0, 2);
    let corrected_seconds = if seconds_2_dp == 60.0 {
        0.0
    } else {
        seconds_2_dp
    };
    let corrected_remainder = if seconds_2_dp == 60.0 {
        total_seconds + 60.0
    } else {
        total_seconds
    };
    let minutes = (corrected_remainder / 60.0).floor() % 60.0;
    let unsigned_degrees = (corrected_remainder / 3600.0).floor();
    let signed_degrees = if decimal_degrees < 0.0 {
        -1.0 * unsigned_degrees
    } else {
        unsigned_degrees
    };

    return (signed_degrees, minutes, corrected_seconds.floor());
}
