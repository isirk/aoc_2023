input = open("1_input.txt", "r")
sum = 0

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
           "six": 6, "seven": 7, "eight": 8, "nine": 9,
           "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

def is_value(line):
    return [val for key, val in numbers.items() if key in line]

for line in input:
    nums = is_value(line)
    if len(nums) == 1:
        string = str(nums[0]) + str(nums[0])
        sum += int(string)
    else:
        string = str(nums[0]) + str(nums.pop())
        sum += int(string)

input.close()
print(sum)