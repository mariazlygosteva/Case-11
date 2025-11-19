# Case-study # 11
# Developers: Sedelnikova P., Simonov A., Fedotova M.
#
from turtle import *
import math
import random
import ru_local as ru


def koch(n, a):
    if n == 0:
        fd(a)
    else:
        koch(n - 1, a / 3)
        lt(60)
        koch(n - 1, a / 3)
        rt(120)
        koch(n - 1, a / 3)
        lt(60)
        koch(n - 1, a / 3)


def koch_snowflake(n, a):
    for _ in range(3):
        koch(n, a)
        rt(120)


def tree(height, length, angle):
    if height == 0:
        return
    else:
        fd(length)
        current_pos = position()
        current_heading = heading()
        rt(angle)
        tree(height - 1, length * 0.7, angle)
        pu()
        goto(current_pos)
        setheading(current_heading)
        pd()
        lt(angle)
        tree(height - 1, length * 0.7, angle)
        pu()
        goto(current_pos)
        setheading(current_heading)
        pd()


def mandala(depth, size):
    if depth == 0:
        circle(size * 0.2)
    else:
        for i in range(8):
            fd(size * 0.3)
            mandala(depth - 1, size * 0.6)
            bk(size * 0.3)
            lt(45)


def rotating_squares(size, n):
    if n == 0:
        return
    for i in range(4):
        fd(size)
        rt(90)
    rt(7)
    pu()
    fd(size * 0.1)
    pd()
    rotating_squares(size * 0.9, n - 1)


def recursive_squares(size, n):
    if n == 0:
        fd(size)
        return
    else:
        recursive_squares(size / 2, n - 1)
        rt(-90)
        recursive_squares(size / 2, n - 1)
        rt(90)
        recursive_squares(size / 2, n - 1)
        rt(90)
        recursive_squares(size / 2, n - 1)
        recursive_squares(size / 2, n - 1)
        rt(-90)
        recursive_squares(size / 2, n - 1)
        rt(-90)
        recursive_squares(size / 2, n - 1)
        rt(90)
        recursive_squares(size / 2, n - 1)


def leha(size, n):
    def l():
        leha(size / 3, n - 1)
        rt(90)
        leha(size / 3, n - 1)
        rt(180)
        pu()
        leha(size / 3, n - 1)
        pd()
        leha(size / 3, n - 1)
        rt(135)
        leha((((size / 3) ** 2) * 2) ** 0.5, n - 1)
        leha((((size / 3) ** 2) * 2) ** 0.5, n - 1)
        rt(-135)

    def e():
        leha(size / 3, n - 1)
        leha(size / 3, n - 1)
        rt(90)
        leha(size / 3, n - 1)
        rt(90)
        pu()
        leha(size / 3, n - 1)
        pd()
        rt(90)
        leha(size / 3, n - 1)
        rt(-90)
        pu()
        leha(size / 3, n - 1)
        pd()
        rt(-90)
        leha(size / 3, n - 1)
        leha(size / 3, n - 1)

    def h():
        rt(-90)
        leha(size / 3, n - 1)
        leha(size / 3, n - 1)
        rt(180)
        pu()
        leha(size / 3, n - 1)
        leha(size / 3, n - 1)
        pd()
        rt(-90)
        leha(size / 3, n - 1)
        rt(-90)
        leha(size / 3, n - 1)
        leha(size / 3, n - 1)
        rt(180)
        pu()
        leha(size / 3, n - 1)
        leha(size / 3, n - 1)
        pd()
        rt(-90)
        leha(size / 3, n - 1)
        rt(-90)
        leha(size / 3, n - 1)
        leha(size / 3, n - 1)
        rt(180)
        pu()
        leha(size / 3, n - 1)
        leha(size / 3, n - 1)
        pd()
        rt(-90)
        leha(size / 3, n - 1)

    def a():
        rt(-90)
        leha(size / 3, n - 1)
        leha(size / 3, n - 1)
        rt(135)
        leha((((size / 3) ** 2) * 2) ** 0.5, n - 1)
        rt(135)
        leha(size / 3, n - 1)
        rt(180)
        pu()
        leha(size / 3, n - 1)
        pd()
        rt(45)
        leha((((size / 3) ** 2) * 2) ** 0.5, n - 1)
        rt(-135)
        pu()
        leha(size / 3, n - 1)
        pd()
        rt(90)
        leha(size / 3, n - 1)

    if n == 0:
        fd(size)
        return
    else:
        l()
        e()
        h()
        a()


def ice(order, size):
    if order == 0:
        fd(size)
    else:
        ice(order - 1, size / 2)
        lt(90)
        ice(order - 1, size / 4)
        lt(180)
        ice(order - 1, size / 4)
        lt(90)
        ice(order - 1, size / 2)


def ice2(order, size):
    if order == 0:
        fd(size)
    else:
        ice2(order - 1, size / 2)
        x, y = position()
        heading_ = heading()
        lt(60)
        ice2(order - 1, size / 4)
        pu()
        goto(x, y)
        setheading(heading_)
        pd()
        lt(120)
        ice2(order - 1, size / 4)
        pu()
        goto(x, y)
        setheading(heading_)
        pd()
        ice2(order - 1, size / 2)


def levi(order, size):
    if order == 0:
        fd(size)
    else:
        lt(45)
        levi(order - 1, size)
        rt(90)
        levi(order - 1, size)
        lt(45)


def peano(a, n):
    if n == 0:
        fd(a)
    else:
        peano(a, n - 1)
        rt(90)
        peano(a, n - 1)
        lt(90)
        peano(a, n - 1)
        lt(90)
        peano(a, n - 1)
        lt(90)
        peano(a, n - 1)
        rt(90)
        peano(a, n - 1)
        rt(90)
        peano(a, n - 1)
        rt(90)
        peano(a, n - 1)
        lt(90)
        peano(a, n - 1)


def wool_ball(min_radius):
    ROTATION = 15
    MIN_ANGLE = -400
    MAX_ANGLE = 400
    RANDOM_ANGLE = 10
    ANGLE_COUNT = 10

    def draw_wool(x, y, r, angle, n):
        if r <= min_radius:
            return
        ang_rad = math.radians(angle)
        x1 = x + r * math.cos(ang_rad)
        y1 = y + r * math.sin(ang_rad)
        pensize(max(1, n))
        pu()
        goto(x, y)
        pd()
        goto(x1, y1)
        new_r = r * 0.8
        new_n = n - 1 if n > 0 else 0
        if angle + ROTATION < MAX_ANGLE:
            new_angle = angle + ROTATION + random.uniform(-RANDOM_ANGLE, RANDOM_ANGLE)
            draw_wool(x1, y1, new_r, new_angle, new_n)
        if angle - ROTATION > MIN_ANGLE:
            new_angle = angle - ROTATION - random.uniform(-RANDOM_ANGLE, RANDOM_ANGLE)
            draw_wool(x1, y1, new_r, new_angle, new_n)

    R = 50
    center_x, center_y = 0, 0
    while R > 0:
        color = (random.random(), random.random(), random.random())
        pencolor(color)
        for i in range(ANGLE_COUNT):
            angle = (360 / ANGLE_COUNT) * i
            draw_wool(center_x, center_y, R, angle, 1)
        R -= 2


def main():
    tracer(0, 0)

    print('Доступные фракталы:')
    print('1. Кривая Коха')
    print('2. Двоичное дерево')
    print('3. Кривая Маша (мандала)')
    print('4. Квадрат')
    print('5. Кривая Минковского')
    print('6. Фрактал Леха')
    print('7. Ледяной фрактал (1)')
    print('8. Кривая Леви')
    print('9. Кривая Полина (Пеано)')
    print('10. Снежинка Коха')
    print('11. Ледяной фрактал (2)')
    print('12. Комок шерсти')

    choice = input('Выберите фрактал (1-12): ')

    if choice == '1':
        order = int(input('Глубина рекурсии: '))
        size = int(input('Длина стороны: '))
        pu()
        goto(-100, 0)
        pd()
        koch(order, size)

    elif choice == '2':
        height = int(input('Высота дерева: '))
        angle = int(input('Величина угла: '))
        pu()
        goto(0, -200)
        pd()
        lt(90)
        tree(height, 100, angle)

    elif choice == '3':
        depth = int(input('Глубина рекурсии: '))
        size = int(input('Длина стороны: '))
        bgcolor('black')
        pencolor('white')
        pu()
        goto(0, -size / 4)
        pd()
        mandala(depth, size)

    elif choice == '4':
        n = int(input('Количество квадратов: '))
        rotating_squares(100, n)

    elif choice == '5':
        n = int(input('Глубина рекурсии: '))
        recursive_squares(50, n)

    elif choice == '6':
        n = int(input('Глубина рекурсии: '))
        pu()
        goto(-300, 0)
        pd()
        leha(20, n)

    elif choice == '7':
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        ice(n, a)

    elif choice == '8':
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        levi(n, a)

    elif choice == '9':
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        peano(a, n)

    elif choice == '10':
        order = int(input('Глубина рекурсии: '))
        size = int(input('Длина стороны: '))
        pu()
        goto(-150, 90)
        pd()
        koch_snowflake(order, size)

    elif choice == '11':
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        ice2(n, a)

    elif choice == '12':
        min_radius = float(input("Введите минимальный радиус (от 1 до 20): "))
        if min_radius < 1 or min_radius > 20:
            min_radius = 8
        wool_ball(min_radius)

    else:
        print('Неверный выбор')
        return

    update()
    done()


if __name__ == '__main__':
    main()