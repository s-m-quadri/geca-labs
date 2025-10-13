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

def activity_selection(a):
    a.sort(key=lambda x: x[1])
    n = len(a)
    if n == 0:
        return 0, []
    c = 1
    s = [a[0]]
    lf = a[0][1]
    for i in range(1, n):
        if a[i][0] >= lf:
            s.append(a[i])
            c += 1
            lf = a[i][1]
    return c, s

if __name__ == "__main__":
    a = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    m, s = activity_selection(a)
    print(f"Maximum number of non-overlapping activities: {m}")
    print(f"Selected activities: {s}")
