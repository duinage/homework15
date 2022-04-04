# Описати клас для реалізації мультимножини цілих чисел на базі словника.
# Мультимножина-це множина в якій для кожного елемента запам’ятовується не лише його входження,але й кількість входжень.
# Кількість входжень елемента k (0<=k<=n) у мультимножину - це значення елемента словника з ключем k.
class MultiSet(dict):
    def __init__(self):
        super().__init__()
        self.multiset = {}

    # зробити мультимножину порожньою;
    def clear(self):
        self.multiset.clear()

    # чи є мультимножина порожньою;
    def if_clear(self):
        if self.multiset == {}:
            return True
        else:
            return False

    # додати елемент до мультимножини;
    def add_item(self, k):
        self.multiset[k] = self.multiset.get(k, 0) + 1

    # забрати елемент з мультимножини (кількість входжень елемента зменшується на 1, якщо елемент не входить -відмова);
    def pick_up_item(self, k):
        if self.multiset.get(k, 0) == 0:
            print('Відмова: елемент не входить')
        elif self.multiset.get(k) == 1:
            del self.multiset[k]
        else:
            self.multiset[k] = self.multiset.get(k) - 1

    # кількість входжень елемента у мультимножину;
    def number_of_item(self, k):
        return self.multiset.get(k, 0)

    # об’єднання двох мультимножин
    # (в результаті об’єднання кіlькість входжень елемента визначається як максимальна з двох мультимножин);

    def comb(self, multiset2):
        new_set = MultiSet()

        for key in self.multiset.keys():
            if self.multiset[key] < multiset2.number_of_item(key):
                new_set[key] = multiset2.number_of_item(key)
            else:
                new_set[key] = self.multiset[key]
        return new_set

    # перетин двох мультимножин
    # (в результаті кількість входжень елемента визначається як мінімальна з двох мультимножин);

    def intersection(self, multiset2):

        new_set = MultiSet()

        for key in self.multiset.keys():
            if self.multiset[key] >= multiset2.number_of_item(key):
                new_set[key] = multiset2.number_of_item(key)
            else:
                new_set[key] = self.multiset[key]
        return new_set


# перевірити, чи складаються рядки S1, S2 з одних і тих же символів, які входять у ці рядки однакову кількість разів;


s1 = 'cccbba'  # str(input('please, enter s1: '))
s2 = 'cccbba'  # str(input('please, enter s2: '))

s1_multiset = MultiSet()
for el in s1:
    s1_multiset.add_item(el)

s2_multiset = MultiSet()
for el in s2:
    s2_multiset.add_item(el)

new = s1_multiset.comb(s2_multiset)
print(new)

new2 = s1_multiset.intersection(s2_multiset)
print(new2)

if s1_multiset.comb(s2_multiset) == s1_multiset.intersection(s2_multiset):
    print(True)
else:
    print(False)
