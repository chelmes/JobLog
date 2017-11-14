#!/usr/bin/python

# Small script to demonstrate the features of JobLog
# Best used with python -i test.py

from pylab import *
import matplotlib.pyplot as plt
import numpy
import pandas as pd
import logger.item.item as litem

# We want to have distinctive column names for the final dataframe
columns=['Start','End','net_time','Name']

# At the beginning this dataframe is empty and gets filled afterwards
JobLog=pd.DataFrame(columns=columns)

#dummy items for the demo
first=litem.Item("maintenance",60)
second=litem.Item("design",30)
third=litem.Item("testing",50)

# they need to be entered into the dataframe, will be placed in an own function
# later on
JobLog.ix[first.get('id')]=first.dataframe_entry()
JobLog.ix[second.get('id')]=second.dataframe_entry()
JobLog.ix[third.get('id')]=third.dataframe_entry()

# Visualize the working day in a pie chart
JobLog.plot.pie(y='net_time',labels=JobLog.loc[:,'Name'])
plt.show()
print(JobLog)
        
