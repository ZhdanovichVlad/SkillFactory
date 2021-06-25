def print_field(game_field,stage):
    '''The function checks the victory conditions'''

    for  y_axis  in game_field: # нorizontal win
        if y_axis[0] == stage and y_axis[1] == stage and y_axis[2] == stage:
            return True

    for x_axis in range(3): #vertical win
        count = 0
        for y_axis in range(3):
           if game_field[y_axis][x_axis] == stage:
               count += 1
        if count == 3:
            return True

    if all([game_field[0][0] == stage,game_field[1][1] == stage,
            game_field[2][2] == stage]) or \
            all([game_field[0][2] == stage,game_field[1][1] == stage,
            game_field[2][0] == stage]): # diagonal win
        return True

    return False


def print_game_field(game_field):
    print("   x\y", "1 ", "  2 ", "  3 ")
    for i in range(3):
        print("  ", i + 1, game_field[i])


def main():
    '''Main directory'''

    print("Добро пожаловать и косольную игру крестики нолики"
          " от Владислава Ждановича")
    print("В игре нужно указывать ")
    game_field = [["-" for i in range(3)] for i in range(3)]
    stage = "X"
    count = 0

    while True:

        print_game_field(game_field)

        if count == 9:
            print("Игра окончена, у нас ничья")
            break

        step = input(f"Ход {stage}. Введите через пробел кординаты на оси X и Y,напоминание от 1 до 3 \n")

        try:
            coordinates = list(map(lambda x: x - 1,map(int,step.strip(" ").split(" "))))
        except ValueError :
            print("Ошибка введены буквы или символы, или стоит лишний пробел, попробуйте ещё раз")

        if len(coordinates) != 2:
            print("Вы ввели три или более символа")
            continue

        if not all([0 <= coordinates[0] <= 2,0 <= coordinates[1] <= 2]):
            print("Введена цифра больше трех или меньше еденицы, попробуем ещё раз")
            continue

        if game_field[coordinates[0]][coordinates[1]] == "X" or game_field[coordinates[0]][coordinates[1]] == "0":
            print(f"Данное поле занято, тут стоит {game_field[coordinates[0]][coordinates[1]]} введите данные заново")
            continue

        game_field[coordinates[0]][coordinates[1]] = stage

        count += 1
        if print_field(game_field, stage):
            print(f"Выйграл {stage}")
            print_game_field(game_field)
            break

        if stage == "X":
            stage = "0"
        else:
            stage = "X"

main()# Start of the program
