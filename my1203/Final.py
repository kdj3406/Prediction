from prediction_util import PredictionUtil
from classfication_util import ClassficationUtil
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
gildong = PredictionUtil()
cheulsu = ClassficationUtil()

gildong.read('avocado.csv')
# cheulsu.read('avocado.csv')
#
# gildong.show_unique_column()
# cheulsu.myhist()
#
# gildong.pairplots(['4046','4225','4770', 'AveragePrice'])
#
# gildong.heatmap(['AveragePrice', 'Total Volume', '4046', '4225', '4770'])
#
# gildong.plot_3d('4046','4225','4770')

# gildong.drop('region')
# print(gildong.df.head())

gildong.run_all(['4046','4225','4770'], 'AveragePrice')

