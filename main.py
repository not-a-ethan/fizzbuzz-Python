for i in range(100):
    if (i % 5 == 0) and (i % 3 == 0):
        print("fizzbuzz", i)
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
