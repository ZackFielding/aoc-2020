import sys
import funcs


def main():
    if len(sys.argv) < 2:
        print("Failed to provide data ... terminating program.")
        sys.exit(-1)

    # return dictionary of string, bag class instances
    bags_dict = funcs.createDS(sys.argv[1])

    # test
    # funcs.printHeldBags(bags_dict)

    # get view of objects in dict for p1
    dview = bags_dict.values()

    # p1 solution
    bag_count = funcs.countBagsThatHold(dview, "shiny gold")
    print("{} bags can hold a \"shiny gold\" bag".format(bag_count))

    # p2 solution
    sub_bag_count = (funcs.r_countSubBags(bags_dict, "shiny gold") - 1)
    print(("{} bags contained in a single \"shiny gold\" bag"
           .format(sub_bag_count)))


if __name__ == "__main__":
    main()
