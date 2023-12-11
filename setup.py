import json
import os
import sqlite3

try:
	import discord
except ImportError as e:
	print("discord.py isnt installed, attempting to install.")
	os.system("py -m pip install discord.py")

base_path = os.path.abspath(__file__)[:-8]


print("Creating config.")
config_file = open(base_path + "config.json", "w")

config = {
	"token" : "",
	"prefix" : "",
	"admin_ids" : [],
	"moderator_ids" : [],
	"logs" : True,
	"log_time" : 24
}

config["token"] = input("Input your bot's token")
config["prefix"] = input("Input your preffered prefix")
config["admin_ids"][0] = input("Input your discord id")

config_file.write(json.dumps(config))
config_file.close()

print("Created config \nCreating the database")

conn = sqlite3.connect(base_path + "database.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE bans (
                    id INTEGER PRIMARY KEY,
                    discord_id INTEGER NOT NULL,
               		timestamp INTEGER NOT NULL,
                    banned INTEGER NOT NULL

                )''')

cursor.execute('''CREATE TABLE users (
                    id INTEGER PRIMARY KEY,
                    discord_id INTEGER,
                    license TEXT NOT NULL UNIQUE,
                    registered INTEGER NOT NULL,
                    banned INTEGER,
                    FOREIGN KEY(banned) REFERENCES bans(banned) 
                )''')

