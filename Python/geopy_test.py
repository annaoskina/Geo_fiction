from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='annaoskina@gmail.com')
some_place = input("Input your address: ")
location = geolocator.geocode(some_place)
lat = location.latitude
lon = location.longitude
coordinates = []
coordinates.append(lat)
coordinates.append(lon)
print("Lat and Lon of the said address: ", coordinates)
