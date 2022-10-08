import folium
import dash
from dash import html

from lokacije.B_postaje import T_B_L1_OUTPUT # autobus
from lokacije.E_bicikli_postaje import T_E_BICIKLI_OUTPUT # e-bicikli
from lokacije.M_bicikli_postaje import T_M_BICIKLI_OUTPUT # bicikli
from lokacije.V_postaje import T_V_OUTPUT # vlak

def lokacijaL1(ime,):
    x = T_B_L1_OUTPUT[ime]['X']
    y = T_B_L1_OUTPUT[ime]['Y']
    return [x, y]

def lokacijaMB(ime,):
    x = T_M_BICIKLI_OUTPUT[ime]['X']
    y = T_M_BICIKLI_OUTPUT[ime]['Y']
    return [x, y]

def lokacijaV(ime,):
    x = T_V_OUTPUT[ime]['X']
    y = T_V_OUTPUT[ime]['Y']
    return [x, y]

def lokacijaEB(ime,):
    x = T_E_BICIKLI_OUTPUT[ime]['X']
    y = T_E_BICIKLI_OUTPUT[ime]['Y']
    return [x, y]

def ikona(ikona):
    return folium.features.CustomIcon(ikona, icon_size=(40, 50))

def infoL1(naslov, opis = None, ak = None, ka = None, slika = None,):
    return folium.Popup(f"""<H4>{naslov}</H4>
                        <p><i>{opis}</i></p>
                        <b>KOLODVOR -> KAMPUS</b>
                        <p><b>Busko se nalazi na čvoru u:</b>
                        {ka}</p>
                        <b>KAMPUS -> KOLODVOR</b>
                        <p><b>Busko se nalazi na čvoru u:</b>
                        {ak}</p>
                        <p><b><u>*Vozi samo radnim danima (pon-pet). Ne vozi vikendom (sub i ned).</u></b></p>
                        <img src="{slika}" alt = "Postaja" style="width:300px;height:160px;/>"
                        """)
    
def infoMB_EB(naslov, opis = None, slika = None,):
    return folium.Popup(f"""<H4>{naslov}</H4>
                        <p><i>{opis}</i></p>
                        <b><u>*Korištenje bicikala se ne naplaćuje. Potrebno je posjedovanje kartice.</u></b>
                        <p></p>
                        <img src="{slika}" alt = "Postaja" style="width:300px;height:170px;/>"
                        """)
    
def infoV(naslov, opis = None, dk_ime = None, dk = None,ok_ime = None, ok = None, slika = None,):
    return folium.Popup(f"""<H4>{naslov}</H4>
                        <p><i>{opis}</i></p>
                        <b>{dk_ime}</b>
                        <p><b>Vlak dolazi na čvor u:</b>
                        {dk}</p>
                        <b>{ok_ime}</b>
                        <p><b>Vlak se nalazi na čvoru u:</b>
                        {ok}</p>
                        <p><b><u>*Vozni red prikazan je samo za radni tjedan (pon-pet). Vozni red vikendom razlikuje se od prikazanog.</u></b></p>
                        <img src="{slika}" alt = "Postaja" style="width:300px;height:150px;/>"
                        """)

m = folium.Map(location = [46.1639, 16.83], zoom_start = 14.8)
folium.TileLayer('cartodbdark_matter').add_to(m)

# autobusne postaje
folium.Marker(location = lokacijaL1('AUTOBUSNI KOLODVOR'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bus.png'), popup = infoL1('AUTOBUSNI KOLODVOR','Kolodvorska ul. 31, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'], 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/autobusni.jpg')).add_to(m)
folium.Marker(location = lokacijaL1('TRG MLADOSTI'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bus.png'), popup = infoL1('TRG MLADOSTI', 'Trg mladosti 1, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'], 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/mladosti.jpg')).add_to(m)
folium.Marker(location = lokacijaL1('BOLNICA'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bus.png'), popup = infoL1('BOLNICA', 'Ulica braće Radić 8, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'], 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/bolnica.jpg')).add_to(m)
folium.Marker(location = lokacijaL1('STADION'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bus.png'), popup = infoL1('STADION', 'Ulica Mihovila Pavleka Miškine, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'], 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/stadion.jpg')).add_to(m)
folium.Marker(location = lokacijaL1('KAMPUS'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bus.png'), popup = infoL1('KAMPUS', 'Trg dr. Žarka Dolinara 1, 48000, Koprivnica', T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['K-A'], T_B_L1_OUTPUT['AUTOBUSNI KOLODVOR']['A-K'],'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/kampus.jpg')).add_to(m)

# bicikl postaje
folium.Marker(location = lokacijaMB('LENIŠĆE'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bicikl.png'), popup = infoMB_EB('LENIŠĆE', 'Centar Lenišće, 48000, Koprivnica','https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/bicikli.jpg')).add_to(m)
folium.Marker(location = lokacijaMB('CERINE'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bicikl.png'), popup = infoMB_EB('CERINE', 'Ulica Miroslava Krleže 81, 48000, Koprivnica','https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/bicikli.jpg')).add_to(m)
folium.Marker(location = lokacijaMB('KAMPUS'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bicikl.png'), popup = infoMB_EB('KAMPUS', 'Trg dr. Žarka Dolinara 1, Koprivnica','https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/bicikli.jpg')).add_to(m)
folium.Marker(location = lokacijaMB('ŽELJEZNIČKI KOLODVOR'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bicikl.png'), popup = infoMB_EB('ŽELJEZNIČKI KOLODVOR', 'Kolodvorska, 48000, Koprivnica','https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/bicikli.jpg')).add_to(m)
folium.Marker(location = lokacijaMB('GROBLJE'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bicikl.png'), popup = infoMB_EB('GROBLJE', 'Varaždinska cesta, 48000, Koprivnica','https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/bicikli.jpg')).add_to(m)
folium.Marker(location = lokacijaMB('ZRINSKI TRG'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bicikl.png'), popup = infoMB_EB('ZRINSKI TRG', 'Zrinski trg, 48000, Koprivnica','https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/bicikli.jpg')).add_to(m)
folium.Marker(location = lokacijaMB('DOM MLADIH'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bicikl.png'), popup = infoMB_EB('DOM MLADIH', 'Opatička ulica, 48000, Koprivnica','https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/bicikli.jpg')).add_to(m)

folium.Marker(location = lokacijaEB('SVEUČILIŠTE SJEVER'), icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/bicikl.png'), popup = infoMB_EB('SVEUČILIŠTE SJEVER', 'Trg dr. Žarka Dolinara 1, 48000, Koprivnica','https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/ebicikli.jpg')).add_to(m)

# vlak postaje i info o dolascima/odlascima

folium.Marker(
    location = lokacijaV('KC-VŽ'),
    icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/vlak.png'),
    popup = infoV(
    naslov = 'SMJER VARAŽDIN',
    opis = 'željeznička pruga prema Varaždinu.',
    slika = 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/vlak.jpg',
    dk_ime = 'VARAŽDIN -> KOPRIVNICA',
    ok_ime= 'KOPRIVNICA -> VARAŽDIN',
    ok = T_V_OUTPUT['KC-VŽ']['OK'],
    dk = T_V_OUTPUT['KC-VŽ']['PK'],
            )).add_to(m)

folium.Marker(
    location = lokacijaV('KC-BT'),
    icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/vlak.png'),
    popup = infoV(
    naslov = 'SMJER BUDIMPEŠTA',
    opis = 'željeznička pruga prema Budimpešti.',
    slika = 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/vlak.jpg',
    dk_ime = 'BUDIMPEŠTA -> KOPRIVNICA',
    ok_ime= 'KOPRIVNICA -> BUDIMPEŠTA',
    ok = T_V_OUTPUT['KC-BT']['OK'],
    dk = T_V_OUTPUT['KC-BT']['PK'],
            )).add_to(m)

folium.Marker(
    location = lokacijaV('KC-VT'),
    icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/vlak.png'),
    popup = infoV(
    naslov = 'SMJER VIROVITICA',
    opis = 'željeznička pruga prema Virovitici.',
    slika = 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/vlak.jpg',
    dk_ime = 'VIROVITICA -> KOPRIVNICA',
    ok_ime= 'KOPRIVNICA -> VIROVITICA',
    ok = T_V_OUTPUT['KC-VT']['OK'],
    dk = T_V_OUTPUT['KC-VT']['PK'],
            )).add_to(m)

folium.Marker(
    location = lokacijaV('KC-ZG'),
    icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/vlak.png'),
    popup = infoV(
    naslov = 'SMJER ZAGREB',
    opis = 'željeznička pruga prema Zagrebu.',
    slika = 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/vlak.jpg',
    dk_ime = 'ZAGREB -> KOPRIVNICA',
    ok_ime= 'KOPRIVNICA -> ZAGREB',
    ok = T_V_OUTPUT['KC-ZG']['OK'],
    dk = T_V_OUTPUT['KC-ZG']['PK'],
            )).add_to(m)

folium.Marker(
    location = lokacijaV('KUNOVEC-SUBOTICA'),
    icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/vlak.png'),
    popup = infoV(
    naslov = 'KUNOVEC-SUBOTICA',
    opis = 'željezničko stajalište.',
    slika = 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/vlak.jpg',
    dk_ime = 'KUNOVEC-SUBOTICA -> KOPRIVNICA',
    ok_ime= 'KOPRIVNICA -> KUNOVEC-SUBOTICA',
    ok = T_V_OUTPUT['KUNOVEC-SUBOTICA']['OK'],
    dk = T_V_OUTPUT['KUNOVEC-SUBOTICA']['PK'],
            )).add_to(m)

folium.Marker(
    location = lokacijaV('DRNJE'),
    icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/vlak.png'),
    popup = infoV(
    naslov = 'DRNJE',
    opis = 'željezničko stajalište.',
    slika = 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/vlak.jpg',
    dk_ime = 'DRNJE -> KOPRIVNICA',
    ok_ime= 'KOPRIVNICA -> DRNJE',
    ok = T_V_OUTPUT['DRNJE']['OK'],
    dk = T_V_OUTPUT['DRNJE']['PK'],
            )).add_to(m)

folium.Marker(
    location = lokacijaV('BREGI'),
    icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/vlak.png'),
    popup = infoV(
    naslov = 'BREGI',
    opis = 'željeznički kolodvor.',
    slika = 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/vlak.jpg',
    dk_ime = 'KOPRIVNIČKI BREGI -> KOPRIVNICA',
    ok_ime= 'KOPRIVNICA -> KOPRIVNIČKI BREGI',
    ok = T_V_OUTPUT['BREGI']['OK'],
    dk = T_V_OUTPUT['BREGI']['PK'],
            )).add_to(m)

folium.Marker(
    location = lokacijaV('MUČNA REKA'),
    icon = ikona('https://raw.githubusercontent.com/dkundih/dkundih-busko/master/ikone/vlak.png'),
    popup = infoV(
    naslov = 'MUČNA REKA',
    opis = 'željeznički kolodvor.',
    slika = 'https://raw.githubusercontent.com/dkundih/dkundih-busko/master/slike/vlak.jpg',
    dk_ime = 'MUČNA REKA -> KOPRIVNICA',
    ok_ime= 'KOPRIVNICA -> MUČNA REKA',
    ok = T_V_OUTPUT['MUČNA REKA']['OK'],
    dk = T_V_OUTPUT['MUČNA REKA']['PK'],
            )).add_to(m)


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
    'color' : 'yellow',
    'weight' : 7,
    'fillColor' : 'yellow',
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

# Autobusni Stilovi

B1 = {
    'color' : 'orange',
    'weight' : 7,
    'fillColor' : 'orange',
    'fillOpacity' : 0.1,
}


# Autobusne rute
folium.GeoJson('lokacije/B_L1.geojson', style_function = lambda x: B1, name = 'B_L1').add_to(m)


m.save(r'karta\karta.html')

#APP

app = dash.Dash(__name__)
server = app.server
app.title = 'dkundih-promet'


app.layout = html.Div([
    
    html.Div([
        html.Div(['ODRŽIVA MOBILNOST U KOPRIVNICI',
                  ], className='header_style'),
    ], id='header'),

    html.Div([
    html.Iframe(id = 'mapa', srcDoc= open('karta/karta.html', 'r', encoding = 'utf8').read(), width = '100%', height = '830'),
    ], id = 'body'),
    
    html.Div([
        html.Div(['(c) ',
                  html.A('David Kundih, 2022.',
                         href='https://www.linkedin.com/in/dkundih/'),
                  ], className='footer_style'),
        html.Div(['Aplikaciju pokreće ', html.A('Dash', href='https://plotly.com/dash/')],
                 className='footer_style'),
        html.Div(['Programski kod dostupan na ', html.A('GitHub repozitoriju ', href='https://www.github.com/dkundih')],
                 className='footer_style'),
                html.Div(['Ova aplikacija služi samo za potrebe demonstracije. ',],
                 className='footer_style'),
    ], id='footer'),

])

if __name__ == '__main__':
    app.run_server()
    