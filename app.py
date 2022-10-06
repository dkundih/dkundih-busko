import folium
import json
import dash
from dash import html
from datetime import datetime

now = datetime.now()

željeznički_kolodvor = {
    'Ime' : 'Željeznički kolodvor',
    'X' : 46.16474814765847,
    'Y' : 16.817654371261597,
}

'''
# in case locations are imported from geojson format
with open('lokacije/linija1_postaje.geojson') as f:
    gj = json.load(f)
features = gj['features']
'''

t1 = [željeznički_kolodvor['X'], željeznički_kolodvor['Y']]
t1_icon = folium.features.CustomIcon('https://avatars.githubusercontent.com/u/86894643?v=4', icon_size=(30, 30))
t1_popup = folium.Popup(f"""<H4>ŽELJEZNIČKI KOLODVOR</H4>
                        <p>Početak linije</p>
                        <img src="https://raw.githubusercontent.com/dkundih/dkundih/main/.logistics/BLUERED_GHiLI.jpg" alt = "Željeznički kolodvor" style="width:300px;height:80px;/>"
                        <p>Sada je: {now}</p>
                        """)


m = folium.Map(location = [46.1639, 16.83], zoom_start = 14.8)

style = {
    'color' : 'green',
    'weight' : 5,
    'fillColor' : 'green',
    'fillOpacity' : 0.1,
}

folium.GeoJson('lokacije/linija1.geojson', style_function = lambda x: style, name = 'linija1').add_to(m)
folium.Marker(location = t1, icon = t1_icon, popup = t1_popup).add_to(m)


m.save(r'karta\karta.html')

#APP

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    html.Iframe(id = 'map', srcDoc= open('karta/karta.html', 'r', encoding = 'utf8').read(), width = '100%', height = '1000')
)

if __name__ == '__main__':
    now = datetime.now()
    app.run_server()