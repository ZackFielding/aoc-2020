def readData(file_str):
    # read data from file into strings
    file = open(file_str, 'r', 1, "ascii", "None", '\n')

    # garuntee that first line is valid
    str_list = [file.readline()]
    b_append = False

    for line in file:
        if line == "\n":
            b_append = True
        else:
            if not b_append:
                end_pos = len(str_list)-1
                # add leading white space
                line = " " + line
                # concat string with current string
                str_list[end_pos] += line[:len(line)]
            else:
                # if previous line was empty => append current string
                str_list.append(line[:len(line)])
                b_append = False
    file.close()
    return str_list


def findValidPassports(str_list):
    # does not include 'cid' currently (p1)
    valid_count = 0
    comp_set = frozenset({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"})
    valid_set = set()
    for idx, passport in enumerate(str_list):
        # create empty set for current case
        cur_set = set()
        for id in comp_set:
            if id in passport:
                cur_set.add(id)

        # now see the difference between the two sets
        dif = comp_set - cur_set
        if len(dif) == 0:
            valid_count += 1
            valid_set.add(passport)

    return valid_count, valid_set
