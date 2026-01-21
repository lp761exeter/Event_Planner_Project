from pathlib import Path

# relative directory
BASE_DIR = Path(__file__).parent

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

def power_set(list):
    result = [[]]

    for i in list:
        subsets = []
        for subset in result:
            subset = subset + [i]
            subsets.append(subset)
        result.extend(subsets)

    return result

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

def brute_force(power_set, event_list, constraint, max_time, budget):
    max_score = 0 
    best_schedule = [] 
    for schedule in power_set: 
        time, cost, enjoyment = score_schedule(schedule, event_list) 
        # check if schedule has highest happieness so far
        if enjoyment > max_score: 
            # ensure the schedule follows selected constraint and if so make it new best schedule
            if constraint == "time": 
                if time <= max_time: 
                    best_schedule = schedule 
                    max_score = enjoyment 
            elif constraint == "cost": 
                if cost <= budget: 
                    best_schedule = schedule 
                    max_score = enjoyment 
            elif constraint == "both": 
                if (time <= max_time) and (cost <= budget): 
                    best_schedule = schedule 
                    max_score = enjoyment 
            else:
                print("invalid constraint")
    return best_schedule