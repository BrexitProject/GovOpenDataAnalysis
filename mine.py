import os
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from minepy import MINE

def compute(x, y, indicator):
	mine = MINE(alpha=0.6, c=15, est="mic_approx")
	mine.compute_score(x, y)
	# r = np.around(np.corrcoef(x, y)[0, 1], 1)
	print(indicator + ': ' + str(mine.mic()))
	# print("person: " + r)

# get current work dir
dirname = os.getcwd()
filename = 'EU-referendum-result-data.csv'

# read poll data
df0 = pd.read_csv(os.path.join(dirname, filename), index_col = None)

# read all csv file in source directory
files = os.listdir(os.path.join(dirname, 'source'))
csvfiles = list(filter(lambda x: x[-4:]=='.csv' , files))


# outer join data on area code column
for csvfile in csvfiles:
	# df = pd.DataFrame.from_csv(csvfile)
	df = pd.read_csv(os.path.join(dirname,'source',csvfile), index_col = None)

	# get indicator (NOTE: the column name and file name is should be the same)
	indicator = os.path.splitext(csvfile)[0]

	# inner join two dataframe on the Area Code column
	tmp = df0.merge(df, how = 'inner', on = 'Area_Code')

	# compute the mic and person value 
	compute(tmp['Pct_Leave'], tmp[indicator], indicator)

# plt.figure(facecolor = 'white')
# generate()
# plt.tight_layout()
# plt.show()