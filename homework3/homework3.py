list = []
while True:
    num = input("Введите число: ")
    if num.isdigit() or num == "end":
        if num == "end":
            break
        else:
            list.append(int(num))
    else:
        print("Введена буква")

print( "Нечетные элементы списка: ")
for i in list:
    if i % 2 == 1:
        print(i)
