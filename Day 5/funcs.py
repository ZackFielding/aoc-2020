def readData(file_str):
    file = open(file_str, 'r', 1, "ascii", "None", "\n")
    sl = []
    for line in file:
        sl.append(line[:-1])
    file.close()
    return sl


# p1 solution
# boarding pass, upper bound, lower move char
def findBinaryPos(bp, ub, lmc):
    # upper bound (+1 to make the math easier)
    ub = ub+1
    # lower bound
    lb = 0
    # first seven chars are front/back splitting
    for move in bp:
        # compute half
        cph = (ub-lb)/2
        if move == lmc:
            ub = lb + cph
        else:
            lb = ub-cph
    # correct for rows being 0-indexed
    ub -= 1
    return ub


# p2 solution
# returns -1 if missing seat not found
def findMissingSeat(seatidl):
    # iterate through sorted list and
    # find gap that == 2
    for pos in range(len(seatidl)-1):
        # if gap of 2 found => return missing seat id (+1)
        if seatidl[pos+1] - seatidl[pos] == 2:
            return seatidl[pos] + 1

    # error
    return -1