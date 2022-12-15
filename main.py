from peewee import *
import pandas as pd
import random
import sqlite3

db = SqliteDatabase('football.db')






db.connect()

# db.create_tables([Player, PlayerStat])






# close the database connection
db.close()