library(tidyverse)
library(leaflet)
read_csv("https://raw.githubusercontent.com/annaoskina/Geo_fiction/main/csv/result_tally.csv") -> data

data %>% 
  filter(author == '菊池寛') %>% 
  group_by(place_name, lat, lon) %>%
  summarise(total_freq = sum(frequency),
            all_titles = str_c(title_jp, collapse = "<br>")) -> 
  Kikuchi

pal_bin <- colorBin("Spectral", domain = Kikuchi$total_freq)

Kikuchi %>% 
  leaflet() %>% 
  addTiles() %>% 
  #addProviderTiles('CartoDB.DarkMatterNoLabels') %>% 
  addCircles(lng = ~lon,
             lat = ~as.numeric(lat),
             label = ~place_name, 
             opacity = 1,
             color = ~pal_bin(total_freq),
             radius = ~total_freq*1000,
             popup = Kikuchi$all_titles) %>% 
  addLegend(pal = pal_bin,
            values = ~total_freq,
            title = 'Kikuchi Kan')
