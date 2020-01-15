import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
import pandas as pd
import xlsxwriter
import os
print("Welcome to the binomial model checker!")
print()
print("Here we produce a graph representing the likelihood that given binomial")
print("probabilities would produce the sampled results.")


successes=input("For your data set, how many successes have you had?")
failures=input("For your data set, how many failures have you had?")

i=0
percentage = 0
array = np.full([1000,],0.0000000000000)
pdf_array = np.full([1000,],0.0000000000000)

while i < 1000:
    array[i] =binom.pmf(int(successes),int(failures)+int(successes),percentage,loc=0)#### Here is where we enter the results, 25 being succeses, 35 being total trials
    i+=1
    percentage+=0.001
sum = np.sum(array)
i=0
while i < len(array):
    array[i] = array[i]/sum
    i+=1

numArray = np.full([1000,],0.0000000000000)
i=0
while i <1000:
    numArray[i]=i/1000
    i+=1

workbook = xlsxwriter.Workbook('BinomialDistribution.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write_column('A1', numArray)
worksheet.write_column('B1', array)

chart = workbook.add_chart({'type': 'line'})
chart.add_series({'values': '=Sheet1!$B$1:$B$1000',
                 'categories': '=Sheet1!$A$1:$A$1000'})
chart.set_x_axis({
    'name': 'Tested Odds',
    'name_font': {'size': 14, 'bold': True},
    'num_font':  {'italic': True },
})
chart.set_y_axis({
    'name': 'Odds that tested Odds produced results',
    'name_font': {'size': 14, 'bold': True},
    'num_font':  {'italic': True },
})
chart.set_size({'width': 800, 'height': 560})
chart.set_legend({'none': True})

chart.set_title({
    'name': 'PDF of Binomial Correlations',
    'overlay': True,
    'layout': {
        'x': 0.35,
        'y': 0.03
    }
})
worksheet.insert_chart('E2', chart, {'x_offset': 25, 'y_offset': 10})


workbook.close()
os.system("start BinomialDistribution.xlsx")
