import sys


def readData(file_str):
    # 1. open file and get line length from discarded first row
    df = open(file_str, 'r', 1, "ascii", "replace", '\n')
    slist = []
    line_len = len(df.readline())-1
    for cur_line in df:
        slist.append(cur_line[:line_len+1])
    print("Line length: " + str(line_len))
    return slist, line_len


def countTrees(slist, line_len, r_step, d_step):
    # set right step pos to start at right step width
    pos = r_step
    tree_counter = 0
    line = 0
    # adjust down step starting point
    line = d_step - 1

    while line < len(slist):
        if slist[line][pos] == '#':
            tree_counter += 1
        pos += r_step
        # check to see if next pos is > line length
        if pos >= line_len:
            pos -= line_len
        # increment by given downward step
        line += d_step

    print(f"Number of trees: {tree_counter}.")
    return tree_counter


# main
if len(sys.argv) <= 1:
    print("Failure to provide file ... terminating.")
    sys.exit(-1)

# list of strings, line_length
res_tup = readData(sys.argv[1])


p1_num_trees = countTrees(res_tup[0], res_tup[1], 3, 1)
print(f"Number of trees encountered in part 1: {p1_num_trees}.")

# list of tuples
mov_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

tree_product = 1
for right, down in mov_list:
    tree_product *= countTrees(res_tup[0], res_tup[1], right, down)
print(f"Product of trees encountered in part 2: {tree_product}.")
