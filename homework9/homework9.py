import re
milo = input("Введите почту:")
print(f"Почта пользователя: {milo}")
razb = re.search(r'([\w\.\-\_\:]+)\@([\w\.]+)', milo)
print(f"Username: {razb[1]}")
print(f"Domain: {razb[2]}")