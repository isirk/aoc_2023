input = open("1_input.txt", "r")
sum = 0

for line in input:
    nums = [int(x) for x in line if x.isdigit()]
    if len(nums) == 1:
        string = str(nums[0]) + str(nums[0])
        sum += int(string)
    else:
        string = str(nums[0]) + str(nums.pop())
        sum += int(string)

input.close()
print(sum)