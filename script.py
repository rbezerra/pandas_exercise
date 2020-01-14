import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def create_data_frame_from_csv(path):
    return pd.read_csv(path, encoding='ISO-8859-1', engine='python')


def has_missing_values(df: pd.core.frame.DataFrame):
    return df.isnull().values.any()


def filter_data_frame(df, filter_name, filter_value):
    return df[df[filter_name] == filter_value]


def remove_column(df, column):
    return df.drop([column], axis=1)


def drop_duplicates(df):
    return df.drop_duplicates()


def reduce_genres(df):
    for i in df['top genre']:
        if 'pop' in i:
            df['top genre'] = df['top genre'].replace(i, 'pop')
        elif 'hip hop' in i:
            df['top genre'] = df['top genre'].replace(i, 'hip hop')
        elif 'edm' in i:
            df['top genre'] = df['top genre'].replace(i, 'edm')
        elif 'r&b' in i:
            df['top genre'] = df['top genre'].replace(i, 'pop')
        elif 'latin' in i:
            df['top genre'] = df['top genre'].replace(i, 'latin')
        elif 'room' in i:
            df['top genre'] = df['top genre'].replace(i, 'room')
        elif 'electro' in i:
            df['top genre'] = df['top genre'].replace(i, 'edm')
        elif 'chicago rap' in i:
            df['top genre'] = df['top genre'].replace(i, 'hip hop')

    return df


def get_unique_values(df, key):
    return df[key].unique()


def show_histogram(df, key):
    plt.hist(df[key])
    plt.show()


def get_top(df, key, n):
    return df.nlargest(n, key)


def get_frequency_unique_values(df, key):
    return pd.value_counts(df[key].ravel())


data = create_data_frame_from_csv("./top10s.csv")

print(type(data))
print(data.head())
print(data.info())

filteredValues = filter_data_frame(data, 'top genre', 'pop')
print(filteredValues)

print(has_missing_values(data))

data = remove_column(data, "ID")
print(data)

data = drop_duplicates(data)
print(data)

print(data['top genre'].value_counts())
data = reduce_genres(data)
print(data['top genre'].value_counts())

artists = get_unique_values(data, 'artist')
print(artists)


print(get_top(data, 'pop', 10))

print(get_frequency_unique_values(data, 'bpm'))

plt.hist(data.live)
print(data[data['bpm'] == 206].title)
plt.show()
