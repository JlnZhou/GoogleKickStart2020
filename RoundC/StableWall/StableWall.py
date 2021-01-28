T = int(input()) # Number of test cases
for i in range(T):
    # R rows
    # C columns
    R, C = [int(s) for s in input().split(" ")]
    wall = []
    for j in range(R):
        # We replace letters by int values
        line = []
        for letter in input():
            line.append(letter)
        wall.append(line)
    constraints = []
    for col in range(C):
        for row in range(R-1):
            up = wall[row][col]
            down = wall[row+1][col]
            if up != down:
                if not([down, up] in constraints):
                    constraints.append([down, up])
                if not([up, " "] in constraints):
                    constraints.append([up, " "])
                if not([down, " "] in constraints):
                    constraints.append([down, " "])
            else:
                if not([up, " "] in constraints):
                    constraints.append([up, " "])
    result = []
    result_existence = True
    for current, after in constraints:
        if len(result) == 0: # initialisation of the result
            result.append(current)
            if after != " ":
                result.append(after)
        else:
            # Insertion de current
            max_index = len(result)
            min_index = 0
            concerned_constraints = []
            for concerned_before, concerned_after in constraints:
                if concerned_before == current:
                    concerned_constraints.append(concerned_after)
            for concerned_after in concerned_constraints:
                if concerned_after in result:
                    max_index = min(max_index, result.index(concerned_after))
            concerned_constraints = []
            for concerned_before, concerned_after in constraints:
                if concerned_after == current:
                    concerned_constraints.append(concerned_before)
            for concerned_before in concerned_constraints:
                if concerned_before in result:
                    min_index = max(min_index, result.index(concerned_before)+1)
            if min_index > max_index:
                result_existence = False
            elif current in result:
                current_index = result.index(current)
                if (current_index < min_index) | (current_index > max_index):
                    result_existence = False
            else:
                result.insert(min_index, current)
            # Insertion de after
            if after != " ":
                max_index = len(result)
                min_index = 0
                concerned_constraints = []
                for concerned_before, concerned_after in constraints:
                    if concerned_before == after:
                        concerned_constraints.append(concerned_after)
                for concerned_after in concerned_constraints:
                    if concerned_after in result:
                        max_index = min(max_index, result.index(concerned_after))
                concerned_constraints = []
                for concerned_before, concerned_after in constraints:
                    if concerned_after == after:
                        concerned_constraints.append(concerned_before)
                for concerned_before in concerned_constraints:
                    if concerned_before in result:
                        min_index = max(min_index, result.index(concerned_before)+1)
                if min_index > max_index:
                    result_existence = False
                elif after in result:
                    current_index = result.index(after)
                    if (current_index < min_index) | (current_index > max_index):
                        result_existence = False
                else:
                    result.insert(min_index, after)
    if result_existence:
        result_print = ""
        for letter in result:
            result_print = result_print + letter
        print("Case #{}: {}".format(i+1, result_print))
    else:
        print("Case #{}: {}".format(i+1, -1))