input = open("1_input.txt", "r")
sum = 0

for line in input:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                digits.append(str(d + 1))
    sum += int(digits[0] + digits[-1])

input.close()
print(sum)