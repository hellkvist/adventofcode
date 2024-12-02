INPUT_FILE_PATH = "2024/1/input.txt"

def get_lists() -> tuple[list[float], list[float]]:
    with open(INPUT_FILE_PATH, "r") as input_file:
        lines = input_file.readlines()

    list_A = []
    list_B = []
    for i, line in enumerate(lines):
        splits = line.rstrip("\n").split("   ")
        list_A.append(float(splits[0]))
        list_B.append(float(splits[1]))

    return [list_A, list_B]

def get_distance(list_A: list[float], list_B: list[float]) -> float:
    assert len(list_A) == len(list_B)

    distance = 0
    for i, items in enumerate(zip(list_A, list_B)):
        distance += abs(items[0] - items[1])

    return distance

def sort_list(list_: list):
    return sorted(list_)

def get_similarity(list_A: list[float], list_B: list[float]) -> float:
    similarity = 0 # init

    for number in list_A:
        number_count_in_B = list_B.count(number)
        similarity += number * number_count_in_B

    return similarity


def main():
    """
    Part 1: Given two lists, add up the distances between the smallest number in each list, the second smallest, and so on.
    Part 2: Compute similarity between the lists defined by the following:
        For each number (item) in the first list, increase the similarity score by the number multiplied with how many times it appears in the second list.
    """
    list_A, list_B = get_lists()

    # Part 1
    sorted_A = sort_list(list_A)
    sorted_B = sort_list(list_B)
    distance = get_distance(sorted_A, sorted_B)
    print(f"Distance: {distance}")

    # Part 2
    similarity = get_similarity(list_A, list_B)
    print(f"Similiarty: {similarity}")



if __name__=="__main__":
    main()