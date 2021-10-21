
####################################################
# CS 5600/6600: F20: Assignment 1
# YOUR NAME: Connor Osborne
# YOUR A#: A01880782
#####################################################

import numpy as np

class and_percep:

    def __init__(self):
        # your code here
        np.random.seed(9)
        self.w0 = np.array([0.5, 0.5])
        self.b = -1

    def output(self, x):
        # your code here
        z1 = np.dot(x, self.w0)

        if z1 >= -1 * self.b:
            a2 = 1
            return a2
        else:
            a2 = 0
            return a2


class or_percep:
    
    def __init__(self):
        # your code here
        self.w0 = np.array([1.01, 1.01])
        self.b = -1

    def output(self, x):
        # your code here
        z1 = np.dot(x, self.w0)

        if z1 >= -1 * self.b:
            a2 = 1
            return a2
        else:
            a2 = 0
            return a2


class not_percep:
    
    def __init__(self):
        # your code here
        self.w0 = np.array([-1])
        self.b = 0.5

    def output(self, x):
        # your code here
        z1 = np.dot(x, self.w0)

        if z1 >= -1 * self.b:
            a2 = 1
            return a2
        else:
            a2 = 0
            return a2


class xor_percep:
    
    def __init__(self):
        # your code here
        self.andp1 = and_percep()
        self.andp2 = and_percep()

        self.orp = or_percep()

        self.notp = not_percep()

    def output(self, x):
        # your code here
        z1 = self.orp.output(x)
        z2 = self.andp2.output(x)
        z3 = self.notp.output(np.array([z2]))
        z4 = self.andp1.output(np.array([z1, z3]))

        return z4


class xor_percep2:
    def __init__(self):
        self.w0 = np.array([0.51, 0.51])
        self.w1 = np.array([1.01, 1.01])
        self.w2 = np.array([-1.5, 1.01])

        self.b = -1

    def threshold(self, x):
        # your code here
        z1 = np.dot(x, self.w1)
        if z1 >= -1 * self.b:
            a1 = 1
        else:
            a1 = 0

        z2 = np.dot(x, self.w0)
        if z2 >= -1 * self.b:
            a2 = 1
        else:
            a2 = 0

        a = np.array([a2, a1])
        return a

    def output(self, x):
        # your code here
        a = self.threshold(x)
        z3 = np.dot(a, self.w2)

        if z3 >= -1 * self.b:
            a3 = 1
            return np.array([a3])
        else:
            a3 = 0
            return np.array([a3])


class percep_net:
    
    def __init__(self):
        # your code here
        self.orp1 = or_percep()
        self.notp = not_percep()
        self.andp = and_percep()
        self.orp2 = or_percep()

    def output(self, x):
        # your code here
        z1 = self.orp1.output(np.array([x[0], x[1]]))
        z2 = self.notp.output(np.array(x[2]))
        z3 = self.andp.output(np.array([z1, z2]))
        z4 = self.orp2.output(np.array([z3, x[3]]))

        return z4
