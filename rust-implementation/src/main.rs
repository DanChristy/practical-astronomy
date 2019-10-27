mod lib;
mod tests;

use crate::tests::datetime as DTT;

fn main() {
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
}
