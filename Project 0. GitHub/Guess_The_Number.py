
import math
def game_core(number):
    '''It is a game core.'''
    count = 1
    max_number = 100
    min_number = 0
    predict = 50

    while number != predict:
        count+=1
        if number > predict:
            min_number = predict
            predict = math_round(predict + (max_number - predict)/2)
        if number < predict:
            max_number = predict
            predict = math_round(predict - (predict - min_number)/2)
        if predict == 1 and number != predict:
            predict -= 1
            count += 1

    return(count)


def math_round (number):
    '''Function for mathematically rounded to the nearest integer '''
    x = abs(number)
    r=math.floor(x)+math.floor(2*(x%1))
    return r if x>=0 else -r


for i in range(101):
   print(f"Число {i} программа угадывает за {game_core(i)} количество пыпоток")