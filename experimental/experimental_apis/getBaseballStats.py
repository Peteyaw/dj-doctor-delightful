### IMPORTS

from __future__ import print_function
import mlbgame

### FUNCTIONS

def getAllGamesGivenTeamAndTime(team, year, month=None, day=None, home=None):
	if month:
		if day:
			homeGames = mlbgame.day(year, month, day, home=team)
			awayGames = mlbgame.day(year, month, day, away=team)
			return homeGames + awayGames
		else:
			homeGames = mlbgame.day(year, month, home=team)
			awayGames = mlbgame.day(year, month, away=team)
	else:
		homeGames = mlbgame.day(year, home=team)
		awayGames = mlbgame.day(year, away=team)
	if home == both:
		return homeGames + awayGames
	if home:
		return homeGames
	return awayGames

def getGameGivenTeamAndDate(team, year, month, day):
	return getAllGamesGivenTeamAndTime(team, year, month, day)[0]

def getPlayerStatsGivenGame(game):
	return mlbgame.player_stats(game.game_id)

def getTeamStatsGivenGame(game):
	return mlbgame.team_stats(game.game_id)

def getPitcherStatsGivenGame(game):
	return mlbgame.PitcherStats(game)

def getBatterStatsGivenGame(game):
	return mlbgame.BatterStats(game)





