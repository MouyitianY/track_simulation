import folium
# import pandas as pd

# define the world map
world_map = folium.Map()

# display world map
print('ok')
world_map

latitude = 37.77
longitude = -122.42
# Create map and display it
san_map = folium.Map(location=[latitude, longitude], zoom_start=12)
# Display the map of San Francisco
san_map


map2 = folium.Map(location=[43.7, -79.4], tiles='cartodbpositron',zoom_start=11) # set default location on the map
marker_cluster = folium.plugins.MarkerCluster().add_to(map2)
# add the location to the marker cluster

for point in range(len(locationlist)): # loop through the plots

    # include popup
    popup1 = folium.Popup(df['Condo Address'][point], parse_html=True)

    # include icon
    icon1 = folium.Icon(color=df['color'][point])

    # mark every addresses in the map from the data
folium.Marker(locationlist[point],popup=popup1,icon = icon1).add_to(marker_cluster)
