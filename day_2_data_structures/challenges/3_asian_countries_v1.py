##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# In this program we will learn about
# 1. Iterate over a Dictionary Data Structure
# 2. Delete dictionary entries
# 3. Get the dictionary keys

# List all the Asian countries with population > 100 M 
import csv

file_1 = open( "./data/asia_countries.csv" )
asia_countries_f = csv.reader ( file_1 )
asia_countries = []

for row in asia_countries_f : 
    asia_countries.append ( row [0])

file_2 = open( "./data/countries_population.csv" )
countries_population_f = csv.reader ( file_2 )
countries_population = {}

for row in countries_population_f : 
    countries_population [ row[0] ] = row[1]

# Remove all countries in countries_population < 20 Million
countries_population.pop('country')
for key in list(countries_population.keys()) :
    if int(countries_population[key]) < 100000000 : 
        del countries_population[key]

asia_countries_pop_100m = []

for key in list(countries_population.keys())  :
    if asia_countries.count(key) == 0:
        del countries_population[key]


    