/** Simple Greenwich Date structure (month, fractional day, year) */
struct GreenwichDate {
	int month;
	float day;
	int year;
};

/** Simple time structure (24 hour clock) */
struct GeneralTime {
	int hours;
	int minutes;
	int seconds;
};