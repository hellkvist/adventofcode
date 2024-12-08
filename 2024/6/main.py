from itertools import cycle
import copy

def print_map(map: list[list[str]]):
    with open("2024/6/output.txt", 'w') as file:
        for row in map:
            file.write("".join(row))
            file.write("\n")



def part1():
    map: list[str] = open("2024/6/input.txt").read().split("\n")
    # Convert each row to list of chars
    for i, row in enumerate(map):
        map[i] = list(row)

    # Find the initial position of the guard "^"
    for i_row, row in enumerate(map):
        value_finder = [(col,value) for col, value in enumerate(row) if value == "^"]
        if value_finder:
            initial_row = i_row
            initial_col = value_finder[0][0]
            break
    assert map[i_row][initial_col] == "^"

    max_col = len(map[0])-1
    max_row = len(map)-1

    pos = {"current_row": initial_row, "current_col": initial_col}
    dir = "^"

    print_map(map)

    is_inside = True
    while is_inside:
        # Get the slice of the map which is infront of the guard
        # And update the direction while we are at it
        if dir == "^":
            dir = ">"

            map_slice_in_front = [row[pos["current_col"]] for row in map[0:pos["current_row"]]]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = -1

                # Then put X instead of guard
                map[i_closest_obstacle+1][pos["current_col"]] = "^"
            else:
                # The last '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles.pop()

                # put guard below closest obstacle
                map[i_closest_obstacle+1][pos["current_col"]] = "^"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_row in range(i_closest_obstacle+2,pos["current_row"]+1):
                map[i_row][pos["current_col"]] = "^"

            # Update guard pos
            pos["current_row"] = i_closest_obstacle+1

        elif dir == ">":
            dir = "V"

            map_slice_in_front = map[pos["current_row"]][pos["current_col"]:max_col+1]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = max_col+1

                # Then put X instead of guard
                map[pos["current_row"]][i_closest_obstacle-1] = ">"
            else:
                # The first '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles[0]

                # put guard to the left of closest obstacle
                new_col_i = pos["current_col"]+i_closest_obstacle-1
                map[pos["current_row"]][new_col_i] = ">"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_col in range(pos["current_col"], new_col_i):
                map[pos["current_row"]][i_col] = ">"

            # Update guard pos
            pos["current_col"] = new_col_i

        elif dir == "V":
            dir = "<"

            map_slice_in_front = sum([[row[pos["current_col"]]] for row in map[pos["current_row"]+1:max_row]], [])

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = max_row+1

                # Then put X instead of guard
                map[i_closest_obstacle-1][pos["current_col"]] = "V"
            else:
                # The first '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles[0]

                # put guard above closest obstacle
                new_row_i = pos["current_row"] + i_closest_obstacle
                map[new_row_i][pos["current_col"]] = "V"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_row in range(pos["current_row"], new_row_i):
                map[i_row][pos["current_col"]] = "V"

            # Update guard pos
            pos["current_row"] = new_row_i

        elif dir == "<":
            dir = "^"

            map_slice_in_front = map[pos["current_row"]][0:pos["current_col"]]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = -1

                # Then put X instead of guard
                map[pos["current_row"]][i_closest_obstacle+1] = "<"
            else:
                # The last '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles.pop()

                # put guard to the right of closest obstacle
                map[pos["current_row"]][i_closest_obstacle+1] = "<"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_col in range(i_closest_obstacle+2, pos["current_col"]+1):
                map[pos["current_row"]][i_col] = "<"

            # Update guard pos
            pos["current_col"] = i_closest_obstacle+1

        else:
            raise Exception("wtf")

        print_map(map)
    1 == 1

    n_visited = 0
    for row in map:
        n_visited += sum(
            [
                1 for value in row if value in ["X", "^", ">", "V", "<"]
            ]
        )
    print(n_visited)

def part2_old():
    map: list[str] = open("2024/6/input.txt").read().split("\n")
    # Convert each row to list of chars
    for i, row in enumerate(map):
        map[i] = list(row)

    # Find the initial position of the guard "^"
    for i_row, row in enumerate(map):
        value_finder = [(col,value) for col, value in enumerate(row) if value == "^"]
        if value_finder:
            initial_row = i_row
            initial_col = value_finder[0][0]
            break
    assert map[i_row][initial_col] == "^"

    max_col = len(map[0])-1
    max_row = len(map)-1

    pos = {"current_row": initial_row, "current_col": initial_col}
    dir = "^"

    print_map(map)

    p2 = 0
    is_inside = True
    while is_inside:
        # Get the slice of the map which is infront of the guard
        # And update the direction while we are at it
        if dir == "^":
            map_slice_in_front = [row[pos["current_col"]] for row in map[0:pos["current_row"]]]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = -1

                # Then put X instead of guard
                map[i_closest_obstacle+1][pos["current_col"]] = "^"
            else:
                # The last '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles.pop()

                # put guard below closest obstacle
                map[i_closest_obstacle+1][pos["current_col"]] = ">"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_row in range(i_closest_obstacle+2,pos["current_row"]+1):
                map[i_row][pos["current_col"]] = "^"

            # Update guard pos and dir
            pos["current_row"] = i_closest_obstacle+1
            dir = ">"

            # If the new path crosses a previous path of the next direction,
            # i.e., where there already are ">" then we found a place where
            # an obstacle would make it loop
            for i, point in enumerate(map_slice_in_front[i_closest_obstacle::]):
                if point == ">":
                    # Then an obstacle in the point above point makes a loop
                    p2 += 1

        elif dir == ">":

            map_slice_in_front = map[pos["current_row"]][pos["current_col"]:max_col+1]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = max_col+1

                # Then put X instead of guard
                map[pos["current_row"]][i_closest_obstacle-1] = ">"
            else:
                # The first '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles[0]

                # put guard to the left of closest obstacle
                new_col_i = pos["current_col"]+i_closest_obstacle-1
                map[pos["current_row"]][new_col_i] = "V"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_col in range(pos["current_col"], new_col_i):
                map[pos["current_row"]][i_col] = ">"

            # Update guard pos
            pos["current_col"] = new_col_i
            dir = "V"

            # If the new path crosses a previous path of the next direction,
            # i.e., where there already are "V" then we found a place where
            # an obstacle would make it loop
            for i, point in enumerate(map_slice_in_front[0:i_closest_obstacle]):
                if point == "V":
                    # Then an obstacle in the point right of point makes a loop
                    p2 += 1

        elif dir == "V":
            new_dir = "<"

            map_slice_in_front = sum([[row[pos["current_col"]]] for row in map[pos["current_row"]+1:max_row]], [])

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = max_row+1

                # Then put X instead of guard
                map[i_closest_obstacle-1][pos["current_col"]] = "V"
            else:
                # The first '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles[0]

                # put guard above closest obstacle
                new_row_i = pos["current_row"] + i_closest_obstacle
                map[new_row_i][pos["current_col"]] = "<"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_row in range(pos["current_row"], new_row_i):
                map[i_row][pos["current_col"]] = "V"

            # Update guard pos
            pos["current_row"] = new_row_i
            dir = new_dir

            # If the new path crosses a previous path of the next direction,
            # i.e., where there already are ">" then we found a place where
            # an obstacle would make it loop

            for i, point in enumerate(map_slice_in_front[0:i_closest_obstacle]):
                if point == "<":
                    # Then an obstacle in the point below point makes a loop
                    p2 += 1

        elif dir == "<":
            new_dir = "^"

            map_slice_in_front = map[pos["current_row"]][0:pos["current_col"]]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = -1

                # Then put X instead of guard
                map[pos["current_row"]][i_closest_obstacle+1] = "<"
            else:
                # The last '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles.pop()

                # put guard to the right of closest obstacle
                map[pos["current_row"]][i_closest_obstacle+1] = "^"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_col in range(i_closest_obstacle+2, pos["current_col"]+1):
                map[pos["current_row"]][i_col] = "<"

            # Update guard pos
            pos["current_col"] = i_closest_obstacle+1
            dir = "^"

            # If the new path crosses a previous path of the next direction,
            # i.e., where there already are ">" then we found a place where
            # an obstacle would make it loop

            for i, point in enumerate(map_slice_in_front[i_closest_obstacle::]):
                if point == "^":
                    # Then an obstacle in the point left of point makes a loop
                    p2 += 1

        else:
            raise Exception("wtf")

        print_map(map)

    1 == 1

    n_visited = 0
    for row in map:
        n_visited += sum(
            [
                1 for value in row if value in ["^", ">", "V", "<"]
            ]
        )
    print(n_visited)
    print(p2)

def part1_with_detect(map, pos, dir):
    map.remove([])
    max_col = len(map[0])-1
    max_row = len(map)-1

    # print_map(map)

    is_inside = True
    is_loop = False
    while is_inside and not is_loop:
        # Get the slice of the map which is infront of the guard
        # And update the direction while we are at it
        if dir == "^":
            dir = ">"

            map_slice_in_front = [row[pos["current_col"]] for row in map[0:pos["current_row"]]]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = -1

                # Then put X instead of guard
                map[i_closest_obstacle+1][pos["current_col"]] = "^"
            else:
                # The last '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles.pop()

                # Check if the point on below the map already contains "+" because then it is a loop
                if map[i_closest_obstacle+1][pos["current_col"]] == ">":
                    is_loop = True

                # put guard below closest obstacle
                map[i_closest_obstacle+1][pos["current_col"]] = "^"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_row in range(i_closest_obstacle+2,pos["current_row"]+1):
                map[i_row][pos["current_col"]] = "^"

            # Update guard pos
            pos["current_row"] = i_closest_obstacle+1

        elif dir == ">":
            dir = "V"

            map_slice_in_front = map[pos["current_row"]][pos["current_col"]:max_col+1]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = max_col+1
                new_col_i = max_col
                # Then put X instead of guard
                map[pos["current_row"]][i_closest_obstacle-1] = ">"
            else:
                # The first '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles[0]

                # Check if the point on the map left of obstacle already contains "V" because then it is a loop
                if map[pos["current_row"]][pos["current_col"]+i_closest_obstacle] == "V":
                    is_loop = True

                # put guard to the left of closest obstacle
                new_col_i = pos["current_col"]+i_closest_obstacle-1
                map[pos["current_row"]][new_col_i] = ">"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_col in range(pos["current_col"]+1, new_col_i):
                map[pos["current_row"]][i_col] = ">"

            # Update guard pos
            pos["current_col"] = new_col_i

        elif dir == "V":
            dir = "<"

            map_slice_in_front = sum([[row[pos["current_col"]]] for row in map[pos["current_row"]+1:max_row]], [])

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = max_row+1
                new_row_i = i_closest_obstacle-1
                # Then put X instead of guard
                map[new_row_i][pos["current_col"]] = "V"
            else:
                # The first '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles[0]

                # Check if the point on the map above obstacle already contains "<" because then it is a loop
                if map[pos["current_row"]+i_closest_obstacle][pos["current_col"]] == "<":
                    is_loop = True

                # put guard above closest obstacle
                new_row_i = pos["current_row"] + i_closest_obstacle
                map[new_row_i][pos["current_col"]] = "V"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_row in range(pos["current_row"]+1, new_row_i):
                map[i_row][pos["current_col"]] = "V"

            # Update guard pos
            pos["current_row"] = new_row_i

        elif dir == "<":
            dir = "^"

            map_slice_in_front = map[pos["current_row"]][0:pos["current_col"]]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = -1

                # Then put X instead of guard
                map[pos["current_row"]][i_closest_obstacle+1] = "<"
            else:
                # The last '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles.pop()

                # Check if the point on the map right of obstacle already contains "^" because then it is a loop
                if map[pos["current_row"]][i_closest_obstacle+1] == "^":
                    is_loop = True

                # put guard to the right of closest obstacle
                map[pos["current_row"]][i_closest_obstacle+1] = "<"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_col in range(i_closest_obstacle+2, pos["current_col"]):
                map[pos["current_row"]][i_col] = "<"

            # Update guard pos
            pos["current_col"] = i_closest_obstacle+1

        else:
            raise Exception("wtf")

        # print_map(map)
    if is_loop:
        1 == 1
    return is_loop

def part2_old():
    map: list[str] = open("2024/6/input.txt").read().split("\n")
    # Convert each row to list of chars
    for i, row in enumerate(map):
        map[i] = list(row)

    # Find the initial position of the guard "^"
    for i_row, row in enumerate(map):
        value_finder = [(col,value) for col, value in enumerate(row) if value == "^"]
        if value_finder:
            initial_row = i_row
            initial_col = value_finder[0][0]
            break
    assert map[i_row][initial_col] == "^"

    max_col = len(map[0])-1
    max_row = len(map)-1

    pos = {"current_row": initial_row, "current_col": initial_col}
    dir = "^"

    # print_map(map)

    p2 = 0
    obstacles_which_makes_loops=[]
    is_inside = True
    while is_inside:
        # Get the slice of the map which is infront of the guard
        # And update the direction while we are at it
        if dir == "^":
            map_slice_in_front = [row[pos["current_col"]] for row in map[0:pos["current_row"]]]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = -1

            else:
                # The last '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles.pop()

            # For each point to traverse, replace it with # and detect if it is a loop
            for i in range(i_closest_obstacle+1, pos["current_row"]):
                if [i,pos["current_col"]] not in obstacles_which_makes_loops:
                    map_copy = copy.deepcopy(map)
                    map_copy[i][pos["current_col"]] = "#"
                    is_loop = part1_with_detect(copy.deepcopy(map_copy), copy.deepcopy(pos), "^")
                    if is_loop:
                        p2 += 1
                        obstacles_which_makes_loops.append([i,pos["current_col"]])

            if not i_obstacles:
                # Then put X instead of guard
                map[i_closest_obstacle+1][pos["current_col"]] = "^"
            else:
                # put guard below closest obstacle
                map[i_closest_obstacle+1][pos["current_col"]] = ">"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_row in range(i_closest_obstacle+2,pos["current_row"]+1):
                map[i_row][pos["current_col"]] = "^"

            # Update guard pos and dir
            pos["current_row"] = i_closest_obstacle+1
            dir = ">"

        elif dir == ">":

            map_slice_in_front = map[pos["current_row"]][pos["current_col"]:max_col+1]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = max_col+1
            else:
                # The first '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles[0]

            new_col_i = pos["current_col"]+i_closest_obstacle-1
            # For each point to traverse, replace it with # and detect if it is a loop
            for i in range(pos["current_col"], new_col_i):
                if [pos["current_row"],i] not in obstacles_which_makes_loops:
                    map_copy = copy.deepcopy(map)
                    map_copy[pos["current_row"]][i] = "#"
                    is_loop = part1_with_detect(copy.deepcopy(map_copy), copy.deepcopy(pos), ">")
                    if is_loop:
                        p2 += 1
                        obstacles_which_makes_loops.append([pos["current_row"],i])

            if not i_obstacles:
                # Then put X instead of guard
                map[pos["current_row"]][new_col_i] = ">"
            else:
                # put guard to the left of closest obstacle
                new_col_i = pos["current_col"]+i_closest_obstacle-1
                map[pos["current_row"]][new_col_i] = "V"

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_col in range(pos["current_col"], new_col_i):
                map[pos["current_row"]][i_col] = ">"

            # Update guard pos
            pos["current_col"] = new_col_i
            dir = "V"

        elif dir == "V":
            new_dir = "<"

            map_slice_in_front = sum([[row[pos["current_col"]]] for row in map[pos["current_row"]+1:max_row]], [])

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = max_row+1
                new_row_i = i_closest_obstacle-1

                # Then put X instead of guard
                map[new_row_i][pos["current_col"]] = "V"
            else:
                # The first '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles[0]

                # put guard above closest obstacle
                new_row_i = pos["current_row"] + i_closest_obstacle
                map[new_row_i][pos["current_col"]] = "<"

            # For each point to traverse, replace it with # and detect if it is a loop
            for i in range(pos["current_row"], new_row_i):
                if [i,pos["current_col"]] not in obstacles_which_makes_loops:
                    map_copy = copy.deepcopy(map)
                    map_copy[i][pos["current_col"]] = "#"
                    is_loop = part1_with_detect(copy.deepcopy(map_copy), copy.deepcopy(pos), "V")
                    if is_loop:
                        p2 += 1
                        obstacles_which_makes_loops.append([i,pos["current_col"]])

            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_row in range(pos["current_row"], new_row_i):
                map[i_row][pos["current_col"]] = "V"

            # Update guard pos
            pos["current_row"] = new_row_i
            dir = new_dir

        elif dir == "<":
            new_dir = "^"

            map_slice_in_front = map[pos["current_row"]][0:pos["current_col"]]

            i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
            if not i_obstacles:
                is_inside = False
                i_closest_obstacle = -1
                new_col_i = i_closest_obstacle+1

            else:
                # The last '#' in the slice corresponds to the obstacle closest to the guard
                i_closest_obstacle = i_obstacles.pop()
                new_col_i = i_closest_obstacle+1

            # For each point to traverse, replace it with # and detect if it is a loop
            for i in range(new_col_i, pos["current_col"]):
                if [pos["current_row"],i] not in obstacles_which_makes_loops:
                    map_copy = copy.deepcopy(map)
                    map_copy[pos["current_row"]][i] = "#"
                    is_loop = part1_with_detect(copy.deepcopy(map_copy), copy.deepcopy(pos), "<")
                    if is_loop:
                        p2 += 1
                        obstacles_which_makes_loops.append([pos["current_row"],i])

            if not i_closest_obstacle:
                # Then put X instead of guard
                map[pos["current_row"]][new_col_i] = "<"
            else:
                # put guard to the right of closest obstacle
                map[pos["current_row"]][new_col_i] = "^"
            # put X:es on the indexes from (including) guard to i_closest_obstacle
            for i_col in range(i_closest_obstacle+2, pos["current_col"]+1):
                map[pos["current_row"]][i_col] = "<"

            # Update guard pos
            pos["current_col"] = i_closest_obstacle+1
            dir = "^"

        else:
            raise Exception("wtf")

        # print_map(map)

    1 == 1

    n_visited = 0
    for row in map:
        n_visited += sum(
            [
                1 for value in row if value in ["^", ">", "V", "<"]
            ]
        )
    print(n_visited)
    print(p2)

def part2():
    # Try to place an obstacle on every coordinate,
    # And check if it makes a loop
    p2 = 0

    original_map: list[str] = open("2024/6/input.txt").read().split("\n")
    original_map.remove('')

    # Convert each row to list of chars
    for i, row in enumerate(original_map):
        original_map[i] = list(row)

    max_col = len(original_map[0])-1
    max_row = len(original_map)-1

    n_col = len(original_map[0])
    n_row = len(original_map)

    for r_obs in range(n_row):
        for c_obs in range(n_col):
            seen = []

            map = copy.deepcopy(original_map)
            if map[r_obs][c_obs] not in ["#", "^"]:
                map[r_obs][c_obs] = "#"
                print((r_obs+1, c_obs+1))

                # Find the initial position of the guard "^"
                for i_row, row in enumerate(map):
                    value_finder = [(col,value) for col, value in enumerate(row) if value == "^"]
                    if value_finder:
                        initial_row = i_row
                        initial_col = value_finder[0][0]
                        break
                assert map[i_row][initial_col] == "^"

                pos = {"current_row": initial_row, "current_col": initial_col}
                dir = "^"

                # print_map(map)

                is_inside = True
                while is_inside:
                    if (pos["current_row"], pos["current_col"], dir) in seen:
                        print_map(map)
                        p2 += 1
                        break

                    # Get the slice of the map which is infront of the guard
                    # And update the direction while we are at it
                    if dir == "^":
                        dir = ">"

                        map_slice_in_front = [row[pos["current_col"]] for row in map[0:pos["current_row"]]]

                        i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
                        if not i_obstacles:
                            is_inside = False
                            i_closest_obstacle = -1

                            # Then put X instead of guard
                            map[i_closest_obstacle+1][pos["current_col"]] = "^"
                            seen.append((i_closest_obstacle+1, pos["current_col"], "^"))
                        else:
                            # The last '#' in the slice corresponds to the obstacle closest to the guard
                            i_closest_obstacle = i_obstacles.pop()

                            # put guard below closest obstacle
                            map[i_closest_obstacle+1][pos["current_col"]] = dir
                            seen.append((i_closest_obstacle+1, pos["current_col"], "^"))

                        # put X:es on the indexes from (including) guard to i_closest_obstacle
                        for i_row in range(i_closest_obstacle+2,pos["current_row"]+1):
                            map[i_row][pos["current_col"]] = "^"
                            seen.append((i_row, pos["current_col"], "^"))

                        # Update guard pos
                        pos["current_row"] = i_closest_obstacle+1

                    elif dir == ">":
                        dir = "V"

                        map_slice_in_front = map[pos["current_row"]][pos["current_col"]:max_col+1]

                        i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
                        if not i_obstacles:
                            is_inside = False
                            i_closest_obstacle = max_col+1
                            new_col_i = i_closest_obstacle-1
                            # Then put X instead of guard
                            map[pos["current_row"]][new_col_i] = ">"
                            seen.append((pos["current_row"], new_col_i, ">"))
                        else:
                            # The first '#' in the slice corresponds to the obstacle closest to the guard
                            i_closest_obstacle = i_obstacles[0]

                            # put guard to the left of closest obstacle
                            new_col_i = pos["current_col"]+i_closest_obstacle-1
                            map[pos["current_row"]][new_col_i] = dir
                            seen.append((pos["current_row"], new_col_i, ">"))

                        # put X:es on the indexes from (including) guard to i_closest_obstacle
                        for i_col in range(pos["current_col"], new_col_i):
                            map[pos["current_row"]][i_col] = ">"
                            seen.append((pos["current_row"], i_col, ">"))

                        # Update guard pos
                        pos["current_col"] = new_col_i

                    elif dir == "V":
                        dir = "<"

                        map_slice_in_front = sum([[row[pos["current_col"]]] for row in map[pos["current_row"]+1:max_row+1]], [])

                        i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
                        if not i_obstacles:
                            is_inside = False
                            i_closest_obstacle = max_row+1
                            new_row_i = i_closest_obstacle-1
                            # Then put X instead of guard
                            map[new_row_i][pos["current_col"]] = "V"
                            seen.append((new_row_i, pos["current_col"], "V"))
                        else:
                            # The first '#' in the slice corresponds to the obstacle closest to the guard
                            i_closest_obstacle = i_obstacles[0]

                            # put guard above closest obstacle
                            new_row_i = pos["current_row"] + i_closest_obstacle
                            map[new_row_i][pos["current_col"]] = dir
                            seen.append((new_row_i, pos["current_col"], "V"))

                        # put X:es on the indexes from (including) guard to i_closest_obstacle
                        for i_row in range(pos["current_row"], new_row_i):
                            map[i_row][pos["current_col"]] = "V"
                            seen.append((i_row, pos["current_col"], "V"))

                        # Update guard pos
                        pos["current_row"] = new_row_i

                    elif dir == "<":
                        dir = "^"

                        map_slice_in_front = map[pos["current_row"]][0:pos["current_col"]]

                        i_obstacles = [i for i, value in enumerate(map_slice_in_front) if value == '#']
                        if not i_obstacles:
                            is_inside = False
                            i_closest_obstacle = -1
                            new_col_i = i_closest_obstacle + 1
                            # Then put X instead of guard
                            map[pos["current_row"]][new_col_i] = "<"
                            seen.append((pos["current_row"], new_col_i, "<"))
                        else:
                            # The last '#' in the slice corresponds to the obstacle closest to the guard
                            i_closest_obstacle = i_obstacles.pop()
                            new_col_i = i_closest_obstacle + 1
                            # put guard to the right of closest obstacle
                            map[pos["current_row"]][new_col_i] = dir
                            seen.append((pos["current_row"], new_col_i, "<"))

                        # put X:es on the indexes from (including) guard to i_closest_obstacle
                        for i_col in range(new_col_i+1, pos["current_col"]+1):
                            map[pos["current_row"]][i_col] = "<"
                            seen.append((pos["current_row"], i_col, "<"))

                        # Update guard pos
                        pos["current_col"] = new_col_i

                    else:
                        raise Exception("wtf")

                    # print_map(map)
            1 == 1

            n_visited = 0
            for row in map:
                n_visited += sum(
                    [
                        1 for value in row if value == "X"
                    ]
                )
            print(n_visited)
    print(p2)



def main():
    part1()
    part2()

if __name__=='__main__':
    main()