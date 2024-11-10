import re

milo = input("Введите почту:")
print(f"Почта пользователя: {milo}")
razb = re.search(r'([^@]+)@(.+)', milo)
check = ["", ""]
if "@" in milo:
    check[0],check[1] = milo.split("@")
if check[0] and check[1]:
    print(f"Username: {razb[1]}")
    print(f"Domain: {razb[2]}")
else:
    print("Некорректный email")
