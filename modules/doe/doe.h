#ifndef DOE_H
#define DOE_H

/** This class provides functionality for determining the date of Easter. */
class CDoe {
public:
	CDoe();

	/** Return a string representing the date of Easter, for the year specified.  */
	std::string GetEaster(float year);
};
#endif
