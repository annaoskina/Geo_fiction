from geopy.geocoders import Nominatim
import csv

def extract_csv(name_csv):
	with open(name_csv, encoding = 'utf-8') as r_file:
		data = csv.reader(r_file, delimiter = ',')
		data_list = list(data)
	return data_list

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

def write_csv(data_list, filename):
	with open('{}.csv'.format(filename), 'w', encoding = 'utf-8') as file:
	    for row in data_list:
	    	row.append('\n')
	    	for srting in row:
	    		file.write(string)
	return 0

name_csv = 'result_tally.csv'
data_new_list = extract_csv(name_csv)
for line in data_new_list:
	if line[3]:
		place_name = line[3]
		try:
			line.extend(find_coordinates(place_name))
		except:
			print('Nominatim Error: ', place_name)

filename = 'places_with_coordinates'
write_csv(data_new_list, filename)
print('Done')