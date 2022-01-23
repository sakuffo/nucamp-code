
x = 0

while x != 10:
    x = x + 1
    if x < 5:
        print(x)
    elif x == 6:
        print(x)
        continue
    elif x >= 5 and x <= 8:
        print("x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)
    else:
        print("x is bigger than 8. It is:", x)


x = 0
while x < 10:
    x = x+1
    if x == 1:
        print("small")
    if x > 2:
        x = x+1
        print("medium")
    if x == 5:
        x = 7
        print("big")

x = 10
if x < 11 and x > 9:
    print("if")
elif x > 10:
    print("elif")
else:
    print("else")

while True:
    print("True")
    break
    print("Break")
    break
    print("False")
