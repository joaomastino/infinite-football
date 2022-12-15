import random
from classes import Player, PlayerStat
import sqlite3

# Import the Peewee ORM and the Model base class
from peewee import *

# Define the database and the model
database = SqliteDatabase('football.db')

def qb_calc_values(player):
    # For recently created QBs, create record inside the Playerstat table and assign calculated values
    # for player in players:
      passing_calc = (player.arm_strength * 0.4 + player.accuracy * 0.6 )
      mobility_calc = ((player.footwork * 0.3) + (player.agility * 0.1) + (player.deception * 0.1) + (player.athleticism * 0.1) + (player.endurance * 0.1) + (player.speed * 0.3))
      game_reading_calc = ((player.processing * 0.3) + (player.decision_making * 0.3) + (player.playbook * 0.1) + (player.confidence * 0.1) + (player.instinct * 0.2))
      team_leading_calc = ((player.leadership * 0.3) + (player.concentration * 0.2) + (player.coolness * 0.1) + (player.resilience * 0.1) + (player.discipline * 0.1) + (player.confidence * 0.2))
      playerstat = PlayerStat(player_id=player.id, 
                      passing = passing_calc, 
                      mobility = mobility_calc, 
                      game_reading = game_reading_calc,
                      team_leading = team_leading_calc,
                      qb_skill_index = (passing_calc * 0.5 + mobility_calc * 0.2 + game_reading_calc * 0.2 + team_leading_calc * 0.1)
                      )
      playerstat.save()

def rb_calc_values(player):
    # For recently created RBs, create record inside the Playerstat table and assign calculated values
    rushing_calc = ((player.speed * 0.3) + (player.acceleration * 0.2) + (player.vision * 0.2) + (player.power * 0.2) + (player.elusiveness * 0.1))
    receiving_calc = ((player.catching * 0.5) + (player.ball_security * 0.3) + (player.body_control * 0.1) + (player.position * 0.1))
    blocking_calc = ((player.pass_blocking * 0.7) + (player.run_blocking * 0.3))
    playerstat = PlayerStat(player_id=player.id, 
                    rushing = rushing_calc, 
                    receiving = receiving_calc, 
                    blocking = blocking_calc,
                    rb_skill_index = ((rushing_calc * 0.6) + (receiving_calc * 0.2) + (blocking_calc * 0.2))
                    )
    playerstat.save()

def wr_calc_values(player):
    # For recently created WRs, create record inside the Playerstat table and assign calculated values
    rushing_calc = ((player.speed * 0.5) + (player.acceleration * 0.3) + (player.vision * 0.1) + (player.power * 0.1))
    receiving_calc = ((player.catching * 0.5) + (player.ball_security * 0.2) + (player.separation * 0.2) + (player.body_control * 0.1))
    playerstat = PlayerStat(player_id=player.id, 
                    rushing = rushing_calc, 
                    receiving = receiving_calc, 
                    wr_skill_index = (rushing_calc * 0.3 + receiving_calc * 0.7)
                    )
    playerstat.save()

def te_calc_values(player):
    # For recently created TEs, create record inside the Playerstat table and assign calculated values
    rushing_calc = ((player.speed * 0.3) + (player.acceleration * 0.2) + (player.vision * 0.2) + (player.power * 0.2) + (player.elusiveness * 0.1))
    receiving_calc = ((player.catching * 0.5) + (player.ball_security * 0.3) + (player.position * 0.2))
    blocking_calc = ((player.pass_blocking * 0.5) + (player.run_blocking * 0.5))
    playerstat = PlayerStat(player_id=player.id, 
                    rushing = rushing_calc, 
                    receiving = receiving_calc, 
                    blocking = blocking_calc,
                    te_skill_index = ((rushing_calc * 0.2) + (receiving_calc * 0.4) + (blocking_calc * 0.3))
                    )
    playerstat.save()

def ol_calc_values(player):
    # For recently created OLs, create record inside the Playerstat table and assign calculated values
    blocking_calc = ((player.pass_blocking * 0.5) + (player.run_blocking * 0.5))
    protection_calc = ((player.position * 0.2) + (player.reaction * 0.2) + (player.anchor * 0.4) + (player.athleticism * 0.2))
    game_reading_calc = ((player.processing * 0.3) + (player.discipline * 0.3) + (player.awareness * 0.1) + (player.instinct * 0.1) + (player.concentration * 0.2))
    playerstat = PlayerStat(player_id=player.id, 
                    blocking = blocking_calc,
                    protection = protection_calc,
                    game_reading = game_reading_calc,
                    ol_skill_index = ((blocking_calc * 0.5) + (protection_calc * 0.3) + (game_reading_calc * 0.2))
                    )
    playerstat.save()

def random_value(skill_level):
  # Implementare la gestione dell'età con valori 1, 2, 3 per giovane, maturo, veterano
  # skill level da 1 a 5 assegna diversi range di valore
    if skill_level == 5:
      value = random.randint(75, 90)
    elif skill_level == 4:
      value = random.randint(70, 85)
    elif skill_level == 3:
      value = random.randint(60, 80)
    elif skill_level == 2:
      value = random.randint(55, 75)
    elif skill_level == 1:
      value = random.randint(50, 90)
    else:
      # Handle the case where skill_level does not match any of the expected values
      value = random.randint(0, 100)
    return value

def random_firstName():
  conn = sqlite3.connect("football.db")
  query = "SELECT name FROM firstNames ORDER BY RANDOM() LIMIT 1"
  cursor = conn.cursor()
  cursor.execute(query)
  random_player_name = cursor.fetchone()[0]
  return  random_player_name

def random_lastName():
  conn = sqlite3.connect("football.db")
  query = "SELECT last_name FROM lastNames ORDER BY RANDOM() LIMIT 1"
  cursor = conn.cursor()
  cursor.execute(query)
  random_player_lname = cursor.fetchone()[0]
  return  random_player_lname

# Player creating functions
def create_QB(skill_level):
  new_qb = Player.create(
    first_name = random_firstName(),
    last_name = random_lastName(),
    age = random.randint(22, 34),
    role = 'QB',
    team_id = 0,
    form = random.randint(60, 100),
    injury = 0,
    potential = random.randint(30, 100),
    peak = random.randint(28, 34),
    # Intangible skill set
    leadership = random_value(skill_level),
    playbook = random_value(skill_level),
    awareness = random_value(skill_level),
    concentration = random_value(skill_level),
    coolness = random_value(skill_level),
    confidence = random_value(skill_level),
    resilience = random_value(skill_level),
    discipline = random_value(skill_level),
    instinct = random_value(skill_level),
    # Physical skill set
    height = random.randint(180, 195),
    weigth = random.randint(90, 110),
    athleticism = random_value(skill_level),
    endurance = random_value(skill_level),
    strength = random_value(skill_level),
    agility = random_value(skill_level), # WR, OL
    power = random_value(skill_level), # RB, OL
    body_control = random_value(skill_level), # CB, WR, S
    arm_strength = random_value(skill_level),
    # QB skill set
    accuracy = random_value(skill_level),
    processing = random_value(skill_level), # OL, LB, DL
    decision_making = random_value(skill_level), # OL
    footwork = random_value(skill_level), # OL
    deception = random_value(skill_level), # QB, RB
    # RB skill set
    speed = random.randint(60,85), # WR
    acceleration = random.randint(50,80), # WR
    vision = random_value(skill_level), # QB, OL
    ball_security = random_value(skill_level), # TE, WR
    elusiveness = random.randint(50,80),
    # WR skill set
    catching = random.randint(30,75), # TE
    route_running = random.randint(30,75), # TE
    jumping = random.randint(30,75), # TE
    separation = random.randint(30,75), # TE
    # OL skill set
    pass_blocking = random.randint(30,75), # TE, RB
    run_blocking = random.randint(30,75), # TE, RB
    position = random.randint(60,80),# TE, WR
    reaction = random_value(skill_level),
    anchor = random.randint(50,75), # OL, DT
    # DEF skill set
    tackling = random.randint(30,75), # LB, DL, DB
    coverage = random.randint(30,55), # DB, LB
    pass_rush = random.randint(30,55),
    ball_extraction = random.randint(30,55)
  )
  new_qb.save()
  qb_calc_values(new_qb)
 
def create_RB(skill_level):
  new_rb = Player.create(
    first_name = random_firstName(),
    last_name = random_lastName(),
    age = random.randint(22, 30),
    role = 'RB',
    team_id = 0,
    form = random.randint(60, 100),
    injury = 0,
    potential = random.randint(30, 100),
    peak = random.randint(26, 30),
    # Intangible skill set
    leadership = random.randint(60,99),
    playbook = random_value(skill_level),
    awareness = random.randint(60,99),
    concentration = random.randint(60,99),
    confidence = random.randint(60,99),
    coolness = random.randint(60,99),
    resilience = random.randint(60,99),
    discipline = random.randint(60,99),
    instinct = random.randint(60,99),
    # Physical skill set
    height = random.randint(177, 185),
    weigth = random.randint(88, 98),
    athleticism = random_value(skill_level),
    endurance = random_value(skill_level),
    strength = random_value(skill_level),
    agility = random_value(skill_level), # WR, OL
    power = random_value(skill_level), # RB, OL
    body_control = random_value(skill_level), # CB, WR, S
    arm_strength = random.randint(50,75),
    # QB skill set
    accuracy = random.randint(40,65),
    processing = random_value(skill_level), # OL, LB, DL
    decision_making = random.randint(60,99), # OL
    footwork = random_value(skill_level), # OL
    deception = random_value(skill_level), # QB, RB
    # RB skill set
    speed = random_value(skill_level), # WR
    acceleration = random_value(skill_level), # WR
    vision = random_value(skill_level), # QB, OL
    ball_security = random_value(skill_level), # TE, WR
    elusiveness = random_value(skill_level),
    # WR skill set
    catching = random.randint(60,99), # TE
    route_running = random.randint(60,99), # TE
    jumping = random.randint(60,80), # TE
    separation = random.randint(60,99), # TE
    # OL skill set
    pass_blocking = random.randint(60,80), # TE, RB
    run_blocking = random.randint(60,80), # TE, RB
    position = random.randint(60,80),# TE, WR
    reaction = random.randint(60,80),
    anchor = random.randint(50,75), # OL, DT
    # DEF skill set
    tackling = random.randint(30,70), # LB, DL, DB
    coverage = random.randint(30,55), # DB, LB
    pass_rush = random.randint(30,55),
    ball_extraction = random.randint(30,55)
  )
  new_rb.save()
  rb_calc_values(new_rb)

def create_WR(skill_level):
  new_wr = Player.create(
    first_name = random_firstName(),
    last_name = random_lastName(),
    age = random.randint(22, 30),
    role = 'WR',
    team_id = 0,
    form = random.randint(60, 100),
    injury = 0,
    potential = random.randint(30, 100),
    peak = random.randint(28, 32),
    # Intangible skill set
    leadership = random.randint(60,99),
    playbook = random_value(skill_level),
    awareness = random.randint(60,99),
    concentration = random.randint(60,99),
    coolness = random.randint(60,99),
    confidence = random.randint(60,99),
    resilience = random.randint(60,99),
    discipline = random.randint(60,99),
    instinct = random.randint(60,99),
    # Physical skill set
    height = random.randint(177, 196),
    weigth = random.randint(85, 105),
    athleticism = random_value(skill_level),
    endurance = random_value(skill_level),
    strength = random_value(skill_level),
    agility = random_value(skill_level), # WR, OL
    power = random_value(skill_level), # RB, OL
    body_control = random_value(skill_level), # CB, WR, S
    arm_strength = random.randint(50,75),
    # QB skill set
    accuracy = random.randint(40,65),
    processing = random_value(skill_level), # OL, LB, DL
    decision_making = random.randint(60,80), # OL
    footwork = random.randint(60,80), # OL
    deception = random.randint(60,80), # QB, RB
    # RB skill set
    speed = random_value(skill_level), # WR
    acceleration = random_value(skill_level), # WR
    vision = random.randint(60,90), # QB, OL
    ball_security = random_value(skill_level), # TE, WR
    elusiveness = random_value(skill_level),
    # WR skill set
    catching = random_value(skill_level), # TE
    route_running = random_value(skill_level), # TE
    jumping = random_value(skill_level), # TE
    separation = random_value(skill_level), # TE
    # OL skill set
    pass_blocking = random.randint(50,70), # TE, RB
    run_blocking = random.randint(50,70), # TE, RB
    position = random_value(skill_level),# TE, WR
    reaction = random_value(skill_level),
    anchor = random.randint(50,75), # OL, DT
    # DEF skill set
    tackling = random.randint(30,70), # LB, DL, DB
    coverage = random.randint(30,55), # DB, LB
    pass_rush = random.randint(30,55),
    ball_extraction = random.randint(30,55)
  )
  new_wr.save()
  wr_calc_values(new_wr)

def create_TE(skill_level):
  new_te = Player.create(
    first_name = random_firstName(),
    last_name = random_lastName(),
    age = random.randint(22, 30),
    role = 'TE',
    team_id = 0,
    form = random.randint(60, 100),
    injury = 0,
    potential = random.randint(30, 100),
    peak = random.randint(28, 32),
    # Intangible skill set
    leadership = random.randint(60,99),
    playbook = random_value(skill_level),
    awareness = random.randint(60,99),
    concentration = random.randint(60,99),
    coolness = random.randint(60,99),
    confidence = random.randint(60,99),
    resilience = random.randint(60,99),
    discipline = random.randint(60,99),
    instinct = random.randint(60,99),
    # Physical skill set
    height = random.randint(188, 198),
    weigth = random.randint(96, 118),
    athleticism = random_value(skill_level),
    endurance = random_value(skill_level),
    strength = random_value(skill_level),
    agility = random.randint(60,85), # WR, OL
    power = random_value(skill_level), # RB, OL
    body_control = random_value(skill_level), # CB, WR, S
    arm_strength = random.randint(50,75),
    # QB skill set
    accuracy = random.randint(40,65),
    processing = random_value(skill_level), # OL, LB, DL
    decision_making = random.randint(60,80), # OL
    footwork = random.randint(60,80), # OL
    deception = random.randint(60,80), # QB, RB
    # RB skill set
    speed = random.randint(60,80), # WR
    acceleration = random.randint(60,80), # WR
    vision = random.randint(60,85), # QB, OL
    ball_security = random_value(skill_level), # TE, WR
    elusiveness = random.randint(60,85),
    # WR skill set
    catching = random_value(skill_level), # TE
    route_running = random_value(skill_level), # TE
    jumping = random.randint(60,88), # TE
    separation = random.randint(60,88), # TE
    # OL skill set
    pass_blocking = random.randint(70,90), # TE, RB
    run_blocking = random.randint(70,90), # TE, RB
    position = random_value(skill_level),# TE, WR
    reaction = random.randint(70,90),
    anchor = random.randint(70,90), # OL, DT
    # DEF skill set
    tackling = random.randint(30,70), # LB, DL, DB
    coverage = random.randint(30,55), # DB, LB
    pass_rush = random.randint(30,55),
    ball_extraction = random.randint(30,55)
  )
  new_te.save()
  te_calc_values(new_te)

def create_OL(skill_level):
  new_ol = Player.create(
    first_name = random_firstName(),
    last_name = random_lastName(),
    age = random.randint(22, 30),
    role = 'OL',
    team_id = 0,
    form = random.randint(60, 100),
    injury = 0,
    potential = random.randint(30, 100),
    peak = random.randint(28, 32),
    # Intangible skill set
    leadership = random.randint(60,99),
    playbook = random_value(skill_level),
    awareness = random_value(skill_level),
    concentration = random_value(skill_level),
    coolness = random_value(skill_level),
    confidence = random.randint(60,99),
    resilience = random_value(skill_level),
    discipline = random_value(skill_level),
    instinct = random_value(skill_level),
    # Physical skill set
    height = random.randint(188, 201),
    weigth = random.randint(135, 160),
    athleticism = random_value(skill_level),
    endurance = random_value(skill_level),
    strength = random_value(skill_level),
    agility = random.randint(50, 75), # WR, OL
    power = random_value(skill_level), # RB, OL
    body_control = random.randint(50,75), # CB, WR, S
    arm_strength = random.randint(50,65),
    # QB skill set
    accuracy = random.randint(40,65),
    processing = random_value(skill_level), # OL, LB, DL
    decision_making = random.randint(60,80), # OL
    footwork = random_value(skill_level), # OL
    deception = random.randint(60,80), # QB, RB
    # RB skill set
    speed = random.randint(40, 70), # WR
    acceleration = random.randint(60,80), # WR
    vision = random.randint(60,85), # QB, OL
    ball_security = random_value(skill_level), # TE, WR
    elusiveness = random.randint(40,65),
    # WR skill set
    catching = random.randint(40,65), # TE
    route_running = random.randint(40,65), # TE
    jumping = random.randint(30,55), # TE
    separation = random.randint(30,55), # TE
    # OL skill set
    pass_blocking = random_value(skill_level), # TE, RB
    run_blocking = random_value(skill_level), # TE, RB
    position = random_value(skill_level), # TE, WR
    reaction = random_value(skill_level),
    anchor = random_value(skill_level), # OL, DT
    # DEF skill set
    tackling = random.randint(30,80), # LB, DL, DB
    coverage = random.randint(30,55), # DB, LB
    pass_rush = random.randint(30,55),
    ball_extraction = random.randint(30,75)
  )
  new_ol.save()
  ol_calc_values(new_ol)

def create_K(skill_level):
  new_k = Player.create(
    first_name = random_firstName(),
    last_name = random_lastName(),
    age = random.randint(22, 30),
    role = 'K',
    team_id = 0,
    form = random.randint(60, 100),
    injury = 0,
    potential = random.randint(30, 100),
    peak = random.randint(27, 37),
    # Intangible skill set
    leadership = random.randint(60,99),
    playbook = random_value(skill_level),
    awareness = random_value(skill_level),
    concentration = random_value(skill_level),
    coolness = random_value(skill_level),
    confidence = random_value(skill_level),
    resilience = random_value(skill_level),
    discipline = random_value(skill_level),
    instinct = random_value(skill_level),
    # Physical skill set
    height = random.randint(177, 188),
    weigth = random.randint(77, 95),
    athleticism = random_value(skill_level),
    endurance = random_value(skill_level),
    strength = random_value(skill_level),
    agility = random_value(skill_level), # WR, OL
    power = random_value(skill_level), # RB, OL
    body_control = random.randint(50,75), # CB, WR, S
    arm_strength = random.randint(50,65),
    # QB skill set
    accuracy = random_value(skill_level), # QB, K
    processing = random_value(skill_level), # OL, LB, DL
    decision_making = random.randint(60,80), # OL
    footwork = random.randint(60,80), # OL
    deception = random.randint(60,80), # QB, RB
    # RB skill set
    speed = random.randint(40, 80), # WR
    acceleration = random.randint(60,80), # WR
    vision = random.randint(60,85), # QB, OL
    ball_security = random.randint(40,60), # TE, WR
    elusiveness = random.randint(40,60),
    # WR skill set
    catching = random.randint(40,65), # TE
    route_running = random.randint(40,65), # TE
    jumping = random.randint(30,55), # TE
    separation = random.randint(30,55), # TE
    # OL skill set
    pass_blocking = random.randint(40,60), # TE, RB
    run_blocking = random.randint(40,60), # TE, RB
    position = random.randint(40,60), # TE, WR
    reaction = random.randint(40,60),
    anchor = random.randint(40,60), # OL, DT
    # DEF skill set
    tackling = random.randint(40,60), # LB, DL, DB
    coverage = random.randint(40,60), # DB, LB
    pass_rush = random.randint(40,60),
    ball_extraction = random.randint(40,60),
  )
  new_k.save()

def create_LB(skill_level):
  new_lb = Player.create(
    first_name = random_firstName(),
    last_name = random_lastName(),
    age = random.randint(22, 30),
    role = 'LB',
    team_id = 0,
    form = random.randint(60, 100),
    injury = 0,
    potential = random.randint(30, 100),
    peak = random.randint(26, 32),
    # Intangible skill set
    leadership = random.randint(60,99),
    playbook = random_value(skill_level),
    awareness = random_value(skill_level),
    concentration = random_value(skill_level),
    coolness = random_value(skill_level),
    confidence = random.randint(60,99),
    resilience = random_value(skill_level),
    discipline = random_value(skill_level),
    instinct = random_value(skill_level),
    # Physical skill set
    height = random.randint(177, 190),
    weigth = random.randint(95, 120),
    athleticism = random_value(skill_level),
    endurance = random_value(skill_level),
    strength = random_value(skill_level),
    agility = random_value(skill_level), # WR, OL
    power = random_value(skill_level), # RB, OL
    body_control = random_value(skill_level), # CB, WR, S
    arm_strength = random.randint(50,65),
    # QB skill set
    accuracy = random.randint(50,65), # QB, K
    processing = random_value(skill_level), # OL, LB, DL
    decision_making = random_value(skill_level), # OL
    footwork = random.randint(60,80), # OL
    deception = random.randint(60,80), # QB, RB
    # RB skill set
    speed = random_value(skill_level), # WR
    acceleration = random_value(skill_level), # WR
    vision = random_value(skill_level), # QB, OL
    ball_security = random.randint(40,60), # TE, WR
    elusiveness = random.randint(40,60),
    # WR skill set
    catching = random.randint(40,65), # TE
    route_running = random.randint(40,65), # TE
    jumping = random_value(skill_level), # TE
    separation = random.randint(30,55), # TE
    # OL skill set
    pass_blocking = random.randint(40,60), # TE, RB
    run_blocking = random.randint(40,60), # TE, RB
    position = random.randint(40,60), # TE, WR
    reaction = random.randint(40,60),
    anchor = random.randint(40,60), # OL, DT
    # DEF skill set
    tackling = random_value(skill_level), # LB, DL, DB
    coverage = random.randint(40,80), # DB, LB
    pass_rush = random.randint(60,90),
    ball_extraction = random.randint(60,90),
  )
  new_lb.save()

def create_DL(skill_level):
  new_dl = Player.create(
    first_name = random_firstName(),
    last_name = random_lastName(),
    age = random.randint(22, 30),
    role = 'DL',
    team_id = 0,
    form = random.randint(60, 100),
    injury = 0,
    potential = random.randint(30, 100),
    peak = random.randint(26, 32),
    # Intangible skill set
    leadership = random.randint(60,99),
    playbook = random_value(skill_level),
    awareness = random_value(skill_level),
    concentration = random_value(skill_level),
    coolness = random_value(skill_level),
    confidence = random.randint(60,99),
    resilience = random_value(skill_level),
    discipline = random_value(skill_level),
    instinct = random_value(skill_level),
    # Physical skill set
    height = random.randint(190, 200),
    weigth = random.randint(127, 136),
    athleticism = random_value(skill_level),
    endurance = random_value(skill_level),
    strength = random_value(skill_level),
    agility = random_value(skill_level), # WR, OL
    power = random_value(skill_level), # RB, OL
    body_control = random.randint(60,85), # CB, WR, S
    arm_strength = random.randint(50,65),
    # QB skill set
    accuracy = random.randint(50,65), # QB, K
    processing = random.randint(50,85), # OL, LB, DL
    decision_making = random.randint(60,80), # OL
    footwork = random.randint(60,80), # OL
    deception = random.randint(60,80), # QB, RB
    # RB skill set
    speed = random.randint(60, 85), # WR
    acceleration = random.randint(60,85), # WR
    vision = random.randint(60,85), # QB, OL
    ball_security = random.randint(40,60), # TE, WR
    elusiveness = random.randint(40,60),
    # WR skill set
    catching = random.randint(40,65), # TE
    route_running = random.randint(40,65), # TE
    jumping = random.randint(30,55), # TE
    separation = random.randint(30,55), # TE
    # OL skill set
    pass_blocking = random.randint(40,60), # TE, RB
    run_blocking = random.randint(40,60), # TE, RB
    position = random_value(skill_level), # TE, WR
    reaction = random_value(skill_level),
    anchor = random.randint(40,60), # OL, DT
    # DEF skill set
    tackling = random.randint(60,90), # LB, DL, DB
    coverage = random.randint(40,70), # DB, LB
    pass_rush = random_value(skill_level),
    ball_extraction = random_value(skill_level),
  )
  new_dl.save()

def create_DB(skill_level):
  new_db = Player.create(
    first_name = random_firstName(),
    last_name = random_lastName(),
    age = random.randint(22, 30),
    role = 'DB',
    team_id = 0,
    form = random.randint(60, 100),
    injury = 0,
    potential = random.randint(30, 100),
    peak = random.randint(26, 31),
    # Intangible skill set
    leadership = random.randint(60,99),
    playbook = random_value(skill_level),
    awareness = random_value(skill_level),
    concentration = random_value(skill_level),
    coolness = random_value(skill_level),
    confidence = random.randint(60,99),
    resilience = random_value(skill_level),
    discipline = random_value(skill_level),
    instinct = random_value(skill_level),
    # Physical skill set
    height = random.randint(177, 192),
    weigth = random.randint(84, 95),
    athleticism = random_value(skill_level),
    endurance = random_value(skill_level),
    strength = random_value(skill_level),
    agility = random_value(skill_level), # WR, OL
    power = random_value(skill_level), # RB, OL
    body_control = random_value(skill_level), # CB, WR, S
    arm_strength = random.randint(50,65),
    # QB skill set
    accuracy = random.randint(50,65), # QB, K
    processing = random_value(skill_level), # OL, LB, DL
    decision_making = random_value(skill_level), # OL
    footwork = random.randint(60,80), # OL
    deception = random.randint(60,80), # QB, RB
    # RB skill set
    speed = random_value(skill_level), # WR
    acceleration = random_value(skill_level), # WR
    vision = random_value(skill_level), # QB, OL
    ball_security = random.randint(40,60), # TE, WR
    elusiveness = random.randint(40,60),
    # WR skill set
    catching = random_value(skill_level), # TE
    route_running = random.randint(40,65), # TE
    jumping = random_value(skill_level), # TE
    separation = random.randint(30,55), # TE
    # OL skill set
    pass_blocking = random.randint(40,60), # TE, RB
    run_blocking = random.randint(40,60), # TE, RB
    position = random_value(skill_level), # TE, WR
    reaction = random_value(skill_level),
    anchor = random.randint(40,60), # OL, DT
    # DEF skill set
    tackling = random_value(skill_level), # LB, DL, DB
    coverage = random_value(skill_level), # DB, LB
    pass_rush = random.randint(60,85),
    ball_extraction = random_value(skill_level),
  )
  new_db.save()

database.connect()

# for i in range(4):
  # create_QB(5)
#   create_RB(5)
#   create_TE(5)
#   create_K(5)
#   create_K(4)
#   create_K(3)


# for i in range(6):
#   create_LB(5)
#   create_DL(5)
#   create_DB(5)
#   create_WR(5)

# for i in range(10):
#   create_LB(4)
#   create_DL(4)
#   create_DB(4)

# for i in range(14):
#   create_LB(3)
#   create_DL(3)
#   create_DB(3)



database.close()
  
  







