using csharp_astronomy.Interfaces;
using System;

namespace csharp_astronomy {
    public class AstroDateTime : IAstroDateTime {

        private readonly IMacro macro;

        public AstroDateTime(IMacro macro) {
            this.macro = macro;
        }

        public DateTime Easter(int year) {
            int day, month;

            var a = year % 19;
            var b = Math.Floor((decimal)year / 100);
            var c = year % 100;
            var d = Math.Floor(b / 4);
            var e = b % 4;
            var f = Math.Floor((b + 8) / 25);
            var g = Math.Floor((b - f + 1) / 3);
            var h = ((19 * a) + b - d - g + 15) % 30;
            var i = Math.Floor((decimal)c / 4);
            var k = c % 4;
            var l = (32 + 2 * (e + i) - h - k) % 7;
            var m = Math.Floor((a + (11 * h) + (22 * l)) / 451);
            var n = Math.Floor((h + l - (7 * m) + 114) / 31);
            var p = (h + l - (7 * m) + 114) % 31;

            day = Convert.ToInt32(p + 1);
            month = Convert.ToInt32(n);

            return new DateTime(year, month, day);
        }

        public int DayNumber(DateTime dateTime) {
            int month = dateTime.Month, year = dateTime.Year, day = dateTime.Day;
            if (month <= 2) {
                month = month -= 1;
                if (Utilities.IsLeapYear(dateTime))
                    month *= 62;
                else
                    month *= 63;

                month = Convert.ToInt32(Math.Floor((double)month / 2));
            } else {
                month = Convert.ToInt32(Math.Floor((month + 1) * 30.6));
                if (Utilities.IsLeapYear(dateTime))
                    month -= 62;
                else
                    month -= 63;
            }

            return month + day;
        }

        public int GreenwichToJulianDate(DateTime dateTime) {
            return macro.cd_jd(dateTime);
        }

        public DateTime JulianToGreenwichDate(int julianDate) {
            throw new NotImplementedException();
        }

        public int JulianDateDay(int julianDate) {
            throw new NotImplementedException();
        }
    }
}