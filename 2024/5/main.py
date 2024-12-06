import copy
from operator import itemgetter

INSTRUCTIONS_FILE_PATH = "5/instructions.txt"
UPDATES_FILE_PATH = "5/updates.txt"

def read_file_lines(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def get_instructions() -> list:
    """
    From a text file with lines
    x|y
    a|b
    ...
    Return a dict with {x: set(y), a: set(b)}
    """
    lines = read_file_lines(INSTRUCTIONS_FILE_PATH)
    instructions_dict = {}
    for line in lines:
        leading_number, trailing_number = line.rstrip().split('|')

        if leading_number in instructions_dict.keys():
            instructions_dict[leading_number].add(trailing_number)
        else:
            instructions_dict[leading_number] = set(trailing_number)

    instructions_dict_sorted = \
        {k: sorted([int(v) for v in instructions_dict[k]]) for k in sorted(instructions_dict.keys()) }

    return instructions_dict_sorted

def get_updates() -> list[list[int]]:
    lines = read_file_lines(UPDATES_FILE_PATH)

    updates = []
    for line in lines:
        updates.append([int(value) for value in line.rstrip().split(",")])

    return updates

def validate_update(instructions, update):
    flag = True
    for i, value in enumerate(update):
        for value_in_front in update[0:i]:
            if value_in_front in instructions[str(value)]:
                flag = False
                break
        if not flag:
            break
    return flag

def filter_valid_updates(instructions: dict[str, set[int]], updates: list[list[int]]):
    valid_updates = []
    flags = []

    for update in updates:
        flag = validate_update(instructions, update)
        flags.append(flag)

    valid_updates = [updates[i] for i, flag in enumerate(flags) if flag]
    invalid_updates = [updates[i] for i, flag in enumerate(flags) if not flag]
    return valid_updates, invalid_updates

def get_sum_of_middles(input: list):
    if type(input[0]) == int:
        # Then get middle of the list
        input_len = len(input)
        assert input_len % 2 == 1 # Length must be uneven

        middle_index = int(input_len/2) # E.g. len = 5, len/2 = 2.5, int(len/2) = 2, which is the middle in 0,1,2,3,4

        return input[middle_index]
    elif type(input[0]) == list:
        return sum([get_sum_of_middles(input_i) for input_i in input])
    else:
        raise Exception("input is neither a list or list of lists.")

def fix_invalid_updates(instructions, updates):

    for update_i, update in enumerate(updates):
        flag = False
        while not flag:
            stop_bool = False
            for i, value in enumerate(update):
                for j, value_in_front in enumerate(update[0:i]):
                    if value_in_front in instructions[str(value)]:
                        # Then move value (on i) to position before value_in_front (index j)
                        update.insert(j, update.pop(i))
                        stop_bool = True
                        break
                if stop_bool: break

            flag = validate_update(instructions, update)
        updates[update_i] = update
    return updates

def fix_invalid_updates_backwards(instructions, updates):
    for update_i, update in enumerate(updates):
        flag = False
        while not flag:
            stop_bool = False

            update_enum_rev = reversed(tuple(enumerate(update)))
            for i, value in update_enum_rev:
                for j, value_in_front in enumerate(update[0:i]):
                    if value_in_front in instructions[str(value)]:
                        # Then move value (on i) to position before value_in_front (index j)
                        update.insert(j, update.pop(i))
                        stop_bool = True
                        break
                if stop_bool: break

            flag = validate_update(instructions, update)
        updates[update_i] = update
    return updates

def sort_dontwork(instructions, update):
    if type(update[0]) == list:
        return [sort_dontwork(instructions, copy.deepcopy(update_)) for update_ in update]

    # Get the number of times each number occurs in instructions relevant for this update
    # For a list of 5 numbers, if a number occurs in 5 instructions, then it should be last,
    # if then there is one with 4, it should be second last.
    # IF there are multiple numbers with same nuumber, e.g. 1,
    # we must sort them amognst themselves
    number_of_occurrances = []
    for number in update:
        instructions_for_other_numbers = \
            itemgetter(*[str(other_number) for other_number in update if other_number != number])(instructions)
        if type(instructions_for_other_numbers[0]) == int:
            instructions_for_other_numbers = [instructions_for_other_numbers]
        number_of_occurrances.append(sum(
            [
                number in instruction for instruction in instructions_for_other_numbers
            ]
            ))

    sorted_indexes_list = [[i for i, num in enumerate(number_of_occurrances) if num == n] for n in range(len(update))]
    sorted = []
    if len(sorted_indexes_list[0]) == len(update):
        # Then the numbers do not occur in each others ruleset,
        # and we return the list as is
        return update

    for num_occ in list(reversed(range(len(update)))):
        indexes_with_num_occ = sorted_indexes_list[num_occ]

        if len(indexes_with_num_occ) == 0:
            pass
        elif len(indexes_with_num_occ) == 1:
            sorted = [update[indexes_with_num_occ[0]]] + sorted
        elif len(indexes_with_num_occ) > 1:
            subset_sorted = sort_dontwork(instructions, [update[i] for i in sorted_indexes_list[num_occ]])
            sorted = subset_sorted + sorted
        else:
            raise Exception("wtf")

    assert validate_update(instructions, sorted)
    return sorted

def part1():
    """
    Page ordering problem.
    For an input of page ordering
    23|25
    45|12
    12|29

    And print instructions
    12,45
    29,23,25

    Then we must print
    45, 12,
    23, 25, 29
    As 45 is specified to come before 12, and 23 before 25

    """
    instructions = get_instructions()
    # print(instructions)

    updates = get_updates()
    # print(updates)

    valid_updates, _ = filter_valid_updates(instructions, updates)
    print(len(valid_updates))

    sum_middles_of_valid_updates = get_sum_of_middles(valid_updates)
    print("sum part1: " + str(sum_middles_of_valid_updates))
    1 == 1

def sort(instructions, update):
    if type(update[0]) == list:
        return [sort(instructions, copy.deepcopy(update_)) for i,update_ in enumerate(update)]

    # For each number in update, check the numbers before it
    # If a leading number is the numbers rule set, insert the number at its position

    def rule_check(ruleset, update):
        for j_leading, leading_number in enumerate(update[0:i_rule]):
                if leading_number in ruleset:
                    update.insert(j_leading, update.pop(i_rule))
                    return update
        return None

    update_copy = copy.deepcopy(update)
    while not(validate_update(instructions, update_copy)):
        for i_rule, rule_number in enumerate(update_copy):
            ruleset = instructions[str(rule_number)]
            checked = rule_check(ruleset, update_copy)
            if checked is not None:
                update_copy = copy.deepcopy(checked)
                break

    return update_copy

def part2():
    instructions = get_instructions()
    updates = get_updates()
    valid_updates, invalid_updates = filter_valid_updates(instructions, updates)
    # sorted = sort(instructions, invalid_updates)
    sorted = sort_dontwork(instructions, invalid_updates)
    summed = get_sum_of_middles(sorted)
    print(summed)

def part2_old():
    instructions = get_instructions()
    # print(instructions)

    updates = get_updates()
    # print(updates)

    valid_updates, invalid_updates = filter_valid_updates(instructions, updates)
    # print(valid_updates, invalid_updates)

    fixed_updates = fix_invalid_updates(instructions, copy.deepcopy(invalid_updates))
    validated_fixed_updates, invalidated_fixed_updates = filter_valid_updates(instructions, fixed_updates)
    assert len(fixed_updates) == len(validated_fixed_updates)

    print(len(validated_fixed_updates))
    sum_middles_of_fixed_updates = get_sum_of_middles(fixed_updates)
    print("sum part2: " + str(sum_middles_of_fixed_updates))

    fixed_updates_rev = fix_invalid_updates_backwards(instructions, copy.deepcopy(invalid_updates))
    validated_fixed_updates_rev, invalidated_fixed_updates_rev = filter_valid_updates(instructions, fixed_updates_rev)
    assert len(fixed_updates_rev) == len(validated_fixed_updates_rev)

    print(len(validated_fixed_updates_rev))
    sum_middles_of_fixed_updates_rev = get_sum_of_middles(fixed_updates_rev)
    print("sum part2: " + str(sum_middles_of_fixed_updates_rev))

def sort_master():
    rule_singles = open("5/instructions.txt").read().split("\n")

    # init dicts of rules
    rule_d = {} # rule_d[x] is the numbers that must come after x
    inv_rule_d = {} # inv_rule_d[x] is the numbers that must come before x
    for rule in rule_singles:
        master, slave = (int(n) for n in rule.split("|"))
        rule_d[master] = set()
        inv_rule_d[slave] = set()

    # Populate dicts
    for rule in rule_singles:
        master, slave = (int(n) for n in rule.split("|"))
        rule_d[master].add(slave)
        inv_rule_d[slave].add(master)

    updates = [[int(num) for num in line.split(",")] for line in open("5/updates.txt").read().split("\n")]

    p1_sum = 0
    p2_sum = 0
    for update in updates:
        # Validate update
        is_valid = True
        for i, x in enumerate(update):
            for j, y in enumerate(update):
                if i < j and x in rule_d[y]: # If x is infront of y, and x is a number that must come after y
                    is_valid = False
        # / Validate update

        if is_valid:
            p1_sum += update[len(update)//2]
        else:
            fixed = []
            nullers = []
            # The number of numbers in update that should come before the number 'num'
            rule_count = {num: len(inv_rule_d[num] & set(update)) for num in update}
            for num in update:
                if rule_count[num] == 0: # If there are no numbers in update that shold come before num
                    nullers.append(num)

            while nullers:
                # Put the first number for which no other numbers should come before it, and put first in the fixed list
                leading_nuller = nullers.pop(0)
                fixed.append(leading_nuller)

                # For the slaves of leading_nuller,
                # which are in the update,
                # decrease the number of numbers in the update that should come before slave by 1,
                # and as they race to 0,
                # add them to the list of nullers, i.e., those that should come first in the list
                for slave in rule_d[leading_nuller]:
                    if slave in update:
                        rule_count[slave] -= 1
                        if rule_count[slave] == 0:
                            nullers.append(slave)

            p2_sum += fixed[len(fixed)//2]

            1 == 1

    print(p1_sum)
    print(p2_sum)

def main():
    # part1()
    # part2()
    sort_master()

if __name__=='__main__':
    main()