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

def activity_selection(activities):
    # Step 1: Sort activities by their finish time
    activities.sort(key=lambda x: x[1])
    
    selected_activities = []
    last_finish_time = -1  # Initialize to a time before any activity starts
    
    # Step 2: Iterate and select activities
    for start, finish in activities:
        if start >= last_finish_time:
            selected_activities.append((start, finish))
            last_finish_time = finish
    
    return selected_activities

# Example usage
activities = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
selected = activity_selection(activities)

print("Maximum number of activities:", len(selected))
print("Selected activities:", selected)
