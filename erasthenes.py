#!/usr/bin/env python
# Sieve - take max number to find under, n
#       - return list of primes between 0 and n
#
# [1, 2, 3,...n] start at 2, get rid of all multiples of 2, next, get rid of all multiples of 3, etc.

import math

def primeA(n):

    candidates = range(2,n)

    x = 0
    while x != len(candidates): 
        q = candidates[x]
        candidates = [y for y in candidates if y != q and y % q]
        candidates.insert(0, q)
        x += 1
        
    candidates.insert(0, 1)

    return sorted(candidates)

def primeB(n):

    candidates = range(2,n)

    x = 0
    while x != (math.floor(0.5 * len(candidates))+1): 
        q = candidates[x]
        candidates = [y for y in candidates if y != q and y % q]
        candidates.insert(0, q)
        x += 1
        
    candidates.insert(0, 1)

    return sorted(candidates)

def primeC(n):

    candidates = range(2,n)

    x = 0
    while x != (math.sqrt(len(candidates))+1): 
        q = candidates[x]
        candidates = [y for y in candidates if y != q and y % q]
        candidates.insert(0, q)
        x += 1
        
    candidates.insert(0, 1)

    return sorted(candidates)
