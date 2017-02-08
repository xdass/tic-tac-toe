import random

board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

win = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
       (0, 3, 6), (1, 4, 7), (2, 5, 8),
       (0, 4, 8), (2, 4, 6))


def draw_board(field):
    print('{}  {}  {}'.format(field[0], field[1], field[2]))
    print('{}  {}  {}'.format(field[3], field[4], field[5]))
    print('{}  {}  {}'.format(field[6], field[7], field[8]))


def player_turn():
    while True:
        try:
            choice = input('Выберите куда ставить крестик: ')
            if board[int(choice)] != 'X' and board[int(choice)] != 'O':
                board[int(choice)] = 'X'
                break
            else:
                print('Недопустимый ход!')
        except ValueError:
            pass


def ai_turn():
    print('Ход компьютера')
    while True:
        x = random.choice(range(0, 9))
        if board[x] != 'X' and board[x] != 'O':
            board[x] = 'O'
            break


def check():
    count = 0
    winer = None
    etalon = None
    first = True
    for group in win:
        for item in group:
            if first:
                if board[item].isalpha():
                    etalon = board[item]
                    count += 1
                    first = False
                    continue
            if board[item] == etalon:
                winer = etalon
                count += 1
        if count == 3:
            return True, winer
        count = 0
        first = True
    return False, None


def game():
    first_turn = True
    game_counter = 0
    draw_board(board)
    while True:
        result = check()
        game_counter += 1
        if result[0]:
            print('Победил - {}'.format(result[1]))
            break
        elif game_counter == 9:
            print('Ничья')
            break
        if first_turn:
            player_turn()
            first_turn = False
        else:
            ai_turn()
            first_turn = True
        draw_board(board)

if __name__ == '__main__':
    game()
