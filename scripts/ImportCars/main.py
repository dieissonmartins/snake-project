import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# read the online file by the URL provided above, and assign it to variable "df"
path = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

data = pd.read_csv(path, header=None)

# print values
print(data.to_string())

# export csv values
dir_to = dir_path + '/tmp/automobile.csv'
data.to_csv(dir_to)
