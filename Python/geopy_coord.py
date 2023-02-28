from functools import partial
from geopy.geocoders import Nominatim

s = input('Input your coordinates: ')
geolocator = Nominatim(user_agent="your_email")
reverse = partial(geolocator.reverse, language="jp")
print('Address of the said coordinates: ', reverse(s))
