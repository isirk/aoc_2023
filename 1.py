input = open("1_input.txt", "r")
output = open("1_output.txt", "w")

for line in input:
    for c in line:
        nums = [int(x) for x in line if x.isdigit()]
        output.write(nums[0] + nums[nums.len() - 1])

# doesnt work yet, i need to get the last number in the list but error handle if there is only one number in the line and repeat that
# also need to print is out as a string so it doesn't just add the numbers