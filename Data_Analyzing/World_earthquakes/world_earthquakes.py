import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Load data into list
filename = 'data/world_eq_data.json'
with open(filename) as file:
	all_eq_data = json.load(file)

all_eq_dicts = all_eq_data['features']

magni, longi, lati, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
	magni.append(eq_dict['properties']['mag'])
	longi.append(eq_dict['geometry']['coordinates'][0])
	lati.append(eq_dict['geometry']['coordinates'][1])
	hover_text.append(eq_dict['properties']['title'])

# Maping earthquakes
data = [{
	'type': 'scattergeo',
	'lon': longi,
	'lat': lati,
	'text': hover_text,
	'marker': {
		'size': [5*mag for mag in magni],
		'color': magni,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'},
	},
}]

my_layout = Layout(title="Global Earthquakes")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')