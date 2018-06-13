# 2018-06-11
# InfoShare: day 06.
# task04 - docstringi

def do_nothing(x, y = 10):
    """

    :param x: jakiś tam argument
    :param y:
    :return:
    """
    pass

# test

def test(a: str, b: str, c: int = 34) -> int:
    """Cos sobie tam robi

    :param str a: pierwszy arguemnt
    :param str b: drugi argument
    :param int c: a tutaj daj wiek
    """
    print(a, b, c)
    return a

test()