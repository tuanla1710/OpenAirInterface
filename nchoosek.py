from __future__ import division
from math import factorial
def nchoosek(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)