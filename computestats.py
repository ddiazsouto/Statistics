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
    
    def factorial(number: int):
    
    def C(n, x):
        """ Calculates n choose x """
        
        if n == 0 or x > n:  
            return 0
        elif  x == 0 or n == x:
            return 1
        
        n_minus_x_factorial = x_factorial = n_factorial = 1  
        n_minus_x = n-x
        
        for i in range(1, n+1):
            n_factorial = n_factorial*i            
        for j in range(1, x+1):
            x_factorial = x_factorial*j            
        for k in range(1, n_minus_x+1):
            n_minus_x_factorial = n_minus_x_factorial*k
            
        return (n_factorial)//(x_factorial*n_minus_x_factorial)




class stats(Stats):   

        
    
    def critical_v(probability_function: list, s_level=0.05):
        
        cumulative_probability = 0
        
        for count, i in enumerate(probability_function): 
            cumulative_probability = cumulative_probability + i
            
            if cumulative_probability*2 >= s_level:
                return count - 1

    
    def p_function(n: int, event_p=0.5, s_level=0.05, graph=False):
        
        p_x = []        
        p_each_outcome = float((event_p)**n)
        
        for possibility in range(0, n+1):
            
            ways_to_arrange = stats.C(n, possibility)           
            p_this_outcome = p_each_outcome * ways_to_arrange
              
            p_x.append(round(p_this_outcome, 4))      
        
        if graph == True:
            c_value = 'critical value =' + str(stats.critical_v(p_x))
            pd.DataFrame(p_x).plot(kind='bar',  figsize=(9,6), legend=False, title = c_value)
        
        return p_x
    
    
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
    