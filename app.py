import folium
import json
import dash
from dash import html

with open(r'lokacije\linija1_postaje.geojson') as f:
    gj = json.load(f)
features = gj['features']

t1 = [features[0]['geometry']['coordinates'][1], features[0]['geometry']['coordinates'][0]]
t1_icon = folium.features.CustomIcon('https://avatars.githubusercontent.com/u/86894643?v=4', icon_size=(30, 30))
t1_popup = folium.Popup('<H4>ŽELJEZNIČKI KOLODVOR</H4><p>Početak linije</p><img src="https://raw.githubusercontent.com/dkundih/dkundih/main/.logistics/BLUERED_GHiLI.jpg" alt = "Početak" style="width:300px;height:80px;"/>')
t2 = [features[1]['geometry']['coordinates'][1], features[1]['geometry']['coordinates'][0]]
t3 = [features[2]['geometry']['coordinates'][1], features[2]['geometry']['coordinates'][0]]

m = folium.Map(location = [46.1639, 16.83], zoom_start = 14.8)

style = {
    'color' : 'red',
    'weight' : 5,
    'fillColor' : 'red',
    'fillOpacity' : 0.1,
}

folium.GeoJson(r'lokacije\linija1.geojson', style_function = lambda x: style, name = 'linija1').add_to(m)
folium.Marker(location = t1, icon = t1_icon, popup = t1_popup).add_to(m)
folium.Marker(location = t2).add_to(m)
folium.Marker(location = t3).add_to(m)

m.save(r'karta\karta.html')

#APP

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Iframe(id = 'map', srcDoc= open(r'karta\karta.html', 'r', encoding = 'utf8').read(), width = '100%', height = '1000')
)


if __name__ == '__main__':
    app.run_server(debug = True)