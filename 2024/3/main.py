import re


INPUT_FILE_PATH = "2024/3/input.txt"

def read_file_lines(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def lines_to_string(lines: list[str]) -> str:
    output = ""
    for line in lines:
        output += line.rstrip()
    return output

def get_all_mul_ops(input_str: str) -> list[str]:
    """
    returns a list of strings on form mul(x,y)
    """
    regex = "mul\(\d+,\d+\)"

    matches = re.findall(rf"{regex}", input_str)

    return matches

def get_all_instructions(input_str: str) -> list[str]:
    regex = "mul\(\d+,\d+\)|do\(\)|don't\(\)"

    matches = re.findall(rf"{regex}", input_str)

    return matches

def get_all_mul_tuples(mul_ops: list[str]) -> list[list[float, float]]:
    regex = "\d+,\d+"
    mul_tuples_str = [re.findall(rf"{regex}", mul_op)[0].split(",") for mul_op in mul_ops]
    mul_tuples_float = [[float(mul_tup_str[0]), float(mul_tup_str[1])] for mul_tup_str in mul_tuples_str]

    return mul_tuples_float

def mulitply_list_of_list(input: list[float, float]) -> list[float]:
    multplied = [tuple[0]*tuple[1] for tuple in input]
    return multplied

def filter_list_on_instructions(input: list[str]) -> list[str]:

    flag = True
    filtered_list = []

    for item in input:
        if item == "do()":
            flag = True
        elif item == "don't()":
            flag = False
        else:
            if flag:
                filtered_list.append(item)

    return filtered_list


def part1():
    """
    For a corrupted string, e.g.,
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)),
    find the substrings of form mul(x,y) and add the results up, where mul(x,y) is the multiplication of x and y.
    """
    input_lines = read_file_lines(INPUT_FILE_PATH)
    input_str = lines_to_string(input_lines)
    all_mul_ops = get_all_mul_ops(input_str)
    all_mul_tuples = get_all_mul_tuples(all_mul_ops)
    mulled = mulitply_list_of_list(all_mul_tuples)
    summed = sum(mulled)
    print(f"Summed: {summed}")

def part2():
    """
    For a corrupted string, e.g.,
    xmul(2,4)%&mul[3,7]!@^don't()(5,5)+mul(32,64]do()then(mul(11,8)mul(8,5)),
    find the substrings of form mul(x,y) and add the results up, where mul(x,y) is the multiplication of x and y.
    Do not include mul's follwing don't(), but include those following do().
    I.e., dont include those between don't() and do(), but include those after do().
    Include those before the first don't().
    """
    input_lines = read_file_lines(INPUT_FILE_PATH)
    input_str = lines_to_string(input_lines)
    all_ins_ops = get_all_instructions(input_str)
    filtered_mul_ops = filter_list_on_instructions(all_ins_ops)
    filtered_mul_tuples = get_all_mul_tuples(filtered_mul_ops)
    mulled = mulitply_list_of_list(filtered_mul_tuples)
    summed = sum(mulled)
    print(f"Summed: {summed}")


def main():
    part1()
    part2()

if __name__=='__main__':
    main()