import funcs
import p2funcs
import sys
# main
# get text str from command line
if len(sys.argv) <= 1:
    print("Failed to enter text file ... terminating.")
    sys.exit(-1)

str_list = funcs.readData(sys.argv[1])
valid_tup = funcs.findValidPassports(str_list)
print(f"[PART 1] Number of valid passports found: {valid_tup[0]}.")

ip2_ret = p2funcs.validateCriteria(valid_tup[1])
print(f"[PART 2] Number of valid passports found: {ip2_ret}.")
# print(str_list[1][len(str_list[1])-2])
