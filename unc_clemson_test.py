from cbb_replay_models import *
from cbb_replay_game import *

game = Game()
game.home = Team()
game.away = Team()
game.teams = [game.home, game.away]
game.home.name = "North Carolina"
game.home.opponent = game.away
game.away.name = "Clemson"
game.away.opponent = game.home
#Make Rosters
game.home.roster = []
game.away.roster = []
hansbrough = Player()
hansbrough.name = "Hansbrough"
hansbrough.primary_position = "c"
hansbrough.shot_rating = 17
hansbrough.shot_extra_flip = True
hansbrough.three_point_rating = None
hansbrough.shots_per_game = 12
hansbrough.defensive_rebound_rating = 20
hansbrough.dominant_defensive_rebound_rating = (20, 20)
hansbrough.offensive_rebound_rating = 13
hansbrough.assist_rating = 8
hansbrough.offense_results.plays = {"fg_foul_range": (1, 20), "fg_range": None, "assist_range": (21, 26),
                                    "foul_range": (27, 67), "miss_range": (68, 86), "block_range": None,
                                    "offensive_foul_range": (87, 90), "turnover_range": (91, 93), 
                                    "steal_range": (94, 99)}
hansbrough.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 25), "assist_range": None,
                                    "foul_range": (26, 39), "miss_range": (40, 67), "block_range": (68, 78),
                                    "offensive_foul_range": None, "turnover_range": (79, 88), 
                                    "steal_range": (89, 99)}
hansbrough.offense_results.three_point_shot = (1, 3)
hansbrough.offense_results.free_throw_shot = (1, 76)
hansbrough.defense_results.three_point_shot = (1, 31)
game.home.roster.append(hansbrough)

green = Player()
green.name = "Green"
green.primary_position = "f"
green.shot_rating = 7
green.shot_extra_flip = True
green.three_point_rating = 12
green.shots_per_game = 5
green.defensive_rebound_rating = 16
green.dominant_defensive_rebound_rating = (0,0)
green.offensive_rebound_rating = 7
green.assist_rating = 18
green.offense_results.plays = {"fg_foul_range": (1, 9), "fg_range": (10,26), "assist_range": (27,35),
                                    "foul_range": (36, 53), "miss_range": (54, 80), "block_range": None,
                                    "offensive_foul_range": (81, 90), "turnover_range": None,
                                    "steal_range": (92, 99)}
green.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 24), "assist_range": None,
                                    "foul_range": (25, 46), "miss_range": (47, 49), "block_range": (50, 80),
                                    "offensive_foul_range": None, "turnover_range": (81, 83), 
                                    "steal_range": (84, 99)}
green.offense_results.three_point_shot = (1, 24)
green.offense_results.free_throw_shot = (1, 84)
green.defense_results.three_point_shot = (1, 33)
game.home.roster.append(green)

lawson = Player()
lawson.name = "Lawson"
lawson.primary_position = "g"
lawson.shot_rating = 10
lawson.shot_extra_flip = False
lawson.three_point_rating = 13
lawson.shots_per_game = 8
lawson.defensive_rebound_rating = 9
lawson.dominant_defensive_rebound_rating = (0,0)
lawson.offensive_rebound_rating = 3
lawson.assist_rating = 46
lawson.offense_results.plays = {"fg_foul_range": (1, 10), "fg_range": (11,26), "assist_range": (27,38),
                                    "foul_range": (39, 59), "miss_range": (60, 81), "block_range": None,
                                    "offensive_foul_range": (82, 87), "turnover_range": None,
                                    "steal_range": (88, 99)}
lawson.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 24), "assist_range": None,
                                    "foul_range": (25, 43), "miss_range": (44, 76), "block_range": (77, 79),
                                    "offensive_foul_range": None, "turnover_range": None, 
                                    "steal_range": (80, 99)}
lawson.offense_results.three_point_shot = (1, 36)
lawson.offense_results.free_throw_shot = (1, 68)
lawson.defense_results.three_point_shot = (1, 31)
game.home.roster.append(lawson)

wright = Player()
wright.name = "Wright"
wright.primary_position = "f"
wright.shot_rating = 13
wright.shot_extra_flip = False
wright.three_point_rating = None
wright.shots_per_game = 10
wright.defensive_rebound_rating = 18
wright.dominant_defensive_rebound_rating = (0,0)
wright.offensive_rebound_rating = 9
wright.assist_rating = 8
wright.offense_results.plays = {"fg_foul_range": (1, 11), "fg_range": (12,35), "assist_range": (36,47),
                                    "foul_range": (48, 70), "miss_range": (71, 82), "block_range": None,
                                    "offensive_foul_range": (83, 83), "turnover_range": (84,92),
                                    "steal_range": (93, 99)}
wright.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 30), "assist_range": None,
                                    "foul_range": (31, 33), "miss_range": None, "block_range": (34, 78),
                                    "offensive_foul_range": None, "turnover_range": (79,89), 
                                    "steal_range": (90, 99)}
wright.offense_results.three_point_shot = (1, 3)
wright.offense_results.free_throw_shot = (1, 56)
wright.defense_results.three_point_shot = (1, 31)
game.home.roster.append(wright)

ellington = Player()
ellington.name = "Ellington"
ellington.primary_position = "g"
ellington.shot_rating = 9
ellington.shot_extra_flip = True
ellington.three_point_rating = 15
ellington.shots_per_game = 10
ellington.defensive_rebound_rating = 10
ellington.dominant_defensive_rebound_rating = (0,0)
ellington.offensive_rebound_rating = 3
ellington.assist_rating = 18
ellington.offense_results.plays = {"fg_foul_range": (1, 3), "fg_range": (4,21), "assist_range": (22,35),
                                    "foul_range": (36, 40), "miss_range": (41, 78), "block_range": None,
                                    "offensive_foul_range": (79, 79), "turnover_range": (80,93),
                                    "steal_range": (94, 99)}
ellington.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 29), "assist_range": None,
                                    "foul_range": (30, 33), "miss_range": (34, 74), "block_range": (75,75),
                                    "offensive_foul_range": None, "turnover_range": (76,90), 
                                    "steal_range": (91, 99)}
ellington.offense_results.three_point_shot = (1, 39)
ellington.offense_results.free_throw_shot = (1, 83)
ellington.defense_results.three_point_shot = (1, 32)
game.home.roster.append(ellington)

frasor = Player()
frasor.name = "Frasor"
frasor.primary_position = "g"
frasor.shot_rating = 5
frasor.shot_extra_flip = False
frasor.three_point_rating = 9
frasor.shots_per_game = 2
frasor.defensive_rebound_rating = 6
frasor.dominant_defensive_rebound_rating = (0,0)
frasor.offensive_rebound_rating = 1
frasor.assist_rating = 34
frasor.offense_results.plays = {"fg_foul_range": (1, 2), "fg_range": (3,20), "assist_range": (21,31),
                                    "foul_range": (32, 34), "miss_range": (35, 77), "block_range": None,
                                    "offensive_foul_range": (78, 84), "turnover_range": (85,85),
                                    "steal_range": (86, 99)}
frasor.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 28), "assist_range": None,
                                    "foul_range": (29, 41), "miss_range": (42, 78), "block_range": None,
                                    "offensive_foul_range": None, "turnover_range": None, 
                                    "steal_range": (79, 99)}
frasor.offense_results.three_point_shot = (1, 39)
frasor.offense_results.free_throw_shot = (1, 37)
frasor.defense_results.three_point_shot = (1, 35)
game.home.roster.append(frasor)

thompson = Player()
thompson.name = "Thompson"
thompson.primary_position = "f"
thompson.shot_rating = 10
thompson.shot_extra_flip = False
thompson.three_point_rating = None
thompson.shots_per_game = 4
thompson.defensive_rebound_rating = 16
thompson.dominant_defensive_rebound_rating = (0,0)
thompson.offensive_rebound_rating = 12
thompson.assist_rating = 7
thompson.offense_results.plays = {"fg_foul_range": (1, 2), "fg_range": (3,30), "assist_range": (31,45),
                                    "foul_range": (46, 49), "miss_range": (50, 77), "block_range": None,
                                    "offensive_foul_range": (78, 90), "turnover_range": None,
                                    "steal_range": (91, 99)}
thompson.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 21), "assist_range": None,
                                    "foul_range": (22, 53), "miss_range": (54, 63), "block_range": (64,82),
                                    "offensive_foul_range": None, "turnover_range": (83,90), 
                                    "steal_range": (91, 99)}
thompson.offense_results.three_point_shot = (1, 3)
thompson.offense_results.free_throw_shot = (1, 64)
thompson.defense_results.three_point_shot = (1, 34)
game.home.roster.append(thompson)

terry = Player()
terry.name = "Terry"
terry.primary_position = "c"
terry.shot_rating = 9
terry.shot_extra_flip = True
terry.three_point_rating = 13
terry.shots_per_game = 7
terry.defensive_rebound_rating = 20
terry.dominant_defensive_rebound_rating = (0,0)
terry.offensive_rebound_rating = 6
terry.assist_rating = 16
terry.offense_results.plays = {"fg_foul_range": (1, 10), "fg_range": (11,24), "assist_range": (25,34),
                                    "foul_range": (35, 54), "miss_range": (55, 81), "block_range": None,
                                    "offensive_foul_range": (82, 88), "turnover_range": None,
                                    "steal_range": (89, 99)}
terry.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 23), "assist_range": None,
                                    "foul_range": (24, 45), "miss_range": (46, 62), "block_range": (63,80),
                                    "offensive_foul_range": None, "turnover_range": (81,91), 
                                    "steal_range": (92, 99)}
terry.offense_results.three_point_shot = (1, 53)
terry.offense_results.free_throw_shot = (1, 73)
terry.defense_results.three_point_shot = (1, 32)
game.home.roster.append(terry)

ginyard = Player()
ginyard.name = "Ginyard"
ginyard.primary_position = "g"
ginyard.secondary_position = "f"
ginyard.shot_rating = 6
ginyard.shot_extra_flip = True
ginyard.three_point_rating = 7
ginyard.shots_per_game = 3
ginyard.defensive_rebound_rating = 15
ginyard.dominant_defensive_rebound_rating = (0,0)
ginyard.offensive_rebound_rating = 13
ginyard.assist_rating = 19
ginyard.offense_results.plays = {"fg_foul_range": (1, 8), "fg_range": (9,23), "assist_range": (24,32),
                                    "foul_range": (33, 47), "miss_range": (48, 79), "block_range": None,
                                    "offensive_foul_range": (80, 87), "turnover_range": (88,89),
                                    "steal_range": (90, 99)}
ginyard.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 26), "assist_range": None,
                                    "foul_range": (27, 41), "miss_range": (42, 73), "block_range": (74,78),
                                    "offensive_foul_range": None, "turnover_range": None, 
                                    "steal_range": (79, 99)}
ginyard.offense_results.three_point_shot = (1, 20)
ginyard.offense_results.free_throw_shot = (1, 78)
ginyard.defense_results.three_point_shot = (1, 32)
game.home.roster.append(ginyard)

hamilton = Player()
hamilton.name = "Hamilton"
hamilton.primary_position = "g"
hamilton.shot_rating = 10
hamilton.shot_extra_flip = False
hamilton.three_point_rating = 13
hamilton.shots_per_game = 11
hamilton.defensive_rebound_rating = 8
hamilton.dominant_defensive_rebound_rating = (0,0)
hamilton.offensive_rebound_rating = 2
hamilton.assist_rating = 25
hamilton.offense_results.plays = {"fg_foul_range": (1,7), "fg_range": (8,27), "assist_range": (28,37),
                                    "foul_range": (38,51), "miss_range": (52,76), "block_range": None,
                                    "offensive_foul_range": (77,78), "turnover_range": (79,85),
                                    "steal_range": (86,99)}
hamilton.defense_results.plays = {"fg_foul_range": None, "fg_range": (1,33), "assist_range": None,
                                    "foul_range": (34,38), "miss_range": (39,75), "block_range": (76,77),
                                    "offensive_foul_range": None, "turnover_range": None, 
                                    "steal_range": (78, 99)}
hamilton.offense_results.three_point_shot = (1, 27)
hamilton.offense_results.free_throw_shot = (1, 48)
hamilton.defense_results.three_point_shot = (1, 33)
game.away.roster.append(hamilton)

hammonds = Player()
hammonds.name = "Hammonds"
hammonds.primary_position = "g"
hammonds.shot_rating = 5
hammonds.shot_extra_flip = False
hammonds.three_point_rating = 10
hammonds.shots_per_game = 9
hammonds.defensive_rebound_rating = 8
hammonds.dominant_defensive_rebound_rating = (0,0)
hammonds.offensive_rebound_rating = 2
hammonds.assist_rating = 29
hammonds.offense_results.plays = {"fg_foul_range": (1,5), "fg_range": (6,31), "assist_range": (32,46),
                                    "foul_range": (47,56), "miss_range": (57,75), "block_range": None,
                                    "offensive_foul_range": (76,79), "turnover_range": (80,94),
                                    "steal_range": (95,99)}
hammonds.defense_results.plays = {"fg_foul_range": None, "fg_range": (1,32), "assist_range": None,
                                    "foul_range": (33,41), "miss_range": (42,74), "block_range": (75,78),
                                    "offensive_foul_range": None, "turnover_range": (79,80), 
                                    "steal_range": (81, 99)}
hammonds.offense_results.three_point_shot = (1, 41)
hammonds.offense_results.free_throw_shot = (1, 63)
hammonds.defense_results.three_point_shot = (1, 32)
game.away.roster.append(hammonds)

rivers = Player()
rivers.name = "Rivers"
rivers.primary_position = "g"
rivers.shot_rating = 6
rivers.shot_extra_flip = False
rivers.three_point_rating = 12
rivers.shots_per_game = 11
rivers.defensive_rebound_rating = 12
rivers.dominant_defensive_rebound_rating = (0,0)
rivers.offensive_rebound_rating = 7
rivers.assist_rating = 15
rivers.offense_results.plays = {"fg_foul_range": (1,6), "fg_range": (7,25), "assist_range": (26,39),
                                    "foul_range": (40,50), "miss_range": (51,75), "block_range": None,
                                    "offensive_foul_range": (76,82), "turnover_range": (83,97),
                                    "steal_range": (98,99)}
rivers.defense_results.plays = {"fg_foul_range": None, "fg_range": (1,30), "assist_range": None,
                                    "foul_range": (31,44), "miss_range": (45,76), "block_range": (77,79),
                                    "offensive_foul_range": None, "turnover_range": (80,85), 
                                    "steal_range": (86, 99)}
rivers.offense_results.three_point_shot = (1, 45)
rivers.offense_results.free_throw_shot = (1, 73)
rivers.defense_results.three_point_shot = (1, 33)
game.away.roster.append(rivers)

mays = Player()
mays.name = "Mays"
mays.primary_position = "f"
mays.secondary_position = "c"
mays.shot_rating = 13
mays.shot_extra_flip = False
mays.three_point_rating = 14
mays.shots_per_game = 10
mays.defensive_rebound_rating = 18
mays.dominant_defensive_rebound_rating = (0,0)
mays.offensive_rebound_rating = 13
mays.assist_rating = 23
mays.offense_results.plays = {"fg_foul_range": (1,13), "fg_range": (14,19), "assist_range": (20,26),
                                    "foul_range": (27,54), "miss_range": (55,80), "block_range": None,
                                    "offensive_foul_range": (81,85), "turnover_range": None,
                                    "steal_range": (86,99)}
mays.defense_results.plays = {"fg_foul_range": None, "fg_range": (1,29), "assist_range": None,
                                    "foul_range": (30,46), "miss_range": (47,57), "block_range": (58,80),
                                    "offensive_foul_range": None, "turnover_range": None, 
                                    "steal_range": (81, 99)}
mays.offense_results.three_point_shot = (1, 11)
mays.offense_results.free_throw_shot = (1, 54)
mays.defense_results.three_point_shot = (1, 33)
game.away.roster.append(mays)

booker = Player()
booker.name = "Booker"
booker.primary_position = "f"
booker.secondary_position = "c"
booker.shot_rating = 9
booker.shot_extra_flip = False
booker.three_point_rating = None
booker.shots_per_game = 8
booker.defensive_rebound_rating = 20
booker.dominant_defensive_rebound_rating = (0,0)
booker.offensive_rebound_rating = 19
booker.assist_rating = 10
booker.offense_results.plays = {"fg_foul_range": (1,7), "fg_range": (8,29), "assist_range": (30,44),
                                    "foul_range": (45,58), "miss_range": (59,76), "block_range": None,
                                    "offensive_foul_range": (77,88), "turnover_range": None,
                                    "steal_range": (89,99)}
booker.defense_results.plays = {"fg_foul_range": None, "fg_range": (1,30), "assist_range": None,
                                    "foul_range": (31,50), "miss_range": None, "block_range": (51,84),
                                    "offensive_foul_range": None, "turnover_range": (85,92), 
                                    "steal_range": (93,99)}
booker.offense_results.three_point_shot = (1, 3)
booker.offense_results.free_throw_shot = (1, 61)
booker.defense_results.three_point_shot = (1, 33)
game.away.roster.append(booker)

perry = Player()
perry.name = "Perry"
perry.primary_position = "f"
perry.shot_rating = 8
perry.shot_extra_flip = False
perry.three_point_rating = 9
perry.shots_per_game = 4
perry.defensive_rebound_rating = 14
perry.dominant_defensive_rebound_rating = (0,0)
perry.offensive_rebound_rating = 10
perry.assist_rating = 15
perry.offense_results.plays = {"fg_foul_range": (1,9), "fg_range": (10,18), "assist_range": (19,23),
                                    "foul_range": (24,41), "miss_range": (42,77), "block_range": None,
                                    "offensive_foul_range": (78,89), "turnover_range": None,
                                    "steal_range": (90,99)}
perry.defense_results.plays = {"fg_foul_range": None, "fg_range": (1,26), "assist_range": None,
                                    "foul_range": (27,54), "miss_range": (55,66), "block_range": (67,83),
                                    "offensive_foul_range": None, "turnover_range": None,
                                    "steal_range": (84,99)}
perry.offense_results.three_point_shot = (1, 32)
perry.offense_results.free_throw_shot = (1, 47)
perry.defense_results.three_point_shot = (1, 34)
game.away.roster.append(perry)

powell = Player()
powell.name = "Powell"
powell.primary_position = "f"
powell.shot_rating = 4
powell.shot_extra_flip = False
powell.three_point_rating = 10
powell.shots_per_game = 3
powell.defensive_rebound_rating = 10
powell.dominant_defensive_rebound_rating = (0,0)
powell.offensive_rebound_rating = 6
powell.assist_rating = 8
powell.offense_results.plays = {"fg_foul_range": (1,6), "fg_range": (7,13), "assist_range": (14,18),
                                    "foul_range": (19,30), "miss_range": (31,75), "block_range": None,
                                    "offensive_foul_range": (76,85), "turnover_range": None,
                                    "steal_range": (94,99)}
powell.defense_results.plays = {"fg_foul_range": None, "fg_range": (1,29), "assist_range": None,
                                    "foul_range": (30,50), "miss_range": (51,69), "block_range": (70,80),
                                    "offensive_foul_range": None, "turnover_range": (81,94),
                                    "steal_range": (95,99)}
powell.offense_results.three_point_shot = (1, 14)
powell.offense_results.free_throw_shot = (1, 56)
powell.defense_results.three_point_shot = (1, 36)
game.away.roster.append(powell)

potter = Player()
potter.name = "Potter"
potter.primary_position = "g"
potter.secondary_position = "f"
potter.shot_rating = 8
potter.shot_extra_flip = False
potter.three_point_rating = 12
potter.shots_per_game = 3
potter.defensive_rebound_rating = 11
potter.dominant_defensive_rebound_rating = (0,0)
potter.offensive_rebound_rating = 6
potter.assist_rating = 17
potter.offense_results.plays = {"fg_foul_range": (1,5), "fg_range": (6,16), "assist_range": (17,23),
                                    "foul_range": (24,33), "miss_range": (34,75), "block_range": None,
                                    "offensive_foul_range": (76,89), "turnover_range": None,
                                    "steal_range": (90,99)}
potter.defense_results.plays = {"fg_foul_range": None, "fg_range": (1,25), "assist_range": None,
                                    "foul_range": (26,60), "miss_range": (61,75), "block_range": (76,84),
                                    "offensive_foul_range": None, "turnover_range": (85,95),
                                    "steal_range": (96,99)}
potter.offense_results.three_point_shot = (1, 3)
potter.offense_results.free_throw_shot = (1, 60)
potter.defense_results.three_point_shot = (1, 37)
game.away.roster.append(potter)

sykes = Player()
sykes.name = "Skyes"
sykes.primary_position = "f"
sykes.secondary_position = "c"
sykes.shot_rating = 5
sykes.shot_extra_flip = True
sykes.three_point_rating = None
sykes.shots_per_game = 2
sykes.defensive_rebound_rating = 14
sykes.dominant_defensive_rebound_rating = (0,0)
sykes.offensive_rebound_rating = 13
sykes.assist_rating = 7
sykes.offense_results.plays = {"fg_foul_range": (1,7), "fg_range": (8,30), "assist_range": (31,45),
                                    "foul_range": (46,59), "miss_range": (60,77), "block_range": None,
                                    "offensive_foul_range": (78,94), "turnover_range": (95,95),
                                    "steal_range": (96,99)}
sykes.defense_results.plays = {"fg_foul_range": None, "fg_range": (1,30), "assist_range": None,
                                    "foul_range": (31,55), "miss_range": None, "block_range": (56,86),
                                    "offensive_foul_range": None, "turnover_range": (87,96),
                                    "steal_range": (97,99)}
sykes.offense_results.three_point_shot = (1, 3)
sykes.offense_results.free_throw_shot = (1, 51)
sykes.defense_results.three_point_shot = (1, 36)
game.away.roster.append(sykes)

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
for p in game.home.roster:
    print p.name, p.game_stats.points, p.game_stats.reb, p.game_stats.assists, p.game_stats.fouls
for p in game.away.roster:
    print p.name, p.game_stats.points, p.game_stats.reb, p.game_stats.assists, p.game_stats.fouls