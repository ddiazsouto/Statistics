# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:26:26 2021

@author: DestRuktoR
"""
import pandas as pd


class Stats:
    """
        This is an ADT for various distributions (normal, binomial...) 
        includes:
        n choose x tools and ploting tools
    """
    
    def factorial(number_input: int, cut_short=1):
        """ Calculates the factorial of a number """
        
        factorial = 1
        
        for i in range(number_input, cut_short, -1):
            factorial = factorial * i        
        return factorial
    
    
    def C(n, x):
        """ Calculates n choose x """
        
        if n == 0 or x > n:  
            return 0
        elif  x == 0 or n == x:
            return 1
        return (Stats.factorial(n)) // (Stats.factorial(x) * Stats.factorial(n-x))



class Discretedistribution(Stats):
    """ Abstract Data Type that will be reused to generate a p.m.f. """
    
    def plot(self):
        
        pmf = self.probability_distribution
        title_value = 'critical value =' + str(self.c_value())
        pd.DataFrame(pmf).plot(kind='bar',  figsize=(9,6), legend=False, title = title_value)



class Binomial(Discretedistribution):
    """
        Implementing a binomial distribution
    """
    
    def __init__(self, n: int, p: int):
        """ Initiates the class modelling X ~ B(n,p) """
        
        self.probability_distribution = self.p_function(n, p)
        self.cumulative_distribution  = []
        self.s_level = 0.05

    
    def c_value(self, s_level=0.05):
        
        cumulative_probability = 0
        self.s_level = s_level
        
        for count, i in enumerate(self.probability_distribution): 
            cumulative_probability = cumulative_probability + i
            
            if cumulative_probability*2 >= 0.05:
                return count - 1

    
    def p_function(self, n: int, p: float):
        
        pmf = []        
        
        for X in range(0, n+1):            
            ways_to_arrange = Binomial.C(n, X)           
            P_of_X = ways_to_arrange * ((p)**X) * ((1-p)**(n-X))
              
            pmf.append(round(P_of_X, 4))      
        
        self.probability_distribution = pmf
        return pmf
    
    def P(self, X):
        return self.probability_distribution[X]
    
    
from random import randint
            

class CLT:
    def __init__(self):
        pass
    

                

def select_sample(n, fromdata):
   section = []
   for i in range(n):
       section.append(fromdata[randint(0,len(fromdata)-1)])
   return section


    


def many_samples(how_many, sample_size, fromdata):
   out = []
   for i in range(how_many):
       new_sample = select_sample(sample_size, fromdata)
       frame = pd.DataFrame(new_sample)
       out.append(float(frame.mean()))
   return out


def plot(any_list):
    frame = pd.DataFrame(any_list)
    frame.plot(kind='hist')
    