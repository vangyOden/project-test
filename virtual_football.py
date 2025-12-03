import time
import random

# Declaring my global variables

team_a_name = input("what name would you give the first team? ").upper()
team_b_name = input("what name would you give the second team? ").upper()
team_a_score = 0
team_b_score = 0

match_duration = 90        
runtime_minutes = int(input("How long should this match last (in real minutes)? "))     
virtual_time = 0

ACTIVITIES = ["GOAL", "FREE KICK", "PENALTY", "CORNER"]

