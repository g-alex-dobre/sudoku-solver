board = [[5, 6, 0, 9, 0, 3, 0, 0, 0],
         [0, 0, 0, 0, 8, 7, 0, 1, 0],
         [1, 9, 7, 0, 0, 0, 0, 8, 0],
         [0, 0, 0, 8, 9, 0, 2, 0, 0],
         [9, 0, 0, 0, 4, 5, 8, 0, 0],
         [8, 5, 1, 0, 2, 0, 3, 4, 0],
         [7, 3, 4, 0, 0, 0, 5, 9, 8],
         [2, 0, 0, 5, 0, 8, 0, 6, 4],
         [0, 0, 0, 4, 0, 9, 0, 0, 2]]


def turn_to_strings(board_to_process):
    new_board = []
    for i in board_to_process:
        new_board.append([str(x) for x in i])
    return new_board


def complete_missing_nums(list1):
    missing_nums = ""
    for i in range(1, 10):
        if str(i) not in list1:
            missing_nums += str(i)
    new_list = []
    for i in range(0, len(list1)):
        if list1[i] == "0":
            new_list.append(missing_nums)
        else:
            new_list.append(list1[i])
    return new_list


def get_max(list):
    maxim = "9"
    for item in list:
        if len(item) > 1:
            maxim = item
    return maxim

def getBlocks(board):
    answer = []
    for r in range(3):
        for c in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[3*r + i][3*c + j])
            answer.append(block)
    return answer


def build_from_blocks(list):
    l = getBlocks(list)
    l2 = build_from_rows(l)
    output = getBlocks(l2)
    return output


def build_from_rows(board_to_process):
    new_board = []
    for row in board_to_process:
        new_board.append(complete_missing_nums(row))
    return new_board


def transpose_matrix(board_to_process):
    new_board = []
    for col in range(len(board_to_process[0])):
        new_col = []
        for row in range(len(board_to_process)):
            new_col.append(board_to_process[row][col])
        new_board.append(new_col)
    return new_board


def build_from_columns(board_to_process):
    new_board = []
    for col in range(len(board_to_process[0])):
        new_col = []
        for row in range(len(board_to_process)):
            new_col.append(board_to_process[row][col])
        new_board.append(complete_missing_nums(new_col))
    return transpose_matrix(new_board)


def str_intersection(str1, str2, str3):
    output_str = ""
    for char in str1:
        if char in str2 and char in str3:
            output_str += char
    return output_str

def show_matrix(a):
    for row in a:
        print(row)

def intersect_matrices(board1, board2, board3):
    output = []
    ok = False
    sum = 0
    for row in range(len(board1)):
        row_list = []
        for col in range(len(board1[row])):
            value = str_intersection(board1[row][col], board2[row][col], board3[row][col])
            row_list.append(value)
            sum += int(value)
        output.append(row_list)
    if sum == 405:
        ok = True
    return output, ok


def cleanm(matrix):
    new_matrix = []
    for list in matrix:
        new_list = []
        for item in list:
            if len(item) > 1:
                new_list.append("0")
            else:
                new_list.append(item)
        new_matrix.append(new_list)
    return new_matrix

def solve_sudoku(board):
    ok = False
    str_board = turn_to_strings(board)
    result = str_board.copy()
    while not ok:
        board1 = build_from_rows(str_board)
        board2 = build_from_columns(str_board)
        board3 = build_from_blocks(str_board)
        result, ok = intersect_matrices(board1, board2, board3)
        if not ok:
            str_board = cleanm(result)
        else:
            return result


solved_sudoku = solve_sudoku(board)


print("The solution is: \n")
for row in solved_sudoku:
    print(row)

