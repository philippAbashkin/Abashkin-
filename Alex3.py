a = int(input())
maxx = a

while a != 0:  # "" внутри только текст, не числа
    a = int(input())
    if a > maxx:
        maxx = a

print(maxx)

# a == 0
# maxx == 4