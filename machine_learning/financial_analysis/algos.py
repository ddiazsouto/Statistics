#from derivative_function import dy_dx
import numpy as np
import pandas as pd


""" Auxiliary functions """

def percentage_change(first_value: float, second_value: float) -> float:
    """ Auxiliary function that calculates the percentage that an amount 
        changes from the first_value to second_value and returns it
        That simple  """        
    difference = second_value - first_value
    percentage_change = (difference*100) / first_value
    return percentage_change
        
        

"""  HERE we define the function or pn(r) used for the loss function J(pn) """


class J_function():
    """
        This is a strange thing, it is a Function Data Type
        
        It is for sure an abstract structure.
        
        It needs to contain the overall market dataframe, it just makes life 
        easier that way
        
        Theta needs to take the theta for each iteration, although at this 
        stage that is not entirely clear
        
        for sure it needs a method that optimizes r
    """
    
    def __init__(self, market_data: pd.DataFrame, purchase_time: object = 156):
        """ We initialise the class with general information"""
        self.market_data_df = market_data
        self.purchase_time = purchase_time
        self.n_dimensions = int
        
    
    def of(self, r_caret):
        """ Executes J function, which we want to minimize """
        
        number_of_dimensions = len(r_caret)
        normalizing_constant = 1/ (2 * number_of_dimensions)
        
        market_results = self._pn(r_caret)
        
        print(market_results)
        # We calculate the squared difference to a 1000% of each individual
        # dimension or asset class and store it in a vector
        
        # TODO: Wel, well... This is J, the loss and is what we need to
        #       differenciate, and we need to differenciate its rate of 
        #       change in each direction. So while _pn is a valid function,
        #       this is what we need to minimize and differenciate.
        vector = []
        for dimension in range(number_of_dimensions):
            
            loss = ( 1000 - market_results[dimension] )**2
            vector.append(loss)
            
        print(vector)
       
        # We need to find the derivatives here
        
        dJ = dy_dx(self._pn)
        
    
    def _pn(self, r_caret: np.array) -> np.array:
        """ This function takes r_caret which is a vector with the 
            ratios for each asset class and calculates another vector 
            which contains the change in the portfolio in 3 years
            ---
            inputs:
                r_caret: is a numpy array including assigned ratios
            outputs:
                portfolio_growth_percent: is a numpy array that contains the
                                          growth percentage in each dimension
            Preconditions: 
                There is a pd.DataFrame which contains the prices of asset classes
                over a period of time merged on date """
        
        delay = 22   # 22 months ahead (factored in some months of no data)
        
        
        
        # We calculate the state of portfolio when buying and selling
        buy  = self._portfolio( self.purchase_time, self.market_data_df )        
        sell = self._portfolio( self.purchase_time + delay, self.market_data_df)
        
        market_growth = percentage_change(buy, sell)        
        # Next line probably unnecessary
        portfolio_growth_percent = market_growth.dot(r_caret)
        
        vector_returns = market_growth * r_caret
        
        # TODO: the output would be better if it was a dot product it
        #       would require, however to change the derivative function
        #       (see line 144, 147)
        return vector_returns
    
    
    def get_theta(self, theta):
        """ TO BE MODIFIED, STORE THE TIME LINKED TO THETA """
        self.purchase_time = theta
        

    def _portfolio(self, start: {int, object}, df: pd.DataFrame) -> np.array:
        """ Auxiliary function, calculates the value of the portfolio at a 
        specific time """
        find_row_and_to_list = list(df.loc[start])
        # Discarding the date
        find_row_and_to_list.pop(0)
        clean_row_array = np.array(find_row_and_to_list)
        return clean_row_array
    
    
    
    
"""  TO BE IMPORTED   """


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
        
    def d(self, x: {float,np.ndarray,list}, verbose=False, dx=1e-4) -> float:
        
        f_x = self.function(x)
        dimensions = len(x)
        
        if type(x) == float:
            f_x_dx = self.function(x + dx)
            gradient = ( f_x_dx - f_x ) /dx
        # TODO: improve the gradient descent by calculating the partial
        #       derivatives using the rate of change betweek the TOTAL loss
        #       of J against rate of change of dx in each dimension
        else:
            f_x_dx = self.function([x + dx for x in x])
            gradient = np.array( [f_x_dx[j] - f_x[j] 
                                  for j in range(dimensions)])
        gradient = gradient / dx

        # We store the points computed to be able to plot them later
        point = (x, f_x)
        self.points.append( point )        
        if verbose:
            print("Here is x", x)
            print("Here f(x) is", f_x)        
            print("Now f(x+dx) is", f_x_dx)
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
        