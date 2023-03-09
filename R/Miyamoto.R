library(tidyverse)
library(leaflet)
read_csv("https://raw.githubusercontent.com/annaoskina/Geo_fiction/main/csv/result_tally.csv") -> data

data %>% 
  filter(author == '菊池寛') %>% 
  group_by(place_name, lat, lon) %>%
  summarise(total_freq = sum(frequency),
            all_titles = str_c(title_jp, collapse = "<br>")) -> 
  Miyamoto

pal_bin <- colorBin("Spectral", domain = Miyamoto$total_freq)

Miyamoto %>% 
  leaflet() %>% 
  addTiles() %>% 
  #addProviderTiles('CartoDB.DarkMatterNoLabels') %>% 
  addCircles(lng = ~lon,
             lat = ~as.numeric(lat),
             label = ~place_name, 
             opacity = 1,
             color = ~pal_bin(total_freq),
             radius = ~total_freq*1000,
             popup = Miyamoto$all_titles) %>% 
  addLegend(pal = pal_bin,
            values = ~total_freq,
            title = 'Miyamoto Yuriko')
