n = int(input())

while True:
    if n % 4  == 0 and n % 100 != 0:
        print(True)
        break
    elif n % 400 == 0:
        print(True)
        break
    else:
        print(False)
        break