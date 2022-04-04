"""
Описати клас TriangleEx – нащадок Triangle, у якому реалізувати класовий метод fromsegment(cls, s, p)
побудови трикутника за даним відрізком s та даною точкою p.
Описати також клас помилки невалідного трикутника.
Забезпечити ініціювання помилки у методі fromsegment, якщо трикутник невалідний.
З використанням класу TriangleEx розв’язати задачу.
Дано відрізок та послідовність точок.
Побудувати на цьому відрізку трикутник найбільшої площі з використанням однієї з точок.
Виконати обробку помилки невалідного триктуника з виведенням повідомлення та продовженням роботи.
"""
from t14_01_triangle import *


class InvalidTriangleError(Exception):
    def __str__(self):
        return "Невалідний трикутник"


class TriangleEx(Triangle):
    def fromsegment(cls, s, p):
        """
        :param s: об'єкт класу Segment
        :param p: об'єкт класу Point2
        :return: об'єкт класу Triangle
        """
        s1 = s.len()
        s2 = Segment(s._a, p).len()
        s3 = Segment(s._b, p).len()
        if not (s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2):
            raise InvalidTriangleError
        t = Triangle(s._a, s._b, p)
        return t
    fromsegment = classmethod(fromsegment)


if __name__ == "__main__":
    s0 = Segment(Point2(0, 0), Point2(0, 1))
    points = [Point2(0, 0), Point2(2, 0), Point2(3, 0)]
    triangles = []
    for point in points:
        try:
            triangles.append(TriangleEx.fromsegment(s0, point))
        except InvalidTriangleError:
            print(f"З точкою {point} будується невалідний трикутник")

    biggest_triangle = None
    biggest_area = 0
    for triangle in triangles:
        if triangle.square() > biggest_area:
            biggest_triangle = triangle
            biggest_area = triangle.square()
    print(biggest_triangle)
