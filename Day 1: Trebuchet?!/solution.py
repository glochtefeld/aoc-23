import re
import sys


digit_lookup = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4',
        'five': '5',
		'six': '6',
		'seven': '7', 
		'eight': '8',
        'nine': '9'
}

def find_nums(line):
    allNums = re.findall('(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
    asNums = []
    for num in allNums:
        if num.isdigit():
            asNums.append(num)
        else:
            asNums.append(digit_lookup[num])
    return asNums

def first_last_num(line):
    allNums = find_nums(line)
    return allNums[0] + allNums[-1]

def solve(input_fname):
    print()
    with open(input_fname, 'r') as infile:
        nums = [int(first_last_num(line)) for line in infile]
        for num in nums:
            print(num)
        total = sum(nums)
        print(total)
    print()

if __name__ == '__main__':
    solve(sys.argv[1])
