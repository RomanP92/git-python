def f(x):
    if x <= -2:
        a = 1 - (x + 2)**2
    elif -2 < x <= 2:
        a = -x/2
    else:
        a = (x - 2)**2 + 1
    return a