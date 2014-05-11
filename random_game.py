from cbb_replay_models import *
from cbb_replay_game import *
from player_archetypes import *

game = Game()
game.home = Team()
game.away = Team()
game.teams = [game.home, game.away]
game.home.name = "Team 1"
game.home.opponent = game.away
game.away.name = "Team 2"
game.away.opponent = game.home
#Make Rosters
game.home.roster = [StarPointGuard(), StarPointGuard(), StarPointGuard(), StarShootingGuard(), StarComboGuard(), StarForwardCenter(), StarForwardCenter(), StarForwardCenter()]
game.away.roster = [StarPointGuard(), StarShootingGuard(), StarComboGuard(), StarComboGuard(), StarForwardCenter(), StarForwardCenter(), StarForwardCenter(), StarForwardCenter()]

#Make Starting Lineups
for p in game.home.roster:
    if p.primary_position == "c":
        if game.home.on_court["c"] == None:
            game.home.on_court["c"] = p
        elif p.secondary_position == "f":
            if game.home.on_court["sf"] == None:
                game.home.on_court["sf"] = p
            elif game.home.on_court["pf"] == None:
                game.home.on_court["pf"] = p
        else:
            pass
    elif p.primary_position == "f":
        if game.home.on_court["sf"] == None:
            game.home.on_court["sf"] = p
        elif game.home.on_court["pf"] == None:
            game.home.on_court["pf"] = p
        elif p.secondary_position == "c":
            if game.home.on_court["c"] == None:
                game.home.on_court["c"] = p
            else:
                pass
        elif p.secondary_position == "g":
            if game.home.on_court["pg"] == None:
                game.home.on_court["pg"] = p
            elif game.home.on_court["sg"] == None:
                game.home.on_court["sg"] = p
            else:
                pass
    elif p.primary_position == "g":
        if game.home.on_court["pg"] == None:
            game.home.on_court["pg"] = p
        elif game.home.on_court["sg"] == None:
            game.home.on_court["sg"] = p
        elif p.secondary_position == "f":
            if game.home.on_court["sf"] == None:
                game.home.on_court["sf"] = p
            elif game.home.on_court["pf"] == None:
                game.home.on_court["pf"] = p
            else:
                pass
    else:
        pass
for p in game.away.roster:
    if p.primary_position == "c":
        if game.away.on_court["c"] == None:
            game.away.on_court["c"] = p
        elif p.secondary_position == "f":
            if game.away.on_court["sf"] == None:
                game.away.on_court["sf"] = p
            elif game.away.on_court["pf"] == None:
                game.away.on_court["pf"] = p
        else:
            pass
    elif p.primary_position == "f":
        if game.away.on_court["sf"] == None:
            game.away.on_court["sf"] = p
        elif game.away.on_court["pf"] == None:
            game.away.on_court["pf"] = p
        elif p.secondary_position == "c":
            if game.away.on_court["c"] == None:
                game.away.on_court["c"] = p
            else:
                pass
        elif p.secondary_position == "g":
            if game.away.on_court["pg"] == None:
                game.away.on_court["pg"] = p
            elif game.away.on_court["sg"] == None:
                game.away.on_court["sg"] = p
            else:
                pass
    elif p.primary_position == "g":
        if game.away.on_court["pg"] == None:
            game.away.on_court["pg"] = p
        elif game.away.on_court["sg"] == None:
            game.away.on_court["sg"] = p
        elif p.secondary_position == "f":
            if game.away.on_court["sf"] == None:
                game.away.on_court["sf"] = p
            elif game.away.on_court["pf"] == None:
                game.away.on_court["pf"] = p
            else:
                pass
    else:
        pass
# print game.home.on_court
# print game.away.on_court
game = game_runner(game)
if game.home.points > game.away.points:
    print "%s won %s-%s" %(game.home.name, game.home.points, game.away.points)
elif game.away.points > game.home.points:
    print "%s won %s-%s" %(game.away.name, game.away.points, game.home.points)
else:
    print "they tied at %s" %(game.home.points)
print "%s Results:" %(game.home.name)
for p in game.home.roster:
    print p.name, p.primary_position, p.game_stats.points, p.game_stats.reb, p.game_stats.assists, p.game_stats.fouls
print "%s Results:" %(game.away.name)
for p in game.away.roster:
    print p.name, p.primary_position, p.game_stats.points, p.game_stats.reb, p.game_stats.assists, p.game_stats.fouls