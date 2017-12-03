

def get_total(file):
    total = 0
    for line in file:
        nums = line.split()
        min = int(nums[0])
        max = int(nums[0])
        for num in nums:
            if int(num) < min:
                min = int(num)
            elif int(num) > max:
                max = int(num)
        total = total +(max - min)
    print(total)


def get_div_total(file):
    total = 0
    for line in file:
        found = False
        nums = line.split()
        while not found:
            current = int(nums.pop())
            for y in range(0, len(nums)):
                if is_div(current, int(nums[y])):
                    total = total + div_diff(current, int(nums[y]))
                    # print(div_diff(current, int(nums[y])))
                    found = True
    print(total)


def is_div(current, at_index):
    if current > at_index:
        a = current
        b = at_index
    else:
        a = at_index
        b = current
    result = False
    if a % b == 0:
        result = True
    return result


def div_diff(current, at_index):
    if current > at_index:
        return current/at_index
    return at_index/current



num_file = open("inputs/2_input", "r")
num_file_sample = open("inputs/2_sample", "r")
num_file_sample_b = open("inputs/2_sample_b", "r")
# get_total(num_file)
# get_total(num_file_sample)

get_div_total(num_file)
