def createDS(fs):
    file = open(fs, 'r', 1, "ascii", "None", "\n")
    # dictionary [key == string, value == list of n tuples(int, string)]
    dtup = {}

    for idx, cur_line in enumerate(file):

        # get holding bag string [tuple (string, last ws pos)]
        key_tup = getSplice(cur_line, 0)

        # create bag instance and set class.id
        dtup[key_tup[0]] = bag(key_tup[0])

        # set bags
        dtup[key_tup[0]].createBagListAndSet((cur_line[key_tup[1]:]))

    file.close()
    return dtup


def getSplice(line, spos):
    wsf = False
    for idx in range(spos, len(line)):
        # count white spaces
        if line[idx] == ' ':
            if not wsf:
                wsf = True
            else:
                # return substring of current bag
                return line[spos:idx], idx+13
    # error == empty string
    return ""


# testing
def printHeldBags(bags_dict):
    v_bags_dict = bags_dict.values()
    for v in v_bags_dict:
        print("{} {}".format(v.num_bag_list, v.bag_set))


# p1
def countBagsThatHold(dview, bag_of_interest):
    # create queue of bags that have not been visited
    from collections import deque

    q = deque([bag_of_interest])
    # track bags that have been visited
    visited = set()
    # track bags that have been added to deque that have
    # not been added to `visited`
    added = set()
    # -1 to exclude `bag_of_interest`
    bag_count = -1

    while True:
        # pop off next bag in queue
        # if queue is empty => break
        cur_bag = getNextBag(q, visited)
        if cur_bag != "":
            bag_count += 1
            visited.add(cur_bag)
            # print("{} visited".format(cur_bag))  # dbug
            added.clear()  # clear set for next loop
        else:
            break

        # if current bag is in this bags "can hold"
        # and is not already in the queue
        # or has been visited => add to queue
        for inst in dview:
            # print("Current bag: {}".format(cur_bag), end=' ')
            # print("... bag set: {}".format(inst.bag_set), end=' ')
            # print("... in bag: {}".format(inst.id))
            if cur_bag in inst.bag_set:
                if inst.id not in visited and cur_bag not in added:
                    q.appendleft(inst.id)

    return bag_count


def getNextBag(q, visited):
    while True:
        if len(q) > 0:
            cur_bag = q.pop()
            if cur_bag not in visited:
                return cur_bag
        else:
            return ""


# recrusive function
def r_countSubBags(d, bag_of_interest):
    # base case [if no sub bags => return 1 so count*bag != 0]
    if len(d[bag_of_interest].bag_set) == 0:
        # print("... base case ....")
        return 1

    # get instance from dictionary
    inst = d[bag_of_interest]

    sub_sum = 0
    for b in inst.bag_set:
        sub_sum += (r_countSubBags(d, b) *
                    inst.num_bag_dict[b])

    return sub_sum+1


# abstraction of each bag (name && other bags it can hold)
class bag:
    def __init__(self, id_arg):
        self.id = id_arg
        self.num_bag_dict = {}
        self.bag_set = set()

    def createBagListAndSet(self, slice):
        # find each pos in `line` which .isdecimal() returns True
        dli = bag.findDecimalInstances(slice)

        # get slices of each bag string
        # (ignore position return from getSplice())
        for i_instance in dli:
            bag_str = getSplice(slice, i_instance+2)[0]
            self.num_bag_dict[bag_str] = int(slice[i_instance])
            self.bag_set.add(bag_str)

    @staticmethod
    def findDecimalInstances(string):
        # iterate through string slice and find
        # all instance of an integer
        li = []
        for idx, cur in enumerate(string):
            if cur.isdecimal():
                li.append(idx)

        # case: bag holds no bags
        if len(li) == 0:
            return []

        # error check => if any indxs are adjacent,
        # approach needs to be adjusted (can't handle int >9)
        for i in range(len(li)-2):
            if li[i] - li[i+1] == -1:
                print("ERROR .... integer >9 found in bag count!")

        # still return list to calling func
        return li
