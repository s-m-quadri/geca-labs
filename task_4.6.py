# Task 4.6: Challenge – Activity Selection Problem
# ----------------------------------------------
# This is a classic greedy scheduling problem.
#
# Problem:
# You are given n activities with start and finish times.
# Select the maximum number of activities that can be performed by one person,
# assuming that a person can only work on a single activity at a time.
#
# Input:
# - List of activities with (start_time, finish_time)
#
# Output:
# - Maximum number of non-overlapping activities that can be performed.
#
# Example:
# Activities = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
# Output: 4 activities (choose: (1,2), (3,4), (5,7), (8,9))
#
# Hint: Sort activities by finish time, then pick the next compatible activity.
#
# This is your challenge task for the nerds!
# ----------------------------------------------
# Task 4.6: Challenge – Activity Selection Problem
# ----------------------------------------------

def activity_selection(activities):
    """
    Selects the maximum number of activities that can be performed
    by a single person, assuming only one activity at a time.
    
    activities: list of tuples (start_time, finish_time)
    """
    
    # Step 1: Sort activities by their finish time
    activities.sort(key=lambda x: x[1])
    
    selected = []  # To store selected activities
    last_finish_time = 0  # Track when the last activity finished
    
    # Step 2: Select first activity and then greedily check others
    for start, finish in activities:
        if start >= last_finish_time:
            selected.append((start, finish))
            last_finish_time = finish
    
    return selected


# Example usage:
activities = [
    (1, 3),
    (2, 5),
    (4, 6),
    (6, 8),
    (5, 7),
    (8, 9)
]

selected_activities = activity_selection(activities)

print("Selected activities (start, finish):")
for act in selected_activities:
    print(act)
