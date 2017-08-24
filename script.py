import nflgame
import pandas as pd
import matplotlib.pyplot as plt
import datetime


def loadGame(year):
    games = nflgame.games(year)
    print("Loaded {} games.".format(year))
    return games

def getPlayers(game):
    players = nflgame.combine_game_stats(game)
    print("Loaded all player data.")
    return players

def getRushing(players):
    runs = pd.Series([p.rushing_yds for p in players.rushing()])
    print("Rushing Data: {}".format(runs))
    return runs


def plot(players):
    print("Plotting data")
    fig = plt.figure(figsize=(12,8))

    ax = fig.add_subplot(111)
    ax.set_title('age vs. rushing yds', fontsize=14, color='green')
    fig.subplots_adjust(top=0.85)

    ax.set_ylabel('age(days)')
    ax.set_xlabel('rushing_yds')

    plt.style.use('ggplot')

    for p in players.rushing():
        plt.scatter(p.rushing_yds, (datetime.datetime.today() - datetime.datetime.strptime(p.player.birthdate,'%m/%d/%Y')).days)

def main():
    print("Program Started....")
    games = loadGame(2016)
    players = getPlayers(games)
    runs = getRushing(players)
    plot(players)
    return



main()

