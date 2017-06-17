from theastrologer import Horoscope

horoscope = Horoscope("aquarius")
today = horoscope.today()

def getTodayDataGivenZodiac(zodiac):
	horoscope = Horoscope(zodiac)
	today = horoscope.today()
	return today

def getMetaGivenZodiac(zodiac):
	return getTodayDataGivenZodiac(zodiac)['meta']

def getMoodGivenZodiac(zodiac):
	return getMetaGivenZodiac(zodiac)['mood']

def getKeywordsGivenZodiac(zodiac):
	return getMetaGivenZodiac(zodiac)['keywords']

def getIntensityGivenZodiac(zodiac):
	return getMetaGivenZodiac(zodiac)['intensity']

def getHoroscopeGivenZodiac(zodiac):
	return getTodayDataGivenZodiac(zodiac)['horoscope'].split("(c")[0]



