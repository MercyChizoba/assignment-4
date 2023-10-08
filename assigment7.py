
cities = ('Abuja', 'Ottawa', 'Paris', 'New Delhi', 'Copenhagen')
countries = ('Nigeria', 'Canada', 'France', 'India', 'Denmark')
random_index = {'Nigeria': 100001, 'Canada': 765344, 'France': 52727, 'New Delhi': 15216, 'Denmark': 1182}

for city in countries:
    print (city)

#create an empty list
dict_list = []
# I assigned values using indexing
for city in cities, countries, random_index:
    dict_A = {"city": cities[0], "country": countries [0], "portal": random_index["Nigeria"]}
    dict_B = {"city": cities[1], "country": countries [1], "portal": random_index["Canada"]}
    dict_C = {"city": cities[2], "country": countries [2], "portal": random_index["France"]}
    dict_D = {"city": cities[3], "country": countries [3], "portal": random_index["New Delhi"]}
    dict_E = {"city": cities[4], "country": countries [4], "portal": random_index["Denmark"]}
#create a list
dict_list.append(dict_A)
dict_list.append(dict_B)
dict_list.append(dict_C)
dict_list.append(dict_D)
dict_list.append(dict_E)

print(dict_list)


