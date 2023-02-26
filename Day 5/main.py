import sys
import funcs

if len(sys.argv) == 1:
    print("Failed to provide data document.")
    sys.exit(-1)

sl = funcs.readData(sys.argv[1])

# for each binary boarding pass => find seat
greatest_bp = 0
for idx, bp in enumerate(sl):
    cur_bp_val = (funcs.findBinaryPos(bp[:8], 127, "F")
                  * 8
                  + funcs.findBinaryPos(bp[-3:], 7, "L"))
    print("%d BP : %d." % (idx, cur_bp_val))
    if cur_bp_val > greatest_bp:
        greatest_bp = cur_bp_val

print("The highest unique seat id found is %d." % greatest_bp)
