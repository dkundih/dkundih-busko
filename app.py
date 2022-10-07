import folium
import json
import dash
from dash.dependencies import Input, Output
from dash import html
from dash import dcc
from datetime import datetime


time = datetime.now()


from lokacije.postaje import T_B_L1_OUTPUT


def lokacijaL1(ime,):
    x = T_B_L1_OUTPUT[ime]['X']
    y = T_B_L1_OUTPUT[ime]['Y']
    return [x, y]

def ikona(ikona):
    return folium.features.CustomIcon(ikona, icon_size=(30, 30))

def infoL1(naslov, opis = None, ak = None, ka = None, slika = None,):
    return folium.Popup(f"""<H4>{naslov}</H4>
                        <p>{opis}</p>
                        <b>KOLODVOR -> KAMPUS</b>
                        <p><b>Busko prolazi kroz čvor u:</b>
                        {ka}</p>
                        <b>KAMPUS -> KOLODVOR</b>
                        <p><b>Busko prolazi kroz čvor u:</b>
                        {ak}</p>
                        <img src="{slika}" alt = "Postaja" style="width:300px;height:80px;/>"
                        """)

m = folium.Map(location = [46.1639, 16.83], zoom_start = 14.8)

folium.Marker(location = lokacijaL1('AUTOBUSNI KOLODVOR'), icon = ikona('https://avatars.githubusercontent.com/u/86894643?v=4'), popup = infoL1('AUTOBUSNI KOLODVOR','Kolodvorska ul. 31, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'], 'https://raw.githubusercontent.com/dkundih/dkundih/main/.logistics/BLUERED_GHiLI.jpg')).add_to(m)
folium.Marker(location = lokacijaL1('TRG MLADOSTI'), icon = ikona('https://avatars.githubusercontent.com/u/86894643?v=4'), popup = infoL1('TRG MLADOSTI', 'Trg mladosti 1, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'], 'https://raw.githubusercontent.com/dkundih/dkundih/main/.logistics/BLUERED_GHiLI.jpg')).add_to(m)
folium.Marker(location = lokacijaL1('BOLNICA'), icon = ikona('https://avatars.githubusercontent.com/u/86894643?v=4'), popup = infoL1('BOLNICA', 'Ulica braće Radić 8, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'], 'https://raw.githubusercontent.com/dkundih/dkundih/main/.logistics/BLUERED_GHiLI.jpg')).add_to(m)
folium.Marker(location = lokacijaL1('STADION'), icon = ikona('https://avatars.githubusercontent.com/u/86894643?v=4'), popup = infoL1('STADION', 'Ulica Mihovila Pavleka Miškine, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'], 'https://raw.githubusercontent.com/dkundih/dkundih/main/.logistics/BLUERED_GHiLI.jpg')).add_to(m)
folium.Marker(location = lokacijaL1('KAMPUS'), icon = ikona('https://avatars.githubusercontent.com/u/86894643?v=4'), popup = infoL1('KAMPUS', 'Trg dr. Žarka Dolinara 1, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'],'https://raw.githubusercontent.com/dkundih/dkundih/main/.logistics/BLUERED_GHiLI.jpg')).add_to(m)

# Željeznički Stilovi

Ž1 = {
    'color' : 'green',
    'weight' : 7,
    'fillColor' : 'green',
    'fillOpacity' : 0.1,
}

Ž2 = {
    'color' : 'red',
    'weight' : 7,
    'fillColor' : 'red',
    'fillOpacity' : 0.1,
}

Ž3 = {
    'color' : 'blue',
    'weight' : 7,
    'fillColor' : 'blue',
    'fillOpacity' : 0.1,
}

Ž4 = {
    'color' : 'magenta',
    'weight' : 7,
    'fillColor' : 'magenta',
    'fillOpacity' : 0.1,
}

# Željezničke rute
folium.GeoJson('lokacije/Ž_ČK-KC.geojson', style_function = lambda x: Ž1, name = 'Ž_ČK-KC').add_to(m)
folium.GeoJson('lokacije/Ž_VT-KC.geojson', style_function = lambda x: Ž2, name = 'Ž_VT-KC').add_to(m)
folium.GeoJson('lokacije/Ž_ZG-KC.geojson', style_function = lambda x: Ž3, name = 'Ž_ZG-KC').add_to(m)
folium.GeoJson('lokacije/Ž_BT-KC.geojson', style_function = lambda x: Ž4, name = 'Ž_BT-KC').add_to(m)


m.save(r'karta\karta.html')

#APP

app = dash.Dash(__name__)
server = app.server
app.title = 'dkundih-busko'

app.layout = html.Div([
    
    html.Iframe(id = 'mapa', srcDoc= open('karta/karta.html', 'r', encoding = 'utf8').read(), width = '100%', height = '1000'),

])

if __name__ == '__main__':
    app.run_server(debug = True)
    