# Обчислення даного виразу
def step1(a, b, u):  # Обчислення першого кроку виразу: ¬A ∩ B
    not_a = u - a
    r = not_a & b
    return r


def step2(a, b, u):  # Обчислення другого кроку виразу: ¬B ∩ ¬A
    not_a = u - a
    not_b = u - b
    r = not_a & not_b
    return r


def step3(a, b, u):  # Обчислення третього кроку виразу: ¬A ∪ B
    not_a = u - a
    r = not_a | b
    return r


def step4(var, u):  # Обчислення четвертого кроку виразу: ¬(¬A ∩ B)
    r = u - var
    return r


def step5(var2, u):  # Обчислення п'ятого кроку виразу: ¬(¬B ∩ ¬A)
    r = u - var2
    return r


def step6(c, var4):  # Обчислення шостого кроку виразу: C ∪ ¬(¬A ∩ B)
    r = c | var4
    return r


def step7(var6, var5):  # Обчислення сьомого кроку виразу: C ∪ ¬(¬A ∩ B) ∩ ¬(¬B ∩ ¬A)
    r = var6 & var5
    return r


def step8(var7, var3):  # Обчислення восьмого кроку виразу: C ∪ ¬(¬A ∩ B) ∩ ¬(¬B ∩ ¬A) ∩ (¬A ∪ B)
    r = var7 & var3
    return r


# Обчислення спрощеного виразу
def first_short_step(a, c):  # Знаходить об'єднання множин C та A
    return c | a


def second_short_step(var, b):  # Обчислення спрощеного виразу: (C ∪ A) ∩ B
    return var & b


# Обчислення другої логічної операції за допомогою вбудованих функцій Python
def calc(not_a, c):  # Знаходить об'єднання комплемента множини A та множини C
    return not_a | c


# Обчислення другої логічної операції власною функцією
def cuscalc(not_a, c):  # Знаходить об'єднання комплемента множини A та множини C власною функцією
    for i in c:
        if i not in not_a:
            not_a.add(i)
    return not_a
