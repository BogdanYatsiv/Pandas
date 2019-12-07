import numpy as np
import pandas as pd

data_meters = pd.read_csv("DataMeters.csv", delimiter = ";")
prices = pd.read_csv("Prices.csv", delimiter = ";")

print(prices)

pr_indexes = list(prices.index)
pr_columns = list(prices.columns)[1:]

print(prices[pr_columns[0]][pr_indexes[0]])

for column in pr_columns:
    for i in pr_indexes:
        if pd.isna(prices[column][i]):
            prices[column][i] = prices[column][i-1]

print(prices)

print(data_meters.sort_values(by = "e_meter"))

prices = prices.merge(data_meters.sample(12))
print(prices.groupby(pd.Grouper(key = "date", freq="D")).sum())