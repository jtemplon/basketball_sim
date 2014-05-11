import random
import names
#Note: One thing we're definitely doing is converting X to 100

class PlayerResults():
    plays = {}
    three_point_shot = (0, 0)
    def __init__(self, side):
        if side == "o":
            self.free_throw_shot = (0, 0)
        else:
            self.free_throw_shot = None

class GameStats():
    fouls = 0
    shots = 0
    points = 0
    turnovers = 0
    steals = 0
    blocks = 0
    assists = 0
    oreb = 0
    reb = 0

class Player():
    name = ""
    team = None
    primary_position = ""
    secondary_position = None
    shot_rating = 0
    shot_extra_flip = False
    three_point_rating = 0
    shots_per_game = 0
    defensive_rebound_rating = 0
    dominant_defensive_rebound_rating = (0, 0)
    offensive_rebound_rating = 0
    dominant_offensive_rebound_rating = (0, 0)
    assist_rating = 0
    offense_results = PlayerResults("o")
    defense_results = PlayerResults("d")
    def __init__(self):
        self.game_stats = GameStats()

class Team():
    def __init__(self):
        self.on_court = {"pg": None, "sg": None, "sf": None,
                         "pf": None, "c": None}
        self.name = ""
        self.roster = []
        self.points = 0
        self.fouls = 0

class Game():
    home = Team()
    away = Team()
    total_time_segments = 0
    total_overtime_segments = 0
    allowed_first_half_time_segments = 130
    allowed_second_half_time_segments = 143
    allowed_overtime_segments = 45
    player_ranges = {"pg": (1, 15),
                          "sg": (16, 30),
                          "c": (31, 45),
                          "sf": (46, 60),
                          "pf": (61, 75),
                          "defender": (76, 100)}
    technical_fouls = {"coach": (1, 75),
                            "player": (76, 95),
                            "bench": (96, 99),
                            "trainer": 100}
    rebound_count = 0

#This is the main element of game play
def flip_card():
    side_num = random.randint(1,2)
    if side_num == 1:
        side = "off"
    else:
        side = "def"
    position_dict = {1: "pg", 2: "sg", 3: "sf", 4: "pf", 5: "c"}
    position = position_dict[random.randint(1,5)]
    action = random.randint(1,20)
    action_type = random.randint(1,100)
    return side, position, action, action_type

def make_random_results(player, o_or_d):
    if o_or_d == "o":
        break_points = []
        i = 0
        while i < 8:
            bk = random.randint(0,99)
            break_points.append(bk)
            i += 1
        print break_points
        break_points = sorted(break_points)
        player.offense_results.plays["fg_foul_range"] = (1, break_points[0])
        player.offense_results.plays["fg_range"] = (break_points[0]+1, break_points[1])
        player.offense_results.plays["assist_range"] = (break_points[1]+1, break_points[2])
        player.offense_results.plays["foul_range"] = (break_points[2]+1, break_points[3])
        player.offense_results.plays["miss_range"] = (break_points[3]+1, break_points[4])
        player.offense_results.plays["block_range"] = (break_points[4]+1, break_points[5])
        player.offense_results.plays["offensive_foul_range"] = (break_points[5]+1, break_points[6])
        player.offense_results.plays["turnover_range"] = (break_points[6]+1, break_points[7])
        player.offense_results.plays["steal_range"] = (break_points[7]+1, 99)
        three_point_max = random.randint(1,40)
        ft_pct = random.randint(30,90)
        player.offense_results.three_point_shot = (1, three_point_max)
        player.offense_results.free_throw_shot = (1, ft_pct)
    else:
        break_points = []
        i = 0
        while i < 5:
            bk = random.randint(0,99)
            break_points.append(bk)
            i += 1
        break_points = sorted(break_points)
        player.defense_results.plays["fg_foul_range"] = None
        player.defense_results.plays["fg_range"] = (1, break_points[0])
        player.defense_results.plays["assist_range"] = None
        player.defense_results.plays["foul_range"] = (break_points[0]+1, break_points[1])
        player.defense_results.plays["miss_range"] = (break_points[1]+1, break_points[2])
        player.defense_results.plays["block_range"] = (break_points[2]+1, break_points[3])
        player.defense_results.plays["offensive_foul_range"] = None
        player.defense_results.plays["turnover_range"] = (break_points[3]+1, break_points[4])
        player.defense_results.plays["steal_range"] = (break_points[4]+1, 99)
        three_point_max = random.randint(1,40)
        player.defense_results.three_point_shot = (1, three_point_max)

def make_random_players():
    roster = []
    i = 0
    position_dict = {1: "g", 2: "f", 3: "c"}
    while i < 13:
        player = Player()
        player.name = names.get_full_name(gender='male')
        position_num = random.randint(1,3)
        player.primary_position = position_dict[position_num]
        position_random = random.randint(1,100)
        if position_random < 15 and position_num != 1:
            position_num -= 1
            player.secondary_position = position_dict[position_num]
        elif position_random > 85 and position_num != 3:
            position_num += 1
            player.secondary_position = position_dict[position_num]
        else:
            pass
        player.power_rating = random.randint(1,10)
        shot_random = random.randint(1,20)
        if player.primary_position in ["pg", "sg", "sf"]:
            three_random = random.randint(0,10)
            if (shot_random + three_random) > 23:
                player.three_point_rating = 23
            else:
                player.three_point_rating = shot_random + three_random
        else:
            player.three_point_rating = None
        player.shot_rating = shot_random
        if shot_random % 3 == 0:
            player.shot_extra_flip = True
        else:
            player.shot_extra_flip = False
        player.shots_per_game = random.randint(1,25)
        if player.shots_per_game > 20:
            player.call_for_ball_times = player.shots_per_game - 20
        else:
            player.call_for_ball_times = 0
        player.defensive_rebound_rating = random.randint(1,20)
        if player.defensive_rebound_rating > 15 and random.randint(1,5) > 3:
            player.dominant_defensive_rebound_rating = (15, player.defensive_rebound_rating)
        else:
            player.dominant_defensive_rebound_rating = (0, 0)
        player.offensive_rebound_rating = round(random.normalvariate(9, 4))
        if player.offensive_rebound_rating < 1:
            player.offensive_rebound_rating = 1
        if player.offensive_rebound_rating > 15 and random.randint(1,5) == 5:
            player.dominant_offensive_rebound_rating = (15, player.offensive_rebound_rating)
        else:
            player.dominant_offensive_rebound_rating = (0, 0)
        player.assist_rating = random.randint(1,25)
        make_random_results(player, "o")
        make_random_results(player, "d")
        roster.append(player)
        i += 1
    return roster