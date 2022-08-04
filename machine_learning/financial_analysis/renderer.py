import pandas as pd

from configparser import Interpolation
from functools import reduce
import matplotlib.pyplot as plt

#Comienza matplot
colors = ['tab:blue',
            'tab:orange',
            'tab:green',
            'tab:red',
            'tab:purple',
            'tab:brown',
            'tab:pink',
            'tab:gray',
            'tab:olive',
            'tab:cyan']

#Crea subplots con y-Axes independientes
axS =[]
def newTwix(label, ax1, indice, interpolated_merged_df):
    print(label)
    actualPos = len(axS)
    axS.append(ax1.twinx())
    axS[actualPos].set_ylabel(label, color = colors[actualPos%10])
    axS[actualPos].plot(indice, interpolated_merged_df[label], color=colors[actualPos%10])
    axS[actualPos].tick_params(axis='y', labelcolor=colors[actualPos%10])

def renderDataFrames(interpolated_merged_df):
    
    xLabel = str( interpolated_merged_df.columns[0] )

    #trunca las filas para mostrar solo 50 Y-Ticks
    truncador = int( interpolated_merged_df[xLabel].size / 50)
    interpolated_merged_df = interpolated_merged_df[::truncador]

    #Prepara los plots y los sub-Y-Axes
    fig, ax1 = plt.subplots()
    indice = interpolated_merged_df[xLabel]
    ax1.set_xlabel( xLabel)
    ax1.set_xticklabels(interpolated_merged_df[xLabel], rotation=45, ha="right")
    
    primerLabel = str( interpolated_merged_df.columns[1] )
    ax1.set_ylabel(primerLabel, color = colors[0])
    ax1.plot(indice, interpolated_merged_df[primerLabel], color = colors[0])
    ax1.tick_params(axis='y', labelcolor = colors[0])
    
    identacion = 0.046
    p = 1
    for i in range(2,len(interpolated_merged_df.columns)):
        newTwix(str(interpolated_merged_df.columns[i]), ax1, indice, interpolated_merged_df)
        if (len(axS) == 1):
            axS[len(axS)-1].spines.right.set_position(("axes", p))
        else:
            p = int((p + identacion)*1000)/1000
            axS[len(axS)-1].spines.right.set_position(("axes", p))

    #empieza el renderizado
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.subplots_adjust(left=0.04, right=0.674, bottom=0.1)
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    
    plt.show()