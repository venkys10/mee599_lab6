#!/usr/bin/env python

import math

class Roots:
    def __init__(self, x_2, x, c):
    #Check if roots are real or complex
        self.a = x_2
        self.b = x
        self.c = c

    def disc(self):
        self.discr = ((self.b) **2) - (4 * self.a * self.c)


        if self.discr > 0:
            print "Real Roots for this expression", self.discr
            root1 = (-self.b + math.sqrt(self.discr)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(self.discr)) / (2 * self.a)
            return root1, root2

        elif self.discr == 0:
            print "One real root for this expression", self.discr
            root1 = (-self.b) / (2 * self.a)
            return root1

        else:
            print "Complex roots for this expression", self.discr
            real_root1 = (-self.b)/(2*self.a)
            imag_root1 = math.sqrt(abs(self.discr)) / (2 * self.a)
            real_root2 = (-self.b)/(2*self.a)
            imag_root2 = (-math.sqrt(abs(self.discr))) / (2 * self.a)
            return "(" + str(real_root1) + str(imag_root1) + "i" + ")", "(" + str(real_root2) + "-" + str(imag_root2) + "i" + ")"

    def __str__(self):
        return self.disc
'''
        disc1 = abs(disc)
        root1 = (-x + math.sqrt(disc1) + "i") / (2.0 * x_2)
        
        # calculate roots
        root1 = (-x + math.sqrt(disc)) / (2.0 * x_2)
        root2 = (-x - math.sqrt(disc)) / (2.0 * x_2)
        #print "Roots are:",root1, root2
        return root1, root2


        root = -x / (2.0 * x_2)
        #print "Root is:", root
        return root
'''



if __name__ == '__main__':
    c = Roots(1,2,1)
    c.disc()
    #print c

