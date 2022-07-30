import pandas as pd

from configparser import Interpolation
from functools import reduce
import matplotlib.pyplot as plt

#Comienza matplot

def renderDataFrames(interpolated_merged_df):
    i = 0.075

    #trunca las filas a una de cada 365
    interpolated_merged_df = interpolated_merged_df[::365]
    fig, ax1 = plt.subplots()
    #indice = interpolated_merged_df.index
    indice = interpolated_merged_df["Date"]


    color = 'tab:red'
    ax1.set_xlabel('DATE')
    #ax1.xaxis.set_ticks(interpolated_merged_df["Date"])
    ax1.set_xticklabels(interpolated_merged_df["Date"], rotation=45, ha="right")
    ax1.set_ylabel('GOLD', color = color)
    ax1.plot(indice, interpolated_merged_df["Gold"], color = color)
    ax1.tick_params(axis='y', labelcolor = color )

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    ax2.set_ylabel('Silver', color = color)  # we already handled the x-label with ax1
    ax2.plot(indice, interpolated_merged_df["Silver"], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:green'
    ax3.set_ylabel('SP500', color = color)
    ax3.plot(indice, interpolated_merged_df["SP500"], color=color)
    ax3.tick_params(axis='y', labelcolor=color)

    ax4 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:orange'
    ax4.set_ylabel('Real Estate USA', color = color)
    ax4.plot(indice, interpolated_merged_df["Median Home Price (NSA)"], color=color)
    ax4.tick_params(axis='y', labelcolor=color)

    ax5 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:purple'
    ax5.set_ylabel('Oil', color = color)
    ax5.plot(indice, interpolated_merged_df["Oil"], color=color)
    ax5.tick_params(axis='y', labelcolor=color)

    ax6 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:cyan'
    ax6.set_ylabel('bonds10Y', color = color)
    ax6.plot(indice, interpolated_merged_df["bonds10Y"], color=color)
    ax6.tick_params(axis='y', labelcolor=color)

    ax7 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:brown'
    ax7.set_ylabel('Growth', color = color)
    ax7.plot(indice, interpolated_merged_df["Growth percentile"], color=color)
    ax7.tick_params(axis='y', labelcolor=color)

    ax8 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:pink'
    ax8.set_ylabel('Inflation', color = color)
    ax8.plot(indice, interpolated_merged_df["Inflation percentile"], color=color)
    ax8.tick_params(axis='y', labelcolor=color)
    
    p = 1 + i                                   #este es diferente para poner axis encima del valor 1.15
    #ax2.spines.right.set_position(("axes", p))
    ax3.spines.right.set_position(("axes", p))
    p = p + i

    ax4.spines.right.set_position(("axes", p))
    p = p + i
    ax5.spines.right.set_position(("axes", p))
    p = p + i

    ax6.spines.right.set_position(("axes", p))
    p = p + i
    ax7.spines.right.set_position(("axes", p))
    p = p + i

    ax8.spines.right.set_position(("axes", p))
    p = p + i



    #empieza el renderizado
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.subplots_adjust(left=0.04, right=0.674, bottom=0.1)
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    
    plt.show()