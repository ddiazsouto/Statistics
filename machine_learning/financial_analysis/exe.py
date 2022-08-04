import renderer as rend
import load_dataset as ld
from algos import gradient_descent


#pd.set_option('display.max_rows', None)

#print(ld.get_assets_dataframe())
#print(ld.get_Indicators_DataFrame())

#rend.renderDataFrames(ld.get_assets_dataframe())
rend.renderDataFrames(ld.get_Indicators_DataFrame())

#get_assets_dataframe().to_csv('inter-merg-DF.csv')

#gradient_descent(get_assets_dataframe())