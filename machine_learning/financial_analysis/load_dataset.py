#import pymysql
import pandas as pd
import numpy as np

from configparser import Interpolation
from functools import reduce

#if (response:= input("refresh from database?\nYes/No\n>> ") == 'Yes'):
#    """  THIS FILE IS DATABASE SPECIFIC (MySQL) """
    
#    # Connecting to database
#    password = input("Introduce database password\n>> ")
#    Make=pymysql.connect(host='127.0.0.1', user='root', passwd=password, db='mysql')
#    MySQL=Make.cursor()
#    MySQL.execute('USE portfolio')
    
#    # Querying gold
#    MySQL.execute('SELECT date, PriceUSD FROM gold WHERE priceUSD')
#    gold=MySQL.fetchall()
#    # Into a dataframe
#    gold_df = pd.DataFrame(gold, columns= ['Date', 'Price'])
#    gold_df.to_csv("DATA/gold_dataset.csv", index=False, header=True)
    
#    # Querying silver
#    MySQL.execute('SELECT date, PriceUSD FROM silver WHERE priceUSD')
#    silver=MySQL.fetchall()
#    # Into a dataframe
#    silver_df = pd.DataFrame(silver, columns= ['Date', 'Price'])
#    #silver_df.to_csv("DATA/silver_dataset.csv", index=False, header=True)

def get_assets_dataframe() -> pd.DataFrame:
    """  THIS PREPARES THE DATAFRAME WITH THE PARAMETERS WE NEED  """

    #import assets CSVs
    gold_df             = pd.read_csv("financial_analysis/DATA/gold_dataset.csv")
    silver_df           = pd.read_csv("financial_analysis/DATA/silver_dataset.csv")
    sandp_df            = pd.read_csv("financial_analysis/DATA/s&p500_dataset.csv")
    usaRealEstate_df    = pd.read_csv("financial_analysis/DATA/historical-median-home-value_dateset.csv")
    oil_df              = pd.read_csv("financial_analysis/DATA/oil_dataset.csv")
    bonds10_df          = pd.read_csv("financial_analysis/DATA/bonds-10Y_dataset.csv")
    
    #Creates array with all the assets DataFrames
    allDFs              = [gold_df,
                          silver_df,
                          sandp_df[['SP500', 'Date']],
                          usaRealEstate_df[['Median Home Price (NSA)', 'Date']],
                          oil_df[['Oil', 'Date']],
                          bonds10_df]
    
    #1) Creates a DataFrame, 2)Sorted by Date, 3)Eliminates NaN by linear interpolation
    all_merged_df = reduce(lambda  left,right: pd.merge(left,right,on=['Date'], how='outer'), allDFs)
    all_merged_df.sort_values(by="Date", inplace=True)

    interpolated_merged_df = all_merged_df.interpolate(method='linear', limit_direction ='forward')
    
    return interpolated_merged_df

def get_Indicators_DataFrame() -> pd.DataFrame:

    #import Indicartors CSV
    #5 more indicators pending to add
    inflation_df                = pd.read_csv("financial_analysis/DATA/inflation-percentils_dataset.csv")
    growth_df                   = pd.read_csv("financial_analysis/DATA/growth-percentils_dataset.csv")
    national_income_df          = pd.read_csv("financial_analysis/DATA/adjusted-net-national-income.csv")
    money_growth_df             = pd.read_csv("financial_analysis/DATA/broad-money-growth.csv")
    us_debt_df                  = pd.read_csv("financial_analysis/DATA/united-states-gdp_debt.csv")

    us_debt_df[['US Debt as GDP percentage']] = us_debt_df[['US Debt as GDP percentage']].pct_change()
    us_debt_df.rename(columns={'US Debt as GDP percentage': 'US Debt as GDP percentage annual percentual change'}, inplace=True)
    

    #Creates array with all the indicators DataFrames
    indicatorsDFs              = [inflation_df,
                                  growth_df,
                                  national_income_df,
                                  money_growth_df,
                                  us_debt_df[['Date','US Debt as GDP percentage annual percentual change','US GDP annual Growth']]]#,
                                  #usa_Debt_as_GDP_percentage_annual_Variance]

    #1) Creates a DataFrame, 2)Sorted by Date, 3)Eliminates NaN by linear interpolation
    indicators_merged_df = reduce(lambda  left,right: pd.merge(left,right,on=['Date'], how='outer'), indicatorsDFs)
    indicators_merged_df.sort_values(by="Date", inplace=True)

    interpolated_indicators_merged_df = indicators_merged_df.interpolate(method='linear', limit_direction ='forward')

    return interpolated_indicators_merged_df