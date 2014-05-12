from cbb_replay_models import *
import random
import names

class StarPointGuard(Player):
    #This is a star PG think Ty Lawson, Dominic James, etc.
    def __init__(self):
        self.name = names.get_full_name(gender='male')
        self.primary_position = "g"
        self.shot_rating = random.randint(9,13)
        self.three_point_rating = self.shot_rating + random.randint(2,5)
        self.shots_per_game = random.randint(7,13)
        self.defensive_rebound_rating = random.randint(7,11)
        self.offensive_rebound_rating = random.randint(1,4)
        self.assist_rating = int(round(random.normalvariate(41, 3)))
        self.offense_results.three_point_shot = (1, (28+random.randint(0,14)))
        self.offense_results.free_throw_shot = (1, random.randint(65,86))
        self.defense_results.three_point_shot = (1, random.randint(25,33))
        fgf_o_tweak = random.randint(0,8)
        fg_o_range = random.randint(7,15)
        fg_o_end = 10 + fgf_o_tweak + fg_o_range
        assist_range = random.randint(5,11)
        assist_end = fg_o_end + 1 + assist_range
        to_range = random.randint(0,2)
        o_foul_range = random.randint(0,5)
        steal_range = random.randint(8,19)
        steal_start = 99 - steal_range
        to_start = steal_start - 1 - to_range
        o_foul_start = to_start - 1 - o_foul_range
        miss_range = random.randint(16,34)
        miss_start = o_foul_start - 1 - miss_range
        if (miss_start-1) < (assist_end+1):
            miss_start = assist_end+2
        self.offense_results.plays = {"fg_foul_range": (1, 9+fgf_o_tweak), "fg_range": (10+fgf_o_tweak, fg_o_end), 
                                      "assist_range": (fg_o_end+1, assist_end), "foul_range": (assist_end+1, miss_start-1), 
                                      "miss_range": (miss_start, o_foul_start-1), "block_range": None, 
                                      "offensive_foul_range": (o_foul_start, to_start-1), "turnover_range": (to_start, steal_start-1), 
                                      "steal_range": (steal_start, 99)}
        fg_d_tweak = random.randint(0,9)
        foul_d_tweak = int(round(random.normalvariate(10, 2)))
        miss_d_range = random.randint(32,38)
        miss_d_start = fg_d_tweak + foul_d_tweak + 26
        miss_d_end = miss_d_start + miss_d_range
        block_range = random.randint(0,4)
        block_end = miss_d_end + 1 + block_range
        to_d_range = random.randint(0,11)
        to_d_end = block_end + 1 + to_d_range
        self.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 24+fg_d_tweak), "assist_range": None,
                                      "foul_range": (25+fg_d_tweak, 25+fg_d_tweak+foul_d_tweak), "miss_range": (miss_d_start, miss_d_end), 
                                      "block_range": (miss_d_end+1, block_end), "offensive_foul_range": None, 
                                      "turnover_range": (block_end+1, to_d_end), "steal_range": (to_d_end+1, 99)}
        self.game_stats = GameStats()

class StarShootingGuard(Player):
    #Stephen Curry is the elite of this group, think Wayne Ellington at UNC
    def __init__(self):
        self.name = names.get_full_name(gender='male')
        self.primary_position = "g"
        second_position_check = random.randint(1,10)
        if second_position_check > 8:
            self.secondary_position = "f"
        else:
            self.secondary_position = None
        self.shot_rating = random.randint(9,13)
        self.three_point_rating = self.shot_rating + random.randint(2,9)
        self.shots_per_game = random.randint(9,17)
        self.defensive_rebound_rating = random.randint(6,11)
        self.offensive_rebound_rating = random.randint(1,3)
        self.assist_rating = int(round(random.normalvariate(18, 3)))
        self.offense_results.three_point_shot = (1, (38+random.randint(0,14)))
        self.offense_results.free_throw_shot = (1, random.randint(72,90))
        self.defense_results.three_point_shot = (1, random.randint(29,33))
        fgf_o_tweak = random.randint(2,6)
        fg_o_range = random.randint(6,17)
        fg_o_end = 10 + fgf_o_tweak + fg_o_range
        assist_range = random.randint(2,13)
        assist_end = fg_o_end + 1 + assist_range
        to_range = random.randint(0,14)
        o_foul_range = random.randint(0,4)
        steal_range = random.randint(6,13)
        steal_start = 99 - steal_range
        to_start = steal_start - 1 - to_range
        o_foul_start = to_start - 1 - o_foul_range
        miss_range = random.randint(24,37)
        miss_start = o_foul_start - 1 - miss_range
        if (miss_start-1) < (assist_end+1):
            miss_start = assist_end+2
        self.offense_results.plays = {"fg_foul_range": (1, 9+fgf_o_tweak), "fg_range": (10+fgf_o_tweak, fg_o_end), 
                                      "assist_range": (fg_o_end+1, assist_end), "foul_range": (assist_end+1, miss_start-1), 
                                      "miss_range": (miss_start, o_foul_start-1), "block_range": None, 
                                      "offensive_foul_range": (o_foul_start, to_start-1), "turnover_range": (to_start, steal_start-1), 
                                      "steal_range": (steal_start, 99)}
        fg_d_tweak = random.randint(0,9)
        foul_d_tweak = random.randint(0,11)
        miss_d_range = random.randint(30,37)
        miss_d_start = fg_d_tweak + foul_d_tweak + 26
        miss_d_end = miss_d_start + miss_d_range
        block_range = random.randint(0,8)
        block_end = miss_d_end + 1 + block_range
        to_d_range = random.randint(0,15)
        to_d_end = block_end + 1 + to_d_range
        self.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 22+fg_d_tweak), "assist_range": None,
                                      "foul_range": (25+fg_d_tweak, 25+fg_d_tweak+foul_d_tweak), "miss_range": (miss_d_start, miss_d_end), 
                                      "block_range": (miss_d_end+1, block_end), "offensive_foul_range": None, 
                                      "turnover_range": (block_end+1, to_d_end), "steal_range": (to_d_end+1, 99)}
        self.game_stats = GameStats()

class StarComboGuard(Player):
  # Jerel McNeal, Avery Bradley, etc.
  def __init__(self):
      self.name = names.get_full_name(gender='male')
      self.primary_position = "g"
      self.shot_rating = random.randint(5,13)
      self.three_point_rating = self.shot_rating + random.randint(2,5)
      self.shots_per_game = random.randint(8,13)
      self.defensive_rebound_rating = random.randint(5,13)
      self.offensive_rebound_rating = random.randint(1,6)
      self.assist_rating = int(round(random.normalvariate(30, 3)))
      self.offense_results.three_point_shot = (1, int(round(random.normalvariate(36, 5))))
      self.offense_results.free_throw_shot = (1, random.randint(62,82))
      self.defense_results.three_point_shot = (1, random.randint(25,35))
      fgf_o_tweak = random.randint(0,13)
      fg_o_range = random.randint(10,25)
      fg_o_end = 5 + fgf_o_tweak + fg_o_range
      assist_range = random.randint(3,14)
      assist_end = fg_o_end + 1 + assist_range
      to_range = random.randint(0,14)
      o_foul_range = random.randint(2,8)
      steal_range = int(round(random.normalvariate(10, 2)))
      steal_start = 99 - steal_range
      to_start = steal_start - 1 - to_range
      o_foul_start = to_start - 1 - o_foul_range
      miss_range = random.randint(15,31)
      miss_start = o_foul_start - 1 - miss_range
      if (miss_start-1) < (assist_end+1):
          miss_start = assist_end+2
      self.offense_results.plays = {"fg_foul_range": (1, 4+fgf_o_tweak), "fg_range": (5+fgf_o_tweak, fg_o_end), 
                                    "assist_range": (fg_o_end+1, assist_end), "foul_range": (assist_end+1, miss_start-1), 
                                    "miss_range": (miss_start, o_foul_start-1), "block_range": None, 
                                    "offensive_foul_range": (o_foul_start, to_start-1), "turnover_range": (to_start, steal_start-1), 
                                    "steal_range": (steal_start, 99)}
      fg_d_tweak = random.randint(0,10)
      foul_d_tweak = random.randint(4,19)
      miss_d_range = random.randint(26,36)
      miss_d_start = fg_d_tweak + foul_d_tweak + 25
      miss_d_end = miss_d_start + miss_d_range
      block_range = random.randint(1,9)
      block_end = miss_d_end + 1 + block_range
      to_d_range = random.randint(0,12)
      to_d_end = block_end + 1 + to_d_range
      if to_d_end > 98:
          to_d_end = 98
      self.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 23+fg_d_tweak), "assist_range": None,
                                    "foul_range": (24+fg_d_tweak, 24+fg_d_tweak+foul_d_tweak), "miss_range": (miss_d_start, miss_d_end), 
                                    "block_range": (miss_d_end+1, block_end), "offensive_foul_range": None, 
                                    "turnover_range": (block_end+1, to_d_end), "steal_range": (to_d_end+1, 99)}
      self.game_stats = GameStats()

class StarForwardCenter(Player):
    # Not a ton of these in college basketball. Think Josh McRoberts
    def __init__(self):
        self.name = names.get_full_name(gender='male')
        self.primary_position = "f"
        self.secondary_position = "c"
        self.shot_rating = random.randint(10,13)
        three_point_shot = random.randint(0,2)
        if three_point_shot == 0:
            self.three_point_rating = None
        else:
            self.three_point_rating = self.shot_rating + three_point_shot
        self.shots_per_game = random.randint(8,10)
        self.defensive_rebound_rating = random.randint(17,20)
        self.offensive_rebound_rating = random.randint(6,19)
        self.assist_rating = random.randint(10,26)
        self.offense_results.three_point_shot = (1, random.randint(3,11))
        self.offense_results.free_throw_shot = (1, random.randint(54,70))
        self.defense_results.three_point_shot = (1, random.randint(25,33))
        fgf_o_tweak = random.randint(0,8)
        fg_o_range = random.randint(6,21)
        fg_o_end = 8 + fgf_o_tweak + fg_o_range
        assist_range = random.randint(6,14)
        assist_end = fg_o_end + 1 + assist_range
        to_range = random.randint(0,9)
        o_foul_range = random.randint(3,11)
        steal_range = random.randint(7,13)
        steal_start = 99 - steal_range
        to_start = steal_start - 1 - to_range
        o_foul_start = to_start - 1 - o_foul_range
        miss_range = random.randint(20,27)
        miss_start = o_foul_start - 1 - miss_range
        if (miss_start-1) < (assist_end+1):
            miss_start = assist_end+2
        self.offense_results.plays = {"fg_foul_range": (1, 7+fgf_o_tweak), "fg_range": (8+fgf_o_tweak, fg_o_end), 
                                      "assist_range": (fg_o_end+1, assist_end), "foul_range": (assist_end+1, miss_start-1), 
                                      "miss_range": (miss_start, o_foul_start-1), "block_range": None, 
                                      "offensive_foul_range": (o_foul_start, to_start-1), "turnover_range": (to_start, steal_start-1), 
                                      "steal_range": (steal_start, 99)}
        fg_d_tweak = random.randint(0,6)
        foul_d_tweak = random.randint(10,19)
        miss_d_range = random.randint(0,10)
        miss_d_start = fg_d_tweak + foul_d_tweak + 28
        miss_d_end = miss_d_start + miss_d_range
        block_range = random.randint(22,42)
        block_end = miss_d_end + 1 + block_range
        to_d_range = random.randint(0,7)
        to_d_end = block_end + 1 + to_d_range
        #this deals with guys that block a ton of shots
        if block_end > 98:
            block_end = 98
            to_d_end = 99
            steal_d_start = 99
        elif to_d_end > 98:
            to_d_end = 99
            steal_d_start = 99
        else:
            steal_d_start = to_d_end+1
        self.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 27+fg_d_tweak), "assist_range": None,
                                      "foul_range": (28+fg_d_tweak, 28+fg_d_tweak+foul_d_tweak), "miss_range": (miss_d_start, miss_d_end), 
                                      "block_range": (miss_d_end+1, block_end), "offensive_foul_range": None, 
                                      "turnover_range": (block_end+1, to_d_end), "steal_range": (steal_d_start, 99)}
        self.game_stats = GameStats()

class StarStretchForward(Player):
    # Not a ton of these in college basketball. Think Josh McRoberts
    def __init__(self):
        self.name = names.get_full_name(gender='male')
        self.primary_position = "f"
        self.shot_rating = random.randint(6,14)
        three_point_shot = random.randint(2,5)
        self.three_point_rating = self.shot_rating + three_point_shot
        self.shots_per_game = random.randint(7,14)
        self.defensive_rebound_rating = random.randint(9,20)
        self.offensive_rebound_rating = random.randint(3,13)
        self.assist_rating = random.randint(5,20)
        self.offense_results.three_point_shot = (1, 38+random.randint(0,17))
        self.offense_results.free_throw_shot = (1, random.randint(68,78))
        self.defense_results.three_point_shot = (1, random.randint(28,35))
        fgf_o_tweak = random.randint(0,8)
        fg_o_range = random.randint(6,14)
        fg_o_end = 11 + fgf_o_tweak + fg_o_range
        assist_range = random.randint(5,10)
        assist_end = fg_o_end + 1 + assist_range
        to_range = random.randint(0,13)
        o_foul_range = random.randint(1,10)
        steal_range = random.randint(2,11)
        steal_start = 99 - steal_range
        to_start = steal_start - 1 - to_range
        o_foul_start = to_start - 1 - o_foul_range
        miss_range = random.randint(14,26)
        miss_start = o_foul_start - 1 - miss_range
        if (miss_start-1) < (assist_end+1):
            miss_start = assist_end+2
        self.offense_results.plays = {"fg_foul_range": (1, 10+fgf_o_tweak), "fg_range": (11+fgf_o_tweak, fg_o_end), 
                                      "assist_range": (fg_o_end+1, assist_end), "foul_range": (assist_end+1, miss_start-1), 
                                      "miss_range": (miss_start, o_foul_start-1), "block_range": None, 
                                      "offensive_foul_range": (o_foul_start, to_start-1), "turnover_range": (to_start, steal_start-1), 
                                      "steal_range": (steal_start, 99)}
        fg_d_tweak = random.randint(0,8)
        foul_d_tweak = random.randint(5,21)
        miss_d_range = random.randint(4,36)
        miss_d_start = fg_d_tweak + foul_d_tweak + 28
        miss_d_end = miss_d_start + miss_d_range
        block_range = random.randint(30,36) - miss_d_range
        if block_range < 0:
            block_range = 0
        block_end = miss_d_end + 1 + block_range
        to_d_range = random.randint(8,21)
        to_d_end = block_end + 1 + to_d_range
        #this deals with guys that block a ton of shots
        if block_end > 98:
            block_end = 98
            to_d_end = 99
            steal_d_start = 99
        elif to_d_end > 98:
            to_d_end = 99
            steal_d_start = 99
        else:
            steal_d_start = to_d_end+1
        self.defense_results.plays = {"fg_foul_range": None, "fg_range": (1, 23+fg_d_tweak), "assist_range": None,
                                      "foul_range": (28+fg_d_tweak, 28+fg_d_tweak+foul_d_tweak), "miss_range": (miss_d_start, miss_d_end), 
                                      "block_range": (miss_d_end+1, block_end), "offensive_foul_range": None, 
                                      "turnover_range": (block_end+1, to_d_end), "steal_range": (steal_d_start, 99)}
        self.game_stats = GameStats()

star_sg = StarStretchForward()
print star_sg.offense_results.__dict__
print star_sg.defense_results.__dict__