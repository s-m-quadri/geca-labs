def activity_selection(activities):
    """
    Greedy algorithm for activity selection problem.
    
    Args:
        activities: List of tuples (start_time, finish_time)
    
    Returns:
        tuple: (max_activities, selected_activities)
        selected_activities is list of selected (start, finish) tuples
    """
    if not activities:
        return 0, []

    # Sort activities by finish time
    # Add original index to track which activities we select
    indexed_activities = [(start, finish, i) for i, (start, finish) in enumerate(activities)]
    indexed_activities.sort(key=lambda x: x[1])  # Sort by finish time

    selected = []
    last_finish_time = float('-inf')

    for start, finish, original_index in indexed_activities:
        # If this activity starts after the last selected activity finishes
        if start >= last_finish_time:
            selected.append((start, finish))
            last_finish_time = finish

    return len(selected), selected

def print_activity_solution(activities, max_count, selected):
    """Print detailed solution of activity selection problem."""
    print(f"Input activities: {activities}")
    print(f"Maximum non-overlapping activities: {max_count}")
    print(f"Selected activities: {selected}")

    # Show timeline visualization
    print("\nTimeline visualization:")
    all_times = set()
    for start, finish in activities:
        all_times.add(start)
        all_times.add(finish)

    min_time = min(all_times) if all_times else 0
    max_time = max(all_times) if all_times else 0

    print(f"Time range: {min_time} to {max_time}")

    # Show selected activities
    print("Selected activities timeline:")
    for i, (start, finish) in enumerate(selected):
        timeline = ['-'] * (max_time - min_time + 1)
        for t in range(start - min_time, finish - min_time):
            if t < len(timeline):
                timeline[t] = str(i + 1)
        print(f"Activity {i+1} ({start},{finish}): {''.join(timeline)}")

def is_valid_selection(selected_activities):
    """Verify that selected activities don't overlap."""
    for i in range(len(selected_activities)):
        for j in range(i + 1, len(selected_activities)):
            start1, finish1 = selected_activities[i]
            start2, finish2 = selected_activities[j]

            # Check if activities overlap
            if not (finish1 <= start2 or finish2 <= start1):
                return False, f"Activities {selected_activities[i]} and {selected_activities[j]} overlap"

    return True, "All activities are non-overlapping"

if __name__ == "__main__":
    # Test case from the example
    activities1 = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]

    print("Test Case 1:")
    print("=" * 60)
    max_count1, selected1 = activity_selection(activities1)
    print_activity_solution(activities1, max_count1, selected1)

    # Verify solution
    is_valid, message = is_valid_selection(selected1)
    print(f"Solution validation: {message}")
    print()

    # Additional test case
    activities2 = [(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]

    print("Test Case 2:")
    print("=" * 60)
    max_count2, selected2 = activity_selection(activities2)
    print_activity_solution(activities2, max_count2, selected2)

    # Verify solution
    is_valid2, message2 = is_valid_selection(selected2)
    print(f"Solution validation: {message2}")
    print()

    # Edge case: No activities
    activities3 = []
    print("Test Case 3 (Empty input):")
    print("=" * 60)
    max_count3, selected3 = activity_selection(activities3)
    print(f"Input activities: {activities3}")
    print(f"Maximum activities: {max_count3}")
    print(f"Selected activities: {selected3}")