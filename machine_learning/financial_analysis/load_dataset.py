import pymysql
import pandas as pd

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


gold_df     = pd.read_csv("DATA/gold_dataset.csv")
silver_df   = pd.read_csv("DATA/silver_dataset.csv")
snp_dataset = pd.read_csv("DATA/s&p500_dataset.csv")