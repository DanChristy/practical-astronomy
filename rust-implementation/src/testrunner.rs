use crate::tests::coordinates as CST;
use crate::tests::datetime as DTT;

/// Run all functional tests.
pub fn run_tests() {
    run_datetime_tests();

    run_coordinate_tests();
}

pub fn run_datetime_tests() {
    DTT::test_easter(4, 20, 2003);
    DTT::test_day_numbers();

    let mut test_civil_time = DTT::TestCivilTimeScaffold {
        civil_hours: 18,
        civil_minutes: 31,
        civil_seconds: 27,
    };
    test_civil_time.test_civil_time_to_decimal_hours();
    test_civil_time.test_decimal_hours_to_civil_time();
    test_civil_time.test_decimal_time_parts();

    let mut test_local_civil_time = DTT::TestLocalCivilTimeScaffold {
        lct_hours: 3,
        lct_minutes: 37,
        lct_seconds: 0,
        is_daylight_savings: true,
        zone_correction: 4,
        local_day: 1,
        local_month: 7,
        local_year: 2013,
    };
    test_local_civil_time.test_local_civil_time_to_universal_time();
    test_local_civil_time.test_universal_time_to_local_civil_time();

    let mut test_universal_time_sidereal_time = DTT::TestUniversalTimeSiderealTimeScaffold {
        ut_hours: 14,
        ut_minutes: 36,
        ut_seconds: 51.67,
        gw_day: 22,
        gw_month: 4,
        gw_year: 1980,
    };
    test_universal_time_sidereal_time.test_universal_time_to_greenwich_sidereal_time();
    test_universal_time_sidereal_time.test_greenwich_sidereal_time_to_universal_time();

    let mut test_greenwich_sidereal_local_sidereal =
        DTT::TestGreenwichSiderealLocalSiderealScaffold {
            gst_hours: 4,
            gst_minutes: 40,
            gst_seconds: 5.23,
            geographical_longitude: -64.0,
        };
    test_greenwich_sidereal_local_sidereal.test_greenwich_sidereal_time_to_local_sidereal_time();
    test_greenwich_sidereal_local_sidereal.test_local_sidereal_time_to_greenwich_sidereal_time();

    DTT::test_julian_date_to_day_of_week();
}

pub fn run_coordinate_tests() {
    let mut test_angle_decimal_degrees = CST::TestAngleDecimalDegreesScaffold {
        degrees: 182.0,
        minutes: 31.0,
        seconds: 27.0,
    };
    test_angle_decimal_degrees.test_angle_to_decimal_degrees();
    test_angle_decimal_degrees.test_decimal_degrees_to_angle();
}
