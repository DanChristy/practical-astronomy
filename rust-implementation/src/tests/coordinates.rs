use crate::lib::coordinates as CS;
use crate::lib::util;

pub struct TestAngleDecimalDegreesScaffold {
    pub degrees: f64,
    pub minutes: f64,
    pub seconds: f64,
}

impl TestAngleDecimalDegreesScaffold {
    pub fn test_angle_to_decimal_degrees(&mut self) {
        let decimal_degrees = util::round_f64(
            CS::angle_to_decimal_degrees(self.degrees, self.minutes, self.seconds),
            6,
        );

        println!(
            "Angle to decimal degrees: [DMS] {}d {}m {}s = [Decimal Degrees] {}",
            self.degrees, self.minutes, self.seconds, decimal_degrees
        );

        assert_eq!(decimal_degrees, 182.524167, "Decimal Degrees");
    }

    pub fn test_decimal_degrees_to_angle(&mut self) {
        let decimal_degrees = util::round_f64(
            CS::angle_to_decimal_degrees(self.degrees, self.minutes, self.seconds),
            6,
        );

        let (degrees, minutes, seconds) = CS::decimal_degrees_to_angle(decimal_degrees);

        println!(
            "Decimal degrees to angle: [Decimal Degrees] {} = [DMS] {}d {}m {}s",
            decimal_degrees, degrees, minutes, seconds
        );

        assert_eq!(degrees, 182.0, "Degrees");
        assert_eq!(minutes, 31.0, "Minutes");
        assert_eq!(seconds, 27.0, "Seconds");
    }
}
