from pathlib import Path

# relative directory
BASE_DIR = Path(__file__).parent

"""
Input function  
    - Opens an input file via a relative path and processes it into 3 ints and an event dictionary 
    - The event dictionary is structured such that the event name is the key and the data per key is a tuple containing the time, cost, and enjoyment value. example: {Karaoke: (2, 100, 200) 
    - The path to the input files assumes that the program is in the same directory as a folder named “inputs” containing the input txt files 
    - Accepts: input file name as str (i.e. “input_small.txt”) 
    - Returns: tuple containing (activities, time, budget, event dictionary) 
"""
def load_input(name):
    # relative file pathing
    file_path = BASE_DIR / "inputs" / name
    text = file_path.read_text(encoding="utf-8")
    
    # split file input text into lines, remove the last empty line
    lines = text.split("\n")
    lines.pop()

    activities = lines[0]

    time_budget = lines[1].split(" ")
    time, budget = time_budget[0], time_budget[1]

    events = {}

    # loop through the lines and assemble the dictionary, ignore first two lines and empty last line
    for i in range(2,len(lines)):
        line = lines[i].split(" ")
        data = line[1],line[2],line[3]
        events[line[0]]=data

    return int(activities), int(time), int(budget), events

"""
Schedule scoring function
    - accepts a proposed schedule, the list of events and their properties
    - returns the total time, cost, and enjoyment of the proposed schedule
"""
def score_schedule(schedule, events):
    total_time = 0
    total_cost = 0
    total_enjoyment = 0

    # catch case where no activities passed in
    if len(schedule)  == 0:
        return 0, 0, 0   
    # loop through each activity looking up its time, cost, and enjoyment value from events
    for index in range(0, len(schedule)): 
        curr_act_data = events[schedule[index]] 
        total_time += int(curr_act_data[0]) 
        total_cost += int(curr_act_data[1]) 
        total_enjoyment += int(curr_act_data[2]) 
    return total_time, total_cost, total_enjoyment

"""
Brute force algorithm
    - generates every possible schedule and keeps track of the best schedule as they are generated
    - Accepts:
        - a list of the names of the events (for keying) 
        - the event-properties dictionary
        - the constraint to be considered ("time","budget, or "both)
        - the maximum time allowed
        - the maximum cost allowed
    - returns the best schedule generated
"""
def brute_force(events, event_list, constraint, max_time, budget):
    result = [[]]
    max_score = 0 
    best_schedule = [] 

    for i in events:
        subsets = []
        for subset in result:
            subset = subset + [i]
            subsets.append(subset)
            time, cost, enjoyment = score_schedule(subset, event_list) 
            
            # check if subset has highest happiness so far
            if enjoyment > max_score: 
                # ensure the subset follows selected constraint and if so make it new best schedule
                if constraint == "time": 
                    if time <= max_time: 
                        best_schedule = subset
                        max_score = enjoyment 
                elif constraint == "cost": 
                    if cost <= budget: 
                        best_schedule = subset
                        max_score = enjoyment 
                elif constraint == "both": 
                    if (time <= max_time) and (cost <= budget): 
                        best_schedule = subset
                        max_score = enjoyment 
                else:
                    print("invalid constraint")
        result.extend(subsets)
    
    return best_schedule
