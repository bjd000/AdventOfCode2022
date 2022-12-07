if __name__ == "__main__":
    infile = open("data/test.txt", "r")
    curr = ""
    stk = []
    m = {}
    count = 0
    for line in infile:
        words = line.split()

        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "..":
                    curr = stk.pop(0)
                    count += 1
                elif words[2] == "/":
                    curr = str(count) + "/"
                    stk.insert(0, curr)
                else:
                    curr = str(count) + curr + "/" + words[2]
                    stk.insert(0, curr)
        elif words[0] == "dir":
            x = 1
        else:
            for i in stk:
                tot = m.get(i, 0)
                tot += int(words[0])
                m[i] = tot
    infile.close()
    total = 0
    print(m)
    for k in m:
        v = m[k]
        if v <= 100000:
            total += v
    print(total)
