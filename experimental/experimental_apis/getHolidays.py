### IMPORTS

import holidays

from datetime import date


### STATIC VARIABLES

today = date.today()

australia_holidays = holidays.Australia()
austria_holidays = holidays.Austria()
canada_holidays = holidays.Canada()
colombia_holidays = holidays.Colombia()
czech_holidays = holidays.Czech()
denmark_holidays = holidays.Denmark()
england_holidays = holidays.England()
europeancentralbank_holidays = holidays.EuropeanCentralBank()
germany_holidays = holidays.Germany()
ireland_holidays = holidays.Ireland()
mexico_holidays = holidays.Mexico()
netherlands_holidays = holidays.Netherlands()
newzealand_holidays = holidays.NewZealand()
northernireland_holidays = holidays.NorthernIreland()
norway_holidays = holidays.Norway()
portugal_holidays = holidays.Portugal()
portugalext_holidays = holidays.PortugalExt()
scotland_holidays = holidays.Scotland()
spain_holidays = holidays.Spain()
unitedkingdom_holidays = holidays.UnitedKingdom()
unitedstates_holidays = holidays.UnitedStates()
wales_holidays = holidays.Wales()

def isDateHoliday(date, countryHolidays):
	return date in country

def isTodayHoliday(countryHolidays):
	return today in countryHolidays

def whatIsTodaysHoliday(countryHolidays):
	if isTodayHoliday(countryHolidays):
		return countryHolidays(today)
	return "Today is not a holiday in " + str(countryHolidays.country)


### FUNCTIONS

