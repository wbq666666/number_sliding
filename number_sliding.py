import random


def print_board(board):
    for row in board:
        print(row)


def check_win(board):
    return board == [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]]


def find_empty_space(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j


def move_left(board):
    empty_i, empty_j = find_empty_space(board)
    if empty_j > 0 :
        board[empty_i][empty_j], board[empty_i][empty_j - 1] = board[empty_i][empty_j - 1], board[empty_i][empty_j]
        return True
    return False


def move_right(board):
    empty_i, empty_j = find_empty_space(board)
    if empty_j < 2 :
        board[empty_i][empty_j + 1], board[empty_i][empty_j] = board[empty_i][empty_j], board[empty_i][empty_j + 1]
        return True
    return False


def move_up(board):
    empty_i, empty_j = find_empty_space(board)
    if empty_i > 0:
        board[empty_i][empty_j], board[empty_i - 1][empty_j] = board[empty_i - 1][empty_j], board[empty_i][empty_j]
        return True
    return False


def move_down(board):
    empty_i, empty_j = find_empty_space(board)
    if empty_i < 2:
        board[empty_i][empty_j], board[empty_i + 1][empty_j] = board[empty_i + 1][empty_j], board[empty_i][empty_j]
        return True
    return False


def generate_random_board():
    # 创建包含数字1到8的列表
    numbers = list(range(1, 9))

    # 随机打乱列表中的元素

    random.shuffle(numbers)
    # 将打乱后的元素填充到3x3的游戏板中
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    for i in range(2):
        for j in range(3):

            board[i][j] = numbers.pop()

    board[2][2] = 0
    board[2][0] = numbers.pop()
    board[2][1] = numbers.pop()
    return board

def main():
    board = generate_random_board()
    print_board(board)

    while True:
        if check_win(board):
            print("游戏结束！")
            break

        move = input("请输入移动方向（上：w，下：s，左：a，右：d）：")

        if move == 'w':
            move_up(board)  # 调用向上移动函数
            print_board(board)
            pass
        elif move == 's':
            move_down(board)  # 调用向下移动函数
            print_board(board)
            pass
        elif move == 'a':
            move_left(board)
                # board = move_left(board)  # 调用向下移动函数
            print_board(board)
        elif move == 'd':
            move_right(board)
                # board = move_down(board)
            print_board(board)  # 调用向右移动函数
            pass
        else:
            print("无效的移动指令，请重新输入！")

    # if __name__ == "__main__":
    #     random_board = generate_random_board()
    #     for row in random_board:
    #         print(row)


if __name__ == "__main__":
    main()
