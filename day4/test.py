# open our input file
fh = open("input.txt", "r")

# init total count
total = 0

# loop through lines of the file
for line in fh:
    # remove trailing newline, if it exists
    line = line.strip()

    # split something like 2-4,3-4 into various components
    a, b = line.split(",")
    c, d = a.split("-")
    e, f = b.split("-")

    # if e and f are between c and d, increase count
    if int(e) >= int(c) and int(e) <= int(d) and int(f) >= int(c) and int(f) <= int(d):
        total += 1
    # elif c and d are between e and f, increase count
    elif (
        int(c) >= int(e) and int(c) <= int(f) and int(d) >= int(e) and int(d) <= int(f)
    ):
        total += 1
# print the final total
print(total)
