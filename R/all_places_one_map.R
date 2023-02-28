library(tidyverse)
library(leaflet)
read_csv("https://raw.githubusercontent.com/annaoskina/Geo_fiction/main/places_with_coordinates.csv") -> data

pal_bin <- colorBin("Spectral", domain = data$frequency)	#this is a function for coloring categories

data %>% 
  leaflet() %>%	#calling leaflet 
  addTiles() %>% 	#for more Tiles see: http://leaflet-extras.github.io/leaflet-providers/preview/index.html
  #addProviderTiles('Stamen.TonerLite') %>%	#example of adding another Tile
  addCircles(lng = ~lon,
             lat = ~as.numeric(lat),	#here is a point. This column was a character while I needed numeric values. That’s how I fixed it.
             label = ~frequency,		#you can see frequency, if you touch a circle with a cursor
             popup = data$place,		#you can see place-names, if you click a circle with a cursor
             opacity = 1,
             radius = ~frequency*100,	#then more frequency, then bigger a circle
             color = ~pal_bin(frequency)
  ) %>% 
  addLegend(pal = pal_bin,
            values = ~frequency,
            title = 'All places on one map')
