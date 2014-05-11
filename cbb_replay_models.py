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
        # print "Offensive Ratings"
        total_points = []
        total_points.append(random.randint(1,16))
        total_points.append(round(random.normalvariate(14, 3)))
        total_points.append(round(random.normalvariate(12, 4)))
        total_points.append(round(random.normalvariate(14, 3)))
        total_points.append(round(random.normalvariate(23, 15)))
        total_points.append(round(random.normalvariate(9, 5)))
        total_points.append(random.randint(0,6))
        total_points.append(random.randint(0,10))
        for tp in total_points:
            if tp < 0:
                tp = 0
        # print total_points
        break_points = []
        total = 1
        if sum(total_points) != 98:
            scale = 98/float(sum(total_points))
            for tp in total_points:
                tp = int(tp*scale)
                total += tp
                break_points.append(total)            
        else:
            for tp in total_points:
                total += tp
                break_points.append(total)
        # print break_points
        player.offense_results.plays["fg_foul_range"] = (1, break_points[0])
        player.offense_results.plays["fg_range"] = (break_points[0]+1, break_points[1])
        player.offense_results.plays["assist_range"] = (break_points[1]+1, break_points[2])
        player.offense_results.plays["foul_range"] = (break_points[2]+1, break_points[3])
        player.offense_results.plays["miss_range"] = (break_points[3]+1, break_points[4])
        player.offense_results.plays["block_range"] = None
        player.offense_results.plays["offensive_foul_range"] = (break_points[4]+1, break_points[5])
        player.offense_results.plays["turnover_range"] = (break_points[5]+1, break_points[6])
        player.offense_results.plays["steal_range"] = (break_points[6]+1, 99)
        if player.three_point_rating is None:
            player.offense_results.three_point_shot = (1, 3)
        else:
            three_point_rating = round(random.normalvariate(0.33, 0.05)*100)+3
            player.offense_results.three_point_shot = (1, three_point_rating)
        ft_pct = round(random.normalvariate(0.64, 0.08)*100)
        player.offense_results.free_throw_shot = (1, ft_pct)
        # print player.offense_results.plays
    else:
        # print "Defensive ratings"
        total_points = []
        total_points.append(round(random.normalvariate(24, 3)))
        total_points.append(round(random.normalvariate(25, 5)))
        block_range = random.randint(0,30)
        if block_range > 25:
            miss_range = 0
        else:
            miss_range = round(random.normalvariate(24, 4))
        total_points.append(miss_range)
        total_points.append(block_range)
        steal_range = random.randint(0,25)
        if steal_range > 20:
            to_range = 0
        elif steal_range > 15:
            to_range = random.randint(1,10)
        else:
            to_range = round(random.normalvariate(15, 2))
        total_points.append(to_range)
        total_points.append(steal_range)
        for tp in total_points:
            if tp < 0:
                tp = 0
        # print total_points
        break_points = []
        total = 1
        if sum(total_points) != 98:
            scale = 98/float(sum(total_points))
            for tp in total_points:
                tp = int(tp*scale)
                total += tp
                break_points.append(total)            
        else:
            for tp in total_points:
                total += tp
                break_points.append(total)
        # print break_points
        player.defense_results.plays["fg_foul_range"] = None
        player.defense_results.plays["fg_range"] = (1, break_points[0])
        player.defense_results.plays["assist_range"] = None
        player.defense_results.plays["foul_range"] = (break_points[0]+1, break_points[1])
        player.defense_results.plays["miss_range"] = (break_points[1]+1, break_points[2])
        player.defense_results.plays["block_range"] = (break_points[2]+1, break_points[3])
        player.defense_results.plays["offensive_foul_range"] = None
        player.defense_results.plays["turnover_range"] = (break_points[3]+1, break_points[4])
        player.defense_results.plays["steal_range"] = (break_points[4]+1, 99)
        three_point_max = round(random.normalvariate(24, 3))
        player.defense_results.three_point_shot = (1, three_point_max)
        # print player.defense_results.plays

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
        #Guards shoot more threes
        if player.primary_position is "g":
            top_shot_rating = round(random.normalvariate(20, 5)*0.60)
            shot_rating_diff = round(random.normalvariate(3, 4))
            if shot_rating_diff > (top_shot_rating/float(0.75)):
                shot_rating_diff = round(top_shot_rating/float(0.75))
            if shot_rating_diff == 0:
                player.three_point_rating = None
                player.two_point_rating = top_shot_rating
            else:
                player.three_point_rating = top_shot_rating
                player.two_point_rating = (top_shot_rating - shot_rating_diff)
        #Made to reflect current forward trends (at least tried to)
        elif player.primary_position is "f":
            top_shot_rating = round(random.normalvariate(20, 5)*0.60)
            shot_rating_diff = round(random.normalvariate(2, 1))
            if shot_rating_diff > (top_shot_rating/float(0.75)):
                shot_rating_diff = round(top_shot_rating/float(0.75))
            if shot_rating_diff == 0:
                player.three_point_rating = None
                player.two_point_rating = top_shot_rating
            else:
                player.three_point_rating = top_shot_rating
                player.two_point_rating = (top_shot_rating - shot_rating_diff)            
        #Centers don't shoot threes, unless they're at Princeton, we ignore that case
        else:
            top_shot_rating = round(random.normalvariate(22, 7)*0.60)
            player.three_point_rating = None
            player.two_point_rating = top_shot_rating
        player.shots_per_game = random.randint(1,25)
        if player.shots_per_game > 20:
            player.call_for_ball_times = player.shots_per_game - 20
        else:
            player.call_for_ball_times = 0
        defensive_rebound_num = round(random.normalvariate(12, 5))
        if defensive_rebound_num > 20:
            player.defensive_rebound_rating = 20
            dom_def_reb_num = 20 - (defensive_rebound_num - 20)
            player.dominant_defensive_rebound_Rating = (dom_def_reb_num, 20)
        else:
            player.defensive_rebound_rating = defensive_rebound_num
        offensive_rebound_num = round(random.normalvariate(10, 3))
        if offensive_rebound_num > 20:
            player.offensive_rebound_rating = 20
            dom_off_reb_num = 20 - (offensive_rebound_num - 20)
            player.dominant_offensive_rebound_Rating = (dom_off_reb_num, 20)
        else:
            player.offensive_rebound_rating = offensive_rebound_num
        assist_num = 7 + random.randint(1,10) + random.randint(0,5)*5
        player.assist_rating = round(assist_num*1.2)
        make_random_results(player, "o")
        make_random_results(player, "d")
        roster.append(player)
        i += 1
    return roster