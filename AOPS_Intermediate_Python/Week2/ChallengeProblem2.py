def get_base_number(num,base):
    '''get_base_number(num,base) -> int
    returns value of num as a base number in the given base'''
    idx = 0
    tot = 0
    for n in reversed(num):
        tot += int(n) * (base**idx)
        idx += 1
    return tot


# test cases
print(get_base_number('10011',2))  # should be 19
print(get_base_number('3202',5))   # should be 427

print(get_base_number('611023', 7))