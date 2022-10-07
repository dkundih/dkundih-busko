import json

točke = ['LENIŠĆE', 'CERINE', 'KAMPUS', 'ŽELJEZNIČKI KOLODVOR', 'GROBLJE', 'ZRINSKI TRG', 'DOM MLADIH']

T_M_BICIKLI_OUTPUT = {}

# in case locations are imported from geojson format
with open('lokacije/T_M_bicikli.geojson') as f:
    gj = json.load(f)
features = gj['features']


for i in range(len(features)):
    tmp = features[i]['geometry']['coordinates']
    T_M_BICIKLI_OUTPUT[točke[i]] = {
        'X' : tmp[1],
        'Y' : tmp[0],
        }
    
#print(T_M_BICIKLI_OUTPUT)
