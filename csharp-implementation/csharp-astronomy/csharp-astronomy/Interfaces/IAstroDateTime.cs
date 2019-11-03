using System;

namespace csharp_astronomy.Interfaces {
    public interface IAstroDateTime {
        DateTime Easter(int year);
        int DayNumber(DateTime dateTime);
        int GreenwichToJulianDate(DateTime dateTime);
        DateTime JulianToGreenwichDate(int julianDate);
        int JulianDateDay(int julianDate);
    }
}