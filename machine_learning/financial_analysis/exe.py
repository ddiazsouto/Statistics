from renderer import renderDataFrames
from load_dataset import get_assets_dataframe
from algos import gradient_descent


#pd.set_option('display.max_rows', None)

#print(get_assets_dataframe())
get_assets_dataframe().to_csv('inter-merg-DF.csv')

#gradient_descent(get_assets_dataframe())