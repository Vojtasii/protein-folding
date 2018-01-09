import math


class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.re and self.im:
            return '(' + str(self.re) + '+' + str(self.im) + 'j'+ ')'
        elif self.re:
            return str(self.re)
        elif self.im:
            return str(self.im) + 'j'

    def __add__(self, other):
        total_re = self.re + other.re
        total_im = self.im + other.im
        return ComplexNumber(total_re, total_im)

    def __mul__(self, other):
        total_re = self.re*other.re - self.im*other.im
        total_im = self.re*other.im + self.im*other.re
        return ComplexNumber(total_re, total_im)

    def size(self):
        dist = math.sqrt(self.re**2 + self.im**2)
        return dist
