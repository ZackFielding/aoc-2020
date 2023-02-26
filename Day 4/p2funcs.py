def validateCriteria(valid_idxs):
    func_dict = {"byr": fbyr, "iyr": fiyr, "eyr": feyr,
                 "hgt": fhgt, "hcl": fhcl, "ecl": fecl,
                 "pid": fpid}
    num_valid_pass_found = 0

    for idx, cur_pass in enumerate(valid_idxs):
        cur_crit_valid_counter = 7
        for cur_crit in list(func_dict):
            # get position of current substring
            pos = cur_pass.find(cur_crit)
            # check to ensure substring was found
            if pos < 0:
                print("ERROR: Failure to find substring index...")
                break
            if func_dict[cur_crit](getSlice(cur_pass, pos+4)):
                cur_crit_valid_counter -= 1
            else:
                print("Passport %d failed %s." % (idx, cur_crit))
        if cur_crit_valid_counter == 0:
            num_valid_pass_found += 1
            print("%d passport passed all conditions." % idx)
    # return
    return num_valid_pass_found


def getSlice(str_file, spos):
    offset = 0
    for c in str_file[spos:]:
        if c == ' ' or c == '\n':
            break
        else:
            offset += 1
    # return slice
    # print("SUBSTRING : " + str_file[spos:spos+offset])
    return str_file[spos:spos+offset]


def fbyr(crit):
    if len(crit) != 4:
        return False
    if int(crit) >= 1920 and int(crit) <= 2002:
        return True
    return False


def fiyr(crit):
    if len(crit) != 4:
        return False
    if int(crit) >= 2010 and int(crit) <= 2020:
        return True
    return False


def feyr(crit):
    if len(crit) != 4:
        return False
    if int(crit) >= 2020 and int(crit) <= 2030:
        return True
    return False


def fhgt(crit):
    if len(crit) <= 2:
        return False
    # slices
    unit = crit[-2:]  # cm or in
    mag = int(crit[:-2])  # int
    # print("UNIT %s ... MAG %d" % (unit, mag))

    if unit == "cm":
        if mag >= 150 and mag <= 193:
            return True
    elif unit == "in":
        if mag >= 59 and mag <= 76:
            return True
    return False


def fhcl(crit):
    if crit[0] != '#':
        return False

    if len(crit[1:]) != 6:
        return False

    count = 0
    for cur in crit[1:]:
        if cur.isdecimal() or (cur >= "a" and cur <= "f"):
            count += 1
        else:
            break

    if count == 6:
        return True
    return False


def fecl(crit):
    if len(crit) != 3:
        return False

    fs = frozenset(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    if crit in fs:
        return True
    return False


def fpid(crit):
    if len(crit) == 9 and crit.isdecimal():
        return True
    return False
