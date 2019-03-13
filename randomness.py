#!/usr/bin/env python3

from math import sqrt

# YOUR CODE GOES HERE
import math
import numpy as np

class randnr:
    def __init__(self, seed=1):
        self.seed = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32
        
    def randint(self):
        return (self.a*self.seed+self.c)%self.m
        
    def random(self):
        return float((self.a*self.seed+self.c)%self.m)/float(self.m)
    
    def exp(self):
        return  -self.c*math.log(1-self.random())
    
    def gauss(self, mean=0, std=1, m=10):
        x_ls = []
        for i in range(m):
            x_ls.append(randnr(self.seed).random())
            self.seed = randnr(self.seed).randint()
        x =  (sum(x_ls)-float(m/2))/sqrt(float(m)/float(12))
        return x*std + mean

