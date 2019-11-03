using csharp_astronomy.Interfaces;
using System;
using System.Collections.Generic;
using Xunit;

namespace csharp_astronomy.UnitTests {
    public class DateTimeTests {

        private readonly IAstroDateTime astroDateTime;

        public DateTimeTests() {
            astroDateTime = new AstroDateTime();
        }

        [Fact]
        public void GetEasterByYear() {
            DateTime easterDate = new DateTime(2009, 4, 12);

            var resultDate = astroDateTime.Easter(easterDate.Year);

            Assert.Equal(easterDate.ToShortDateString(), resultDate.ToShortDateString());
        }

        public static IEnumerable<object[]> DayNumberTestSet => new List<object[]> {
            new object[] { new DateTime(2000, 1, 1), 1 },
            new object[] { new DateTime(2000, 3, 1), 61 },
            new object[] { new DateTime(2003, 6, 1), 152 },
            new object[] { new DateTime(2009, 11, 27), 331 }
        };

        [Theory]
        [MemberData(nameof(DayNumberTestSet))]
        public void DayNumber(DateTime dateTime, int expected) {
            var result = astroDateTime.DayNumber(dateTime);

            Assert.Equal(expected, result);
        }
    }
}