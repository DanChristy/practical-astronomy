#ifndef DOE_H
#define DOE_H

/** This class provides functionality for determining the date of Easter. */
class CDoe
{
private:
	float year;

public:
	CDoe(float year);

	/** Return a string representing the date of Easter, for the year specified at init.  */
	std::string GetEaster();
};
#endif