# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 08:53:47 2021

@author: DestRuktoR
"""
import pandas as pd


class dy_dx:
    """
        dy/dx = f(x + Delta(x)) - f(x) 
                ---------------------
                     Delta(x)
    """
    
    def __init__(self):
        self.x = []
        self.y = []
        
    def _dx(self, x):
        dx = x - self.x[-1]
        print(dx)
        return abs(dx)*100
    
    def _empty(self):
        return (len(self.x)==0) and (len(self.y)==0)
    
    def derivate(self, x: float, func) ->float:
        
        y = func(x)
        if len(self.y)>0 :
            print("x+dx is ", x, "x  is", self.x[-1], "\nf(x+dx) is", y, "\nand f(x) is", self.y[-1])
            
        if self._empty():
            self.x.append(x)
            self.y.append(y)
            return 1
            
        dx = self._dx(x)     
        print('mydx is ', dx)
        gradient = (y - self.y[-1])
        
        print('absolute result', gradient)
        
        gradient = gradient/dx
        
        print(gradient)
        
        self.x.append(x)
        self.y.append(y)
        
        return gradient
    
    def plot(self):
        x = self.x
        y = self.y
        
        frame = pd.DataFrame({'x':x, 'y':y})
        frame = frame.set_index('x')
        frame.plot()
        
        
    