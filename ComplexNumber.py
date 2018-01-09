import math


class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return str(self.re) + " + " + str(self.im) + "j"

    def __add__(self, other):
        total_re = self.re + other.re
        total_im = self.im + other.im
        return ComplexNumber(total_re, total_im)

    def size(self):
        dist = math.sqrt(self.re**2 + self.im**2)
        return dist
