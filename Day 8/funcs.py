def accumulateOrJump(to_return, ival, pos_pol):
    if pos_pol:
        to_return += ival
        return to_return

    to_return -= ival
    return to_return


def executeInstructions(accumulator, data, eis, idx):
    pos_pol = True
    while True:
        # non-infinite loop condition met
        if idx >= len(data):
            return True, accumulator

        # infinite condition loop found
        if idx in eis:
            return False, accumulator

        # add to set
        eis.add(idx)

        instruct = data[idx][:3]
        # print(instruct)
        if instruct == "nop":
            idx += 1
            continue

        # determine polarity
        if data[idx][4] == "-":
            pos_pol = False
        else:
            pos_pol = True

        # get integer
        ival = int(data[idx][5:-1])

        if instruct == "acc":
            accumulator = accumulateOrJump(accumulator, ival, pos_pol)
            idx += 1
        else:
            idx = accumulateOrJump(idx, ival, pos_pol)


def executeModifiedInstructions(data):
    accumulator = 0
    idx = 0
    pos_pol = True
    eis = set()
    while True:
        # print("{}".format(idx))
        # add to set
        # dont need to check if in set => this loop should never repeat
        eis.add(idx)

        # determine polarity
        if data[idx][4] == "-":
            pos_pol = False
        else:
            pos_pol = True

        instruct = data[idx][:3]  # op
        ival = int(data[idx][5:-1])  # value to apply to op

        # determine polarity
        if data[idx][4] == "-":
            pos_pol = False
        else:
            pos_pol = True

        if instruct == "acc":
            accumulator = accumulateOrJump(accumulator, ival, pos_pol)
            idx += 1
            continue

        set_copy = eis
        if instruct == "nop":
            # treat as jmp and cont
            adj_idx = accumulateOrJump(idx, ival, pos_pol)
            tup = executeInstructions(accumulator, data, set_copy, adj_idx)
            if not tup[0]:
                idx += 1
                continue
        else:
            # treat as nop
            tup = executeInstructions(accumulator, data, set_copy, idx+1)
            if not tup[0]:
                idx = accumulateOrJump(idx, ival, pos_pol)
                continue

        if tup[0]:
            return tup[1]

    # error => should never reach this point
    return -1
