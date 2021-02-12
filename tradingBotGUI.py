# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime as dt
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()


generateGraph = tk.Button(root, text="Get Graph", padx=10, pady=10, fg="black")
generateGraph.pack()

root.mainloop()

def handleYear(num, numOfMonthsBack):
    if num - numOfMonthsBack < 1:
        return 1
    else:
        return 0

def handleMonth(num, numOfMonthsBack):
    if num - numOfMonthsBack < 1:
        return (num-numOfMonthsBack) + 12
    else:
        return num-numOfMonthsBack

def makeGraph(name, monthsBack):
    now = dt.datetime.now()
    style.use("ggplot")
    currYear = int(now.strftime("%Y"))
    currMonth = int(now.strftime("%m"))
    startYear = currYear - handleYear(currMonth, monthsBack)
    startMonth = handleMonth(currMonth, monthsBack)
    start = dt.datetime(startYear, startMonth, 1)
    end = dt.datetime.now()
    try:
        df = web.get_data_yahoo(name, start, end)
        df["Adj Close"].plot()
        plt.show()      
    except:
        print("Stock name not listed on NYSE")
    
    

