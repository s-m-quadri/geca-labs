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


# Task 4.6: Challenge – Activity Selection Problem
# ------------------------------------------------

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    last_finish_time = 0 

    # Step 2: Iterate through sorted activities
    for start, finish in activities:
        if start >= last_finish_time:
            selected_activities.append((start, finish))
            last_finish_time = finish  # Update finish time

    return selected_activities


if __name__ == "__main__":
    activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    selected = activity_selection(activities)

    print("Selected activities:", selected)
    print("Maximum number of non-overlapping activities:", len(selected))

