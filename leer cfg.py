import json

with open('configuracion.cfg.json', 'r') as f:
    datos = json.load(f)

print(datos)
