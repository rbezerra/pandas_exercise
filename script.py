import numpy as np
import pandas as pd


def create_data_frame_from_csv(path, sep, encoding, columnNames):
    return pd.read_csv(path, sep, encoding, names=columnNames)


def has_missing_values(df: pd.core.frame.DataFrame):
    return df.isnull().values.any()


def filter_data_frame(df, filterName, filterValue):
    return df[df[filterName] == filterValue]


columnNames = ["", "title", "artist", "top genre", "year", "bpm", "nrgy", "dnce", "dB", "live", "val", "dur", "acous",
               "spch", "pop"];
data = create_data_frame_from_csv("./top10s.csv", ',', 'ISO-8859-1', columnNames)

print(type(data))
print(data.head())
print(data.info())

#filteredValues = filter_data_frame(data, 'year', 2015);
#print(filteredValues)

print(has_missing_values(data))
