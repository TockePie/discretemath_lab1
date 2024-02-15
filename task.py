from tkinter import *
import random, functions


#Функції, які генерують множини
u = set()
def universal_set():
    u.clear()
    global left_border
    left_border = int(left_universal_data.get())
    global right_border
    right_border = int(right_universal_data.get())
    universal_range = range(left_border, right_border+1, 1)
    for i in universal_range:
        u.add(i)
    print(u)
    
    
a = set()
def gen_set_A():
    a.clear()
    print("Генерується множина A")
    power = int(set_a_data.get())
    while len(a) != power:
        number = random.randint(left_border, right_border)
        if number not in a:
            a.add(number)
    print(a)
    
    
b = set()
def gen_set_B():
    b.clear()
    print("Генерується множина B")
    power = int(set_b_data.get())
    while len(b) != power:
        number = random.randint(left_border, right_border)
        if number not in b:
            b.add(number)
    print(b)
    
    
c = set()
def gen_set_C():
    c.clear()
    print("Генерується множина C")
    power = int(set_c_data.get())
    while len(c) != power:
        number = random.randint(left_border, right_border)
        if number not in c:
            c.add(number)
    print(c)


#Функції, які дають можливість ручного вводу
def manual_input_set_a():
    a.clear()
    a_pool = manual_data_set_a.get().split(",")
    for i in a_pool:
        a.add(int(i))
    print("A: ", a)
    
    
def manual_input_set_b():
    b.clear()
    b_pool = manual_data_set_b.get().split(",")
    for i in b_pool:
        b.add(int(i))
    print("B: ", b)
    
    
def manual_input_set_c():
    c.clear()
    c_pool = manual_data_set_c.get().split(",")
    for i in c_pool:
        c.add(int(i))
    print("C: ", c)
    

#Вікно 1
academic_group = 32
number_of_list = 16
variant = (number_of_list + academic_group%60)%30 + 1

root = Tk()
root.title("Вікно 1")
root.geometry("1000x500")
Label(root, text='Крадожон Максим Романович', font='Arial 14').place(x=0)
Label(root, text=f'Група {academic_group}', font='Arial 12').place(x=0, y=24)
Label(root, text=f'Номер в списку: {number_of_list}', font='Arial 12').place(x=75, y=24)
Label(root, text=f'Варіант завдання: {variant}', font='Arial 12').place(x=0, y=46)

Label(root, text ='Задайте границі універсальної множини:', font='Arial 12').place(x=0, y=100)  #Універсальна множина
Label(root, text ='(', font='Arial 12').place(x=0, y=120)
left_universal_data = Entry(root, width=3, font="Arial 12")
left_universal_data.place(x=9, y=120)
Label(root, text =',', font='Arial 12').place(x=50, y=120)
right_universal_data = Entry(root, width=3, font="Arial 12")
right_universal_data.place(x=65, y=120)
Label(root, text =')', font='Arial 12').place(x=95, y=120)
Button(root, width=24, text="Задати універсальну множину", font="Arial 10", command=universal_set).place(x=0, y=150)
Label(root, text ='Введіть потужність множин:', font='Arial 12').place(x=0, y=180)
Label(root, text ='A:', font='Arial 12').place(x=0, y=200)  #Множина А
set_a_data = Entry(root, width=6, font="Arial 12")
set_a_data.place(x=20, y=200)
Button(root, width=11, text="Згенерувати А", font="Arial 10", command=gen_set_A).place(x=0, y=230)
Label(root, text ='B:', font='Arial 12').place(x=140, y=200)  #Множина В
set_b_data = Entry(root, width=6, font="Arial 12")
set_b_data.place(x=160, y=200)
Button(root, width=11, text="Згенерувати B", font="Arial 10", command=gen_set_B).place(x=140, y=230)
Label(root, text ='C:', font='Arial 12').place(x=280, y=200)  #Множина С
set_c_data = Entry(root, width=6, font="Arial 12")
set_c_data.place(x=300, y=200)
Button(root, width=11, text="Згенерувати C", font="Arial 10", command=gen_set_C).place(x=280, y=230)
Label(root, text ='Ручний ввід А:', font='Arial 12').place(x=0, y=260)  #Ручний ввід А
manual_data_set_a = Entry(root, width=12, font="Arial 12")
manual_data_set_a.place(x=2, y=280)
Button(root, width=8, text="Задати А", font="Arial 10", command=manual_input_set_a).place(x=0, y=310)
Label(root, text ='Ручний ввід B:', font='Arial 12').place(x=140, y=260)  #Ручний ввід В
manual_data_set_b = Entry(root, width=12, font="Arial 12")
manual_data_set_b.place(x=140, y=280)
Button(root, width=8, text="Задати B", font="Arial 10", command=manual_input_set_b).place(x=140, y=310)
Label(root, text ='Ручний ввід C:', font='Arial 12').place(x=280, y=260)  #Ручний ввід С
manual_data_set_c = Entry(root, width=12, font="Arial 12")
manual_data_set_c.place(x=280, y=280)
Button(root, width=8, text="Задати C", font="Arial 10", command=manual_input_set_c).place(x=280, y=310)


# Вікно 2
def window2():
    step1res = functions.step1(a, b, u)
    step2res = functions.step2(a, b, u)
    step3res = functions.step3(a, b, u)
    step4res = functions.step4(step1res, u)
    step5res = functions.step5(step2res, u)
    step6res = functions.step6(c, step4res)
    step7res = functions.step7(step6res, step5res)
    step8res = functions.step8(step7res, step3res)
    def saver1():
        f = open(r"D.txt", "w")
        f.write(str(step8res))
        f.close()
    def step1():
        Label(root2, text=f"¬A ∩ B: {step1res}", font='Arial 12').place(x=0, y=60)
    def step2():
        Label(root2, text=f"¬B ∩ ¬A: {step2res}", font='Arial 12').place(x=0, y=80)
    def step3():
        Label(root2, text=f"¬A ∪ B: {step3res}", font='Arial 12').place(x=0, y=100)
    def step4():
        Label(root2, text=f"¬(¬A ∩ B): {step4res}", font='Arial 12').place(x=0, y=120)
    def step5():
        Label(root2, text=f"¬(¬B ∩ ¬A): {step5res}", font='Arial 12').place(x=0, y=140)
    def step6():
        Label(root2, text=f"С ∪ ¬(¬A ∩ B): {step6res}", font='Arial 12').place(x=0, y=160)
    def step7():
        Label(root2, text=f"С ∪ ¬(¬A ∩ B) ∩ ¬(¬B ∩ ¬A): {step7res}", font='Arial 12').place(x=0, y=180)
    def step8():
        Label(root2, text=f"С ∪ ¬(¬A ∩ B) ∩ ¬(¬B ∩ ¬A) ∩ (¬A ∪ B): {step8res}", font='Arial 12').place(x=0, y=200)
        Label(root2, text=f'Результат D: {step8res}', font='Arial 12').place(x=500, y=220)
    root2 = Tk()
    root2.title("Вікно 2")
    root2.title("Вікно 2")
    root2.geometry("750x300")
    Label(root2, text=f'A: {a}  ¬A: {u-a}', font='Arial 12').place(x=0)
    Label(root2, text=f'B: {b}  ¬B: {u-b}', font='Arial 12').place(x=0, y=20)
    Label(root2, text=f'C: {c}', font='Arial 12').place(x=0, y=40)
    Button(root2, width=8, text="Крок 1", font="Arial 10", command=step1).place(x=0, y=220)
    Button(root2, width=8, text="Крок 2", font="Arial 10", command=step2).place(x=80, y=220)
    Button(root2, width=8, text="Крок 3", font="Arial 10", command=step3).place(x=160, y=220)
    Button(root2, width=8, text="Крок 4", font="Arial 10", command=step4).place(x=240, y=220)
    Button(root2, width=8, text="Крок 5", font="Arial 10", command=step5).place(x=320, y=220)
    Button(root2, width=8, text="Крок 6", font="Arial 10", command=step6).place(x=400, y=220)
    Button(root2, width=8, text="Крок 7", font="Arial 10", command=step7).place(x=0, y=250)
    Button(root2, width=8, text="Крок 8", font="Arial 10", command=step8).place(x=80, y=250)
    Button(root2, width=24, text="Завантажити D у файл на ПК", font="Arial 10", command=saver1).place(x=500, y=250)
Button(root, width=8, text="Вікно 2", font="Arial 10", command=window2).place(x=300)

# Вікно 3
def window3():
    step1res = functions.simplestep1(a, c)
    step2res = functions.simplestep2(step1res, b)
    def saver2():
        f = open(r"D_simplified.txt", "w")
        f.write(str(step2res))
        f.close()
    def step1():
        Label(root3, text=f"C ∪ A: {step1res}", font='Arial 12').place(x=0, y=60)
    def step2():
        Label(root3, text=f"C ∪ A ∩ B: {step2res}", font='Arial 12').place(x=0, y=80)
        Label(root3, text=f'Результат D: {step2res}', font='Arial 12').place(x=200, y=125)
    root3 = Tk()
    root3.title("Вікно 3")
    root3.geometry("450x200")
    Label(root3, text=f'A: {a}', font='Arial 12').place(x=0)
    Label(root3, text=f'B: {b}', font='Arial 12').place(x=0, y=20)
    Label(root3, text=f'C: {c}', font='Arial 12').place(x=0, y=40)
    Button(root3, width=8, text="Крок 1", font="Arial 10", command=step1).place(x=0, y=120)
    Button(root3, width=8, text="Крок 2", font="Arial 10", command=step2).place(x=80, y=120)
    Button(root3, width=24, text="Завантажити D у файл на ПК", font="Arial 10", command=saver2).place(x=200, y=150)
Button(root, width=8, text="Вікно 3", font="Arial 10", command=window3).place(x=400)

# Вікно 4
def window4():
    stepres = functions.cuscalc(u-a, c)
    def saver3():
        f = open(r"customZ.txt", "w")
        f.write(str(stepres))
        f.close()
    def step():
        Label(root4, text=f'X ∪ Y: {stepres}', font='Arial 12').place(x=0, y=60)
        Label(root4, text=f'Результат Z: {stepres}', font='Arial 12').place(x=200, y=120)
    root4 = Tk()
    root4.title("Вікно 4")
    root4.geometry("450x200")
    Label(root4, text=f'X: {c}', font='Arial 12').place(x=0)
    Label(root4, text=f'Y: {u-a}', font='Arial 12').place(x=0, y=20)
    Button(root4, width=12, text="Розрахувати", font="Arial 10", command=step).place(x=0, y=120)
    Button(root4, width=24, text="Завантажити Z у файл на ПК", font="Arial 10", command=saver3).place(x=200, y=150)
Button(root, width=8, text="Вікно 4", font="Arial 10", command=window4).place(x=500)

# Вікно 5
def window5():
    def data_read():
        d1 = open(r"D.txt", "r")
        global datad1
        datad1 = d1.read()
        d1.close()
        Label(root5, text=f'D: {datad1}', font='Arial 12').place(x=0)
        d2 = open(r"D_simplified.txt", "r")
        global datad2
        datad2 = d2.read()
        d2.close()
        Label(root5, text=f'Спрощене D: {datad2}', font='Arial 12').place(x=0, y=20)
        z1 = open(r"customZ.txt", "r")
        global dataz1
        dataz1 = z1.read()
        z1.close()
        Label(root5, text=f'Z обчислене функцією яка написана мною: {dataz1}', font='Arial 12').place(x=0, y=40)
    dataz2 = str(functions.calc(u - a, c))
    def step():
        Label(root5, text=f'Z обчислене функціями пайтон: {dataz2}', font='Arial 12').place(x=0, y=60)
    def compare_d():
        if datad1 == datad2:
            Label(root5, text='Результати D є однаковими', font='Arial 12').place(x=500)
        else:
            Label(root5, text='Результати D є різними', font='Arial 12').place(x=500)
    def compare_z():
        if dataz1 == dataz2:
            Label(root5, text='Результати Z є однаковими', font='Arial 12').place(x=500, y=20)
        else:
            Label(root5, text='Результати Z є різними', font='Arial 12').place(x=500, y=20)
    root5 = Tk()
    root5.title("Вікно 5")
    root5.geometry("800x400")
    Button(root5, width=18, text="Зчитати результати", font="Arial 10", command=data_read).place(x=0, y=200)
    Button(root5, width=34, text="Обчислити Z за допомогою функцій пайтон", font="Arial 10", command=step).place(x=0, y=230)
    Button(root5, width=12, text="Порівняти D", font="Arial 10", command=compare_d).place(x=0, y=260)
    Button(root5, width=12, text="Порівняти Z", font="Arial 10", command=compare_z).place(x=0, y=290)
    
    
Button(root, width=8, text="Вікно 5", font="Arial 10", command=window5).place(x=600)
root.mainloop()
