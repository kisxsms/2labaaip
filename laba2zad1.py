a=input("введите пароль ")
b=input("подтвердите пароль ")
if len(a)>=8 and len(b)>=8 and a==b:
    print("пароль принят")
else:
    print("пароль не принят")
