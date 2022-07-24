import pandas as pd

from configparser import Interpolation
from functools import reduce
import matplotlib.pyplot as plt

#Comienza matplot

def renderDataFrames(interpolated_merged_df):
    #trunca las filas a una de cada 100
    interpolated_merged_df = interpolated_merged_df[::100]
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('DATE')
    ax1.xaxis.set_ticks(range(0, len(cases), 5))
    ax1.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax1.set_ylabel('GOLD', color = color)
    ax1.plot(interpolated_merged_df["Date"], interpolated_merged_df["Price_x"], color = color)
    ax1.tick_params(axis='y', labelcolor = color )

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    ax2.set_ylabel('Silver', color = color)  # we already handled the x-label with ax1
    ax2.plot(interpolated_merged_df["Date"], interpolated_merged_df["Price_y"], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:green'
    ax3.set_ylabel('SP500', color = color)
    ax3.plot(interpolated_merged_df["Date"], interpolated_merged_df["SP500"], color=color)
    ax3.tick_params(axis='y', labelcolor=color)

    ax4 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:orange'
    ax4.set_ylabel('Real Estate USA', color = color)
    ax4.plot(interpolated_merged_df["Date"], interpolated_merged_df["Median Home Price (NSA)"], color=color)
    ax4.tick_params(axis='y', labelcolor=color)

    ax5 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:purple'
    ax5.set_ylabel('Oil', color = color)
    ax5.plot(interpolated_merged_df["Date"], interpolated_merged_df["Oil"], color=color)
    ax5.tick_params(axis='y', labelcolor=color)

    ax6 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:cyan'
    ax6.set_ylabel('bonds10Y', color = color)
    ax6.plot(interpolated_merged_df["Date"], interpolated_merged_df["bonds10Y"], color=color)
    ax6.tick_params(axis='y', labelcolor=color)

    #empieza el renderizado
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()