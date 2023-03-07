import funcs

if __name__ == "__main__":
    # read file
    f = open("case_data.txt", mode="r", newline="\n")
    data = []
    for line in f:
        data.append(line)
    f.close()

    # p1 solution
    eis = set()
    accumulator_p1 = funcs.executeInstructions(0, data, eis, 0)
    print("Accumulator value prior to repeat instruction: %d."
          % accumulator_p1[1])

    # p2 solution
    accumulator_p2 = funcs.executeModifiedInstructions(data)
    print("Accumulator post infinite-loop resolution: %d."
          % accumulator_p2)
