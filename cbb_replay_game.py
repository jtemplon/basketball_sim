from cbb_replay_models import *

def jump_ball(game):
    state = flip_card()
    if state[0] == "off":
        if (game.home.on_court[state[1]].defensive_rebound_rating > state[2]) \
        or (game.home.on_court[state[1]].offensive_rebound_rating > state[2]):
           game.possession = game.home
        else:
            jump_ball(game)
    else:
        if (game.away.on_court[state[1]].defensive_rebound_rating > state[2]) \
        or (game.away.on_court[state[1]].offensive_rebound_rating > state[2]):
           game.possession = game.away
        else:
            jump_ball(game)

def substitutions(k, team, available):
    for a in available:
        if k == "sf" or k == "pf" and a.primary_position == "f":
            team.on_court[k] = a
            break
        elif k == "pg" or k == "sg" and a.primary_position == "g":
            team.on_court[k] = a
            break
        elif k == "c" and (a.primary_position == "c" or a.secondary_position == "c"):
            team.on_court[k] = a
            break
        else:
            pass
    
def make_substitutions(game, team):
    available_players = []
    on_court = []
    #Find home players on roster
    for p in team.roster:
        available_players.append(p)
    #Find home players already in game
    for k in team.on_court.keys():
        on_court.append(team.on_court[k])
    #Find difference in those lists
    hoc = set(on_court)
    available = [x for x in available_players if (x not in hoc) and (x.game_stats.fouls < 5)]
    #Go through list and make subs if applicable
    for k in team.on_court.keys():
        #cover foul trouble cases
        if team.on_court[k].game_stats.fouls >= 2 and game.total_time_segments < 130:
            substitutions(k, team, available)
        elif team.on_court[k].game_stats.fouls >= 3 and game.total_time_segments < 195:
            substitutions(k, team, available)
        elif team.on_court[k].game_stats.fouls >= 5:
            substitutions(k, team, available)
        #this is having taken way more shots than you should
        elif team.on_court[k].game_stats.shots >= (int(team.on_court[k].shots_per_game/game.total_time_segments/float(273))+2):
            substitutions(k, team, available)
        else:
            pass

def find_fouler(action_state, opposing_player, game):
    if action_state[0] == "def":
        opposing_player.game_stats.fouls += 1
    else:
        if action_state[3] > 75:
            opposing_player.game_stats.fouls += 1
        else:
            for k in game.player_ranges.keys():
                if game.player_ranges[k][0] <= action_state[3] <= game.player_ranges[k][1]:
                    game.possession.opponent.on_court[k].game_stats.fouls += 1
                else:
                    pass

def rebound_sequence(game, shot_type):
    rebound_state = flip_card()
    offensive_player = game.possession.on_court[rebound_state[1]]
    defensive_player = game.possession.on_court[rebound_state[1]]
    # print defensive_player.defensive_rebound_rating
    # print shot_type
    if game.rebound_count < 4:
        if rebound_state[0] == "off":
            if shot_type == "fg":
                if offensive_player.offensive_rebound_rating > rebound_state[2]:
                    offensive_player.game_stats.oreb += 1
                    offensive_player.game_stats.reb += 1
                    game.rebound_count = 0
                elif defensive_player.dominant_defensive_rebound_rating[0] <= rebound_state[2] <= defensive_player.dominant_defensive_rebound_rating[1]:
                    defensive_player.game_stats.reb += 1
                    game.possession = game.possession.opponent
                    game.rebound_count = 0
                    game_runner(game)
                else:
                    game.rebound_count += 1
                    rebound_sequence(game, shot_type)
            elif shot_type == "ft":
                if (offensive_player.offensive_rebound_rating - 5) > rebound_state[2]:
                    offensive_player.game_stats.oreb += 1
                    offensive_player.game_stats.reb += 1
                    game.rebound_count = 0
                elif defensive_player.dominant_defensive_rebound_rating[0] <= rebound_state[2] <= defensive_player.dominant_defensive_rebound_rating[1]:
                    defensive_player.game_stats.reb += 1
                    game.possession = game.possession.opponent
                    game.rebound_count = 0
                    game_runner(game)
                else:
                    game.rebound_count += 1
                    rebound_sequence(game, shot_type)
        else:
            if shot_type == "fg":
                if defensive_player.defensive_rebound_rating > rebound_state[2]:
                    defensive_player.game_stats.reb += 1
                    game.possession = game.possession.opponent
                    game.rebound_count = 0
                    game_runner(game)
                elif offensive_player.dominant_offensive_rebound_rating[0] <= rebound_state[2] <= offensive_player.dominant_offensive_rebound_rating[1]:
                    offensive_player.game_stats.oreb += 1
                    offensive_player.game_stats.reb += 1
                    game.rebound_count = 0
                else:
                    game.rebound_count += 1
                    rebound_sequence(game, shot_type)
            elif shot_type == "ft":
                if (defensive_player.offensive_rebound_rating + 5) > rebound_state[2]:
                    defensive_player.game_stats.reb += 1
                    game.possession = game.possession.opponent
                    game.rebound_count = 0
                    game_runner(game)
                elif offensive_player.dominant_offensive_rebound_rating[0] <= rebound_state[2] <= offensive_player.dominant_offensive_rebound_rating[1]:
                    offensive_player.game_stats.oreb += 1
                    offensive_player.game_stats.reb += 1
                    game.rebound_count = 0
                else:
                    game.rebound_count += 1
                    rebound_sequence(game, shot_type)
    #ball goes out of bounds instead of endless loop
    else:
        game.rebound_count = 0
        make_substitutions(game, game.home)
        make_substitutions(game, game.away)
        if rebound_state[0] == "off":
            game.possession = game.possession.opponent
            game_runner(game)
        else:
            game_runner(game)

def resolve_play(k, key_player, opposing_player, game, position, action_state):
    # print "RESOLVE"
    # print key_player.name
    if k == "fg_foul_range":
        game.possession.points += 2
        key_player.game_stats.shots += 1
        key_player.game_stats.points += 2
        find_fouler(action_state, opposing_player, game)
        make_substitutions(game, game.home)
        make_substitutions(game, game.away)
        ft_state = flip_card()
        # game.total_time_segments += 1
        if key_player.offense_results.free_throw_shot[1] >= ft_state[3]:
            game.possession.points += 1
            key_player.game_stats.points += 1
            game.possession = game.possession.opponent
            game_runner(game)
        else:
            rebound_sequence(game, "ft")
    elif k == "fg_range":
        game.possession.points += 2
        key_player.game_stats.shots += 1
        key_player.game_stats.points += 2
        assist_state = flip_card()
        if assist_state[1] == position:
            pass
        elif game.possession.on_court[assist_state[1]].assist_rating >= assist_state[2]:
            game.possession.on_court[assist_state[1]].game_stats.assists += 1
        else:
            pass
        game.possession = game.possession.opponent
        game_runner(game)
    elif k == "assist_range":
        assist_state = flip_card()
        #Player makes an awesome play and scores
        if assist_state[1] == position:
            game.possession.points += 2
            key_player.game_stats.shots += 1
            key_player.game_stats.points += 2
            game.possession = game.possession.opponent
            game_runner(game)            
        #Player gets assist and makes basket
        elif game.possession.on_court[assist_state[1]].assist_rating >= assist_state[2]:
            game.possession.on_court[assist_state[1]].game_stats.assists += 1
            game.possession.points += 2
            key_player.game_stats.shots += 1
            key_player.game_stats.points += 2
            game.possession = game.possession.opponent
            game_runner(game)
        #Misses shot because didn't get an assist
        else:
            key_player.game_stats.shots += 1
            rebound_sequence(game, "fg")
    elif k == "foul_range":
        find_fouler(action_state, opposing_player, game)
        make_substitutions(game, game.home)
        make_substitutions(game, game.away)
        game.possession.opponent.fouls += 1
        if game.possession.opponent.fouls < 7:
            game_runner(game)
        #This is shooting 1-and-1
        elif 7 <= game.possession.opponent.fouls < 10:
            ft_state = flip_card()
            # game.total_time_segments += 1
            if key_player.offense_results.free_throw_shot[1] >= ft_state[3]:
                game.possession.points += 1
                key_player.game_stats.points += 1
                ft_state = flip_card()
                # game.total_time_segments += 1
                if key_player.offense_results.free_throw_shot[1] >= ft_state[3]:
                    game.possession.points += 1
                    key_player.game_stats.points += 1
                    game_runner(game)
                else:
                    rebound_sequence(game, "ft")
            else:
                rebound_sequence(game, "ft")
        #This is the double bonus
        else:
            ft_state = flip_card()
            # game.total_time_segments += 1
            if key_player.offense_results.free_throw_shot[1] >= ft_state[3]:
                game.possession.points += 1
                key_player.game_stats.points += 1
            ft_state = flip_card()
            # game.total_time_segments += 1
            if key_player.offense_results.free_throw_shot[1] >= ft_state[3]:
                game.possession.points += 1
                key_player.game_stats.points += 1
                game_runner(game)
            else:
                rebound_sequence(game, "ft")
    elif k == "miss_range":
        key_player.game_stats.shots += 1
        rebound_sequence(game, "fg")
    elif k == "block_range":
        key_player.game_stats.shots += 1
        opposing_player.game_stats.blocks += 1
        rebound_sequence(game, "fg")
    elif k == "offensive_foul_range":
        game.possession = game.possession.opponent
        key_player.game_stats.fouls += 1
        key_player.game_stats.turnovers += 1
        make_substitutions(game, game.home)
        make_substitutions(game, game.away)
        game_runner(game)
    elif k == "turnover_range":
        game.possession = game.possession.opponent
        key_player.game_stats.turnovers += 1
        game_runner(game)
    elif k == "steal_range":
        game.possession = game.possession.opponent
        opposing_player.game_stats.steals += 1
        key_player.game_stats.turnovers += 1
        game_runner(game)
    else:
        print "Unknown k"

def three_point_sequence(key_player, opposing_player, game, position):
    #print "THREES"
    action_state = flip_card()
    # game.total_time_segments += 1
    if action_state[0] == "off":
        if key_player.offense_results.three_point_shot[1] >= action_state[3]:
            game.possession.points += 3
            key_player.game_stats.shots += 1
            key_player.game_stats.points += 3
            assist_state = flip_card()
            if assist_state[1] == position:
                pass
            elif game.possession.on_court[assist_state[1]].assist_rating >= assist_state[2]:
                game.possession.on_court[assist_state[1]].game_stats.assists += 1
            else:
                pass
            game.possession = game.possession.opponent
            game_runner(game)
        else:
            rebound_sequence(game, "fg")
    else:
        if opposing_player.defense_results.three_point_shot[1] >= action_state[3]:
            game.possession.points += 3
            key_player.game_stats.shots += 1
            key_player.game_stats.points += 3
            assist_state = flip_card()
            if assist_state[1] == position:
                pass
            elif game.possession.on_court[assist_state[1]].assist_rating >= assist_state[2]:
                game.possession.on_court[assist_state[1]].game_stats.assists += 1
            else:
                pass
            game.possession = game.possession.opponent
            game_runner(game)
        else:
            rebound_sequence(game, "fg")

def two_point_sequence(key_player, opposing_player, game, position):
    #print "TWOS"
    action_state = flip_card()
    # game.total_time_segments += 1
    if action_state[0] == "off":
        play_values = key_player.offense_results.plays
        play_key = None
        if action_state[3] == 100:
            game_runner(game)
        else:
            for k in play_values.keys():
                #print play_values[k]
                if play_values[k] != None and play_values[k][0] <= action_state[3] <= play_values[k][1]:
                    play_key = k
            # print play_key
            resolve_play(play_key, key_player, opposing_player, game, position, action_state)
    else:
        play_values = opposing_player.defense_results.plays
        play_key = None
        if action_state[3] == 100:
            game_runner(game)
        else:
            for k in play_values.keys():
                if play_values[k] != None and play_values[k][0] <= action_state[3] <= play_values[k][1]:
                    play_key = k
            # print play_key
            resolve_play(play_key, key_player, opposing_player, game, position, action_state)

def shot_sequence(game):
    #print "SHOTS"
    start_state = flip_card()
    game.total_time_segments += 1
    position = start_state[1]
    start_side = start_state[0]
    if game.possession == game.home:
        key_player = game.home.on_court[position]
        opposing_player = game.away.on_court[position]
    else:
        key_player = game.away.on_court[position]
        opposing_player = game.home.on_court[position]
    # print game.possession.name
    # print key_player.name
    if start_side == "off":
        #If a two-point shot is possible
        if key_player.shot_rating >= start_state[2]:
            two_point_sequence(key_player, opposing_player, game, position)
            game_runner(game)
        #If a three-point shot is possible
        elif key_player.three_point_rating != None and key_player.three_point_rating >= start_state[2]:
            three_point_sequence(key_player, opposing_player, game, position)
            game_runner(game)
        #If neither you just repeat the process
        else:
            game_runner(game)
    else:
        #If a two-point shot is possible
        if opposing_player.shot_rating >= start_state[2]:
            two_point_sequence(key_player, opposing_player, game, position)
            game_runner(game)
        #If a three-point shot is possible
        elif opposing_player.three_point_rating != None and opposing_player.three_point_rating >= start_state[2]:
            three_point_sequence(key_player, opposing_player, game, position)
            game_runner(game)
        #If neither you just repeat the process
        else:
            game_runner(game)

def end_game(game):
    return game

def game_runner(game):
    # print "GAME"
    # print game.total_time_segments
    #Start the game
    if game.total_time_segments == 0:
        print "Starting"
        jump_ball(game)
        game.possession_arrow = game.possession.opponent
        shot_sequence(game)
    #Play the first half
    elif game.total_time_segments < 130:
        shot_sequence(game)
    #This is halftime
    elif game.total_time_segments == 130:
        print "Halftime"
        game.possession = game.possession_arrow
        game.possession_arrow = game.possession.opponent
        shot_sequence(game)
    #This is the second half
    elif game.total_time_segments < 273:
        shot_sequence(game)
    #This is the potential end of the game
    else:
        pass
    return game