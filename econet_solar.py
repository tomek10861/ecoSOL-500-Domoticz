import requests
import json

# dane do logowania w Domoticza
domoticza_url = 'http://192.168.25.24:8080/json.htm'
domoticza_username = 'admin'
domoticza_password = 'haslo_do_domoticza'

# tablica mapowania idx
idx_mapping = {
    'T1': '114',
    'T2': '182',
    'T3': '112',
    'T4': '113',
    'T6': '115',
    'P1': '189',
    'P2': '188',
    'Uzysk_ca_kowity': '184'
}

# pobranie JSON-a, dane sterownika econet
response = requests.get('http://admin:admin@192.168.25.85/econet/regParams')
json_data = response.json()

print('Pobrane dane JSON:')
print(json_data)

# przypisanie wartości z JSON-a do zmiennych
fields = ['T1', 'T2', 'T3', 'T4', 'T6', 'P1', 'P2']
values = {}

# pobieranie wartości z schemaParams jeśli istnieje, w przeciwnym razie z curr
for field in fields:
    if 'schemaParams' in json_data and f'schema_{field}' in json_data['schemaParams']:
        value = float(json_data['schemaParams'][f'schema_{field}'][0][0][0])
    elif 'curr' in json_data and field in json_data['curr']:
        value = float(json_data['curr'][field])
    else:
        continue
    values[field] = value

# Pobranie Uzysk_ca_kowity z curr
if 'Uzysk_ca_kowity' in json_data['curr']:
    uz_value = float(json_data['curr']['Uzysk_ca_kowity'])
    values['Uzysk_ca_kowity'] = uz_value

print('Znalezione wartości:')
print(values)

# wysłanie wartości do Domoticza
for field, value in values.items():
    idx = idx_mapping.get(field)
    if idx is not None:
        params = {'type': 'command', 'param': 'udevice', 'idx': idx, 'nvalue': '0', 'svalue': str(value)}
        print(f'Wysyłanie danych: {params}')
        requests.get(domoticza_url, params=params, auth=(domoticza_username, domoticza_password))
        print(f'Wysłano dane dla pola {field} z wartością {value}')
