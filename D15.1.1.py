"""
Скласти функцію та програму для обчислення суми всіх доданків, модуль яких
не менше e > 0, у комплексній точці z
Використати у цій функції твердження про стан програми assert для перевірки
того, що параметр z відповідає заданій умові. Обробити у програмі помилку
неправильного значення z та показати змістовне повідомлення про помилку.
"""


def f1(e, z):
    assert abs(z) < 1, str(z) + " >= 1"
    total = 0
    n = 0
    while True:
        n += 1
        addition = (-1) ** (n + 1) * z ** n / n
        total += addition
        if abs(addition) < e:
            break
    return total


z_real = float(input('z (real): '))
z_imag = float(input('z (imag): '))
z0 = z_real + z_imag * 1j
epsilon = float(input('epsilon: '))
try:
    print(f1(epsilon, z0))
except AssertionError:
    print('"z" повинно задовольняти умові |z|<1')
