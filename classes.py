from peewee import *

db = SqliteDatabase('football.db')

class Team(Model):
    nickname = CharField()
    city = CharField()
    team_name = f"{city} {nickname}"

    class Meta:
        database = db

class FirstName(Model):
    name = CharField()

    class Meta:
      database = db
      table_name = "firstNames"

class LastName(Model):
    last_name = CharField()

    class Meta:
      database = db
      table_name = "lastNames"



class Player(Model):
    team = ForeignKeyField(Team)
    first_name = CharField()
    last_name = CharField()
    age = IntegerField()
    role = CharField()
    form = IntegerField()
    injury = IntegerField()
    potential = IntegerField()
    peak = IntegerField()
    # Intangible skill set
    leadership = IntegerField()
    concentration = IntegerField()
    confidence = IntegerField()
    coolness = IntegerField()
    resilience = IntegerField()
    discipline = IntegerField()
    playbook = IntegerField()
    awareness = IntegerField()
    position = IntegerField()
    instinct = IntegerField()
    # Physical skill set
    height = IntegerField()
    weigth = IntegerField()
    athleticism = IntegerField()
    strength = IntegerField()
    endurance = IntegerField()
    agility = IntegerField() # WR, OL
    power = IntegerField() # RB, OL
    body_control = IntegerField() # CB, WR, S
    # QB skill set
    arm_strength = IntegerField()
    accuracy = IntegerField()
    processing = IntegerField() # OL, LB, DL
    decision_making = IntegerField() # OL
    footwork = IntegerField() # OL
    deception = IntegerField() # QB, RB
    # RB skill set
    speed = IntegerField() # WR
    acceleration = IntegerField() # WR
    vision = IntegerField() # QB, OL
    ball_security = IntegerField() # TE, WR
    elusiveness = IntegerField()
    # WR skill set
    catching = IntegerField() # TE
    route_running = IntegerField() # TE
    jumping = IntegerField() # TE
    separation = IntegerField() # TE
    # OL skill set
    pass_blocking = IntegerField() # TE, RB
    run_blocking = IntegerField() # TE, RB
    position = IntegerField() # TE, WR
    reaction = IntegerField()
    anchor = IntegerField() # OL, DT
    # DEF skill set
    tackling = IntegerField() # LB, DL, DB
    coverage = IntegerField() # DB, LB
    pass_rush = IntegerField()
    ball_extraction = IntegerField()
    
    class Meta:
        database = db

    def passer(self):
        passing = 0


class Game(Model):
    home_team = ForeignKeyField(Team, related_name="home_games")
    away_team = ForeignKeyField(Team, related_name="away_games")
    home_score = IntegerField()
    away_score = IntegerField()

    class Meta:
        database = db


class PlayerStat(Model):
    player_id = ForeignKeyField(Player, unique=True)
    segments_played =  IntegerField(default=0)
    # calculated values
    qb_skill_index = FloatField(default=0)
    rb_skill_index = FloatField(default=0)
    wr_skill_index = FloatField(default=0)
    te_skill_index = FloatField(default=0)
    ol_skill_index = FloatField(default=0)
    k_skill_index = FloatField(default=0)
    dl_skill_index = FloatField(default=0)
    lb_skill_index = FloatField(default=0)
    db_skill_index = FloatField(default=0)
    passing = FloatField()
    mobility = FloatField(default=0)
    rushing = FloatField(default=0)
    receving = FloatField(default=0)
    game_reading = FloatField(default=0)
    team_leading = FloatField(default=0)
    blocking = FloatField(default=0)
    protection = FloatField(default=0)
    kicking = FloatField(default=0)
    man_cover = FloatField(default=0)
    deep_cover = FloatField(default=0)
    # statistical values
    pass_attempts = IntegerField(default=0)
    pass_complete = IntegerField(default=0)
    completion_percent = FloatField(default=0)
    interceptions_thrown = IntegerField(default=0)
    int_per_attempt = FloatField(default=0)
    passer_rating = FloatField(default=0)
    passing_yards = IntegerField(default=0)
    rushing_yards = IntegerField(default=0)
    rushing_attempts = IntegerField(default=0)
    rush_yards_attempt = FloatField(default=0)
    receiving_yards = FloatField(default=0)
    yards_per_recept = FloatField(default=0)
    targets = IntegerField(default=0)
    receptions = IntegerField(default=0)
    catch_pecentages = FloatField(default=0)
    tds = IntegerField(default=0)
    passing_td = IntegerField(default=0)
    rushing_td = IntegerField(default=0)
    receiving_td = IntegerField(default=0)
    fumbles = IntegerField(default=0)
    sacks_taken = IntegerField(default=0)
    # ol stats
    pressure_allowed = FloatField(default=0)
    sacks_allowed = FloatField(default=0)
    duels_lost = IntegerField(default=0)
    duels_won = IntegerField(default=0)
    duels_win_percent = FloatField(default=0)
    yds_rush_by_block = FloatField(default=0)
    pass_attmpt_by_block = IntegerField(default=0)
    # kicking stats
    extra_points_made = IntegerField(default=0)
    extra_points_fail = IntegerField(default=0)
    extra_points_percent = FloatField(default=0)
    fg_made = IntegerField(default=0)
    fg_attempt = IntegerField(default=0)
    fg_points_percent = FloatField(default=0)
    # defensive stats
    tackles = IntegerField(default=0)
    sacks = IntegerField(default=0)
    interceptions = IntegerField(default=0)
    qb_pressures = IntegerField(default=0)
    passes_avoided = IntegerField(default=0)
    passes_defended = IntegerField(default=0)
    fumbles_forced = IntegerField(default=0)
    fumbles_recovered = IntegerField(default=0)

    class Meta:
        database = db