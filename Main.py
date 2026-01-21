from components import load_input, power_set, score_schedule, brute_force
import time

# welcome message
FILE_INPUT = input("Welcome to this event planner program. Please input the name of your input file (ex: input_small.txt)\n")

# load input file and display information about it
ACTIVITIES_MAX, TIME_MAX, BUDGET, EVENTS = load_input(FILE_INPUT) 
EVENT_NAMES = list(EVENTS.keys())


# Constraint to optimize for. Options: "time", "cost", or "both"
CONSTRAINT_INPUT = input("\nWhat feature would you like to optimize for? time, cost, or both\n")
CONSTRAINT = CONSTRAINT_INPUT

print("\n--- Brute Force Process ---")
BRUTE_FORCE_TIME = time.time()
print("Generating All Schedules...")
POWER_SET = power_set(EVENT_NAMES) 
print("Finding best schedule...")
BEST_SUBSET = brute_force(POWER_SET, EVENTS, CONSTRAINT, TIME_MAX, BUDGET)
BRUTE_FORCE_TIME = time.time()-BRUTE_FORCE_TIME

# output prints
print("\n========================================\nEVENT PLANNER - RESULTS\n========================================")
print("Input File:",FILE_INPUT)
print("Maximum Events:",ACTIVITIES_MAX)
print("Available Time:",TIME_MAX,"hours")
print("Available Budget:",str(BUDGET)+"$")
print("All events:")
for activity in EVENT_NAMES:
    print("   -",activity)
print()

print("--- BRUTE FORCE ALGORITHM ---")
print("Selected Activities:",BEST_SUBSET) 
for activity in BEST_SUBSET:
    print("   -",activity)

TIME, COST, ENJOYMENT = score_schedule(BEST_SUBSET, EVENTS) 
print("Total Enjoyment:",ENJOYMENT)
print("Total Time Used:",TIME)
print("Total Cost:",COST,"\n")
print("Execution Time:",BRUTE_FORCE_TIME,"seconds")
