a = input("Введите первое число: ")
b = input("Введите второе число: ")
flaga = 1
flagb = 1
for i in a:
    if i == ".":
        continue
    elif i.isdigit() == False:
        flagb = 0
        print("неверный ввод")
        break
for i in b:
    if i == ".":
        continue
    elif i.isdigit() == False:
        flagb = 0
        print("неверный ввод")
        break
        
if flaga == 1 and flagb == 1:
    if a < b:
        for i in range(int(float(a) + 1), int(float(b) + 1), 1):
            print(i**2)
    else:
        for i in range(int(float(a) + 1), int(float(b) + 1), 1):
            print(i**2)
