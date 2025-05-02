# Arrays (Merge Overlapping Intervals)



def mergeOverlappingIntervals(intervals):

    sortedIntervals = sorted(intervals, key = lambda x: x[0])
    mergedIntervals = []
    currentInterval = sortedIntervals[0]

    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            mergedIntervals.append(nextInterval)
            currentInterval = nextInterval
    return mergedIntervals

# Example usage
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
merged = mergeOverlappingIntervals(intervals)
print(merged) 