"""
RIDDLE: Crossing a Bridge
A zombie is chasing you and your companions. You come across a bridge which can only allow 2 people to cross at one time.
It is dark so you need to bring a lamp to see your way across. Each of you have different times it will take to cross the bridge.
You take 1 minute to cross, the lab assistant takes 2 minutes, the janitor takes 5 minutes, and the professor takes 10 minutes.
Crossing the bridge will go at the speed of the slowest person. The zombie will get to you in 17 minutes. 
How do you get across?
"""

import itertools

timeToCross = [10, 5, 2, 1]
foundPaths = []

"""
crossingToEnd : bool
    indicates if current crossing is towards end of bridge (False if crossing to start)
movingPeople : list[int]
    the pair or individual attempting to cross
start : list[int]
    the list of people at the start of the bridge
end : list[int]
    the list of people at the end of the bridge
path : list[(bool, list[int])]
    the list of all crossings made, tuple containing direction (crossingToEnd) and pair/individual crossing
"""
def crossing(crossingToEnd, movingPeople, start, end, path):
    # if same pair movement occurred at least twice before, end search
    if (crossingToEnd and path.count((crossingToEnd, movingPeople)) >= 2): return
    path.append((crossingToEnd, movingPeople))

    if crossingToEnd:
        start = list(set(start) - set(movingPeople))
        end.extend(movingPeople)

        # if all people have successfully crossed
        if (len(start) == 0):
            minutes = 0
            moves = []
            for move in path:
                minutes += max(move[1])
                moves.append(move[1])
            # append to found list for final results
            foundPaths.append((minutes, moves))
            return

        for person in end:
            crossing(False, [person], start.copy(), end.copy(), path.copy()) # copy lists so branches don't add to each other
    else:
        end = list(set(end) - set(movingPeople))
        start.extend(movingPeople)

        for pair in list(itertools.combinations(start, 2)):
            sortedPair = list(pair)
            sortedPair.sort(reverse=True) # Sort since order doesn't matter i.e. [2,1] = [1,2]
            crossing(True, sortedPair, start.copy(), end.copy(), path.copy()) # copy lists so branches don't add to each other

# iterate through all initial pairs
for initialPair in list(itertools.combinations(timeToCross, 2)):
    sortedPair = list(initialPair)
    sortedPair.sort(reverse=True) # Sort since order doesn't matter i.e. [2,1] = [1,2]
    crossing(True, sortedPair, timeToCross.copy(), [], [])

# display result sorted by lowest time
for minutes, path in sorted(foundPaths, key=lambda x:x[0]):
    print(f"{minutes} minutes, Path: {path}")