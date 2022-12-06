"""
Quick and dirty pass.  Get's the right answers despite some problems.
Chekc out the v2 version for a class impementation.
"""

with open("day1-input.txt", "r") as f:
    elf_calorie_data = f.readlines()

# print(elf_calorie_data)
calorie_totals: list[int] = []
current_value: int = 0

for i in elf_calorie_data:
    val = i.replace("\n", "")
    if val != "":
        current_value += int(i)
    else:
        calorie_totals.append(current_value)
        current_value = 0
# one last write for the last line captured.  If last line ="" then it would get added twice
calorie_totals.append(current_value)

print(f"The Elf with the most calories has {max(calorie_totals)} calories.")

calorie_totals.sort()
top_three: list[int] = calorie_totals[-3:]

print(f"The Top three Elves have a combined total of {sum(top_three)} calories.")
