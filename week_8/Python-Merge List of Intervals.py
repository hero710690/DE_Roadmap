# input: [[1,3],[2,6],[8,10],[15,18]]
# output: [[1,6],[8,10],[15,18]]
def find_overlap_interval(intervals):
    intervals.sort(key=lambda x : x[0])
    overlap = []
    
    for invterval in intervals:
        if not overlap or overlap[-1][1] < invterval[0]:
            overlap.append(invterval)
        else:
            overlap[-1][1] = max(overlap[-1][1], invterval[1])
    return overlap            

