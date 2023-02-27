from geopy.geocoders import Nominatim
import csv

def extract_tsv(name_tsv):
	with open(name_tsv, encoding = 'utf-8') as r_file:
		data = csv.reader(r_file, delimiter = '\t')
		data_list = list(data)
	return data_list

def find_coordinates(some_place):
	geolocator = Nominatim(user_agent='annaoskina@gmail.com')
	location = geolocator.geocode(some_place)
	lat = location.latitude
	lon = location.longitude
	coordinates = []
	coordinates.append(lat)
	coordinates.append(lon)
	#print(coordinates)
	return coordinates

def write_csv(data_list, filename):
	with open('{}.tsv'.format(filename), 'w', encoding = 'utf-8') as file:
	    for row in data_list:
	    	file.write(row)
	return 0

name_tsv = 'clean_result.tsv'
data_new_list = extract_tsv(name_tsv)
for line in data_new_list:
	if line[5]:
		place_name = line[5]
		try:
			line.extend(find_coordinates(place_name))
		except:
			print(place_name)
write_csv(data_new_list, coordinates)
print('Done')





#		lon_lat = find_coordinates(row[5])
#		row = row + '\t' + coordinates
#	print(type(row))
#write_csv(data_new_list, data_with_coordinates)