/** Simple Greenwich Date structure (month, fractional day, year) */
struct GreenwichDate {
	int month;
	float day;
	int year;

	GreenwichDate();

	GreenwichDate(int initMonth, float initDay, int initYear) : month(initMonth), day(initDay), year(initYear) {};
};

/** Simple time structure (24 hour clock) */
struct GeneralTime {
	int hours;
	int minutes;
	int seconds;

	GeneralTime();

	GeneralTime(int initHours, int initMinutes, int initSeconds) : hours(initHours), minutes(initMinutes), seconds(initSeconds) {};
};