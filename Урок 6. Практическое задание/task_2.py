"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

import memory_profiler as mp


def task(n):
    if n == 0:
        return ''
    else:
        st = str(n % 10)
        return st + task(n // 10)


@mp.profile()
def t(n):
    return task(n)


if __name__ == '__main__':
    print(f'169 - {t(169)}')

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20     18.8 MiB     18.8 MiB           1   @mp.profile()
    21                                         def t(n):
    22     18.8 MiB      0.0 MiB           1       return task(n)


169 - 961


При профилировании рекурсивных алгоритмов через декоратор выводятся данные о каждом вызове функции рекурсии.
В результате получаем сложно анализируемую простыню.
Как вариант можно внести вызов рекурсии в дополнительную функцию и профилировать уже ее.
"""