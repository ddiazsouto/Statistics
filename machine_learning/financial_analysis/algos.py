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
        
    def purchase_time(time: int) -> None:
        self.purchase_time = time
        
    
    def _loss_function(self, r_caret):
        """ Executes J function, which we want to minimize """
        
        number_of_dimensions = len(r_caret)
        normalizing_constant = 1/ (2 * number_of_dimensions)

        market_results = self._pn(r_caret)       

        # We calculate the squared difference to a 1000% of each individual
        # dimension or asset class and store it in a vector
        
        # TODO: Wel, well... This is J, the loss and is what we need to
        #       differenciate, and we need to differenciate its rate of 
        #       change in each direction. So while _pn is a valid function,
        #       this is what we need to minimize and differenciate.
        total_loss = 0
        for case_result in market_results:
            
            loss = 1000 - case_result
            total_loss += loss
            
        return total_loss*normalizing_constant

        
    def gradient_function(self, r_caret, dx = 1e-3):
        """ Returns the partial derivatives"""
        
        J = self._loss_function
        m_dimensions = r_caret.shape[0]
        
        r_caret = r_caret - (dx/m_dimensions)  # Not essential but curious to see it effect
        
        f_x = J(r_caret) # f_x, a float number
        
        partial_diff_vector = np.zeros(m_dimensions)
        
        # Now we need a vector of floating numbers each of which need substracting of f_x
        
        for i in range(m_dimensions):
            
            dr_di   = r_caret
            dr_di[i] += dx
            
            dJ_di = J(dr_di) - f_x
            
            partial_diff_vector[i] = dJ_di/dx
            
        return partial_diff_vector


    def _pn(self, r_caret: np.array, v=False) -> np.array:
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
        portfolio_total_growth = market_growth.dot(r_caret)
        
        # Next line may come handy as it maintains the growth of each asset class
        if v:
            vector_returns = market_growth * r_caret
            print(vector_returns)
        
        # TODO: the output would be better if it was a dot product it
        #       would require, however to change the derivative function
        #       (see line 144, 147)
        return np.array([portfolio_total_growth])
    
    
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
    


def gradient_descent(df: pd.DataFrame, buy_time: int = 156, iters=20):
    """ Execuuted the gradient descent algorithm """
    
    GD_cluster = J_function(df, purchase_time = buy_time)

    alpha = 1e-2
    r = np.array([0.5, 0.5])
    
    for i in range(iters):
        print('When r:', r)
        dJ_dx = GD_cluster.gradient_function(r)
        print('The partial derivatives', dJ_dx)
        change = alpha*dJ_dx
        print('Direct the vector:', change)
        r = r - change
        print('Resulting in r:', r,'\n')
        
    print('\n\nAfter', iters, 'iterations, we end up with r:', r)
    total = sum(r)
    print('resuting in allocation', r/total)
        
        
        