from file_parser import getGames
import sys

max_year = 2018

# Print play_range plays of all dictionaries of a list of games
def print_games(game, play_range=[0]):
	for game in games:
		for num in play_range:
			num = min(num, len(game))
			for key in game[num]:
				print(key + ":    " + game[num][key])
		print()

if __name__ == '__main__':

	# Take argv and decide what years to parse given what args are given
	year_range = [max_year]
	if(len(sys.argv) == 2):
		year_range = list(range(int(sys.argv[1]), max_year + 1))
	elif(len(sys.argv) == 3):
		year_range = list(range(int(sys.argv[1]), int(sys.argv[2])+1))


	games = getGames(year_range, ["home_team", "away_team"])
	print_games(games)
