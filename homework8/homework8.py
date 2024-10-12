import random
def comp_choise():
    return random.randint(1,5)


ticket = [
    [ 1, 2, 3, 4, 5],
    [ 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    ]
print("Лотерейный билет:")
for i in ticket:
    print(i)
print("  ")
user = []
computer = []
for i in range(5):
    while True:
        print(ticket[i])
        usr_choise = input("Выберите одно из 5 чисел по номеру от 1 до 5:")
        if usr_choise in ["1", "2", "3", "4", "5"]:
            user.append(ticket[i][int(usr_choise)-1])
            break
        else:
            print("Неверный ввод")
    computer.append(ticket[i][int(comp_choise())-1])
cnt = 0
for i in range(5):
    if user[i] == computer[i]:
        cnt += 1
print(f"Пользователь выбрал {user}. Компьютер выбрал {computer}")
if cnt == 5:
    print("Вы выиграли миллион!!!")
