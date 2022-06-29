def mysum(*num):
    final = 0
    for n in num:
        final += n
    return final

print(mysum(10, 2, 3))
