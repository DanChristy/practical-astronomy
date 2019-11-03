using System;

namespace csharp_astronomy {
    public static class Utilities {
        public static bool IsLeapYear(DateTime dateTime) {
            if (dateTime.Year % 4 == 0) {
                if (dateTime.Year % 100 == 0) {
                    if (dateTime.Year % 400 == 0) {
                        return true;
                    } else
                        return false;
                } else
                    return true;
            } else
                return false;
        }

        public static double Miles(this double kilometers) {
            return kilometers * 0.6213712;
        }

        public static double Kilometers(this double miles) {
            return miles * 1.609344;
        }
    }
}