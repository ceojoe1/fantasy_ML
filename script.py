import nflgame

year = 2016
week = 1
games = nflgame.games(2016, week=1)
players = nflgame.combine_game_stats(games)
plays = nflgame.combine_plays(games)


print ("\n------ RUSHING YARDS------\n")
for p in players.rushing().sort('rushing_yds').limit(10):
    msg = '%s %d carries for %d yards and %d TDs'
    print( msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))
print ("\n------ PASSING YARDS------\n")
for p in plays.sort('passing_yds').limit(10):
    print p