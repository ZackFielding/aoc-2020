def readData(fs):
    f = open(fs, "r", 1, "ascii", "None", "\n")

    # list of lists of dicts
    # list of groups
    # each element of the list if one group
    # each group is a list of dictionaries
    group = 0
    person = 0
    lld = [[dict([(person, set())])]]

    # clear up previous append if no new group memember follows
    def rem_prev_append(group, person):
        lld[group][person].pop(person)
        del lld[group][person]

    for line in f:
        if line != "\n":
            for c in line:
                if c != "\n":
                    lld[group][person][person].add(c)
                else:
                    person += 1
                    lld[group].append(dict([(person, set())]))
        else:
            # if previous person has an empty set => delete them
            if len(lld[group][person][person]) == 0:
                rem_prev_append(group, person)

            group += 1
            person = 0
            lld.append([dict([(person, set())])])

    # no isolated newline char at EOF (handle line 27 here for last index)
    rem_prev_append(group, person)

    # close file && return list of list of dictionaries
    f.close()
    return lld


def solut_func(lldis, func):
    # determine the number of unique chars across entire group
    # iterate over each person in group
    # creating a set based on unique chars
    # gset = set()
    # gset needs to be set to first group memember
    # or else `&` will not work
    sum = 0
    for group in lldis:
        gset = group[0][0]
        idx = 1
        for person in group[1:]:
            gset = func(gset, person, idx)
            idx += 1
        sum += len(gset)
    return sum
