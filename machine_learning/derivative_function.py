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
    
    def __init__(self, function):
        # We store the result of computations so we can plot the results obtained
        self.points = []
        self.function = function
        
    def derivate(self, x: float, verbose=False) ->float:
        
        dx = 1e-10
        f_of_x = self.function(x)
        f_of_x_plus_dx = self.function(x + dx)
        gradient = ( f_of_x_plus_dx - f_of_x ) /dx
        
        # We store the points computed to be able to plot them later
        point = (x, f_of_x)
        self.points.append( point )        
        if verbose:
            print("Here is x", x)
            print("Here f(x) is", f_of_x)        
            print("Now f(x+dx) is", f_of_x_plus_dx)
            print('result of [f(x+dx) - f(x)] is', gradient)        
        return gradient

    
    def plot(self):

        frame = pd.DataFrame(self.points, columns = ['X', 'Y'])
        #frame = frame.set_index('x')
        frame.plot()
        
        """   FROM coursera
        
        # Plot the data points
        plt.scatter(x_train, y_train, marker='x', c='r')
        # Set the title
        plt.title("Housing Prices")
        # Set the y-axis label
        plt.ylabel('Price (in 1000s of dollars)')
        # Set the x-axis label
        plt.xlabel('Size (1000 sqft)')
        plt.show()
        
        """
        
        
        
        
    