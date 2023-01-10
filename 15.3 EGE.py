def f(x, a):
        return ((x % a != 0) and (x % 21 == 0)) <= (x % 14 == 0)
for a in range(1, 1000):
    if all(f(x, a) == 1 for x  in range(1, 1000)):
        print(a)