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

from typing import List, Tuple


def activity_selection(activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Select the maximum number of non-overlapping activities.
    activities: list of (start, finish)
    Returns list of selected activities sorted by finish time.
    """
    if not all(isinstance(s, int) and isinstance(f, int) for s, f in activities):
        raise TypeError("activities must be list of (int, int)")
    # sort by finish time
    sorted_acts = sorted(activities, key=lambda x: x[1])
    selected = []
    last_finish = -float("inf")
    for s, f in sorted_acts:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f
    return selected


if __name__ == "__main__":
    acts = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    chosen = activity_selection(acts)
    print("Selected activities:", chosen)
