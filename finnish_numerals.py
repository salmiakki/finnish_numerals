import random
from time import sleep
from typing import Optional

numerals_1_10 = "yksi kaksi kolme neljä viisi kuusi seitsemän kahdeksan yhdeksän kymmenen".split()


def get_finnish_numeral(x: int) -> list[str]:
    if x == 0:
        return ["nolla"]
    if 1 <= x <= 10:
        return [get_numeral_1_10(x)]
    if 11 <= x <= 19:
        return [get_numeral_1_10((x % 10)), "toista"]
    if 20 <= x <= 99:
        tens = x // 10
        ones = x % 10
        ones_str = [get_numeral_1_10(ones)] if ones else []
        return [get_numeral_1_10(tens), "kymmentä"] + ones_str
    if x == 100:
        return "sata"
    raise ValueError


def get_numeral_1_10(x: int) -> str:
    return numerals_1_10[x - 1]


def _join_numeral(parts: list[str], *, delimiter: Optional[str] = None) -> str:
    if delimiter is None:
        delimiter = ""
    return delimiter.join(parts)


def display_numeral(x: int, *, delimiter: Optional[str] = None):
    print(_join_numeral(get_finnish_numeral(x), delimiter=delimiter))


if __name__ == '__main__':
    previous = None
    x = None
    while True:
        while x == previous:
            x = random.choice(range(1, 100))
        previous = x
        print(x)

        sleep(2)
        display_numeral(x, delimiter="_")
        sleep(0.5)
        print()
