import sys
import funcs

if len(sys.argv) == 1:
    print("Failed to provide data document.")
    sys.exit(-1)

sl = funcs.readData(sys.argv[1])

# for each binary boarding pass => find seat
greatest_bp = 0
seatidl = []
for idx, bp in enumerate(sl):
    cur_bp_val = (funcs.findBinaryPos(bp[:8], 127, "F")
                  * 8
                  + funcs.findBinaryPos(bp[-3:], 7, "L"))

    # print("%d BP : %d." % (idx, cur_bp_val))

    # add to list [p2]
    seatidl.append(cur_bp_val)

    # check to see if current greatest [p1]
    if cur_bp_val > greatest_bp:
        greatest_bp = cur_bp_val

print("The highest unique seat id found is %d." % greatest_bp)

# p2
# sort list
seatidl.sort()

my_seat = funcs.findMissingSeat(seatidl)
if my_seat == -1:
    print("[ERROR] Missing seat not found.")
else:
    print("Missing unique seat id: %d" % my_seat)
