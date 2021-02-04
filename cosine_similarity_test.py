from surprise import KNNWithMeans
from scipy import spatial
import pandas as pd
import math

# Unit converter for area
units = {"sqft": 1, "m2": 10.7639}

def parse_size(size):
    if (isinstance(size, float)):
        return size
    print(size.split(' '))
    result = [string.strip() for string in size.split(' ')]
    return int(float(result[0]) if len(result) == 1 else float(result[0])*units[result[1]])

# Bathroom + Bedroom fomatter
def parse_bedrooms(size):
    if isinstance(size, float):
        size = "0"

    return sum([int(string.strip()) for string in size.split(' + ')])

# Get data
listings = pd.read_csv('data.csv', usecols = ['Bathrooms', 'Bedrooms', 'InteriorSize', 'Longitude', 'Latitude'])
listings.dropna(how='all')

listings['Bedrooms'] = [(parse_bedrooms(x)) for x in listings['Bedrooms']]
listings['InteriorSize'] = [(parse_size(x) / 1648) * 10 for x in listings['InteriorSize']]
listings['InteriorSize'] = pd.to_numeric(listings['InteriorSize'])
listings['Longitude'] = [(x + 80) * 10 for x in listings['Longitude']]
listings['Latitude'] = [(x - 43) * 10 for x in listings['Latitude']]

print(listings)

arr = listings.values

cosine_similarity = []
for vec in arr:
    cosine_similarity.append(spatial.distance.cosine(arr[1], vec))

listings['cosine'] = cosine_similarity
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(listings)


