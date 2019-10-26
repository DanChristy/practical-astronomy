use crate::lib::datetime as DT;
use crate::lib::macros as MA;
use crate::lib::util as UT;

/// Test date of Easter.
///
/// ## Input
///
/// 2003
///
/// ## Expected Output
///
/// 4/20/2003
pub fn test_easter(expected_month: u32, expected_day: u32, input_year: u32) {
    let (month, day, year) = DT::get_date_of_easter(input_year);

    println!(
        "Date of Easter: [Year] {} = [Date of Easter] {}/{}/{}",
        input_year, month, day, year
    );

    assert_eq!(month, expected_month, "Month of Easter");
    assert_eq!(day, expected_day, "Day of Easter");
    assert_eq!(year, input_year, "Year of Easter");
}

/// Test day numbers (various)
pub fn test_day_numbers() {
    test_day_number(1, 1, 2000, 1);
    test_day_number(3, 1, 2000, 61);
    test_day_number(6, 1, 2003, 152);
    test_day_number(11, 27, 2009, 331);
}

/// Tests calculation of a day number.
///
/// Asserts that the calculated result matches the expected result.
///
/// ## Input
///
/// input_month, input_day, input_year, expected_result
fn test_day_number(input_month: u32, input_day: u32, input_year: u32, expected_result: u32) {
    let result = DT::civil_date_to_day_number(input_month, input_day, input_year);

    println!(
        "Day number: [Date] {}/{}/{} = [Day Number] {}",
        input_month, input_day, input_year, result
    );

    assert_eq!(result, expected_result, "Day Number");
}

/// Civil Time tests.
pub struct TestCivilTimeScaffold {
    pub civil_hours: u32,
    pub civil_minutes: u32,
    pub civil_seconds: u32,
}

impl TestCivilTimeScaffold {
    /// Test conversion of civil time to decimal hours.
    pub fn test_civil_time_to_decimal_hours(&mut self) {
        let decimal_hours = DT::civil_time_to_decimal_hours(
            self.civil_hours,
            self.civil_minutes,
            self.civil_seconds,
        );

        println!(
            "Civil time to decimal hours: [Time] {}:{}:{} = [Decimal Hours] {}",
            self.civil_hours, self.civil_minutes, self.civil_seconds, decimal_hours
        );

        assert_eq!(UT::round_f64(decimal_hours, 8), 18.52416667);
    }
}

impl TestCivilTimeScaffold {
    /// Test conversion of decimal hours to civil time.
    pub fn test_decimal_hours_to_civil_time(&mut self) {
        let decimal_hours = DT::civil_time_to_decimal_hours(
            self.civil_hours,
            self.civil_minutes,
            self.civil_seconds,
        );
        let (civil_hours, civil_minutes, civil_seconds) =
            DT::decimal_hours_to_civil_time(decimal_hours);

        println!(
            "Decimal hours to civil time: [Decimal Hours] {} = [Civil Time] {}:{}:{}",
            decimal_hours, civil_hours, civil_minutes, civil_seconds
        );

        assert_eq!(civil_hours, self.civil_hours);
        assert_eq!(civil_minutes, self.civil_minutes);
        assert_eq!(civil_seconds, self.civil_seconds);
    }
}

impl TestCivilTimeScaffold {
    /// Test extraction of hour part, minutes part, and seconds part from decimal hours.
    pub fn test_decimal_time_parts(&mut self) {
        let decimal_hours = DT::civil_time_to_decimal_hours(
            self.civil_hours,
            self.civil_minutes,
            self.civil_seconds,
        );

        let hour_part = MA::dh_hour(decimal_hours);
        let minutes_part = MA::dh_min(decimal_hours);
        let seconds_part = MA::dh_sec(decimal_hours);

        println!(
			"Extract time parts from decimal hours: [Decimal Hours] {} = [Hour] {} [Minutes] {} [Seconds] {}",
			decimal_hours, hour_part, minutes_part, seconds_part
		);

        assert_eq!(hour_part, self.civil_hours, "Hour Part");
        assert_eq!(minutes_part, self.civil_minutes, "Minutes Part");
        assert_eq!(seconds_part, self.civil_seconds, "Seconds Part");
    }
}
