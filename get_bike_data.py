#bike data extraction

import os
import os.path
import time
import csv
from datetime import datetime
import pandas as pd
import numpy as np
import glob
os.chdir("C:/Users/Aaron/Desktop/HW20_tableau/Citibike_Data")
new = os.getcwd().replace("\\","/")
df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "*.csv"))))

missing_df = df[(df['start station latitude']==0) |
                (df['start station longitude']==0) |
                (df['end station latitude']==0) |
                (df['end station longitude']==0)]

df = df.drop(missing_df.index)
df.to_csv("threemonth_summer.csv", index=False)