import time
import random

# Declaring my global variables
home_team_name = input("what name would you give the first team? ").upper()
away_team_name = input("what name would you give the second team? ").upper()
home_team_score = 0
away_team_score = 0

# match timing configuration
match_duration = 90        
runtime_minutes = int(input("How long should this match last (in real minutes)? "))     
virtual_time = 0

# list of match activities
ACTIVITIES = ["GOAL", "FREE KICK", "PENALTY", "CORNER"]

# this code declares any match event with a time stamp
def match_status(message, current_minute):
    print(f"[{current_minute:02d}:00] {message}")


# this code will a team randomly to assign activities 
def get_random_team():
    return random.choice([home_team_name, away_team_name])

def match_engine(current_minute):
    global home_team_score, away_team_score # this code ensures that global team variables will be modified

    activity = random.choice(ACTIVITIES) # this code will select a random activity
    team = get_random_team() # this variable calls get_random_team function which selects a random team that assigns a random activity

    if activity == "GOAL":
        if team == home_team_name:
            home_team_score += 1
        else:
            away_team_score += 1
        
        # the function will display match activities in the terminal
        match_status(
            f"GOAL for {team}! Score: {home_team_score} - {away_team_score}",
            current_minute
        )

    else:
        match_status(f"{activity} for {team}", current_minute)

