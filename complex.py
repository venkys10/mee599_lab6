#!/usr/bin/env python

import math


#class that adds real and imaginary parts of a Complex numbers
class Complex:
    def __init__(self, re = 0.0, im = 0.0):
        self.re = re
        self.im = im


    def __str__(self):
        if self.im >= 0:
            return "("+str(self.re)  +" + "+ str(self.im) + "i"+")"
        else:
            return "("+str(self.re)  +" - "+ str(abs(self.im)) + "i"+")"

    def __add__(self, other):
        if isinstance(other, Complex):
            real = self.re + other.re
            imag = self.im + other.im
            return Complex(real, imag)
        else:
            return Complex(self.re + other, self.im)


    def __sub__(self, other):
        if isinstance(other, Complex):
            real = self.re - other.re
            imag = self.im - other.im
            return Complex(real, imag)
        else:
            return Complex(self.re - other, self.im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            real = self.re * other.re
            imag = self.im * other.im
            return Complex(real, imag)
        else:
            return Complex(self.re * other, self.im)

    def __div__(self, other):
        if isinstance(other, Complex):
            real = self.re / other.re
            imag = self.im / other.im
            return Complex(real, imag)
        else:
            return Complex(self.re / other, self.im)

    def __neg__(self):
        return Complex(-self.re, -self.im)

    def complex_conjugate(self):
        return Complex(self.re, -self.im)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return self - other

    def __rmul__(self, other):
        return self * other

    def __rdiv__(self, other):
        return self / other

if __name__  == '__main__':
    c = Complex
    a = Complex(-3,-4)
    b = Complex(3.0,2)
    print c.complex_conjugate(a)         #TODO 1 - a case


