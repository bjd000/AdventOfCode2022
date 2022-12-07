""" did not make this one on my own.  I was close on the first part, 
but stuggled with the running totals.  This site was a big help:

https://bloggingintensifies.com/advent-of-code-2022-day-7/

"""


def main(file: str):

    with open(file, "r") as f:
        data = f.read().split("\n")

    fs: dict = {"/": 0}  # filesystem
    pwd: list = []  # present working directory

    for line in data:
        args = line.split(" ")
        if args[0] == "$":
            if args[1] == "cd":
                if args[2] == "/":
                    pwd = ["/"]
                elif args[2] == "..":
                    pwd.pop()
                else:
                    pwd.append(args[2])
        elif args[0] == "dir":
            fs["".join(pwd) + args[1]] = 0
        else:
            for step in range(0, len(pwd)):
                fs["".join(pwd[0 : step + 1])] += int(args[0])
    # print(fs)

    needed_space = 30000000 - (70000000 - fs["/"])
    size_to_delete = fs["/"]
    total = 0
    for key in fs.keys():
        if fs[key] <= 100000:
            total += fs[key]
        if fs[key] > needed_space and fs[key] < size_to_delete:
            size_to_delete = fs[key]

    print(f"Part one: {total}")

    print(f"Part two: {size_to_delete}")


if __name__ == "__main__":
    main("data/input.txt")
