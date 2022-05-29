# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:26:26 2021

@author: DestRuktoR
"""
import pandas as pd
import numpy as np
import math
import scipy
class Stats:
    """
        This is an ADT for various distributions (normal, binomial...) does not matter whether continuous or
        discrete, it mainly contains mathematical constructs
        includes:
        n choose x tools and ploting tools
    """
    
    def factorial(number_input: int or float, cut_short=1):
        """ Calculates the factorial of a number """
        
        if type(number_input) == int:        
            factorial = 1        
            for i in range(number_input, cut_short, -1):
                factorial = factorial * i        
            return factorial
        else:
            return math.gamma(number_input+1)
    
    
    def C(n, x):
        """ Calculates n choose x """
        
        if n == 0 or x > n:  
            return 0
        elif  x == 0 or n == x:
            return 1
        return scipy.special.comb(n, x)
        # return Stats.factorial(n, cut_short = (n-x) ) // Stats.factorial(x)



class Discretedistribution(Stats):
    """ Abstract Data Type that will be reused to generate a p.m.f. """
    
    def discrete_plot(self):
        
        pmf = self.probability_distribution
        title_value = 'critical value =' + str(self.c_value())
        pd.DataFrame(pmf).plot(kind='bar',  figsize=(9,6), legend=False, title = title_value)
        
    
    def c_value(self, s_level=0.05, dist = False):
        
        cumulative_probability = 0
        self.s_level = s_level
        cmf = []
        
        for count, i in enumerate(self.probability_distribution): 
            cumulative_probability = cumulative_probability + i
            
            # if cumulative_probability*2 >= 0.05 and dist == False:
            #     return 1%(count - 1)
            
            if dist == True:
                cmf.append(cumulative_probability)
        return cmf
        
        
    def __str__(self):
        return str(self.probability_distribution)


class ContinuousDistribution(Stats):
    """
        Abstract Data Type containing elements needed to work with continuous data
        ---
        Inherits Stats class
    """
    def continuous_plot(self):
        pdf = self.probability_distribution
        pd.DataFrame(pdf).plot(kind='area', figsize=(9,6), legend=False, title = None)
        
        


class Poisson(ContinuousDistribution, Discretedistribution):
    """ Implementation of a Poisson model
        ---
        
        f(x) =    -lambda        x
                 e      * lambda
                 ------------------
                         x!
                         
    Treated as continuous
    """
    
    def __init__(self, parameter_lambda: float):
        """ Initialise  """
        self._lambda                  = parameter_lambda
        self.probability_distribution = self.p_function()
        
    def _function(self, parameter_lambda: float, x: float):
        exp_minus_lambda = np.e**(-parameter_lambda)
        exponential_term = parameter_lambda**x
        factorial_term   = Poisson.factorial(x)
        
        return (exponential_term / factorial_term) * exp_minus_lambda
    
    def p_function(self):
        p_x = 1
        x   = 0
        pdf = []
        while (p_x > 1e-10):
            p_x = self._function(self._lambda, x)
            x += 0.05
            pdf.append(p_x)
        return pdf
        
    def P(self, X: float):
        return self._function(self._lambda, X)
        
        


class Binomial(Discretedistribution):
    """
        Implementing a binomial distribution
    """
    
    def __init__(self, n: int, p: int):
        """ Initiates the class modelling X ~ B(n,p) """
        
        self.probability_distribution = self.p_function(n, p)
        self.cumulative_distribution  = self.c_value(dist=True)
        self.s_level = 0.05

    
    # def c_value(self, s_level=0.05, dist = False):
        
    #     cumulative_probability = 0
    #     self.s_level = s_level
    #     cmf = []
    
    """ Probably getting rid of this one"""
    
    #     for count, i in enumerate(self.probability_distribution): 
    #         cumulative_probability = cumulative_probability + i
            
    #         if cumulative_probability*2 >= 0.05 and dist == False:
    #             return 1%(count - 1)
    #         elif dist == True:
    #             cmf.append(cumulative_probability)
    #     return cmf

    
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
    
    def F(self, X):
        return self.cumulative_distribution[X]
    
    
    
    
    
class Geometric(Discretedistribution):
    
    def __init__(self, p):
        self.probability_distribution = self.p_function(p)
        self.cumulative_distribution = self.c_value(dist=True)
        
    def p_function(self, p: float):
        
        pmf = [0]
        X = 1
        last_value = 1
        
        while (last_value > 0.000005 ):
            P_of_X = ((1 - p)**(X-1 )) * p
            pmf.append(round(P_of_X, 4))
            
            X += 1
            last_value = P_of_X          
            
        return pmfcleaned_df.meaq
    
    def P(self, X):
        return self.probability_distribution[X]
    
    def F(self, X):
        return self.cumulative_distribution[X]
    
            
    
"""
    WORKING
"""
  
from scipy.stats import norm
from math import sqrt



class StandardNormal:

    def F(self, Z):
        out = norm.cdf(Z)
        
        #norm.ppf(0.975)
        return out
    
    def quant(self, q):
        out = norm.ppf(q)
        return out
    
    def P(self, x):
        
        exp = (-1/2)*((x-self.mew)/self.sigma)**2        
        compute = (1/(self.sigma*sqrt(2*math.pi)))*math.exp(exp)        
        return compute



class NormalDist(StandardNormal):
    
    def __init__(self, mew, sigma_squared):
        
        self.mew = mew
        self.sigma_squared = sigma_squared
        self.sigma = sqrt(sigma_squared)
    
    def F(self, Z):
        out = norm.cdf(Z)
        
        #norm.ppf(0.975)
        return out
    
    def quant(self, q):
        out = norm.ppf(q)
        return out
    
    def P(self, x):
        
        exp = (-1/2)*((x-self.mew)/self.sigma)**2        
        compute = (1/(self.sigma*sqrt(2*math.pi)))*math.exp(exp)        
        return compute



  
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
    