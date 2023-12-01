input = open("1_input.txt", "r")
sum = 0

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
           "six": 6, "seven": 7, "eight": 8, "nine": 9}

def is_value(line):
    for key in numbers.keys():
        line = line.replace(key, str(numbers[key]))
    return line

for line in input:
    values = is_value(line)
    nums = [int(x) for x in values if x.isdigit()]
    if len(nums) == 1:
        string = str(nums[0]) + str(nums[0])
        sum += int(string)
    else:
        string = str(nums[0]) + str(nums.pop())
        sum += int(string)

input.close()
print(sum)