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


# DOES NOT WORK
# Hitting max recruse limit
# but I think that's because of an error
def quicksort_list(lb, ub, arr):
    if lb >= ub:
        return

    lptr = lb
    pivot = ub
    rptr = pivot - 1

    swap = 0
    while (1):
        # move lptr (find value < pivot)
        while (arr[lptr] < arr[pivot]):
            # print("%d is not less than %d" % (arr[lptr], arr[pivot]))
            lptr += 1
        while (arr[rptr] > arr[pivot] and rptr >= 0):
            rptr -= 1

        # cache lptr value
        swap = arr[lptr]
        if lptr >= rptr:
            # if lptr has passed or is equal to rptr
            # swap lptr with pivot and terminate loop
            arr[lptr] = arr[pivot]
            arr[pivot] = swap
            break
        else:
            # if values are equal => increment both (no need to swap)
            if arr[lptr] == arr[rptr]:
                lptr += 1
                rptr -= 1
            else:
                arr[lptr] = arr[rptr]
                arr[rptr] = swap

    # recrusive calls
    # sort bottom half
    if lptr > 0:
        new_ub = lptr - 1
        quicksort_list(lb, new_ub, arr)
    if lptr < len(arr)-1:
        new_lb = lptr + 1
        quicksort_list(new_lb, ub, arr)
    return
