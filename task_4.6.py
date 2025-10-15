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
# Task 4.6: Activity Selection (Greedy)
# ------------------------------------
# Sort activities by finish time, then pick the next activity whose start
# is >= the finish time of the last selected activity.

def activity_selection(activities):
    """
    activities: list of tuples (start, finish)
    Returns: (selected_count, selected_activities_list)
    """
    if not activities:
        return 0, []

    # Sort by finish time (ascending). If finish times tie, stable sort keeps original order.
    activities_sorted = sorted(activities, key=lambda x: x[1])

    selected = []
    last_finish = -float("inf")

    for start, finish in activities_sorted:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return len(selected), selected


# Example usage
if __name__ == "__main__":
    activities = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
    count, chosen = activity_selection(activities)
    print("Max activities:", count)
    print("Chosen activities:", chosen)
