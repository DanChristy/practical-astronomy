using csharp_astronomy.Interfaces;
using System;

namespace csharp_astronomy {
    public class Macro : IMacro {
        public int cd_jd(DateTime dateTime) {
            int year = dateTime.Year, month = dateTime.Month, day = dateTime.Day;
            double A, B, C, D;

            double Y = (month < 3) ? year - 1 : year;
            double M = (month < 3) ? month + 12 : month;

            if (year > 1582) {
                A = Math.Floor(Y / 100);
                B = 2 - A + Math.Floor(A / 4);
            } else {
                if (year == 1582 && month > 10) {
                    A = Math.Floor(Y / 100);
                    B = 2 - A + Math.Floor(A / 4);
                } else {
                    if (year == 1582 && month == 10 && day >= 15) {
                        A = Math.Floor(Y / 100);
                        B = 2 - A + Math.Floor(A / 4);
                    } else
                        B = 0;
                }
            }

            C = (Y < 0) ? Math.Floor((365.25 * Y) - 0.75) : Math.Floor(365.25 * Y);
            D = Math.Floor(30.6001 * (M + 1));

            return Convert.ToInt32(B + C + D + day + 1720994.5);
        }
    }
}