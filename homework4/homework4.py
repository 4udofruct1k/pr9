list = []
cnt_ch = 0
cnt_nech = 0
while True:
    num = input("Введите число: ")
    if num.isdigit() or num == "end":
        if num == "end":
            break
        else:
            list.append(int(num))
    else:
        print("Введена буква")
print(list)
for i in list:
    if i % 2 == 0:
        cnt_ch += 1
    if i % 2 == 1:
        cnt_nech += 1
print(f"Количество четных чисел - {cnt_ch}")
print(f"Количество нечетных чисел - {cnt_nech}")
