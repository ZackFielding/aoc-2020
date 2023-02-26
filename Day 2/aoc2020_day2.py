# AoC 2020 Day 2 Solution
# read in data
def readDataAndCheckPasswords():
    # 'r' for read only, 'w' for write only, 'r+' for both
    file = open("data.txt", 'r')
    num_valid_passwords_p1 = 0
    num_valid_passwords_p2 = 0

    for line in file:
        # establish comparisons
        tup = findInt(line, 0, '-')
        min = tup[0]
        tup = findInt(line, tup[1], ' ')
        max = tup[0]
        coi = line[tup[1]]
        # keep track of number of times coi is found
        count = 0

        # p1
        start_pos = tup[1] + 3
        for idx in range (start_pos, len(line)):
            # if matches
            if (line[idx] == coi):
                count += 1
            # if max found => stop (in-valid password)
            if count > max:
                break
        # if entire password was read (i.e., max never reached)
        if (count >= min and count <= max):
            num_valid_passwords_p1 += 1

        # p2
        if line[start_pos + (min-1)] == coi or line[start_pos + (max-1)] == coi:
            if line[start_pos + (min-1)] != coi or line[start_pos + (max-1)] != coi:
                num_valid_passwords_p2 += 1

    file.close()
    # return tuple of p1 and p2 answers
    return (num_valid_passwords_p1, num_valid_passwords_p2)

def findInt(line_str, start_pos, term_char):
    for idx in range (start_pos, len(line_str)):
        if line_str[idx] == term_char:
            break

    out = int(line_str[start_pos:idx])
    idx += 1 # +1 for slice to work
    return (out, idx)

# main
ans_tup = readDataAndCheckPasswords()
    # p1 solution
print(f"P1. Number of valid passwords found: {ans_tup[0]}")
    # p2 solution
print(f"P2. Number of valid passwords found: {ans_tup[1]}")
