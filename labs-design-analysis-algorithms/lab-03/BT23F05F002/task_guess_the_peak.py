# Puzzle / Learning focus:
# - You are given a “mountain array” (numbers increase then decrease).
# - Your task is to find the peak element using binary search ideas.
# - Think carefully about how to compare neighbors to detect the peak.
#
# Example test cases:
# Input: [1, 3, 7, 12, 9, 5, 2]
# Output: 12
#
# Input: [0, 2, 4, 6, 3, 1]
# Output: 6


def peak_index(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < arr[m + 1]:
            l = m + 1
        else:
            r = m
    return l

def peak_value(arr):
    return arr[peak_index(arr)]

def main():
    tests = [
        [1, 3, 7, 12, 9, 5, 2],
        [0, 2, 4, 6, 3, 1],
        [1, 2, 3, 4, 3, 2, 1],
        [2, 5, 9, 11, 10],
    ]
    for t in tests:
        idx = peak_index(t)
        print(f"Input: {t} -> Peak index: {idx}, Peak value: {t[idx]}")

if __name__ == "__main__":
    main()
