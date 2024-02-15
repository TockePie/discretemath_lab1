# Обчислення даного виразу
def step1(a, b, u):
    not_a = u - a
    r = not_a & b
    return r


def step2(a, b, u):
    not_a = u - a
    not_b = u - b
    r = not_a & not_b
    return r


def step3(a, b, u):
    not_a = u - a
    r = not_a | b
    return r


def step4(var, u):
    r = u - var
    return r


def step5(var2, u):
    r = u - var2
    return r


def step6(c, var4):
    r = c | var4
    return r


def step7(var6, var5):
    r = var6 & var5
    return r


def step8(var7, var3):
    r = var7 & var3
    return r


# Обчислення спрощеного виразу
def simplestep1(a, c):
    return (c | a)


def simplestep2(var, b):
    return (var & b)


# Обчислення другої лог операції
def calc(not_a, c):
    return (not_a | c)


# Обчислення другої лог. операії власною функцією
def cuscalc(not_a, c):
    for i in c:
        if i not in not_a:
            not_a.add(i)
    return (not_a)
