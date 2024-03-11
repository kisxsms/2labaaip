a = input("Введите пароль ")
b = input("Подтвердите пароль ")
if len(a) >= 8 and len(b) >= 8 and a == b:
    print("Пароль принят")
else:
    print("Пароль не принят")
