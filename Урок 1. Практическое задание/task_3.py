"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
import operator

company = {
    'Salesforce': 800,
    'Adobe': 700,
    'NVIDIA': 1200,
    'Amazon': 900
}

# Вариант 1
# O(N log N)
sorted_one = sorted(company.items(), key=operator.itemgetter(1))

# или
sorted_two = sorted(company.items(), key=lambda x: x[1])


def best_company(*args):
    for i, value in enumerate(sorted_one[::-1]):
        if i < 3:
            print(value)
        else:
            break


best_company(sorted_one)
best_company(sorted_two)


# Вариант 2
# O(N) - самый лучший вариант т.к быстрее и по графику роста линия плавно и медленно поднимается вверх
def three_max(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max

print(three_max(company))
