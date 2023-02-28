from geopy.geocoders import Nominatim

def find_coordinates(some_place):
	geolocator = Nominatim(user_agent='annaoskina@gmail.com')
	location = geolocator.geocode(some_place)
	lat = location.latitude
	lon = location.longitude
	coordinates = []
	coordinates.append(str(lat))
	coordinates.append(str(lon))
	#print(coordinates)
	return coordinates

with open('list_places_tally.txt', 'r', encoding = 'utf-8') as r_file:
	lines = r_file.readlines()
	places_with_coordinates = []
	x = 1
	for line in lines:
		line_as_list = line.split(',')
		try:
			coordinates = find_coordinates(line_as_list[0])
			line = line.strip('\n') + ',' + coordinates[0] + ',' + coordinates[1] + '\n'
			places_with_coordinates.append(line)
			print(x)
			x += 1
		except:
			print(line_as_list[0])

def write_csv(data_list, filename):
	with open('{}.csv'.format(filename), 'w', encoding = 'utf-8') as file:
	    for row in data_list:
	    	file.write(row)
	return 0

filename = 'places_with_coordinates.txt'
write_csv(places_with_coordinates, filename)