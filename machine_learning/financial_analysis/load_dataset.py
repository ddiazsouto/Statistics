import pymysql
import pandas as pd

from configparser import Interpolation
from functools import reduce

"""  THIS FILE IS DATABASE SPECIFIC (MySQL) """

if (response:= input("refresh from database?\nYes/No\n>> ") == 'Yes'):
    
    # Connecting to database
    password = input("Introduce database password\n>> ")
    Make=pymysql.connect(host='127.0.0.1', user='root', passwd=password, db='mysql')
    MySQL=Make.cursor()
    MySQL.execute('USE portfolio')
    
    # Querying gold
    MySQL.execute('SELECT date, PriceUSD FROM gold WHERE priceUSD')
    gold=MySQL.fetchall()
    # Into a dataframe
    gold_df = pd.DataFrame(gold, columns= ['Date', 'Price'])
    gold_df.to_csv("DATA/gold_dataset.csv", index=False, header=True)
    
    # Querying silver
    MySQL.execute('SELECT date, PriceUSD FROM silver WHERE priceUSD')
    silver=MySQL.fetchall()
    # Into a dataframe
    silver_df = pd.DataFrame(silver, columns= ['Date', 'Price'])
    silver_df.to_csv("DATA/silver_dataset.csv", index=False, header=True)


def get_assets_dataframe() -> pd.DataFraFrame:
    """  THIS PREPARES THE DATAFRAME WITH THE PARAMETERS WE NEED  """

    #import CSVs
    gold_df             = pd.read_csv("DATA/gold_dataset.csv")
    silver_df           = pd.read_csv("DATA/silver_dataset.csv")
    sandp_df            = pd.read_csv("DATA/s&p500_dataset.csv")
    usaRealEstate_df    = pd.read_csv("DATA/historical-median-home-value_dateset.csv")
    oil_df              = pd.read_csv("DATA/oil_dataset.csv")
    bonds10_df          = pd.read_csv("DATA/bonds-10Y_dataset.csv")

    #Creates array with all the DataFrames
    allDFs              = [gold_df,
                          silver_df,
                          sandp_df[['SP500', 'Date']],
                          usaRealEstate_df[['Median Home Price (NSA)', 'Date']],
                          oil_df[['Oil', 'Date']],
                          bonds10_df]

    all_merged_df = reduce(lambda  left,right: pd.merge(left,right,on=['Date'], how='outer'), allDFs)
    interpolated_merged_df = all_merged_df.interpolate(method ='linear', limit_direction ='forward')
    
    return interpolated_merged_df