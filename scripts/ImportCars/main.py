
import pandas as pd

# read the online file by the URL provided above, and assign it to variable "df"
path = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

data = pd.read_csv(path, header = None)

print(data.to_string())
