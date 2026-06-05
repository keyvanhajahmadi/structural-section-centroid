import math


def mostatil(l,h):
    x = l/2
    y = h/2
    return x , y
def mosalas(h):
    y = h / 3
    x = 0
    return y , x
def nimdaiere(r):
    x = 0
    y = 4*r/3*math.pi
    return x , y
def robdaire(r):
    x = 4*r/3*math.pi
    y = 4*r/3*math.pi
    return x , y 
def nimbeiezi(a,b):
    x = 0
    y = 4 * b / 3 * math.pi
    return x , y
def robbeizi(a,b):
    x = 4 * a / 3 * math.pi
    y = 4 * b / 3 * math.pi
    return x , y
def sahmavi(a,h):
    x = 0
    y = 3 * h / 5
    return x , y
def robsahamavi(a,h):
    x = 3 * a / 8
    y = 3 * h / 5
    return x , y
def spandrol(a,h,n):
    x = (n + 1 / n + 2) * a
    y = (n + 1 / 4 * n + 2) * h
    return x , y