import pandas as pd
import numpy as np

#  construct a Series object
pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })

california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe.describe()

california_housing_dataframe.head()

california_housing_dataframe.hist('housing_median_age')

# accessing data
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print (type(cities['City name']))
print(cities['City name'])

print (type(cities['City name'][1]))
print(cities['City name'][1])

print (type(cities[0:2]))
print(cities[0:2])

print(population/1000)

np.log(population)

# create a series that indicates whether population is over one million
population.apply(lambda val: val > 1000000)

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
# print(cities)

print("adding a boolean column that is True if the city is named\
		\nafter a saint and greater than 50 square miles")

cities["Big and named after a saint"] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print(cities)

print("re-ordering the cities")

print(city_names.index)
print(cities.index)
cities.reindex([2,0,1])
print(cities)

# print(cities.reindex([0, 4, 5, 2]))