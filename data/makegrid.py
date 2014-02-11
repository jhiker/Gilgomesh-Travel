import json, math
from ast import literal_eval as pythonize

#Takes in data of all cities in json (dict):
#"City, STATE ABBRV": [population rank, latitude, longitude]
#Returns JSON of grid (rounded lat, rounded long ): nearby cities adjusted to population size like gravitational force
#Also returns JSON of formula for cities: dict same as above with number for radius of city


def decode_to_dict(file_):
	return pythonize(open(file_, 'r').read())


def convert_pop_to_radius(cities, citydict={}):
	for key, city in cities.items():
		cityrank=int(float(city[0]))
		newval=int(6/cityrank)
		newval+=int(2*cityrank<50)+int(cityrank<100)+int(cityrank<150)
		geocodes=[int(round(float(city[1]))) ,int(round(float(city[2])))]
		citydict[key]=[newval]+geocodes
	return citydict





def distance(point1, point2):
	(x,y), (x2,y2)=point1, point2
	return math.sqrt(math.pow((x-x2), 2) +math.pow((y-y2),2))

def build_city_grid(cities):
	'''transforms json to indexed form'''
	city_grid={}
	for city in cities:
		key =tuple(cities[city][1:])
		value =city, cities[city][0]
		if key in city_grid:
			city_grid[key].append(value)
		else:
			city_grid[key]= [value,]

	print city_grid #new dict
	raw_input()
	grid ={}
	count=0
	'''loop through all relevant space to and insert cities 
	   according to function of distance and pop'''
	for lat_ in range(15, 60):
		for long_ in range(-125, -67):
			basepoint=str((lat_, long_))
			grid[basepoint]= []
			for i in range(-10, 10):
				for j in range(-10, 10):
					if i+j>16: continue
					point= lat_+i , long_+j
					if point in city_grid:
						for city in city_grid[point]:
							if distance([0,0],[i,j])<=city[1]:
								grid[basepoint].append(city[0])
			if not grid[basepoint]:
				count+=1
				del grid[basepoint]
	return grid

jsonfile = open('cities2.json', 'w')
cities= convert_pop_to_radius(cities)
cities = decode_to_dict(cities_with_pop.json)
json.dump(cities, jsonfile)

cities= pythonize(open('cities.json', 'r').read())
grid = build_city_grid(cities)
jsonfile = open('citygrid.json', 'w')
json.dump(grid, jsonfile)
