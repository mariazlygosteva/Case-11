# Case-study # 11
# Developers: Sedelnikova P., Simonov A., Fedotova M.
#
from turtle import *
import math
import random
import ru_local as ru


def koch(n: int, a: float) -> None:
    '''
    Draws a Koch curve of a given order and size.

    The Koch curve is a fractal curve that is constructed by recursively
    dividing a segment into 3 parts and replacing the middle part with two
    segments, forming an equilateral triangle.

    Args:
        n (int): The order of the curve (depth of recursion).
        When n=0, a straight line is drawn.
        a (float): The length of the initial segment.

    Returns:
        None
    '''
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


def koch_snowflake(n: int, a: float) -> None:
    '''
    Draws a Koch snowflake from three Koch curves.

    A Koch snowflake is a closed curve formed by three Koch curves,
    connected in an equilateral triangle.

    Args:
        n (int): Snowflake order (recursion depth).
        a (float): The side length of the original triangle.

    Returns:
        None
    '''
    for i in range(3):
        koch(n, a)
        rt(120)


def tree(height: int, length: float, angle: int) -> None:
    '''
    Draws a binary tree recursively.

    The tree is built by recursive branching - each branch is divided
    into two sub-branches at a given angle with decreasing length.

    Args:
        height (int): The height of the tree (the number of branching levels).
        length (float): The length of the initial branch.
        angle (int): The angle between the child branches.

    Returns:
        None
    '''
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


def mandala(depth: int, size: float) -> None:
    '''
    Draws a recursive mandala.

    The mandala is constructed as a circular pattern with recursive elements.,
    located in 8 directions.

    Args:
        depth (int): The depth of the recursion.
        It is recommended to use values from 1 to 5.
        size (float): The base size of the mandala.

    Returns:
        None

    Note:
        When depth=0, a simple circle is drawn.
    '''
    if depth == 0:
        circle(size * 0.2)
    else:
        for i in range(8):
            fd(size * 0.3)
            mandala(depth - 1, size * 0.6)
            bk(size * 0.3)
            lt(45)


def rotating_squares(size: float, n: int) -> None:
    '''
    Draws rotating squares.

    Squares are drawn recursively with decreasing size and rotation,
    creating a spiral effect.

    Args:
        size (float): The size of the initial square.
        n (int): The number of squares to draw.

    Returns:
        None
    '''
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


def recursive_squares(size: float, n: int) -> None:
    '''
    Draws recursive squares (Minkowski curve).

    The Minkowski curve is a fractal curve that fills the space
    by recursively dividing a square into smaller squares.

    Args:
        size (float): The size of the initial square.
        n (int): The depth of recursion.

    Returns:
        None
    '''
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


def leha(size: float, n: int) -> None:
    '''
    Draws the fractal 'Lech' (letters LECH).

    A special fractal that forms the letters L, E, X, and A in a recursive way.
    Each letter is built from smaller versions of the fractal itself.

    Args:
        size (float): The size of the fractal.
        n (int): The depth of recursion.

    Returns:
        None
    '''

    def draw_l() -> None:
        '''Draws the letter L of the fractal.'''
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

    def draw_e() -> None:
        '''Draws the letter E of the fractal.'''
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

    def draw_h() -> None:
        '''Draws the letter X of the fractal.'''
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

    def draw_a() -> None:
        '''Draws the letter A of the fractal.'''
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
        draw_l()
        draw_e()
        draw_h()
        draw_a()


def ice_1(order: int, size: float) -> None:
    '''
    Draws the first version of the ice fractal.

    The ice fractal mimics the shape of ice crystals with symmetrical branches.
    The first option has a simpler structure with right angles.

    Args:
        order (int): The order of the fractal (the depth of recursion).
        size (float): The length of the base segment.

    Returns:
        None
    '''
    if order == 0:
        fd(size)
    else:
        ice_1(order - 1, size / 2)
        lt(90)
        ice_1(order - 1, size / 4)
        lt(180)
        ice_1(order - 1, size / 4)
        lt(90)
        ice_1(order - 1, size / 2)


def ice_2(order: int, size: float) -> None:
    '''
    Draws the second version of the ice fractal.

    The second version of the ice fractal has a more complex structure.
    with angles of 60 and 120 degrees, creating a more natural snowflake shape.

    Args:
        order (int): The order of the fractal (the depth of recursion).
        size (float): The length of the base segment.

    Returns:
        None
    '''
    if order == 0:
        fd(size)
    else:
        ice_2(order - 1, size / 2)
        x, y = position()
        heading_ = heading()
        lt(60)
        ice_2(order - 1, size / 4)
        pu()
        goto(x, y)
        setheading(heading_)
        pd()
        lt(120)
        ice_2(order - 1, size / 4)
        pu()
        goto(x, y)
        setheading(heading_)
        pd()
        ice_2(order - 1, size / 2)


def levi(order: int, size: float) -> None:
    '''
    Draws a Levy curve.

    The Levy curve is a fractal curve that is constructed by
    sequential substitution of segments by two segments at an angle of 90 degrees.

    Args:
        order (int): The order of the curve (depth of recursion).
        size (float): The length of the base segment.

    Returns:
        None
    '''
    if order == 0:
        fd(size)
    else:
        lt(45)
        levi(order - 1, size)
        rt(90)
        levi(order - 1, size)
        lt(45)


def peano(a: float, n: int) -> None:
    '''
    Draws a Peano curve.

    The Peano curve is a space-filling curve that
    passes through each point of the square. This implementation represents
    It represents one of the variants of the Peano curve.

    Args:
        a (float): The length of the base segment.
        n (int): The depth of recursion.

    Returns:
        None
    '''
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


def set_random_color() -> None:
    '''
    Sets a random drawing color.

    Generates a random RGB color and sets it as the pen color.

    Returns:
        None
    '''
    pencolor(random.random(), random.random(), random.random())


def main() -> None:
    '''
    The main function of the program.

    Provides a user interface for selecting and rendering different fractals.
    Requests parameters from the user and draws the selected fractal in the center
    of the screen.

    Returns:
        None

    Features:
        - Support for 12 different fractals
        - Centering on the screen
        - Random colors for most fractals
        - Setting parameters for each fractal
    '''
    tracer(0)
    screen = getscreen()
    screen.bgcolor('black')

    print(ru.AVAILABLE)
    print(ru.KOHA)
    print(ru.SNOWFLAKE)
    print(ru.TREE)
    print(ru.SQUARE)
    print(ru.MINKOVSKY)
    print(ru.LEVI)
    print(ru.ICE_1)
    print(ru.ICE_2)
    print(ru.LEHA)
    print(ru.PEANO)
    print(ru.MANDALA)

    choice = input(ru.CHOOSE)

    match choice:
        case '1':
            order = int(input(ru.DEPTH_1))
            size = int(input(ru.LENGTH))
            set_random_color()
            pu()
            goto(-150, 0)
            pd()
            koch(order, size)

        case '2':
            order = int(input(ru.DEPTH_1))
            size = int(input(ru.LENGTH))
            set_random_color()
            pu()
            goto(-100, 60)
            pd()
            koch_snowflake(order, size)

        case '3':
            height = int(input(ru.HEIGHT))
            angle = int(input(ru.CORNER))
            set_random_color()
            pu()
            goto(0, -100)
            setheading(90)
            pd()
            tree(height, 100, angle)

        case '4':
            n = int(input(ru.QUANTITY))
            set_random_color()
            pu()
            goto(-50, 50)
            pd()
            rotating_squares(100, n)

        case '5':
            n = int(input(ru.DEPTH_1))
            set_random_color()
            pu()
            goto(-300, 0)
            pd()
            recursive_squares(75, n)

        case '6':
            n = int(input(ru.DEPTH_1))
            a = int(input(ru.LENGTH))
            set_random_color()
            pu()
            goto(-150, -50)
            pd()
            levi(n, a)

        case '7':
            n = int(input(ru.DEPTH_1))
            a = int(input(ru.LENGTH))
            set_random_color()
            pu()
            goto(-150, 0)
            pd()
            ice_1(n, a)

        case '8':
            n = int(input(ru.DEPTH_1))
            a = int(input(ru.LENGTH))
            set_random_color()
            pu()
            goto(-150, 0)
            pd()
            ice_2(n, a)

        case '9':
            n = int(input(ru.DEPTH_1))
            set_random_color()
            pu()
            goto(-370, 0)
            pd()
            leha(15, n)

        case '10':
            n = int(input(ru.DEPTH_1))
            a = int(input(ru.LENGTH))
            set_random_color()
            pu()
            goto(-130, 0)
            pd()
            peano(a, n)

        case '11':
            depth = int(input(ru.DEPTH_2))
            size = int(input(ru.LENGTH))
            set_random_color()
            pu()
            goto(0, 0)
            pd()
            mandala(depth, size)

        case _:
            print(ru.ERROR)
            return

    update()
    done()


if __name__ == '__main__':
    main()
