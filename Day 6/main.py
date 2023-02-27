import sys
import funcs

if len(sys.argv) == 1:
    print("[ERROR] failed to provide data file.")
    sys.exit(-1)

# read data into list of strings
# returns a list of lists of dictionaries {int, set(chars)}
lldis = funcs.readData(sys.argv[1])

p1_ans = funcs.solut_func(lldis, lambda a, b, c: a | b[c])
print("[P1] %d sum of uniques \'yes\' found across all groups." % p1_ans)

p2_ans = funcs.solut_func(lldis, lambda a, b, c: a & b[c])
print(("[P2] %d sum of \'yes\' in which all person(s) of a group answered."
       % p2_ans))
