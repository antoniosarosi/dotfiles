//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
    { "  ", "checkupdates | wc -l",  60, 0 },
    { "", "brightness",  2, 0 },
    { "", "volume",  2, 0 },
    { "", "battery",  60, 0 },

	{"", "date '+ %d/%m/%Y   %H:%M%p'",					5,		0},
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = "  ";
static unsigned int delimLen = 5;
