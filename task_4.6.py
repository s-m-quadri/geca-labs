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

#solution
def activity_selection(activities):
    """
    Select the maximum number of non-overlapping activities.

    Parameters:
        activities (list of tuples): Each tuple is (start_time, finish_time)

    Returns:
        list: Selected activities (maximum number possible)
    """
    activities = sorted(activities, key=lambda x: x[1])

    selected = []
    last_finish_time = -1  

    for activity in activities:
        start, finish = activity
        if start >= last_finish_time:
            selected.append(activity)
            last_finish_time = finish  

    return selected

# Example (very important)

activities1 = [(0,3), (1,2), (3,5), (4,6), (5,7), (6,8), (7,9)]
selected_activities1 = activity_selection(activities1)
print("\nExample 1:")
print("Maximum number of activities:", len(selected_activities1))
print("Selected activities:", selected_activities1)


activities2 = [(6,8), (1,4), (2,3), (4,7), (5,9)]
selected_activities2 = activity_selection(activities2)
print("\nExample 2:")
print("Maximum number of activities:", len(selected_activities2))
print("Selected activities:", selected_activities2)